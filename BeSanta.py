#Day 5 Exercise 1 - Be Santa!
item = input('What do you want for Christmas? ')
naughty_nice = input('HO HO HO. And have you been naughty? Or have you been nice? ')

#Put the following in a while loop

if naughty_nice == "nice":
    print('You shall have your %s !' % (item)) 
elif naughty_nice == "naughty": 
    print('Well then. Kick rocks kid! Rocks of coal! HO HO HO!')
else:
    print('I don\'t understand you kid! Say \"naughty\" or \"nice.\"')