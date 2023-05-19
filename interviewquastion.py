"""
14. Describe generators in Python and give a brief example of how to use them
A generator in Python is an easy way of creating an iterable object without having to implement the
whole iteration protocol. It is just a simple function that contains a yield statement instead of the return one.

When the interpreter finds a yield statement, it returns a value like it would with a return one but
instead of terminating the functions it puts it in pause, keeping the values and the state of all the
variables and objects contained.

For example, let’s say that we want to create a function to get the Fibonacci sequence like in the former example.

With a generator, we just need to create a function with a loop that calculates these numbers and
after each number is found returns it by using the yield keyword:
"""
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b

if __name__ == '__main__':
    # Create a generator of fibonacci numbers smaller than 1 million
    fibonacci_generator = fibonacci()

    # print out all the sequence until CTRL-C is pressed
    try:
        for fibonacci_number in fibonacci_generator:
            print(fibonacci_number)
    except KeyboardInterrupt:
        print("terminated")

"""
 What are lambda functions?
Lambda functions are short anonymous functions that can have no more than one line of code.

To declare a lambda function, you just need to specify the keyword lambda, the input parameters you will get (if any), and then a colon to separate the expression that has to be evaluated and returned when the lambda is called.

Let’s consider the following example:

>>> square = lambda x : x*x
In this example, we are defining an anonymous lambda function that takes a parameter (x) and returns to the caller its square (x*x). In this example, we have also assigned the function to a name (square) and so we can call this function like this:

>>> square(9)
81
However, to assign a lambda to a name is often not necessary. For example, lambdas are often written inline and passed as a parameter to another function (like the map() or the filter() functions). 

For example, let's say that we have a list of numbers and we want to create another list with their squares. In this case, a lambda passed to a map() function can solve our need with just one line of code:

>>> my_input_numbers = [1, 2, 3, 4, 5, 10, 100, 1000]
>>> my_squares = map(lambda x : x*x, my_input_numbers)
The same result could be achieved also by using list comprehension like this:

>>> my_squares_list = [x*x for x in my_input_numbers]
So another question the interviewer could ask is: what’s the difference between these two methods and what’s
 the best one? The answer here is that while list comprehension creates a list, the map function simply
 returns a map object that is a Python iterable and that is lazy. This means that the evaluation of the lambda is done only when the object is actually iterated. 

To get the idea, try to change the example above pretending that my_input_numbers was huge:

>>> my_input_numbers = range(10**100)
Now, execute both the map and the list comprehension example, and you will see that the map example keeps working and returns a map object that can be iterated, while the list comprehension one hangs consuming more and more memory.

"""