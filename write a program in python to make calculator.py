first_number= input("what is first_number  :  ")
operator = input("Enter the operators of your choice  (+,-,*,/,%)  :  ")
second_number= input("what is second_number : ")
first_number = int(first_number)
second_number= int(second_number)
if operator =="+" :
    print(first_number + second_number)
elif operator == "-" :
    print(first_number - second_number)
elif operator == "-" :
    print(first_number - second_number)
elif operator == "*" :
    print(first_number * second_number)
elif operator == "/" :
    print(first_number / second_number)
elif operator == "%" :
    print(first_number % second_number)
else :
    print("invalid input")