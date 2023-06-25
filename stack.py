def stack():
    stack=[]
    return stack
def isempty(stack):
    return len(stack)==0
def push(stack,item):
    stack.append(item)
    print("pushed item:"+item)
def pop(stack):
    return stack.pop()

s=stack()
push(s,str(2))
push(s,str(3))
push(s,str(4))
push(s,str(7))
print(s)
pop(s)
print(s)

