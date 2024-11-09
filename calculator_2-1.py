import math

#input
while True:
    numb = int(input("Number is :  "))
    op = input("Operation :  ")
    result = 1

    #process

    if op == "√":
        result = math.sqrt(numb)
    elif op == "sin":
        num = math.radians(numb)
        result = math.sin(num)
    elif op == "cos":
        num = math.radians(numb)
        result = math.cos(num)
    elif op == "tan":
        if numb != 90 :
            num = math.radians(numb)
            result = math.tan(num)
        else:
            result = "Not defined"
    elif op == "cot":
        if numb != 0 :
            num = math.radians(numb)
            result = 1 / math.tan(num)
        else:
            result = "Not defined"
    elif op == "fact":
        result = math.factorial(numb)
        #for i in range(1, numb+1):
            #result = result * i
    elif op == "exit" :
        break
    
    else:
        result = "the operation is not defined"

    #output

    print("The asnwer is :  ", result)

