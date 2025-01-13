import time
import platform
import sys

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def run_benchmark(implementation_name):
    test_cases = [2000, 2050, 3000]
    results = {}

    for complexity in test_cases:
        trials = []
        for _ in range(5):
            start_time = time.time()
            factorial(complexity)
            end_time = time.time()
            trials.append(end_time - start_time)
        
        results[complexity] = {
            'min_time': min(trials),
            'max_time': max(trials),
            'total_time': sum(trials),
            'average_time': sum(trials) / len(trials)
        }

    return results

def print_benchmark(results, implementation_name):
    print("\n" + "=" * 40)
    print("Benchmark for " + implementation_name)
    print("Python version: " + platform.python_version())
    print("\n" + "=" * 40)

    for complexity, metrics in results.items():
        print("\nComplexity " + str(complexity) + ":")
        print("  Min Time:    " + "{:.4f}".format(metrics['min_time']) + " seconds")
        print("  Max Time:    " + "{:.4f}".format(metrics['max_time']) + " seconds")
        print("  Total Time:  " + "{:.4f}".format(metrics['total_time']) + " seconds")
        print("  Avg Time:    " + "{:.4f}".format(metrics['average_time']) + " seconds")

def main():
    implementation_name = platform.python_implementation()
    results = run_benchmark(implementation_name)
    print_benchmark(results, implementation_name)

if __name__ == "__main__":
    sys.setrecursionlimit(10000)
    main()
