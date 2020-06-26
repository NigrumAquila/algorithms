def reg_t(fback, reg): 
    count1 = 0
    for j in range(len(fback)):
        if reg[j] == fback[j] == '1':
            count1+=1 
    reg2 = str(count1%2)+reg[:-1]
    return(reg2)
 
def max_len(fback): 
    t=2**len(fback)-1 
    reg_all = ['1'*len(fback)] 
    while True:
        if reg_t(fback, reg_all[-1]) in reg_all:
            break
        reg_all += [reg_t(fback, reg_all [-1])]
 
    return len(reg_all) == t
 
n=8
t=2**n-1
 
for i in range(1, t):
   if max_len(bin(i)[2:].zfill(n)):
        print((bin(i)[2:].zfill(n)))