import csv
from pathlib import Path
import folium
import pandas as pd
from jinja2 import Template
from dronekit import connect
import time
import datetime
import threading
import os
import subprocess

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
    return subprocess.Popen(gst_command)

# Start GStreamer
gst_process = start_gstreamer()


# Connect to the drone's telemetry feed
vehicle = connect('udpin:192.168.0.144:14550', wait_ready=False)
vehicle.initialize(8, 30)
vehicle.wait_ready('autopilot_version')

def get_user_input():
    global user_input
    user_input = input("Type 'q' or 'quit' to exit: ").strip().lower()

user_input = None
input_thread = threading.Thread(target=get_user_input)
input_thread.daemon = True
input_thread.start()

telemetry_count = 0  # Initialize the counter

def print_telemetry():
    """Prints the drone's telemetry data."""
    global telemetry_count
    telemetry_count += 1  # Increment the counter
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Get the current local time
    print(f'Telemetry Data Feed {telemetry_count} - Timestamp: {current_time}')
    print('Location global alt (feet): %s' % (vehicle.location.global_frame.alt * 3.281 if vehicle.location.global_frame.alt else None))
    print('Pitch: %s' % vehicle.attitude.pitch)
    print("Velocity: %s" % vehicle.velocity)
    print("GPS: %s" % vehicle.gps_0)
    print("Flight mode currently: %s" % vehicle.mode.name)
    print('Battery level: %s' % vehicle.battery.level)
    print('Status: %s' % vehicle.system_status.state)
    print('Armed: %s' % vehicle.armed)
    print('Heading: %s' % vehicle.heading)
    print('Speed: %s' % vehicle.groundspeed)
    print('GPS fix: %s' % vehicle.gps_0.fix_type)
    print('Satellites: %s' % vehicle.gps_0.satellites_visible)
    print('Location global lat: %s' % vehicle.location.global_frame.lat)
    print('Location global lon: %s' % vehicle.location.global_frame.lon)
    print('Groundspeed: %s' % vehicle.groundspeed)
    print('Velocity: %s' % vehicle.velocity[2])
    
    # Save telemetry data to a CSV file
    with open(file_path, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([
            vehicle.location.global_frame.lat,
            vehicle.location.global_frame.lon,
            'photo.jpg',  # Placeholder for photo name
            current_time,
            f'Telemetry Data Feed {telemetry_count}'
        ])

    # Update the Folium map
    update_map()

def update_map():
    # Load the updated data
    data = pd.read_csv(file_path)

    # Create a map centered around the average coordinates
    map_center = [data['latitude'].mean(), data['longitude'].mean()]
    m = folium.Map(location=map_center, zoom_start=13)

    # Add markers with popups for each telemetry point
    for idx, row in data.iterrows():
        popup_html = f"""
        <strong>Description:</strong> {row['description']}<br>
        <strong>Timestamp:</strong> {row['timestamp']}<br>
        <img src='{row['photo']}' alt='Photo' width='200'>
        """
        folium.Marker([row['latitude'], row['longitude']], popup=popup_html).add_to(m)

    # Save the Folium map to a string
    folium_map = m._repr_html_()

    # Load the Jinja2 template
    template_html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Drone Photos Map</title>
    </head>
    <body>
        {{ folium_map | safe }}
    </body>
    </html>
    """

    template = Template(template_html)
    rendered_html = template.render(folium_map=folium_map)

    # Save the rendered HTML to a file
    output_path = current_directory / 'map.html'
    with open(output_path, 'w') as f:
        f.write(rendered_html)

exit_flag = False  # Flag to indicate whether to exit the main loop

# Path for the CSV file
current_directory = Path.cwd()
subdirectory = 'Data'
data_directory = current_directory / subdirectory
data_directory.mkdir(exist_ok=True)
file_path = data_directory / 'drone_photos.csv'

# Initialize the CSV file
with open(file_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['latitude', 'longitude', 'photo', 'timestamp', 'description'])

# Continuously print telemetry data every 30 seconds until user quits
while not exit_flag:
    print_telemetry()
    
    # Wait for 30 seconds, but check user_input every second
    for _ in range(30):
        if user_input in ['q', 'quit']:
            exit_flag = True
            break
        time.sleep(1)

# Close the vehicle connection
vehicle.close()