def altInt(num):
    
    AW = [0 for i in range(0, num+1)]

    # base cases inc. 0 to 5
    AW[0] = 0
    AW[1] = 1
    AW[2] = 2
    AW[3] = 4
    AW[4] = 7

    # iterate from 5 to num
    for i in range(5, num+1):
        # [i - int to be used]
        AW[i] = AW[i-1] + AW[i-2] + AW[i-3]
        
    return AW[num]

# define num
print(altInt(5))