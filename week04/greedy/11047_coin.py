import sys
input = sys.stdin.readline


pcs, money = map(int, input().split())
coin_list = []
for _ in range(pcs):
    coin = int(input())
    coin_list.append(coin)

coin_list.sort(reverse=True)

status = 0
for coin in coin_list:
    status += money // coin
    money = money % coin

print(status)
    

