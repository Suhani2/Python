def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
print ("Select operation")
print ("1.Add")
print("2.Subtract")
print("3. Multiply")
print("4. Divide")
print("5. EXIT")

while True:
    choice = input("Enter choice:")
    if choice in ('1','2','3','4'):
        try:
            a = float(input("Enter first number:"))
            b = float(input("Enter second number:"))
        except:
            print("Choice doesnt exist?")
            continue

        if choice == '1':
            print (a, "+", b, "=", add(a, b))
        elif choice =='2':
            print (a, "-", b, "=", subtract(a, b))
        elif choice == '3':
            print(a, "*", b, "=", multiply(a,  b))
        elif choice == '4':
            print(a, "/", b, "=", divide(a, b))

    elif choice == '5':
        break

    else :
        print("Invalid choice")




