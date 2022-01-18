n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]


def solution(n, arr1, arr2):
    answer = []

    for i in range(n):
        x = bin(arr1[i] | arr2[i])[2:]
        x = x.replace("1", "#")
        x = x.replace("0", " ")
        
        if len(x) != n:
            x = " "*(n-len(x)) + x
        answer.append(x)

    return answer