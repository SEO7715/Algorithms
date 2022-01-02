exp1 = "2x^5 + 3x^3 + 2x^1"	
exp2 = "6x^6 + 4x^4 + 3x^3 + 2x^2"


def solution(exp1, exp2):
    exp1, exp2 = map(str, exp1.split('+')), map(str, exp2.split('+'))	
    exp1_list, exp2_list = [], []
    result, new_result = [], []
    
    for char1 in exp1:
        char1 = char1.strip()
        exp1_list.append(char1)

    for char2 in exp2:
        char2 = char2.strip()
        exp2_list.append(char2)
        
    for char1 in exp1_list:
        for char2 in exp2_list:
            if char1[-1] == char2[-1]:
                after_char1 = char1.split('x')
                after_char2 = char2.split('x')
                new_char = int(after_char1[0]) + int(after_char2[0])
                result.append(str(new_char) + 'x' + after_char1[1]) 
                exp1_list.remove(char1)
                exp2_list.remove(char2)

    for char in exp1_list:
        result.append(char)
    for char in exp2_list:
        result.append(char)

    new_result = sorted(result, key = lambda x:x[-1], reverse=True)
    # for i in range(len_new_result):
    #     print(i)
    #     new_result.insert(i+1, '+')
    # print(new_result)

    # for index, case in enumerate(new_result):
    #     print(new_result[index])

    # print(new_result)
    # for _ in 
    # print(' + '.join(new_result))
    # str_new_result = ' + '.join(new_result)
    # str_new_result = '' ''.join(str_new_result)

    
    # each_str_new_result = str_new_result.split('+')
    # print(str_new_result)
    return new_result

print(solution(exp1, exp2))