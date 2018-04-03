
 ## 1 pair-euler, 2d- euler advanced, 3d- R-Cutta, 4- x-error, 5- hop error
import math
# main class that provide all calculatin based on predifined conditions and some input form user. Create array of lists with values on  Y axis.

class Calculations():
    x_points = []
    y_values = []

    def solve_exact(self,  ticks, hop):     # provide Y values for exact solution
        global y_values
        exact_solution = []
        for i in range(ticks):
            x = x_points[i]
            y = x * math.sqrt(1 + 2 * math.log(x))
            exact_solution.append(y)
        y_values.append(exact_solution)

    def run_euler_adv(self, ticks, hop, y0):    # provide Y values for Euler advanced algorithm  solution
        global y_values
        euler_adv_solution=[]
        euler_adv_solution.append(y0)
        for i in range(ticks - 1):
            y = euler_adv_solution[i]
            euler_adv_solution.append(y + hop * self.func(x_points[i] + hop / 2, y + hop / 2 * self.func(x_points[i], y)))
        y_values.append(euler_adv_solution)

    def run_euler(self, ticks, hop, y0):    # provide Y values for Euler algorithm  solution
        global y_values
        euler_solution=[]
        euler_solution.append(y0)
        for i in range(ticks - 1):
            y = euler_solution[i]
            euler_solution.append(y + hop * self.func(x_points[i],y))
        y_values.append(euler_solution)

    def run_cutta(self, ticks, hop, y0):    # provide Y values for Runge-Cutta algorithm  solution
        global y_values
        cutta_solution =[]
        cutta_solution.append(y0)
        for i in range(ticks - 1):
            k1=self.func(x_points[i],cutta_solution[i])
            k2=self.func(x_points[i] + hop / 2, cutta_solution[i] + hop * k1 / 2)
            k3=self.func(x_points[i] + hop / 2, cutta_solution[i] + hop * k2 / 2)
            k4=self.func(x_points[i] + hop, cutta_solution[i] + hop * k3)
            result=cutta_solution[i] + hop /6 * (k1 +2 * k2 + 2 * k3 + k4)
            cutta_solution.append(result)
        y_values.append(cutta_solution)

    # 1- euler, 2- euler adv, 3- cutta
    def x_error_plot(self, mode):     # provude Y values for dependance of error on value of Y by using abs value of difference between exact solution and
        # values provided by methods
        result=[]
        exact= y_values[0]
        method_values= y_values[mode]
        for i in range (len(y_values[0])):
            result.append(math.fabs(exact[i]-method_values[i]))
        return result

    def hop_error_plot(self, start, end, hop, mode):        # given minimal  and maximum number of steps for running algorithms, calculate Y values as max positive
        # value of error.
        ticks = int((end - start) / hop + 1)
        errors = []
        for i in range(ticks):
            calculation = Calculations(start + i * hop)
            exact = calculation.get_y()[0]
            approximation = calculation.get_y()[mode]
            biggest_error = 0
            for j in range(len(exact)):
                delta = math.fabs(approximation[j] - exact[j])
                if delta > biggest_error : biggest_error = delta
            errors.append(delta)
        return errors

    def get_results(self, mode):
        return y_values[mode]

    def func(self, x, y):
        return y / x + x / y

    def __init__(self, num_of_ticks, x0 = 1, y0 = 1, X = 2.3 ):     # main method get data form user and run basic methods
        global x_points
        global y_values
        num_of_ticks= int(num_of_ticks)
        hop = float((X-x0)/(num_of_ticks))
        num_of_ticks+=1
        x_points=[]
        y_values=[]
        for i in range(int(num_of_ticks)):
            x_points.append(x0+i*hop)
        self.solve_exact(num_of_ticks, hop)
        self.run_euler(num_of_ticks, hop, y0)
        self.run_euler_adv(num_of_ticks, hop, y0)
        self.run_cutta(num_of_ticks, hop, y0)

    def get_y(self):
        return y_values

    def get_x(self):
        return x_points


