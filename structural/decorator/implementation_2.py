"""
Using Python's inbuilt decorator mechanism
"""
import time


def logging_decorator(func):
    def wrapper(*args, **kwargs):
        print("Logging decorator: Calling Function now")
        func(*args, **kwargs)
        print("Logging decorator: Function was called")

    return wrapper


def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        print("Timing decorator: Calling Function now")
        func(*args, **kwargs)
        end_time = time.time()
        print(f"Total time of execution: {(end_time - start_time)} seconds")

    return wrapper


@timing_decorator
@logging_decorator
def concrete_component(x: int) -> None:
    time.sleep(1)
    print(f"Concrete Component called with: {x}")


if __name__ == "__main__":
    concrete_component(10)
