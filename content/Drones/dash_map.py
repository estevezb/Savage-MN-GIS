import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd


# Sample data
data = pd.DataFrame({
    'latitude': [45.5236, 45.528, 45.513],
    'longitude': [-122.6750, -122.665, -122.705],
    'photo': ['photo1.jpg', 'photo2.jpg', 'photo3.jpg'],
    'timestamp': ['2024-06-25 10:00:00', '2024-06-25 10:05:00', '2024-06-25 10:10:00'],
    'description': ['Description of photo 1', 'Description of photo 2', 'Description of photo 3']
})

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Graph(id='map-graph'),
    html.Table([
        html.Thead(html.Tr([html.Th(col) for col in data.columns])),
        html.Tbody(id='table-body')
    ])
])

@app.callback(
    Output('map-graph', 'figure'),
    Output('table-body', 'children'),
    Input('map-graph', 'clickData')
)
def update_map_and_table(clickData):
    fig = px.scatter_mapbox(
        data, lat='latitude', lon='longitude', text='description',
        zoom=10, height=600, mapbox_style='open-street-map'
    )
    if clickData is not None:
        selected_point = clickData['points'][0]
        selected_lat = selected_point['lat']
        selected_lon = selected_point['lon']
        selected_data = data[(data['latitude'] == selected_lat) & (data['longitude'] == selected_lon)]
    else:
        selected_data = data

    table_rows = []
    for idx, row in selected_data.iterrows():
        table_rows.append(html.Tr([html.Td(row[col]) for col in data.columns]))
    
    return fig, table_rows

if __name__ == '__main__':
    app.run_server(debug=True)