import plotly.express as px
from dash import Dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd

# New:
from app import app

# LOAD THE DATA
df = pd.read_csv('https://raw.githubusercontent.com/surabhim/Diabetes/master/Diabetes.csv', skiprows=9,
                 names=['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin',
                 'BMI', 'DiabetesPedigreeFunction', 'Age', 'Outcome'])
# Data process

# DEFINE COMPONENTS

def scatterplot(id, x, y):
  return dcc.Graph(id=id,
              figure=px.scatter(
                  df,
                  x=x,
                  y=y,
                  title=f"{x} vs {y}"
              ))

def boxplot(id, y):
  return dcc.Graph(id='graph1',
      figure=px.box(
          df, # Specify the dataframe
          x="Outcome",
          y=y,
          title=f"Distributions of {y} for both outcomes"
      )
    )

# SPECIFY LAYOUT (no longer app.layout)
layout = html.Div([
    # Heading
    html.H1("JupyterDash Demo 3 - Multiple Figures!"),

    # First Row
    html.Div(className="row", style={ 'width':'100%'}, children=[
        # Two scatter plots
        html.Div(scatterplot('scatter_1', 'Glucose', 'BMI'), style={'display': 'inline-block', 'width':'33%'}),
        html.Div(scatterplot('scatter_2', 'SkinThickness', 'BMI'), style={'display': 'inline-block', 'width':'33%'}),
        # Box plot
        html.Div(boxplot('boxplot', 'BMI'), style={'display': 'inline-block', 'width':'33%'})
    ]),
    dcc.Link('Back home', href='/')
])
