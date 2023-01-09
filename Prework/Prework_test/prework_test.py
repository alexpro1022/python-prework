#Write a function to print "hello_USERNAME!" USERNAME is the input of the function.
#the first line of the code has been defined as below.

def hello_name (user_name):
    """print Hello_USERNAME"""
    user_name = input("Enter your username: ")
    return user_name.upper()
    
user_name = hello_name(user_name=(input))
print ("Hello_"+user_name)

#question 2
#Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

def first_odds():
    return [x for x in range(1,100,2 ) if x % 2 != 0]
first_odds


#Question 3
#Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.

def max_num_in_list(a_list):

    high = a_list[0]
    for x in a_list:
        if x > high:
            high = x
    return high


a_list = [1,3,5,4,11,32,56,91,400]
print(max_num_in_list(a_list))

#Question 4
#Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).
def is_leap_year(a_year):

    a_year = int(input("Enter a leap year "))

    if (a_year % 4) == 0 and (a_year % 100) != 0 or (a_year % 400) == 0:
        print (bool(1))
    else:
        print (bool())
is_leap_year(a_year=(bool))


#Question 5
#Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.

 

def is_consecutive(a_list):
    return sorted(a_list)== list(range(min(a_list), max(a_list)+1))

number = [2,3,4,5,6,7]
print(is_consecutive(number))