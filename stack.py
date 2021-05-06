'''
Stack is a linear data structure which follows a particular order in which the operations are performed. 
The order may be LIFO(Last In First Out) or FILO(First In Last Out).
'''
#Function to create a stack
def create_stack():
    stack=[]
    return stack
#Function for isempty operation
def isempty(stack):
    if len(stack)==0:
        return True
    else:
        return False
#Function for push operation
def push(stack,ele):
    stack.append(ele)
    print(ele,'pushed into stack')

#Function for pop operation
def pop(stack):
   if isempty(stack):
       print('Nothing to pop,stack is empty')
   else:
       print(stack.pop(),'popped from stack')

#Function for stacktop operation
def stacktop(stack):
    print('top ele of stack is:' , stack[len(stack)-1])

a=create_stack()
push(a,20)
push(a,30)
pop(a)
stacktop(a)
