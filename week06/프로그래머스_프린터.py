from collections import deque

priorities = [2, 1, 3, 2]	
location = 2


def solution(priorities, location):
    priorities = deque(priorities)

    target_index = location
    answer = 0
    while True:
        x = priorities.popleft()
        if len(priorities) == 0:
            answer = 1
            return answer
        if x >= max(priorities):
            answer += 1
            # 출력한 대상이 target인 경우
            if target_index == 0:
                return answer
            # 출력한 대상이 target이 아닌 경우
            else:
                target_index -= 1
        else:
            priorities.append(x)
            if target_index == 0:
                target_index = len(priorities)-1
            else:
                target_index -= 1

print(solution(priorities, location))