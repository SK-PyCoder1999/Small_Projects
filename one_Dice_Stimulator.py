import random
# r=random.random() ,it can generate(return) any random number (in float format).
# r=random.randint(1,6) ,it returns a random integer in range [start, end] including the end points.    
print("--> Dice Stimulator <--")
x='yes'
while x == 'yes' :
    r=random.randint(1,6)
    print('---------')
    if r == 1 :
        print('[       ]')
        print('[   0   ]')
        print('[       ]')
    elif r == 2 :
        print('[       ]')
        print('[ 0   0 ]')
        print('[       ]')
    elif r == 3 :
        print('[   0   ]')
        print('[   0   ]')
        print('[   0   ]')
    elif r == 4 :
        print('[ 0   0 ]')
        print('[       ]')
        print('[ 0   0 ]')
    elif r == 5 :
        print('[ 0   0 ]')
        print('[   0   ]')
        print('[ 0   0 ]')
    elif r == 6 :
        print('[ 0   0 ]')
        print('[ 0   0 ]')
        print('[ 0   0 ]')
    print('---------')
    x=input("For Roll the Dice again press 'yes'. ")
else:
    print("Ok, Stimulator is closed now.")