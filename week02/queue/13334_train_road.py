import sys
input = sys.stdin.readline


n = int(input())
people_spot = [list(map(int, sys.stdin.readline().strip().split()))for _ in range(n)]
road_limit = int(input())

people_spot.sort()

print(people_spot)

for spot in people_spot:
    spot_distance = abs(spot[1] - spot[0])

    if spot_distance > road_limit:
        continue
