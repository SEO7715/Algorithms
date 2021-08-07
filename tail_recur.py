def r_sum(n):
    if n==1:
        return 1
    else:
        return n+r_sum(n-1)

print(r_sum(10))


def tr_sum(n, total=0):
    if n==0:
        return total
    else:
        return tr_sum(n-1, total+n)

print(tr_sum(10))