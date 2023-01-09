"""numlength accepts one integer checks the length and returns it"""
def numlength(x):
    if(x <= -1):
        x = x*-1
    for i in range(1,10000):
        x = x/10
        if(x <= 1):
            return i
    print("what number are you trying to get the length of here, 10 to the 10000th power, nah")

"""test if a given number is a palindrome(if the number is the same backwards)"""
def isAPalindrome(x):
    if(x == 0):
        return True
    timesToRun = int(numlength(x) / 2)
    if(x < 0):
        x = x * -1
    x = str(x)
    print(timesToRun, x)
    for i in range(timesToRun):
        if(x[0 + i] != x[-1 - i]):
            return False
    return True