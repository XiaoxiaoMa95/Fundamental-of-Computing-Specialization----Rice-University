1.
Question 1
"Invention consists in avoiding the constructing of useless contraptions and in constructing the useful combinations which are in infinite minority",
Henri Poincare
Combinatorics
In this week's material, we will create enumerations, permutations and combinations of items from a set of outcomes. We will then consider sequences of repeated trials that are modeled by these objects. These problems will form our preparation for this week's mini-project on Yahtzee.
Enumeration
Given the set of outcomes corresponding to a coin flipHeads,Tails}, how many sequences of outcomes of length five (repetition allowed) are possible?
32
Correct
Correct. 2^5=32



2.
Question 2
Probability for sequences of trials
Consider a sequence of trials in which a fair four-sided die (with faces numbered 1-4) is rolled twice. What is the expected value of the product of the two die rolls? Enter the answer as a floating point number below.
6.25
Correct


3.
Question 3
Given a trial in which a decimal digit is selected from the list ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"] with equal probability 0.1, consider a five-digit string created by a sequence of such trials (leading zeros and repeated digits are allowed). What is the probability that this five-digit string consists of five consecutive digits in either ascending or descending order (e.g;  "34567" or "43210") ?
Enter your answer as a floating point number with at least four significant digits of precision.
0.00012
Correct
Correct. Each outcome has probability 0.00001. There are six strings with consecutive ascending digits and six string with consecutive descending digits. Therefore, the probability of this event is 0.00012.
4.
Question 4
Permutations
Consider a trial in which five digit strings are formed as permutations of the digits ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]. (In this case, repetition of digits is not allowed.) If the probability of each permutation is the same, what is the probability that this five digits string consists of consecutive digits in either ascending or descending order (e.g; “34567" or  "43210") ?
Enter your answer as a floating point number with at least four significant digits of precision.
0.000396825
Correct
Correct. There are 12 possible permutations out of 10!/5! permutations that are either ascending or descending.

5.
Question 5
In this week's lectures, we discussed an iterative approach to generating all sequences of outcomes where repeated outcomes were allowed. Starting from this program template, implement a function gen_permutations(outcomes, num_trials)gen_permutations(outcomes, num_trials) that takes a list of outcomes and a number of trials and returns a set of all possible permutations of length num_trialsnum_trials (encoded as tuples) from this set of outcomes. 
Hint: gen_permutationsgen_permutations can be built from gen_all_sequencesgen_all_sequences by adding a single if statement that prevents repeated outcomes. When you believe that your code works correctly, select the answer printed at the bottom of the console. 
('b', 'e', 'c', 'd')

6.
Question 6
Subsets
A set S is a subset of another set T (mathematically denoted as S⊆T) if every element xx in SS(mathematically denoted as x∈S) is also a member of T. Which of the following sets are subsets of the set  {1,2}?
{2}
Correct
{1,2}
Correct
A set is always a subset of itself.
{}
Correct
The empty set is a subset of any set.

7.
Question 7
If the set T has n members, how many distinct sets S are subsets of T? You may want to figure out the answer for a few specific values of n first. Enter the answer below as a math expression in n.

2**n
Correct

8.
Question 8
Combinations
Given a standard 52 card deck of playing cards, what is the probability of being dealt a five card hand where all five cards are of the same suit? 
Hint: Use the formula for combinations to compute the number of possible five card hands when the choice of cards is restricted to a single suit versus when the choice of cards is unrestricted.
Compute your answer in Python using  math.factorial and enter the answer below as a floating point number with at least four significant digits of precision.
0.001980792316926771
Correct
Correct. There are 13! /(5! * 8!) possible hands with 5 cards in a single suit. Multiply this value by the number of suits and divide by the 52! /(5! * 47!) possible hands.


9.
Question 9
Pascal's triangle is a triangular array of numbers in which the entry on one row of the triangle corresponds to the sum of the two entries directly above the entry.  This program prints out the first few rows of Pascal's triangle. 
Enter a math expression in mm and nn using factorial (!) that represents the value of the nnth entry of the mmth row of Pascal's triangle. (Both the row numbers and entry numbers are indexed starting at zero.)
m! / (n! * (m-n)!)
Correct
Correct. The nnth entry of the mmth row is the number of combinations of mm items chosen nn at a time.


