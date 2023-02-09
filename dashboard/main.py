"""the main dashboard file"""

import dash
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div(id='outer-div', children=[], style={'border':'Solid 5px Black', 'border-radius': '3px'})


if __name__ == "__main__":
    app.run_server(debug=True)
