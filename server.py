from flask import Flask, request
from master.Core import solver_static_formula
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/second-order/euler', methods=['POST'])
@cross_origin()
def second_order_euler():
    json_data = request.get_json()

    h = float(json_data['h'])
    t_0 = float(json_data['t_0'])
    t_end = float(json_data['t_end'])
    y_0 = float(json_data['y_0'])
    y_1 = float(json_data['y_1'])
    method = int(json_data['method'])

    differential_second_solver = solver_static_formula.SolverSecondDifferential()

    if method == 0:
        result = differential_second_solver.get_result_euler(h, t_0, t_end, y_0, y_1)
    else:
        result = differential_second_solver.get_result_runge(h, t_0, t_end, y_0, y_1)

    return str(result)


if (__name__ == '__main__'):
    app.run()
