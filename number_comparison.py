#Problem 2
first_number = input("What is the first number? ")
second_number = input("What is the second number? ")

first_number = int(first_number)
second_number = int(second_number)

if first_number > second_number:
    print(first_number, "is bigger")
else:
    print(second_number, "is bigger")