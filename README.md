# Missing-Operator-Calculator
Tool/Solver to solve fill the blanks calculations where the operators are missing. 
A calculation/equation with blanks is a mathematical exercise consisting of finding the missing operation 
(addition, subtraction, multiplication, division)

I wrote this small program to solve problems like this : 
> 1?2?3?4 = 10 

If you still confused what is the idea of this program then check this website :
> https://www.dcode.fr/missing-operators-equation-solver

The only thing that is difference is my tool makes cases for parenthesis as well

## Usage
just edit the first string variable to the input that you want for example 1?2?3 will give these outputs:

(1)+((2+3)) = 6

(1)+((2-3)) = 0

(1)+((2*3)) = 7

(1)+((2/3)) = 1.6666666666666665

(1)-((2+3)) = -4

(1)-((2-3)) = 2

(1)-((2*3)) = -5

(1)-((2/3)) = 0.33333333333333337

(1)*((2+3)) = 5

(1)*((2-3)) = -1

(1)*((2*3)) = 6

(1)*((2/3)) = 0.6666666666666666

(1)/((2+3)) = 0.2

(1)/((2-3)) = -1.0

(1)/((2*3)) = 0.16666666666666666

(1)/((2/3)) = 1.5

((1+2))+(3) = 6

((1+2))-(3) = 0

((1+2))*(3) = 9

((1+2))/(3) = 1.0

((1-2))+(3) = 2

((1-2))-(3) = -4

((1-2))*(3) = -3

((1-2))/(3) = -0.3333333333333333

((1*2))+(3) = 5

((1*2))-(3) = -1

((1*2))*(3) = 6

((1*2))/(3) = 0.6666666666666666

((1/2))+(3) = 3.5

((1/2))-(3) = -2.5

((1/2))*(3) = 1.5

((1/2))/(3) = 0.16666666666666666
