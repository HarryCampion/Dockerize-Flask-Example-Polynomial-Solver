#main application - only one view point so no need for views file.

from flask import Flask, render_template
import numpy as np
import plotly
import plotly.graph_objs as go
import json

from module_one.models.sql_model import SqlMock
from module_one.polynomial_solver import PolynomialSolver
from module_one.helpers import read_coordinates

# global data file path, get x and y coords
file_path = "data/"
x = read_coordinates(file_path+"x_coordinates_vector.txt")
y = read_coordinates(file_path+"y_coordinates_vector.txt")

# Create SQL db in memory and store coordinates and read the data back
mock = SqlMock()
mock.run_mock(table_name="coordinates", columns=["x", "y"], values=[x,y])
x, y = list(zip(*mock.read_table(table_name="coordinates")))

# Setup app
app = Flask(__name__)

# define app env
app.config.from_object("config.DevelopmentConfig")

def main():

    # Fit and solve 3rd order polynomial for coordinates obtained in SQL db
    solver = PolynomialSolver(x=x, y=y, deg=3)
    results = solver.solve_polynomial()
    
    new_x = np.linspace(results["x"][0], results["x"][-1], 50)
    # fit coefficients to polynomial function
    func = np.poly1d(results["coefficients"])
    new_y = func(new_x)

    # create plot metadata
    trace1 = go.Scatter(
        x=x,
        y=y,
        mode='markers',
        marker=go.scatter.Marker(color='rgb(255, 127, 14)', size=10),
        name='Data'
        )


    trace2 = go.Scatter(
        x=new_x,
        y=new_y,
        mode='lines',
        marker=go.scatter.Marker(color='rgb(31, 119, 180)', size=6),
        name='Fit'
        )

    layout = go.Layout(
        plot_bgcolor='rgb(229, 229, 229)',
        xaxis=go.layout.XAxis(zerolinecolor='rgb(255,255,255)', gridcolor='rgb(255,255,255)', title="x"),
        yaxis=go.layout.YAxis(zerolinecolor='rgb(255,255,255)', gridcolor='rgb(255,255,255)', title="y")
        )
    
    data = [trace1, trace2]

    fig = go.Figure(data=data, layout=layout)
    
    # store graph as json to render in the browser
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return results, graphJSON


@app.route('/')
def index():
    
    results, graphJSON = main()
    coefficients = zip(["a", "b", "c", "d"], results["coefficients"])
    roots = zip(["x1", "x2", "x3"], results["roots"])
    return render_template('index.html', graphJSON=graphJSON, coefficients=coefficients, roots=roots) 

if __name__ == '__main__':
    app.run()
