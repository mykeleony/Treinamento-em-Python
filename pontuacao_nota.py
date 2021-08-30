#Program that, gived a score between 0.0 and 1.0, prints a grade table. -> Training elif uses

s = input('Enter score: ')
score = float(s)

if score < 0.0 or score > 1.0:
    print('Score out of range. Please enter a valid number.')
    quit() #In cases that the input is out of range (smaller than 0 or greater than 1), a error message is printed and the program

elif score >= 0.9:
    print('A') #Testing each possibility of grade until the last one (F).

elif score >= 0.8:
    print('B')

elif score >= 0.7:
    print('C')

elif score >= 0.6:
    print('D')

elif score < 0.6:
    print('F')
