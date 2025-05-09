# Question 2: Prime Number Analyzer
# Let the user input a range of numbers.
# Use a function to check if a number is prime.
# Write all prime numbers in that range to a file, one per line.

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_number_analyzer():
    start = int(input("Enter start of range: "))
    end = int(input("Enter end of range: "))
    
    prime_numbers = [str(num) for num in range(start, end + 1) if is_prime(num)]
    
    with open('prime_numbers.txt', 'w') as f:
        f.write('\n'.join(prime_numbers))
    
    print(f"Prime numbers written to 'prime_numbers.txt'.")

# Run this function
prime_number_analyzer()
