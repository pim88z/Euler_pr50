# Project Euler problem 50. Which prime, below one-million, 
# can be written as the sum of the most consecutive primes?

# initial values
max_length = 0
max_sum    = 0
i = 0
l = 0
sum = 0
sum_comp = 0
border   = 1000000
# Checking primality of a number
def is_prime(n):
    # Check if a number is prime
    if n < 2: 
         return False
    if n % 2 == 0:             
         return n == 2  
    # Sieve of Eratosthenes
    k = 3
    while k*k <= n:
         if n % k == 0:
             return False
         k += 2
    return True

# Making a list of all the primes under a certain border using the sieve of Eratosthenes
def primes(n):
    list = []
    primes = []
    list.append(2)
    i = 3
    while ( i <= n ): 
      list.append(i)
      i += 2
    # Sieve of Eratosthenes
    h = 2
    k = 3
    while k*k <= n:
      i = 0
      for j in range(h, len(list), 1): 
         if list[j] % k == 0:
            list[j] = 0
      h += 1
      k += 2
    for l in range(0, len(list), 1):
     if list[l] != 0:
      primes.append(list[l])
    return primes


prime_list = primes(border)

# Loop that determines the longest consecutive prime sum that itself is also prime under one milion
for i in range(0, len(prime_list)-1, 1): 
 l = 0
 sum = 0
 while ( sum < border ):
   sum = sum + prime_list[i]
   if is_prime(sum) == True:
      if l + 1 > max_length:
       max_length = l + 1
       max_sum    = sum
   i += 1
   l += 1
 i = 0

print ("Maximum length of consecutive prime sum that is itself also prime:", max_sum)
# Answer:  997651
