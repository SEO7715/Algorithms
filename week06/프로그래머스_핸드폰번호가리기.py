phone_number = "01033334444"	

def solution(phone_number):
    # len_phone_number = len(phone_number)
    # after_phone_number = phone_number[-4:]
    # add_phone_number = len_phone_number - len(after_phone_number)
    # after_phone_number = '*'*add_phone_number + after_phone_number

    # return after_phone_number
    return '*'*(len(phone_number)-4) + phone_number[-4:]

print(solution(phone_number))