import os
import time
import datetime
import pandas as pd
import numpy as np
from mss import mss
from PIL import Image
import pygetwindow as gw
import cv2
import keyboard
from dronekit import connect
from pymavlink import mavutil
import subprocess
import threading  # Import threading module
import dash
from dash import dcc, html, Input, Output, State
import dash_bootstrap_components as dbc
import plotly.express as px

# Function to start GStreamer
def start_gstreamer():
    gst_command = [
        r"C:\gstreamer\1.0\msvc_x86_64\bin\gst-launch-1.0.exe",
        "udpsrc", "port=5600", "buffer-size=524288",
        "!", "application/x-rtp",
        "!", "rtpjitterbuffer", "latency=200",
        "!", "rtph264depay",
        "!", "avdec_h264",
        "!", "videoconvert",
        "!", "autovideosink"
    ]
    print("Starting GStreamer with command:", " ".join(gst_command))
    return subprocess.Popen(gst_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# Start GStreamer
gst_process = start_gstreamer()

# Connect to the drone
vehicle = connect('udpin:192.168.0.144:14550', wait_ready=True)

# Store the original location
original_location = vehicle.location.global_relative_frame
print("Original location: ", original_location)

# Create directories for storing photos
def create_directories():
    data_dir = os.path.join(os.getcwd(), "Data")
    photos_dir = os.path.join(data_dir, "Photos")
    
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
        print(f"Created directory: {data_dir}")

    if not os.path.exists(photos_dir):
        os.makedirs(photos_dir)
        print(f"Created directory: {photos_dir}")

    return photos_dir

# Function to trigger the camera
def trigger_camera():
    msg = vehicle.message_factory.command_long_encode(
        0, 0,  # target_system, target_component
        mavutil.mavlink.MAV_CMD_IMAGE_START_CAPTURE,  # command
        0,  # confirmation
        0,  # param1 (interval between captures, in seconds)
        1,  # param2 (number of captures, 0 for unlimited)
        0,  # param3 (number of frames in a burst)
        0, 0, 0, 0  # param4 - param7 (not used)
    )
    vehicle.send_mavlink(msg)
    vehicle.flush()
    print("Camera trigger command sent")

# Function to capture frame and save
def capture_frame_and_save():
    sct = mss()
    photos_dir = create_directories()
    
    while True:
        # Get the GStreamer window
        gstreamer_windows = gw.getWindowsWithTitle('Direct3D11 renderer')
        if not gstreamer_windows:
            print("GStreamer window not found!")
            continue

        gstreamer_window = gstreamer_windows[0]
        monitor = {
            'top': gstreamer_window.top,
            'left': gstreamer_window.left,
            'width': gstreamer_window.width,
            'height': gstreamer_window.height
        }

        # Capture the screen
        screenshot_img = sct.grab(monitor)
        img = Image.frombytes('RGB', screenshot_img.size, screenshot_img.bgra, 'raw', 'BGRX')
        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        # Save the captured frame
        filename = datetime.datetime.now().strftime("photo_%Y%m%d_%H%M%S.jpg")
        abs_path = os.path.join(photos_dir, filename)
        cv2.imwrite(abs_path, frame)
        print(f"Photo saved as {abs_path}")
        return abs_path  # Return the absolute path of the saved photo

# Initialize an empty DataFrame to store photo metadata
df_photos = pd.DataFrame(columns=["Timestamp", "Latitude", "Longitude", "Photo Path"])

# Function to update the DataFrame
def update_dataframe(photo_path):
    global df_photos
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    latitude = vehicle.location.global_relative_frame.lat
    longitude = vehicle.location.global_relative_frame.lon
    new_data = pd.DataFrame([[timestamp, latitude, longitude, photo_path]], columns=["Timestamp", "Latitude", "Longitude", "Photo Path"])
    df_photos = pd.concat([df_photos, new_data], ignore_index=True)

# Function to handle the key press event
def on_key_event(event):
    if event.name == 'p' and keyboard.is_pressed('ctrl'):
        trigger_camera()
        photo_path = capture_frame_and_save()
        update_dataframe(photo_path)

# Register the key press event
keyboard.on_press(on_key_event)

# Create Dash application
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Layout of the Dash application
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1("Drone Photo Capture Dashboard"), className="text-center")
    ]),
    dbc.Row([
        dbc.Col(dcc.Graph(id="map-graph"), width=8),
        dbc.Col([
            html.Button("Take Photo", id="take-photo-button", className="btn btn-primary"),
            html.Div(id="photo-status", className="mt-3")
        ], width=4)
    ]),
    dbc.Row([
        dbc.Col(dcc.Interval(id="interval-component", interval=10000, n_intervals=0))
    ])
])

@app.callback(
    [Output("photo-status", "children"),
     Output("map-graph", "figure")],
    [Input("take-photo-button", "n_clicks")],
    [State("interval-component", "n_intervals")]
)
def take_photo_and_update_map(n_clicks, n_intervals):
    if n_clicks is None:
        raise dash.exceptions.PreventUpdate

    # Trigger the camera and capture the frame
    trigger_camera()
    photo_path = capture_frame_and_save()
    
    # Update the DataFrame with the photo metadata
    update_dataframe(photo_path)

    # Create a Plotly map to display the photo locations
    fig = px.scatter_mapbox(
        df_photos,
        lat="Latitude",
        lon="Longitude",
        hover_name="Timestamp",
        hover_data={"Photo Path": True},
        zoom=12,  # Adjust zoom level as needed
        height=600
    )
    fig.update_layout(mapbox_style="open-street-map")

    return "Photo taken and saved!", fig

print("Press Ctrl+P to capture a photo")

# Function to listen for key events
def listen_for_key_events():
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Exiting...")

# Start Dash server in the main thread
if __name__ == "__main__":
    # Start the keyboard listener in a separate thread
    key_listener_thread = threading.Thread(target=listen_for_key_events)
    key_listener_thread.daemon = True
    key_listener_thread.start()

    # Run Dash server
    app.run_server(debug=True)

    # Close the vehicle connection
    vehicle.close()