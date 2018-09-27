# lianxi.py
def outsum(lower,upper,mardin = 0):
    blanks = " "* mardin
    print(blanks,lower,upper)
    if lower > upper:
        print(blanks,0)
        return 0
    else:
        result = lower +outsum(lower+1,upper,mardin+4)
        print(blanks,result)
        return result
print(outsum(2,10))