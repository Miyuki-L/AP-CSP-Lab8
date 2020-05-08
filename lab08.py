#Helen Lin
#Start: 5/1/2020
#lab08

def multiples_of_3_5(n):
    """Project Euler Problem 1: Multiples of 3 and 5
    If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
    The sum of these multiples is 23.Find the sum of all the multiples of 3 or 5 below 1000.
    Takes in the input n and finds the multiples of 3 and 5 and then add it to the sum"""
    multiples = []
    num = 1
    #for loop
    while num < n:
        #if function to determine if divisable or not.
        if num%3 == 0 or num%5 == 0:
            #add the multiple to list if multiple of 3 or5
            multiples = multiples +[num]
        #increase the num
        num +=1
    #Return the sum of multiples
    return sum(multiples) 

#print(multiples_of_3_5(1000))

def prime_check(n,p_list):
    """
    This will determine if the number is a prime
    Preconditions: n is an int and p_list is a list of prime numbers
    it returns True or False depending if n is a prime number or not
    """
    for num in p_list:
        #divides the number by every number in the list if it is completely divisible then it is not a factor
        if n%num == 0:
            #the number is divisible by one of the numbers on the list return false
            return False
    #the number was a prime number since it was not divisble without remainders 
    return True

def largest_prime_factor(n):
    """Project Euler Problem 3: Largest Prime Factor
    The prime factors of 13195 are 5, 7, 13 and 29.What is the largest prime factor of the number 600851475143 ?
    where n is an int and the number whose largest factor you are looking for. """
    """ Andrews proposal to optimization.
    arostcles steive. set of number. mark all number that is not prime. testing square root of the number. appro
    aristosines seive method. take out multiples of 3 5 7 2 11. get to NOT squre but half of the largest number. can't be greater than half the largest number
    another vernbe prieme number determination
    recursion method to break down prime numbers. 
    Miller Rabin. 
    Pollard -rho """
    #let primelist be a starting list of basic, don't need two in the list as it could be easily controlled by itteration
    primelist=[3]
    #is prime num starts at five since 4 is even and not prime 
    is_prime_num = 5
    #Until half of the number since factors are all in pairs and the pair greater than 2 and half the number is 1 times the number. 
    while is_prime_num < n/2:
        #checks if the is_prime number is a prime or not. 
        if prime_check(is_prime_num,primelist) == True:
            # add it to the list of primes 
            primelist = primelist + [is_prime_num]
            #sees if its factor
            if n%is_prime_num ==0:
                #set equal to largest prime factor. 
                prime_factor = is_prime_num
        #increase by 2 so it avoids all even numbers since they aren't prime
        is_prime_num +=2
    
    return prime_factor

#print(largest_prime_factor(600851475143))

def largest_prime_factor_v2(num):
    """Project Euler Problem 3"""
    """Since you want factors then start determining the parinings. once you found a pair then there is nothing else that 
    facters perfect. e.g betweing pairing with 1 and pairng with 2 there is is not one between 1 and two that factors nicely. 
    There for once you found that something is divisible by something then worked on the dividend.
    Think Tree diagram learned solution from https://www.youtube.com/watch?v=InvK8aZ-dQA"""
    #Base divisor is 2 since everything is dividable by 1
    divisor = 2
    #divisor can't be bigger than the number since I'll be a fraction.
    while divisor < num:
        #see if num has factors
        if num%divisor ==0:
            #start working on its pairing since there won't be any other interger factor that works bigger than the pair of the one with 2
            num = num/divisor
            #reset the divisor
            divisor = 2
        # the divisor is not an factor so move up to the next interger divisor 
        else:
            divisor += 1
    return num
# print (largest_prime_factor_v2(600851475143))

#import sqrt for smallest multiple question
from math import sqrt

def smallest_multiple(upper_limit):
    """Project Euler Problem number 5
    2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
    What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
    
    perosnal brut force test method found that if the number is a perferct square of a number then have to had it to the list of multiples.
    Thinking behind: think if the range of multiples you need as a word bank. You only get to use that number once each
    time in dividing. So if its a perfect square or cube of a number you have to use that number twice but you can only use it 
    once. So that number has to be included in the products list.
    want everything that is prime or square of a number under the limit.  """
    #list of multiples that needs to be multiplied together in the end to get the desired number
    multiple_list =[]
    #starting multiple
    multiple = 2
    #divisor to check if it is a multiple of other numbers below
    divisor = 2
    while multiple < upper_limit:
        # blank in blank can be check to see if in list
        #blank.is_integer() can check if integer. 
        #squares automattically counts
        #check if it is a multiple of something
        while divisor < multiple:
            if multiple % divisor == 0:
                divisor=2

        #maybe for loop instead?

        






