#in this program edge csaes also covered like  "]))}",
#  "(()", and "([])"

#import stack
#from stackp.py file
from stack import Stack

#parenthesis matching function
def isMatch(p1, p2):
    if p1 == "(" and p2 == ")":
        return True
    elif p1 == "{" and p2 == "}":
        return True
    elif p1 == "[" and "]":
        return True
    else:
        return False

# is parenthesis balanced function
def isParenBalanced(parenString):
    s = Stack() # Stack object
    isBalanced = True
    index = 0       #current index/ position
# loop to iterate over for all parenthesis string
    while index < len(parenString) and isBalanced:
        paren = parenString[index]
        if paren in "({[":
            s.push(paren)
        else:
            if s.is_empty():
                isBalanced = False
            else:
                top = s.pop()
                if not isMatch(top, paren):
                    isBalanced = False
        index += 1

    if s.is_empty() and isBalanced:
        return True
    else:
        return False

#Main fuction
print(isParenBalanced("())"))
