name = input ('Please enter your name ')
if len(name)< 3:
    print('Your name must be a mininum of 3 letters')
    name = input ('Please enter your name ')
if len (name)>20:
    print ('Your name must be under 20 letters')
    name = input ('Please enter your name ')
else:
        print('Welcome to the game   '+ name)
