class SolverSecondDifferential:

    def __init__(self) -> None:
        pass

    def runge_kutta_4(self, func1, func2, y0, y1, t0, t_end, h):
        t_values = [t0]
        y_values = [(y0, y1)]

        while t0 < t_end:
            k1_y = h * func1(y0, y1, t0)
            k1_y1 = h * func2(y0, y1, t0)

            k2_y = h * func1(y0 + k1_y/2, y1 + k1_y1/2, t0 + h/2)
            k2_y1 = h * func2(y0 + k1_y/2, y1 + k1_y1/2, t0 + h/2)

            k3_y = h * func1(y0 + k2_y/2, y1 + k2_y1/2, t0 + h/2)
            k3_y1 = h * func2(y0 + k2_y/2, y1 + k2_y1/2, t0 + h/2)

            k4_y = h * func1(y0 + k3_y, y1 + k3_y1, t0 + h)
            k4_y1 = h * func2(y0 + k3_y, y1 + k3_y1, t0 + h)

            y0 = y0 + (k1_y + 2*k2_y + 2*k3_y + k4_y) / 6
            y1 = y1 + (k1_y1 + 2*k2_y1 + 2*k3_y1 + k4_y1) / 6

            t0 = t0 + h
            t_values.append(t0)
            y_values.append((y0, y1))

        return t_values, y_values
    

    #can be changed
    #discuss
    def func1_for_runge(self, y0, y1, t):
        return y1
    

    def euler_second_order(self, func, y0, y1, t0, t_end, h):
        t_values = [t0]
        y_values = [(y0, y1)]
        
        while t0 < t_end:
            y0_new = y0 + h * y1
            y1_new = y1 + h * func(y0, y1, t0)
            
            t0 = t0 + h
            t_values.append(t0)
            y_values.append((y0_new, y1_new))
            
            y0 = y0_new
            y1 = y1_new
        
        return t_values, y_values


    def predefined_formula(self, y0, y1, t):
        return -2 * y1 - 3 * y0


    def get_result_euler(self, h, t0, t1, y0, y1):

        t, y = self.euler_second_order(self.predefined_formula, y0, y1, t0, t1, h)

        # Вивід результатів
        result = []
        for i in range(len(t)):
            result.append([t[i], y[i][0], y[i][1]])

        return result
    
    
    def get_result_runge(self, h, t0, t1, y0, y1):
        t, y = self.runge_kutta_4(self.func1_for_runge, self.predefined_formula, y0, y1, t0, t1, h)
        
        # Вивід результатів
        result = []
        for i in range(len(t)):
            result.append([t[i], y[i][0], y[i][1]])

        return result
