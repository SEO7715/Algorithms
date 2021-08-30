pat='ABXAB'

def computeLPS(pat, lps):
    leng = 0

    # 항상 lps[0]==0이므로 while문은 i==1부터 시작한다.

    i = 1
    while i < len(pat): # ir
        if pat[i] == pat[leng]:
            leng += 1
            lps[i] = leng
            i += 1
        
        else:
            if leng != 0:
                leng = lps[leng-1]
            else:
                lps[i] = 0
                i += 1

