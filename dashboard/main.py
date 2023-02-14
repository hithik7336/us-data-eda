"""the main dashboard file"""

import dash
import dash_html_components as html
import dash_core_components as dcc

from data import get_average_price_by_state

from style_dicts import DASBOARD_TOPIC_DICT, LEFT_DIV_STYLE, RIGHT_DIV_STYLE, GRAPH_STYLE

app = dash.Dash()

app.layout = html.Div(id='outer-div', children=[html.H1('U.S.A Houses Dashboard',
                                                        style=DASBOARD_TOPIC_DICT),

                                                html.Div(id='left-div',
                                                         children=[dcc.Dropdown(id='us-states'),
                                                                    html.Hr(),
                                                                    dcc.Dropdown(),
                                                                    html.Hr(),
                                                                    dcc.Graph(id='graph-1',
                                                                              style=GRAPH_STYLE),
                                                                    html.Hr(),
                                                                    dcc.Graph(id='graph-2',
                                                                              style=GRAPH_STYLE)],
                                                         style=LEFT_DIV_STYLE),

                                                html.Div(id='right-div',
                                                         children=[dcc.Dropdown(),
                                                                    html.Hr(),
                                                                    dcc.Dropdown(),
                                                                    html.Hr(),
                                                                    dcc.Graph(id='graph-3',
                                                                              style=GRAPH_STYLE),
                                                                    html.Hr(),
                                                                    dcc.Graph(id='graph-4',
                                                                              style=GRAPH_STYLE)],
                                                         style=RIGHT_DIV_STYLE)])

if __name__ == "__main__":
    app.run_server(debug=True)
