import timeit

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

    # Single-threaded execution
    rectangle_area = calculate_rectangle_area(length, width)
    circle_area = calculate_circle_area(radius)

    print(f"Rectangle Area = {rectangle_area} square units")
    print(f"Circle Area = {circle_area} square units")

if __name__ == "__main__":
    execution_time = timeit.timeit("main()", setup="from __main__ import main", number=2)
    print(f"\nExecution Time: {execution_time:.4f} seconds")
