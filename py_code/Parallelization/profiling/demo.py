# import time
# import multiprocessing
# import cProfile

# #is prime: 

# def is_prime(num):
#     if num < 2: 
#         return False
#     for i in range (2, int(num ** 0.5) +1):
#         if i % 2 == 0:
#             return False

#     return True

# #check all primes in range 
# def  check_prime_range(start, end):
#     primes = [] 
#     for num in range(start, end):
#         if is_prime(num):
#             primes.append(num)
    
#     return primes

# def collect_results(res):
#     global all_primes
#     all_primes = []

# def main():
#     global all_primes
#     all_primes = []

#     # Define the range for prime number calculation
#     RANGE_START = 1
#     RANGE_END = 1_000_000
#     NUM_PROCESSES = multiprocessing.cpu_count()  # Use all available CPUs

#     # Split the range into chunks for each process
#     step = (RANGE_END - RANGE_START) // NUM_PROCESSES
#     ranges = [(RANGE_START + i * step, RANGE_START + (i + 1) * step) for i in range(NUM_PROCESSES)]

#     # Use multiprocessing to parallelize the computation
#     start_time = time.time()
#     with multiprocessing.Pool(processes=NUM_PROCESSES) as pool:
#         # Map the ranges to worker processes
#         results = pool.starmap(check_prime_range, ranges)

#     # Flatten the list of primes
#     all_primes = [prime for sublist in results for prime in sublist]
#     end_time = time.time()

#     print(f"Total primes found: {len(all_primes)}")
#     print(f"Time taken with {NUM_PROCESSES} processes: {end_time - start_time:.2f} seconds")

# # Function to profile the script
# def profile_main():
#     cProfile.run('main()')

# if __name__ == "__main__":
#     profile_main()  # Profile the main function
import time
import multiprocessing
import cProfile

# Factorial sum function
def factorial_sum(num):
    """Calculate the sum of factorials of the digits of a number."""
    def factorial(n):
        if n == 0 or n == 1:
            return 1
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

    return sum(factorial(int(digit)) for digit in str(num))

# Check for numbers with a specific property in a range
def check_factorial_property_range(start, end):
    """Find numbers whose factorial sum matches the number itself."""
    results = []
    for num in range(start, end):
        if factorial_sum(num) == num:  # Condition: sum of factorial of digits equals the number
            results.append(num)
    return results

# Collect results
def collect_results(res):
    global all_results
    all_results = []

# Main function
def main():
    global all_results
    all_results = []

    # Define the range for factorial property calculation
    RANGE_START = 1
    RANGE_END = 10_000  # Smaller range for factorial computations
    NUM_PROCESSES = multiprocessing.cpu_count()  # Use all available CPUs

    # Split the range into chunks for each process
    step = (RANGE_END - RANGE_START) // NUM_PROCESSES
    ranges = [(RANGE_START + i * step, RANGE_START + (i + 1) * step) for i in range(NUM_PROCESSES)]

    # Use multiprocessing to parallelize the computation
    start_time = time.time()
    with multiprocessing.Pool(processes=NUM_PROCESSES) as pool:
        # Map the ranges to worker processes
        results = pool.starmap(check_factorial_property_range, ranges)

    # Flatten the list of results
    all_results = [result for sublist in results for result in sublist]
    end_time = time.time()

    # Print the results
    print(f"Total numbers found: {len(all_results)}")
    print(f"Numbers satisfying the condition: {all_results}")
    print(f"Time taken with {NUM_PROCESSES} processes: {end_time - start_time:.2f} seconds")

# Function to profile the script
def profile_main():
    cProfile.run('main()')

if __name__ == "__main__":
    profile_main()  # Profile the main function
