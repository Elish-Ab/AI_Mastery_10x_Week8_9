from flask import Flask, jsonify
import pandas as pd
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import plotly.express as px

# Initialize Flask and Dash
flask_app = Flask(__name__)
dash_app = Dash(server=flask_app, name="Dashboard", external_stylesheets=[dbc.themes.BOOTSTRAP])

# Load data
df = pd.read_csv("fraud_data.csv")  # Replace with your actual fraud data file

# Flask endpoint for summary statistics
@flask_app.route('/summary', methods=['GET'])
def summary():
    summary_data = {
        "total_transactions": len(df),
        "total_fraud_cases": df['fraud'].sum(),
        "fraud_percentage": df['fraud'].mean() * 100
    }
    return jsonify(summary_data)

# Flask endpoint for time series data
@flask_app.route('/fraud_trends', methods=['GET'])
def fraud_trends():
    fraud_trend = df.groupby('date')['fraud'].sum().to_json()
    return jsonify(fraud_trend)

# Dashboard layout and graphs
dash_app.layout = dbc.Container([
    html.H1("Fraud Detection Dashboard"),
    dbc.Row([
        dbc.Col(html.Div("Total Transactions: ")),
        dbc.Col(html.Div(id="total-transactions"))
    ]),
    dbc.Row([
        dbc.Col(html.Div("Fraud Cases: ")),
        dbc.Col(html.Div(id="total-fraud-cases"))
    ]),
    dbc.Row([
        dbc.Col(html.Div("Fraud Percentage: ")),
        dbc.Col(html.Div(id="fraud-percentage"))
    ]),
    dbc.Row(dcc.Graph(id="time-series-graph")),
    dbc.Row(dcc.Graph(id="geo-graph")),
    dbc.Row(dcc.Graph(id="device-bar-graph"))
])

# Callbacks for graphs and summary data
@dash_app.callback(
    [dash.dependencies.Output("total-transactions", "children"),
     dash.dependencies.Output("total-fraud-cases", "children"),
     dash.dependencies.Output("fraud-percentage", "children")],
    []
)
def update_summary_boxes():
    total_transactions = len(df)
    total_fraud_cases = df['fraud'].sum()
    fraud_percentage = df['fraud'].mean() * 100
    return total_transactions, total_fraud_cases, f"{fraud_percentage:.2f}%"

@dash_app.callback(
    dash.dependencies.Output("time-series-graph", "figure"),
    []
)
def update_time_series():
    fig = px.line(df, x="date", y="fraud", title="Fraud Cases Over Time")
    return fig

@dash_app.callback(
    dash.dependencies.Output("geo-graph", "figure"),
    []
)
def update_geo():
    geo_df = df[df['fraud'] == 1]  # Filter for fraud cases
    fig = px.scatter_geo(geo_df, lat="latitude", lon="longitude", title="Fraud Cases by Location")
    return fig

@dash_app.callback(
    dash.dependencies.Output("device-bar-graph", "figure"),
    []
)
def update_device_bar():
    device_df = df.groupby('device').sum().reset_index()
    fig = px.bar(device_df, x="device", y="fraud", title="Fraud Cases by Device")
    return fig

if __name__ == "__main__":
    dash_app.run_server(debug=True, host="0.0.0.0", port=8050)
