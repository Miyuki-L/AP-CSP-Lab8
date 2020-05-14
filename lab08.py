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

def smallest_multiple(upper_limit):
    """Project Euler Problem number 5
    2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
    What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
    
    perosnal brut force test method found that if the number is a perferct square of a number then have to had it to the list of multiples.
    Thinking behind: think if the range of multiples you need as a word bank. You only get to use that number once each
    time in dividing. So if its a perfect square or cube of a number you have to use that number twice but you can only use it 
    once. So that number has to be included in the products list.
    want everything that is prime or square of a number under the limit.
    Solution number 232792560  """
    #list of multiples that needs to be multiplied together in the end to get the desired number
    multiple_list =[]
    #starting multiple
    multiple = 2

    #prevent things like 2^4 added and 4^2 added which makes thing doubled.
    powers_added = []
    #loop to find the primes under the upperlimit    
    while multiple < upper_limit:
        #find primes. add to Multiple list. Alright if the list has non primes since it not looking for primes
        if prime_check(multiple,multiple_list):
            multiple_list= multiple_list + [multiple]

        exponent=2
        #checks if the number to a certain power is w/in the boundary
        while multiple**exponent <upper_limit:
            #make sure it that power hasn't been added 
            if (multiple**exponent in powers_added) == False:
                #add one more of the factor to the list since to create n^2 you need to have 2 n's in your "word bank"
                multiple_list = multiple_list + [multiple]
                powers_added = powers_added + [(multiple**exponent)]
            exponent += 1  
        multiple += 1
        #without the powers added thing the number was 4 time greater than the solution. with it took out all the multiples needed.

    #multiply up all the multiples.
    total = 1

    for num in multiple_list:
        total = total*num
        
    return total, multiple_list, powers_added
    #adding the squares to the list
#print(smallest_multiple(20))

def create_list(ul, ll=1):
    """Creates a list of all the natural numbers between the lower limit ll if not stated would be one. until 
    the upper limit"""
    return list(range(ll,ul+1))

def sum_square_difference(n):
    """Project Euler Problem 6
    The sum of the squares of the first ten natural numbers is,1^2+2^2+...+102=385The square of the sum of 
    the first ten natural numbers is,(1+2+...+10)^2=552=3025. Hence the difference between the sum of the squares 
    of the first ten natural numbers and the square of the sum is 3025−385=2640.Find the difference between the
    sum of the squares of the first one hundred natural numbers and the square of the sum
    where n is the upper limit of numbers """
    #sums up all the numbers then squares it
    sum_squared = (sum(create_list(n)))**2

    # sum of all the numbers first squared then summed.
    squared_sum = 0
    #loops over every number 
    for num in create_list(n):
        squared_sum += num**2

    #return the difference between the squares
    return sum_squared - squared_sum

#print (sum_square_difference(100))

def collatz_sequence(start,dict={}):
    """Part of Project Euler Problem 14
    The following iterative sequence is defined for the set of positive integers:
    n → n/2 (n is even)
    n → 3n + 1 (n is odd)
    Using the rule above and starting with 13, we generate the following sequence:
    13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
    It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not
    been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1. Which starting number,
    under one million, produces the longest chain? 
    NOTE: Once the chain starts the terms are allowed to go above one million."""
    #let num = upper so that we keep a upper as is 
    num = start
    #let terms be the number of steps so we'll know how many steps are in the chain
    steps = 0
    sequence = []
    while num > 1:
        #list of the numbers in the sequense
        sequence.append(num)
        #checks if the number is in the dictionary 
        #if even
        if num%2==0:
            #add to dictionary where keeps number of steps and the number
            num=int(num/2)
        #odd then add the number times 3 plus one.
        else:
            num = num*3 +1
        steps += 1
    return sequence, steps, start

def longest_collatz_sequence(upper):
    """Project Euler Problem 14 
    Although it has not
    been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1. Which starting number,
    under one million, produces the longest chain? 
    NOTE: Once the chain starts the terms are allowed to go above one million.
    maybe use recursion and dict change the terms into steps again. and then just add steps if already did the number"""
    longest_collatz=0
    start_num=0
    num = 2
    while num < upper:
        #checks if the sequence has a longer chain
        if longest_collatz < collatz_memoized(num):
            #store the number of steps and which number it was 
            longest_collatz = collatz_memoized(num)
            start_num = num
        num +=1
    return start_num

def collatz_memoized(start,dict={}):
    steps = 0
    num = start
    #checks if in dictionary
    if start in dict:
        return dict[start]
    else:
        while num > 1:
            #checks if in dictionary 
            if num in dict:
                #if its in the dicitonary add the steps and end it
                return steps + dict[num]
            #if even
            if num%2 == 0:
                num = int(num/2)
            #if odd
            else: 
                num = num*3 + 1
            steps += 1
        #store in dictionary. 
        dict[start] = steps 
        return dict[start]
#print(collatz_memoized(13))
print(longest_collatz_sequence(1000000))


        




