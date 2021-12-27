answers = [1,2,3,4,5]	

def solution(answers):
    N = len(answers)
    result= []
    count_list = [0, 0, 0]
    first_number_list, second_number_list, third_number_list = [1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    new_first_number_list, new_second_number_list, new_third_number_list = [], [], []

    for _ in range(N):
        
        if len(first_number_list) > N:
            break
        for i in range(len(first_number_list)):
            new_first_number_list.append(first_number_list[i%N])

        if len(new_second_number_list) > N:
            break
        for i in range(len(second_number_list)):
            new_second_number_list.append(second_number_list[i%N])

        if len(new_third_number_list) > N:
            break
        for i in range(len(third_number_list)):
            new_third_number_list.append(third_number_list[i%N])

    print(new_first_number_list, new_second_number_list, new_third_number_list)

    for i in range(N):
        if new_first_number_list[i] == answers[i]:
            count_list[0] += 1
        if new_second_number_list[i] == answers[i]:
            count_list[1] += 1
        if new_third_number_list[i] == answers[i]:
            count_list[2] += 1
    print(count_list)

    for i in range(len(count_list)):        
        if count_list[i] == max(count_list):
            result.append(i+1)
        if result and count_list[i] > max(result):
            result.clear()
            result.append(i+1)

    return result

print(solution(answers))