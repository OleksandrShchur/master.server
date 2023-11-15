import math
import numpy as np

class SolverSecondDifferential:

    def __init__(self, h, t_0, t_end, a, b, tau):
        self.t_step = np.arange(t_0, t_end + h, h)
        self.m = int((t_end - t_0)/h) + 1
        print(self.m)
        self.x_step = [0] * self.m
        self.tau = tau
        self.a = a
        self.b = b
        self.h = h
        self.t_0 = t_0

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
    
    def ger_result_euler_cust(self):
        k = 0;
        x_tochne = [0] * self.m
        self.x_step[0] = self.phi(self.t_0)
        x_tochne[0] = self.exact(self.t_step[0])
        for i in range(1, len(self.t_step)):
            if (self.t_step[i - 1] - self.tau <= 0):
                self.x_step[i] = self.f_lessThanZero(self.x_step[i - 1], self.t_step[i], self.h);
            else:
                self.x_step[i] = self.f_moreThanZero(self.x_step[i - 1], self.t_step[i], self.h);
            x_tochne[i] = self.exact(self.t_step[i])

        # Вивід результатів
        result = []
        for i in range(len(self.t_step)):
            result.append([self.t_step[i], self.x_step[i], x_tochne[i]])

        return result

    def f_lessThanZero(self, x_i, t_i, h):
        return x_i + h * (self.a * x_i + self.b * self.phi(t_i - self.tau) + self.func(t_i))

    def f_moreThanZero(self, x_i, t_i, h):
        return x_i + h * (self.a * x_i + self.b * self.v(t_i) + self.func(t_i))

    def phi(self, x):
        return x + 4

    def func(self, t_i):
        return t_i - 1

    def v(self, t_i):
        for i in range(len(self.t_step)):
            if (t_i - self.tau >= self.t_step[i] and t_i - self.tau <= self.t_step[i + 1]):
                    return (t_i - self.tau - self.t_step[i])/self.h * self.x_step[i+1] + (self.t_step[i+1] - t_i + self.tau)/self.h * self.x_step[i]

        return 0;

    def exact(self, t):
        if (t < 0):
            return t + 4
        if (t < 1):
            return -8*math.exp(t) + 2*t +12
        return 24*t*math.exp(t-1) - (8*math.exp(1)+51)*math.exp(t-1)+ 5*t + 36
    # def exact(self, t):
    #     if (t < 0):
    #         return t + 4
    #     if (t < 1):
    #         return t*t - t + 4
    #     return t*t*t/3 -4*t*t + 6*t + 5/3

