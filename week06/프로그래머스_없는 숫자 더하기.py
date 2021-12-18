# # ver 1
# numbers = [1, 2, 3, 4, 6, 7, 8, 0]

# def solution(numbers):

#     number_list = [0,1,2,3,4,5,6,7,8,9]
#     check_number = []
    
#     for i in number_list:
#         if i not in numbers:
#             check_number.append(i)
        
#     return sum(check_number)

    
# print(solution(numbers))

# ver 2

def solution(numbers):
    number_list = [0,1,2,3,4,5,6,7,8,9]

    return sum(number_list) - sum(numbers)