# continuation

def addition(n1, n2):
    return(n1+n2)

def subtraction(n1, n2):
    return(n1-n2)

def multiplication(n1, n2):
    return(n1*n2)

def division(n1, n2):
    return(n1/n2)

operations={
    "+": addition,
    "-": subtraction,
    "*": multiplication,
    "/": division
}
    
def calculator():
    n1 = float(input("Enter first number: "))

    for symbol in operations:
        print(symbol)
    should_continue=True

    while should_continue:
        operation_symbol=input("Choose an operation symbol: ")
        n2 = float(input("Enter next number: "))
        operation_function=operations[operation_symbol]
        result= operation_function(n1, n2)
        print(f"{n1} {operation_symbol} {n2} = {result}")

        if input("Enter 'c' to continue with the calculated number or 'x' to start again: ")== "c":
            n1=result
        else:
            should_continue=False
            calculator()
            
calculator()
    
        