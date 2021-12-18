# def solution(lottos, win_nums):
#     for _ in range(lottos):
#         lottos.remove(0)
#     # lottos = list(filter(0, lottos))
#     print(len(lottos))
#     return print(len(lottos))

# lottos = [44, 1, 0, 0, 31, 25]	
# win_nums = [31, 10, 45, 1, 6, 19]	
# result = [3, 5]

# solution()

lottos = [44, 1, 0, 0, 31, 25]
lottos = list(filter(0, lottos))
print(lottos)

for i in lottos:
    if i == 0:
        lottos.remove(0)

        print(lottos)
