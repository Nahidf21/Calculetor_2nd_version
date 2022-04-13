
def add(number1,number2):
    return number1+number2
def subtract(number1,number2):
        return number1-number2
def multiply(number1,number2):
    return number1*number2
def devide(number1,number2):
    return number1/number2
def oparetions1():
    for key in oparetions:
        print(key)
oparetions={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":devide
}
def calculetor():
    num1=float(input("Enter your first number: "))
    oparetions1()
    action="Yes"
    while action!="No":
        symtable=input("Select your symble: ")
        num2=float(input("enter the second number: "))
        answer1= oparetions[symtable](num1,num2)

        oparetions1()
        symtable2=input("Select your Symbol from the list: ")
        num3=float(input("Enter your third number: "))
        answer2=oparetions[symtable2](answer1,num3)
        print(answer2)
        if input("Select Yes or No ")=="Yes":
            num1= answer2
        else:
            action="No"
            calculetor()

calculetor()    

