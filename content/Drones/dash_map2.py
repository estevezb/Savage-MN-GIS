import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# Sample data
data = pd.DataFrame({
    'latitude': [45.5236, 45.528, 45.513],
    'longitude': [-122.6750, -122.665, -122.705],
    'photo': ['photo1.jpg', 'photo2.jpg', 'photo3.jpg'],
    'timestamp': ['2024-06-25 10:00:00', '2024-06-25 10:05:00', '2024-06-25 10:10:00'],
    'description': ['Description of photo 1', 'Description of photo 2', 'Description of photo 3']
})

# Initialize the Dash app
app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Dropdown(
        id='time-filter',
        options=[
            {'label': 'All Times', 'value': 'ALL'},
            {'label': '10:00:00', 'value': '2024-06-25 10:00:00'},
            {'label': '10:05:00', 'value': '2024-06-25 10:05:00'},
            {'label': '10:10:00', 'value': '2024-06-25 10:10:00'},
        ],
        value='ALL'
    ),
    dcc.Graph(id='map')
])

@app.callback(
    Output('map', 'figure'),
    [Input('time-filter', 'value')]
)
def update_map(selected_time):
    if selected_time == 'ALL':
        filtered_data = data
    else:
        filtered_data = data[data['timestamp'] == selected_time]

    fig = px.scatter_mapbox(
        filtered_data,
        lat='latitude',
        lon='longitude',
        text='description',
        size_max=15,
        zoom=10,
        height=600,
        mapbox_style="open-street-map"
    )

    for i, row in filtered_data.iterrows():
        fig.add_layout_image(
            dict(
                source=row['photo'],
                xref="x",
                yref="y",
                x=row['longitude'],
                y=row['latitude'],
                sizex=0.1,
                sizey=0.1,
                xanchor="center",
                yanchor="middle"
            )
        )

    return fig

if __name__ == '__main__':
    app.run_server(debug=True)