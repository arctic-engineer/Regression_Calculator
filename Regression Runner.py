from dataclasses import dataclass

"""This program preforms a simple linear regression on user inputted data.
The user types in the x correlating y data and the program output the slope, y-intecept, R-squared."""

@dataclass
class DataPoint:
    x_coor: float 
    y_coor: float
    
@dataclass
class DataList:
    x_points: list[float]
    y_points: list[float]

@dataclass
class LinearRegressionOutput:
    m: float
    b: float
    r_squared: float

def convert_to_datalist(points: list[DataPoint]) -> DataList:
    x_points = []
    y_points = []
    for point in points:
        x_points.append(point.x_coor)
        y_points.append(point.y_coor)
    return DataList(x_points, y_points)

def sum_list(numbers: list[float]) -> float:
    total = 0.0
    for number in numbers:
        total += number
    return total

def sum_list_squared(numbers: list[float]) -> float:
    total = 0.0
    for number in numbers:
        total += number ** 2
    return total

def mean(numbers: list[float]) -> float:
    return sum_list(numbers) / len(numbers)
    
def standard_deviation(numbers: list[float]) -> float:
    average = mean(numbers)
    sum_squared_difference = 0.0
    for number in numbers:
        sum_squared_difference += (number - average) ** 2
    return (sum_squared_difference / len(numbers)) ** .5

def linear_regression(points: list[DataPoint]) -> LinearRegressionOutput:
    n = len(points)
    regression_input = convert_to_datalist(points)
    sum_x = sum_list(regression_input.x_points)
    sum_y = sum_list(regression_input.y_points)
    sum_x_squared = sum_list_squared(regression_input.x_points)
    list_xy = []
    for index in range(n):
        list_xy.append(regression_input.x_points[index] * regression_input.y_points[index])
    sum_xy = sum_list(list_xy)
    
    num_calc_m = (n * sum_xy) - (sum_x * sum_y)
    num_calc_b = (sum_y * sum_x_squared) - (sum_x * sum_xy)
    den_calc = (n * sum_x_squared) - (sum_x ** 2)
    
    m = num_calc_m / den_calc
    b = num_calc_b / den_calc
    
    average_y = mean(regression_input.y_points)
    r_calc_num = []
    r_calc_den = []
    for index in range(n):
        r_calc_num.append(((m * regression_input.x_points[index] + b) - regression_input.y_points[index]) ** 2)
        r_calc_den.append((regression_input.y_points[index] - average_y) ** 2)
    r_squared = 1 - sum_list(r_calc_num) / sum_list(r_calc_den)
    return LinearRegressionOutput(m,b,r_squared)
    
def take_input_list() -> list[DataPoint]:
    print()
    datapoints = []
    while True:
        user_input = input("Please enter the x then y value with a space or coma in between. Type done when you are finished entering data.")
        input_string = user_input.lower().strip()
        input_string = input_string.replace(',',' ')
        input_list = input_string.split(' ')
        pontecial_coor = []
        if (input_list == ['done']) or (input_list == ['complete']) or (input_list == ['finish']):
            break
        for text in input_list:
            try:
                float(text)
            except ValueError:
                print("Please enter a valid number or 'done' to finish.")
            pontecial_coor.append(float(text))
        if len(pontecial_coor) == 2:
            x_coor = float(pontecial_coor[0])
            y_coor = float(pontecial_coor[1])
            datapoints.append(DataPoint(x_coor, y_coor))
        else:
            print("There are not a single x and y value. Please enter only 2 numbers.")
    return datapoints


test_1 = [DataPoint(0,0), DataPoint(1, -2), DataPoint(2.5, -4), DataPoint(3.2, -5.3), DataPoint(5.8, -9)]
output_1 = linear_regression(test_1)
print('The slope is ' + ('%10.4f' % output_1.m).strip() + '.')
print('The y-intercept is ' + ('%10.4f' % output_1.b).strip() + '.')
print('The R-squared is ' +  ('%2.5f' % output_1.r_squared).strip() + '.') 

list_to_run = take_input_list()
if len(list_to_run) > 1:
    output = linear_regression(list_to_run)
    print('The slope is ' + ('%10.4f' % output.m).strip() + '.')
    print('The y-intercept is ' + ('%10.4f' % output.b).strip() + '.')
    print('The R-squared is ' +  ('%2.5f' % output.r_squared).strip() + '.') 
else:
    print("Not enough datapoints to run linear regression.")

    