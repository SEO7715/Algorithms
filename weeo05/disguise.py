def solution(clothes):
    answer = 1
    clothes_list = {}
    
    for element in clothes:
        key = element[1]
        value = element[0]
        if key in clothes_list:
            clothes_list[key].append(value)
        else:
            clothes_list[key] = [value]

    for value in clothes_list.values():
        answer *= (len(value) + 1)

    answer -= 1
    return answer

clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(clothes))