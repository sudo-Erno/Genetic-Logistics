import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = [
    {
        "href": "https://fonts.googleapis.com/css2?"
                "family=Lato:wght@400;700&display=swap",
        "rel": ".\GUI\Assets\styles.css",
    },
]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

def run_gui(data):

    times, best_time, best_path = data

    app.layout = html.Div(
        children=[
            html.H1(children="Genetic Logistic",
                className="header-title",),
            html.P(
                children="Que lindo dia",
            ),
            html.Div(
                dcc.Graph(
                    figure={
                        "data": [
                            {
                                "x": len(times),
                                "y": times,
                                "type": "lines",
                            },
                        ],
                        "layout": {
                            "title": "Performance as it evolved.",},
                    },
                )
            ),
            html.Button('Load Locations', id='btn-load-loc', n_clicks=0),            
        ]
    )
    app.run_server(debug=True)

if __name__ == '__main__':
    run_gui(0)