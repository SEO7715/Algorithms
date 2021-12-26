# tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]	
# ticket_dic = {}

# for ticket in tickets:
#     departure = ticket[0]
#     destination = ticket[1]

#     try:
#         ticket_dic[departure].append(destination)

#     except:
#         ticket_dic[departure] = [destination]
#     ticket_dic[departure].sort()

# N = len(ticket_dic)
# print(len(ticket_dic)) #{'ICN': ['ATL', 'SFO'], 'SFO': ['ATL'], 'ATL': ['ICN', 'SFO']}
# visited = [False] * N

# def dfs(node):
#     if not visited[node]:
#         visited[node] = True
#         for next in ticket_dic[node]:
#             print(next)

# print(dfs("ICN"))
