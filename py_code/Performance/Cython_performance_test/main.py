import timeit
import platform
import sys
from factorial_benchmark import factorial  # Import from the Cython file


# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     return n * factorial(n - 1)


def run_benchmark(implementation_name):
    setup_code = "from factorial_benchmark import factorial"  # Import the Cython function

    test_cases = [2000, 2500, 3000]
    results = {}

    for complexity in test_cases:
        trials = [
            timeit.timeit(
                f"factorial({complexity})",
                setup=setup_code,
                number=10
            ) for _ in range(5)
        ]
        results[complexity] = {
            'min_time': min(trials),
            'max_time': max(trials),
            'total_time': sum(trials),
            'average_time': sum(trials) / len(trials)
        }

    return results

def print_benchmark(results, implementation_name):
    print(f"\n{'=' * 40}")
    print(f"Benchmark for {implementation_name}")
    print(f"Python version: {platform.python_version()}")
    print(f"\n{'=' * 40}")

    for complexity, metrics in results.items():
        print(f"\nComplexity {complexity}:")
        print(f"  Min Time:    {metrics['min_time']:.4f} seconds")
        print(f"  Max Time:    {metrics['max_time']:.4f} seconds")
        print(f"  Total Time:  {metrics['total_time']:.4f} seconds")
        print(f"  Avg Time:    {metrics['average_time']:.4f} seconds")

def main():
    implementation_name = platform.python_implementation()
    results = run_benchmark(implementation_name)
    print_benchmark(results, implementation_name)

if __name__ == "__main__":
    sys.setrecursionlimit(10000)
    main()
