# #  ver1
# def solution(x):
#     number_list = []
#     str_x = str(x)
#     for case in str_x:
#         number_list.append(int(case))
#     if x % sum(number_list) == 0:
#         return True
#     else:
#         return False

# ver2
def solution(x):
    check_x = x
    number_list = []
    while check_x != 0:
        number_list.append(check_x % 10)
        check_x = check_x // 10

    if x % sum(number_list) == 0:
        return True
    else:
        return False    

