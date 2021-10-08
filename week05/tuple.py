def solution(s):
    answer = []
    s = s[2:-2]
    s = s.split("},{")
    print(s)
    s.sort(key=len)
    for i in s:
        check_i = i.split(',')
        for j in check_i:
            if int(j) not in answer:
                answer.append(int(j))
    return answer

s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
print(solution(s))