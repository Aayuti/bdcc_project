import timeit
from concurrent.futures import ThreadPoolExecutor

# Define rectangle area calculation
def calculate_rectangle_area(length, width):
    return length * width

# Define circle area calculation
def calculate_circle_area(radius):
    import math
    return math.pi * radius * radius

def main():
    # Generate a larger number of iterations for testing
    num_iterations = 1000000
    length, width = 5, 10
    radius = 7

    with ThreadPoolExecutor() as executor:
        # Submit tasks to the executor for parallel execution
        future_rectangle = executor.submit(calculate_rectangle_area, length, width)
        future_circle = executor.submit(calculate_circle_area, radius)

        # Get the results
        rectangle_area = future_rectangle.result()
        circle_area = future_circle.result()

    print(f"Rectangle Area = {rectangle_area} square units")
    print(f"Circle Area = {circle_area} square units")

if __name__ == "__main__":
    execution_time = timeit.timeit("main()", setup="from __main__ import main", number=2)
    print(f"\nExecution Time: {execution_time:.4f} seconds")
