import math as m

def sigmoid(value):
	res = 1/(1 + m.exp(-value))
	return 1 if value > 0 else 0

def solve_1(values, biases, inputs, outputs):
	for i, arr_input in enumerate(inputs):
		res_1 = sigmoid((values[0][0] * arr_input[0]) + (values[0][1] * arr_input[1]) + biases[0])
		res = sigmoid((values[1][0] * arr_input[0]) + (values[1][1] * arr_input[1]) + (values[1][2] * res_1) + biases[1])
		print(arr_input, res, outputs[i])

def solve_2(values, biases, inputs, outputs):
	for i, arr_input in enumerate(inputs):
		res_1 = sigmoid((values[0][0] * arr_input[0]) + (values[0][1] * arr_input[1]) + biases[0])
		res_2 = sigmoid((values[1][0] * arr_input[0]) + (values[1][1] * arr_input[1]) + biases[1])
		res = sigmoid((values[2][0] * res_1) + (values[2][1] * res_2) + biases[2])
		print(arr_input, res, outputs[i])

inputs = [(0, 0), (0, 1), (1, 0), (1, 1)]
outputs = [0, 1, 1, 0]

# Problem 1
values_p1 = [(1,1),(1,1,-2)]
biases_p1 = [-1.5,-0.5]
print('Problem 1')
solve_1(values_p1, biases_p1, inputs, outputs)

# Problem 2
values_p2 = [(1,1),(1,1),(1,-1)]
biases_p2 = [-0.5, -1.5, -0.5]
print('Problem 2')
solve_2(values_p2, biases_p2, inputs, outputs)

# Problem 3
values_p3 = [(-2,9.2),(4.3,8.8),(-4.5,5.3)]
biases_p3 = [-1.8, -0.1, -0.8]
print('Problem 3')
solve_2(values_p3, biases_p3, inputs, outputs)