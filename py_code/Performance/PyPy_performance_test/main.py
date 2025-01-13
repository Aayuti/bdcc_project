import timeit
import platform
import sys

# Factorial function for performance benchmarking
def factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def run_benchmark(implementation_name):
    setup_code = "from __main__ import factorial"

    # Test cases with increasing complexity
    test_cases = [1000, 1500, 2000]
    results = {}

    for complexity in test_cases:
        trials = [
            timeit.timeit(
                f"factorial({complexity})",
                setup=setup_code,
                number=10  # Number of repetitions per trial
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
    print("\n{}".format("=" * 40))
    print("Benchmark for {}".format(implementation_name))
    print("Python version: {}".format(platform.python_version()))
    print("\n{}".format("=" * 40))

    for complexity, metrics in results.items():
        print("\nComplexity {}:".format(complexity))
        print("  Min Time:    {:.4f} seconds".format(metrics['min_time']))
        print("  Max Time:    {:.4f} seconds".format(metrics['max_time']))
        print("  Total Time:  {:.4f} seconds".format(metrics['total_time']))
        print("  Avg Time:    {:.4f} seconds".format(metrics['average_time']))

def main():
    implementation_name = platform.python_implementation()
    results = run_benchmark(implementation_name)
    print_benchmark(results, implementation_name)

if __name__ == "__main__":
    sys.setrecursionlimit(10000)  # Optional: Increase recursion limit for larger factorials
    main()
