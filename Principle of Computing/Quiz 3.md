1. Basic probability
What is the sum of the probabilities associated with the all possible outcomes of a single trial? Enter the number in the box below.
1

Correct
The sum of the probabilities associated with all possible outcomes is 1.

2. Single trials 
You are dealt a single card from a standard deck of 52 playings cards (4 suits with 13 cards in each suit). What is the probability that the card will be of a specific suit? Enter the probability as a decimal number below.
0.25

Correct
Correct. There are 13 outcomes corresponding to the event. Each outcome has probability  1/52  so the probability of the event is  13/52  which is  0.25.


3. Consider a trial with 36 possible outcomes where each outcome has equal probability. How many outcomes correspond to an event that has probability 1/9? Enter the number of outcomes below.
4

Correct
Correct. Four outcomes, each of probability 1/36, yields an event with probability 4/36  =  1/9

4. Which Python expressions below simulate a single trial corresponding to the roll of a fair six-sided die whose faces are numbered 1 to 6?
random.randrange(1, 7)
random.randrange(6) + 1

5. Given a standard deck of 52 cards, what is the probability that two cards drawn at random will have the same rank? Note that first card drawn is not added back into the deck when the second card is drawn.
1/17
Correct
There are 33 cards among the 51 cards remaining in the deck that match the rank of the first card.


6. Expected value
What is the mean GPA of class where 30% of the students have 4.0 GPA, 40% of the students have a 3.0 GPA and 20% of the students have 2.0 GPA, and 10% of the student have a 1.0 GPA? Review this week's math notes on expected value if necessary.
2.9


7. Consider a dice game in which you roll two dice. If the sum of the dice is odd, you win $1. If the sum of the dice is even, you lose $1. What is the expected value (in terms of your winnings) of a single roll in this game?
The expected value is zero. If I play this game a lot, I expect to break even.

Correct
The expected value is zero since the probability of rolling an even sum equals the probability of rolling an odd sum.


8. What is the expected value of trial(n)trial(n) as a function of n? (Here, assume that nn is a positive integer.) Enter the answer below as a math expression in n

def trial(n):
    val = random.randrange(n)
    return val
    
As a hint, note that the arithmetic sum 0 +1+2+..+k has the value  k(k+1)/2

(n-1)/2
Correct
Correct. The possible outcomes are 0,...,n−1}.


9. Monte Carlo simulations
In all of the previous problems, the sample space (space of possible outcomes) had a finite number of outcomes. However, conducting trials where the outcome lies in a continuous space is perfectly reasonable. 
Consider that following mystery program. This program uses  random.random() to generates a random set of points that are uniformly distributed over the square with corners at (1,1), (−1,1), (1,−1), and (−1,−1). (Here, being uniformly distribution means that each point in the square has an equal chance of being generated.) The method then tests whether these points lie inside a unit circle. 
As one increases the number of trials, the value returned by estimate_mystery tends towards a specific value that has a simple expression involving a well-known constant. 
Enter this value as a math expression below. (Do not enter a floating point number.) You can consult this page if you would like to see a list of math constants that Coursera's quiz system recognizes.
pi/4

Correct
Correct. The function returns the ratio of the number of points inside the circle divided by the total number of points. This value corresponds to the ratio of the area of the circle to the area of the square which is π/4.

10. For the final question of each of the remaining homeworks in PoC1, your task will be to create a list of test cases for a function that you have implemented in IIPP or PoC. Our purpose in these problems is to focus your attention on the process of creating test cases on your own and not relying entirely on OwlTest. To assess the quality of your test cases, we have created a series of OwlTests that automatically assesses how well your test cases detect erroneous programs written by your peers.
For this question, your task is to create a collection of test cases for the function format() that you implemented for the Stopwatch mini-project in IIIPP1. To refresh your memory, the function  format(tenths) takes an integer tenths corresponding to the number of tenths of second elapsed and returns a string of the form:  A:BC.D where  A, C and D are digits in the range 0-9 and B is in the range 0-5. This string is the readout of a digital stopwatch after tenths tenths of seconds have elapsed. Note that the string returned by format should always correctly include leading zeros. Here are several example inputs and outputs for  format():
    format(0) = 0:00.0
    format(11) = 0:01.1
    format(321) = 0:32.1
    format(613) = 1:01.3
To complete this problem, visit this OwlTest page and follow the directions for creating and submitting a list of test cases. Once OwlTest has successfully assessed your test cases, you will see the message TEST CASES successfully assessed. Following this message is a seven-digit number that you should enter in the form below. For this task, please ignore the fact that this message appears under the red Unit Test Failures tab. This program is an example of input to OwlTest that incorporates the four test cases given above.
This OwlTest automatically assesses how effective your list of test cases is in detecting erroneous programs from a suite of implementations of  format() compiled from IIPP. If you do not catch all of the erroneous programs, OwlTest outputs an example of one erroneous program that passes all of your submitted test cases. You must catch all of the erroneous programs to get this question correct. The homework feedback will tell you what percent of erroneous programs you were able to catch.
Note that trying to debug this program to create new test cases may be difficult and you may wish to consider other methods for creating test cases.

NOT DEAL WITH THIS QUESTION



