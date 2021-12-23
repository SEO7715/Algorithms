new_id = "...!@BaT#*..y.abcdefghijklm"	

def solution(new_id):
    answer = ''
    # 대문자를 소문자로 변환
    new_id = new_id.lower()
    #  소문자, 숫자, 빼기, 밑줄, 마침표 제외 제거
    for char in new_id:
        if char.islower() or char.isdigit() or char == '-' or char == '_' or char == '.':
            #  .이 연속된 경우 --> . 추가 안함
            if answer and char == '.' and answer[-1] == '.':
                continue
            answer = answer + char
    # answer의 처음 또는 끝이 .인경우, '.' 제거
    answer = answer.strip('.')
    # answer가 빈문자열인 경우, 'a'로 넣어주기
    if not answer:
        answer = 'a'
    # answer 길이가 16자 이상일 경우, 15자까지 자르기
    if len(answer) >= 16:
        answer = answer[:15]
    # 15자로 자른 후, 처음과 끝에 '.' 제거
        answer = answer.strip('.')
        # answer길이가 2이하면, 길이가 3이될 때까지 answer의 마지막 문자 반복해서 붙여주기
    while len(answer) < 3:
        answer = answer + answer[-1]
    return answer

print(solution(new_id))