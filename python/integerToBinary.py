from stack import Stack

def divBy2(decimalNum):
    s = Stack()
    
    while decimalNum > 0:
        remainder = decimalNum % 2
        s.push(remainder)
        decimalNum = decimalNum // 2


    binaryNum = ""
    while not s.is_empty():
        binaryNum += str(s.pop())

    return binaryNum


print(divBy2(242))
