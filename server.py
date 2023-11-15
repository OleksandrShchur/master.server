from flask import Flask, request
from master.Core import solver_static_formula
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/second-order/euler', methods=['POST'])
@cross_origin()
def second_order_euler():
    json_data = request.get_json()

    step = float(json_data['step'])
    t_0 = float(json_data['t_0'])
    t_end = float(json_data['t_end'])
    alpha = float(json_data['alpha'])
    beta = float(json_data['beta'])
    tau = float(json_data['tau'])
    method = int(json_data['method'])
    f_func = json_data['f_func']
    phi_func = json_data['phi_func']

    differential_second_solver = solver_static_formula.SolverSecondDifferential(step, t_0, t_end, alpha, beta, tau, f_func, phi_func, method)

    if method == 0:
        result = differential_second_solver.ger_result_euler_cust()
    else:
        result = differential_second_solver.get_result_runge(step, t_0, t_end, alpha, beta)

    return str(result)


if (__name__ == '__main__'):
    app.run()
