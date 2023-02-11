"""the main dashboard file"""

import dash
import dash_html_components as html

from style_dicts import DASBOARD_TOPIC_DICT, LAYOUT_SYTLE_DICT

app = dash.Dash()

app.layout = html.Div(id='outer-div', children=[html.H1('U.S.A Houses Dashboard', style=DASBOARD_TOPIC_DICT)],
                      style=LAYOUT_SYTLE_DICT)


if __name__ == "__main__":
    app.run_server(debug=True)
