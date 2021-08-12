N = int(input())

li = []  # N 문자열로 변환하여 저장받는 배열
calc = []
slices = []

sumstr = ''

cnt = 0  # 사이클 횟수를 누적하기 위한 변수 선언
sums = 0

if N < 10:
    N*10

# elif N == 0:
#     cnt = 1

string = str(N)  # N을 문자열로 변환
li = string    # li 배열에 N이 문자열 형태로 append

calc.append(int(li[0]))
calc.append(int(li[1]))   # 연산을 위해 calc에 li 원소 저장
calc.append(int)

sums = int(li[0])+int(li[1])    # 2 + 6 = 8이 sums에 대입

for i in range(1, 5):
    if sumstr != N:
        sums = int(calc[0])+int(calc[1])    # 8 = 2 + 6
        if sums >= 10:  # 만약 더한 값이 10보다 크면
            slices = str(N)  # 앞처럼 문자열로 변환 후
            sums = int(slices[1])   # 가장 오른쪽 자리 수를 sums에 대입

        calc[0] = calc[1]   # 2 <- 6
        calc[1] = int(sums)  # 6 <- 8

        sumstr = str(calc[1])+str(sum)

        cnt += 1

    else:
        break

    i = 1

print(cnt)