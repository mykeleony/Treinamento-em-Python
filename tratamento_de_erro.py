#Program that calculates a employee's payment considering overtime (work time over 40 hours that results in a 50% rate raise) and treating errors.

h = input('Enter hours: ')
r = input('Enter rate per hour: ')

try:
    hrs = float(h)
    rate = float(r) #Ensuring that a number is inserted.
except:
    print('Error, please enter numeric input')
    quit() #Closes the program when a error show up

if hrs > 40.0:
    pay = ((hrs-40.0)*1.5*rate)+(40.0*rate) #Raises payment when there is overtime
else:
    pay = hrs*rate #If there is no overtime, the calculus occurs normally.

print(pay) #Printing the payment at the end.
