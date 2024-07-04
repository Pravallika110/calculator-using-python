def add(p,q):
    return p+q
def sub(p,q):
    return p-q
def multiply(p,q):
    return p*q
def divide(p,q):
    return p/q
print("please select the operation we want")
print("a ,add")
print("s,sub")
print("m, multiply")
print("d,divide")
while True:
    choice=input("please enter the choice(a/s/m/d):")
    if choice in ('a','s','m','d'):
        try:
         num1=int(input( "enter the first number"))
         num2=int(input("enter the second number"))
        except ValueError:
         print("valid number")
         continue
        if choice=='a':
            print(num1,"+",num2,"=",add(num1,num2))
        elif choice=='s':
            print(num1,"-",num2,"=",sub(num1,num2))
        elif choice=='m':
            print(num1,"*",num2,"=",multiply(num1,num2))
        elif choice=='d':
            print(num1,"/",num2,"=",divide(num1,num2))
            next_calculation = input("do another calculation?(yes/no):") 
            if next_calculation=="no":
                break
            else:
                print("invalid input")
    