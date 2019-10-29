#Write a program to determine if a number is a Prime


import math

def isPrime(num):
  test = round(math.sqrt(num))
  while test > 1:
    if num % test == 0:
      return False
    test -= 1  
  return num >= 2

print(isPrime(2))
print(isPrime(3))
print(isPrime(93))


#Implement Sieve of Eratosthenes
def get_primes(num):
  arr = []
  while len(arr) < num + 1:      #initialize with array of size N all True values
    arr.append(True)

  arr[0] = False             #0 is not prime
  arr[1] = False             #1 is not prime

  i = 2
  while i * i <= num:
    if arr[i] == True:
      for j in range(i * 2, num + 1, i):
        arr[j] = False
    i += 1
  
  primes = [i for i in range(len(arr)) if arr[i]] 
  return primes

print(get_primes(30))