# Program that repeatedly prompts a user for integer numbers until the user enters 'done' and then provides the largest and the smallest numbers.

largest = None
smallest = None

while True:                         #Creates an infinite loop
    n = input('Enter a number: ')

    if n == 'done':                 #At the beginning of the loop, it tests if the user asked for the end of the program.
        break

    try:
        number = int(n)   #Preventing tracebacks caused by invalid inputs (such as strings different of "done") with a try-except structure.

    except:
        print('Invalid input')
        continue                #When the program recognizes a invalid input, it returns to the top of the loop and jumps to the next iteration.

    if largest is None:
        largest = number    #Testing if the variable "largest" is empty. If it is, then the user input fills it.

    elif number > largest:
        largest = number    #The next step is to verify if the new number is even largest than the last one.

    elif smallest is None:
        smallest = number   #Once the input is not largest than the largest so far, the program verifies if the variable "smallest" is empty.

    elif number < smallest:
        smallest = number   #In last case, the code verifies if the number is smallest than the smallest so far. If it isn't, none of the variables changes.

print('Maximum is', largest)
print('Minimum is', smallest) #Printing results.
