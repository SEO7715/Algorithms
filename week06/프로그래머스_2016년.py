a = 5
b = 24

# def 요일계산(tmp):
#     if tmp % 7 == 0:
#         return "THU"
#     if tmp % 7 == 1:
#         return "FRI"
#     if tmp % 7 == 2:
#         return "SAT"
#     if tmp % 7 == 3:
#         return "SUN"
#     if tmp % 7 == 4:
#         return "MON"
#     if tmp % 7 == 5:
#         return "TUE"
#     if tmp % 7 == 6:
#         return "WED"

# def solution(a, b):
#     if a == 1:
#         tmp = 0 + b
#     if a == 2:
#         tmp = 31 + b
#     if a == 3:
#         tmp = 60 + b
#     if a == 4:
#         tmp = 91 + b
#     if a == 5:
#         tmp = 121 + b
#     if a == 6:
#         tmp = 152 + b 
#     if a == 7:
#         tmp = 182 + b
#     if a == 8:
#         tmp = 213 + b
#     if a == 9:
#         tmp = 244 + b
#     if a == 10:
#         tmp = 274 + b
#     if a == 11:
#         tmp = 305 + b
#     if a == 12:
#         tmp = 335 + b
#     return 요일계산(tmp)


# print(solution(a, b))
def solution(a, b):
    month_list = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    calculate_day = sum(month_list[:a] + b)
    days = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
    return days[calculate_day % 7]