## x = 5
#name = 'mack'
## y = 3.2
## true = True
## dir(name)
### print(name.upper())
### help()
### for i in range(3):
###    print(name)
## for i in range (3):
##    print(i)
## help(range)
## for i in range (1,5):
##    print (i)

## for i in range (2, 10, 2):
##    print(i)

## l_5 = list(range(5))
## for num in l_5:
##    print (num)
##    print()
##    print(num *2)
##    print()
## print (name[0:3])
## print (name[:7])
## print (name[0:4:3])
## print (name[0:4])
## def hello ():
##     Name= input ("Enter name: ")
##    print ("Hello " + Name)

## hello() 

## def blank():
##    print()

## def blank_3(): 
##    blank()
##    blank()
##    blank()

## def blank_9():
##    blank_3()
##    blank_3()
##    blank_3()

# numbers = [1,-5,2,-4,6,0,10,3]


##for number in numbers:
##    if number %2 == 0:
##        print(number, "is even")
##    else:
##        print (number, "is odd") 

##for number in numbers:
##    if number ==0:
##        print("Zero")
##    elif number > 0:
##        print ("Positive")
##    elif number < 0:
##        print("Negitive")        
       

## def even(x):
#    """enter number to be checked if even"""
##    if x % 2 == 0:
##        return True 
##print (even(4))


## def even(x):
##    return x % 2 == 0
## def odd(y):
##    return y % 2 ! = 0


##print(even(4))
##print(odd(5)) 

#for row in range(5):
#    print("row")
#    for col in range(5):
#        print (col,end='')
# print():




#def Pos_Neg(x):
#    for number in numbers:
#        if number == 0:
#            print("Zero")
#        else:
#            if number > 0:
#                print ("Positive")
#            else: 
#                print("Negative")

#for number in numbers:
#    print(number)
#    Pos_Neg(number)


#for row in range(1,11):
#    for col in range(1,row+1):
#        print('{:3}'.format(col),end='')
#    print()
        
    
#def hello():
#    name = input("Enter Name: ")
#    print( "Hello, " + name + " it's great to meet you!")
#hello()

def hello():
    name = input("Enter Name: ")
    print ("Hello {} nice to meet you!".format(name))
hello() 