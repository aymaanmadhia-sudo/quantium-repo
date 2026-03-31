import pandas as pd
from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import plotly.express as px


data = pd.read_csv("combined.csv")


data["date"] = pd.to_datetime(data["date"])

app = Dash(__name__)

app.layout = html.Div([
    html.Div([
        html.H2("Sales Dashboard",
                style={
                    "textAlign": "center",
                    "color": "blue",
                    "fontFamily":"Italic"
                }),

        dcc.RadioItems(
            id="region",
            options=[
                {"label": "All", "value": "all"},
                {"label": "North", "value": "north"},
                {"label": "South", "value": "south"},
                {"label": "East", "value": "east"},
                {"label": "West", "value": "west"}
            ],
            value="all",
            style={
                "marginBottom": "20px",
                "color": "blue"   
            }
        ),

        dcc.Graph(id="graph")

    ])
],
style={
    "width": "60%",
    "margin": "auto",
    "padding": "20px",
    "backgroundColor": "#f9f9f9",
    "borderRadius": "10px"
})



@app.callback(
    Output("graph", "figure"),
    Input("region", "value")
)

def update(region):
    
    if region == "all":
        df = data
    else:
        df = data[data["region"] == region]

    df = df.sort_values("date")

    fig = px.line(df, x="date", y="sales")

    return fig


if __name__ == "__main__":
    app.run(debug=True)
