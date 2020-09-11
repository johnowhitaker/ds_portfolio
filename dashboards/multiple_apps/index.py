import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from apps import gbv_app, diabetes_app


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):

    # We could make a separate 'homepage app'
    if pathname == "/":
        home = html.Div([
            dcc.Link('Go to diabetes app', href='/apps/diabetes_app'),
            html.P(),
            dcc.Link('Go to gbv app', href='/apps/gbv_app')
        ])
        return home

    elif pathname == '/apps/gbv_app':
        return gbv_app.layout
    elif pathname == '/apps/diabetes_app':
        return diabetes_app.layout
    else:
        return '404'

if __name__ == '__main__':
    app.run_server(debug=True, port=8051, host='localhost')
