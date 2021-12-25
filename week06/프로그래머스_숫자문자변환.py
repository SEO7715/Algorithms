s = "2three45sixseven"

#  ver 1
# str_number_list = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
# int_number_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# def solution(s):
#     answer = ''
#     new_s = ''
#     for case in s:
#         if case in int_number_list:
#             case = str_number_list[int(case)]
#         new_s += case
#     tmp = ''
#     for i in new_s:
#         tmp += i
#         if tmp in str_number_list:
#             tmp_index = str_number_list.index(tmp)
#             answer += int_number_list[tmp_index]
#             tmp = ''    
#     return int(answer)

# ver2

number_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

def solution(s):
    answer = s
    for key, value in number_dic.items():
        answer = answer.replace(key, value)
    return int(answer)

print(solution(s))