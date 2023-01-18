def max_num(num1,num2,num3):
    if num1 > num2 and num1 > num3:
        return "num1 is the largest"
    elif num2 > num1 and num2 > num3:
        return "num2 is the largest"
    elif num3 > num1 and num3 > num2:
        return "num3 is the largest"
    else:
        return "it's a tie"

print(max_num(-10,0,10))
print(max_num(-10,5,-30))
print(max_num(-5,-10,-10))
print(max_num(2,3,3))