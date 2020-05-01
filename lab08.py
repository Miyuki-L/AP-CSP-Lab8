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
    pass



