First_number = eval(input("Enter the first number : " ))
second_number= eval(input("Enter the second number : "))
#output =(First_number - second_number)*(First_number>second_number)+(second_number-First_number)*(First_number < second_number)
output=[First_number - second_number,second_number-First_number][second_number>First_number]
print(output)