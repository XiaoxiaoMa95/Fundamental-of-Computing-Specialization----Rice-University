1. “If you stop at general math, you're only going to make general math money.” - Snoop Dogg
The importance of math
The main emphasis of the homework in this class is helping you learn the math skills required to flourish in Computer Science. You will find these skills indispensable as you tackled more and more difficult topics in Computer Science. Remember that the "Science" part of Computer Science corresponds primarily to Mathematics.
In this homework, we will review some basic topics that you should be familiar with from high school math.
Functions
The first four questions cover mathematical functions. We recommend that you review the material on Functions from week 1 before attempting them.
Consider the following Python function:

def root (a, b, c):
    discriminant = b ** 2 - 4 * a * c
    return (-b - discriminant ** 0.5) / (2 * a)

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
Which mathematical function below computes the same value as this function?

root(a, b, c) = (-b - sqrt(b^2 - 4ac)) / (2a)



2. Which of the mathematical functions displayed below are linear?

g(y)=2y−3
h(z)=3
f(x)=x+10

 

3.  As part of this class, we will develop methods for estimating the running time of various important algorithms as functions of the size of their input. One simple function that we will use in these estimates is the logarithm function, which is defined and discussed in Math notes on "Functions".
Review this part of the Math notes. Then compute the logarithm base 5 of sqrt(5^7) which corresponds to the value of the mathematical expression
log5(sqrt(5^7))Enter the answer the box below in decimal form.

3.5

 
4. Significant figures
An important concept in working with numbers is that of significant figures. The significant figures of a number are those digits that carry meaning contributing to its precision. A digit is significant based on the three following rules:
    •    All non-zero digits are considered significant.
    •    Zeros appearing anywhere between two non-zero digits are significant.
    •    Trailing zeros in a number containing a decimal point are significant.
How many significant digits does the decimal number 0.00400100 have?

6



5.  Scientific notation is a way of writing numbers that are too big or too small to be conveniently written in decimal form. For decimal numbers, scientific notation has the form a*10^b where a is a number in the range 1≤∣a∣<10 and b is an integer. The number a is the mantissa while the integer b is the exponent. The mantissa is usually expressed using the same number of significant digits as used in the original decimal form.
What is the mantissa for 0.00400100 when expressed in scientific notation? 

a=4.00100
Correct. The two trailing zero are significant in 0.00400100.



6. In Python, floating point numbers are represented in a binary version of scientific notation where the base 10 is replaced by 2 and the mantissa is a binary number that lies in the range 1≤∣a∣<2 and has 53 significant bits. Floating point numbers are usually printed out with up to 12 significant digits (although with trailing zeros suppressed).
In some homework problems, you will be asked to write code that computes an answer as a floating point number and then enter your answer as decimal number with a specified number of significant digits. In practice, Python computes more significant digits than are required so you should round your answer to the closest decimal number with the specified number of significant digits.
For this question, look up (or compute) the decimal representation of the number π and enter the value of π with five significant digits of precision in the box below. Remember to round as describe above.

3.1416



7.  Grids
Consider the following code snippet:

row = ...
col = ...
nested_list = [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14]]

print nested_list[row][col]

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
If running this code snippet prints 13 in the console, what are the non-negative values of row and col? Enter these two values below as numbers separated by a space.

2 3


 
8. Review the math notes on Grids. Given a grid of size 4×6, what are the row and column indices for the upper right cell in this grid? Enter the row and columns indices below as numbers separated by a space.

0 5



9. Review the function traverse_grid from the "Grids" video lecture.
Given a 4×4 grid, what values for start_cell and direction would cause traverse_grid to traverse the diagonal of grid connecting the lower right tile to the upper left tile?

start_cell = (3, 3)
direction = (-1, -1)








