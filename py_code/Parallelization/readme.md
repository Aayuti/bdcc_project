## Basic introduction to multithreading 

multithreading is useful when we need to streamline tasks for effcient use of resources and memory. This is possible as threads share the same memory and data space. 

The best application of python mutlithreading in python is for tasks that are extreamly I/O bound. An example of this would be downloading images and files from the internet. Multithreading provides a significant performance game when it comes to such I/O heavy task. However, using multithreading for basic functions can result in a performance loss. This is due to the Global Interpreter Lock(GIL). 

Let us take a simple snippet of code for example. The following code will find the cube and square of a number in python: 

```python 

def print_cube(num):
    return print(f"Cube = {num * num * num}")


def print_square(num):
    return print(f"Square = {num * num}")

def main():

    print_cube(10)
    print_square(10)
    sort_words(words)
    print("done")


if __name__ == "__main__":
    main()
```

This code, when executed on a single thread will execute faster as we are not using any resources to swap to another thread. However if we add multithreading to this program, we will notice that the execution time slows down as the  GIL will require resoruces to move the task from one thread to another, this can be seen the images that show the tests for single thread and multithread performance on a basic operation below, along with an I/O based operation task on single and muli-threadded performance


<!-- insert images of the performance comparison here: -->

