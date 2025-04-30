inputs = [1, 2, 3, 4.5]

weights =[
    [3, 8, 9, 1], 
    [2, 6, 8, -1], 
    [3, 5, 7, 8]
    ]

biases = [1, 5, 5]
output = []
bias_index = 0
for weight in weights:
    single_percep = 0
    for x in range(4):
        single_percep += inputs[x] * weight[x]
    output.append(single_percep + biases[bias_index])
    bias_index += 1

print(output)






