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

##def hello():
##    name = input("Enter Name: ")
##    print ("Hello {} nice to meet you!".format(name))
##hello() 



##i = 0
##i= i + 1
##i += 1

#number = int (input("Enter Number: "))
##number = int(number)
#print (type(number))


#while True: 
#     print ("Mack is God")
#count = int(input("Enter number: "))
#print("Oh My God!")
#while count > 0:
#    print(count)
#    count -= 1
#    if count < 1:  this line isnt needed. to get the same result, remove the print variable from the body of the while statement.
#print('What Happened To Virgil?')

#numbers = [10,5,-9,6,1,-2,-8,4,-1]
#pos = []
#neg = []

##for number in numbers:
##    if number > 0:
##        pos.append(number)
##    else:
##        neg.append(number)
#print(pos)
#print(neg)

#pos = [i for i in range(10) if i >0 ] 
#print(pos)

#list_numbers = []

#for i in range(3):
#    list_numbers.append(list(range(1,6)))
#1, 3, 13, 19, 25
#5, 14, 18, 20, 24
#6, 7, 15, 17, 23
#4, 8 ,9 ,10, 22
#2, 11, 12, 16, 21
#for i in list_numbers:
#    print(i) 

#import random 

#for i in range(10):
#    print(random.randint(1,25))
 
#number = [random.randint(1,25) for i in range (10)]
#print (number)

#numbers = [ i for i in range (1,25)]
#random.shuffle(numbers)
#print (numbers)


#shuffled = [22, 24, 21, 2, 25,
#8, 17, 14, 1, 7, 
#12, 10, 16, 3, 19, 
#15, 20, 13, 6, 11, 
#5, 4, 18, 23, 9]

#horses = [[],
#    [],
#    [],
#    [],
#    []
#]
#for i in range(5):
#    for j in range(5):#
#        horses[j].append( shuffled.pop())
# print(horses)

#for race in horses:
#    race.sort(reverse = True ) " this line makes a list from decending order"
#    race.sort()
#    print(race)


#    def last(x): 
#        return x[-1] 

#new_horses = sorted(horses, key=last, reverse=True) 
#print()
#for race in new_horses:
#    race.sort()
    
#print(new_horses)

#new_horses [0][2:]
#print(new_horses[0][2:]


#def time_table():
#    while True:
#        try:
#            x = int(input("Please Enter a Number: "))
#            for row in range(x):
#                for col in range(x):
#                    print(f"{row*col:3}", end = "")
#                print()
#        except ValueError:
#            print("A Number, Not a letter.: ")
#        q = input("Do you want another table? y/n ").lower()
#        if q[0] == "n":
#            break

#time_table()

def is_prime (num):
    for i in range(2,num):
        if num %i == 0:
            return False
    return True

test = [3,6,11,31]

for num in test:
    print(f"{num} is prime number  {is_prime(num)}")