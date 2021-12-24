array = [1, 5, 2, 6, 3, 7, 4]	
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]	

def solution(array, commands):
    result = []
    for i in range(len(commands)):
        start = commands[i][0] -1
        end = commands[i][1]
        standard = commands[i][2]-1
        new_array = array[start:end]
        new_array.sort()
        result.append(new_array[standard])
    return result

print(solution(array, commands))