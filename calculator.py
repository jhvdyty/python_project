
def div(num1, num2):
    try:    
        return num1 / num2
    except:
        print ("error! you cant / ", num2)
        return 0
    
def mul(num1, num2):
    return num1 * num2

def men(num1, num2):
    return num1 - num2
    
def pls(num1, num2):
    return num1 + num2


def main():
    while 1: 
        print ("entet first number: ")

        num1 = float(input())

        print ("entet second number: ")

        num2 = float(input())

        print ("entet the move / * - +: ")

        mov = str(input())

        result = float()


        if mov == "/":
            result = div(num1, num2)
        elif mov == "*":
            result = mul(num1, num2)
        elif mov == "-":
            result = men(num1, num2)
        elif mov == "+":
            result = pls(num1, num2)


        print ("yuore result is: ", result)
        print()

        #print ("if you wont to exit, type exit")

        exit = str(input())
        if exit == "exit":
            break



main()