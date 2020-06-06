1. Question 1
Analyzing the Greedy Boss Scenario
In this week's mini-project, we will investigate various strategies for the simple (but popular) game "Cookie Clicker". (If you think Cookie Clicker is silly, just remember that "Farmville" made the founders of Zynga rich.)
As a warmup, this week's Practice Activity, The Case of the Greedy Boss, considers a simple scenario that is very similar to Cookie Clicker in which you can repeatedly bribe your boss to have him increase your salary.
This homework will analyze the behavior of the greedy boss simulator for several simple cases. If you have not taken a look at this practice activity, you should work through it first before attempting this homework.
Use the function run_simulations in the greedy boss simulator to plot the graph of total salary earned as a function of the number of days for bribe_cost_increment = 0, 500, 1000, 2000. Which value for bribe_cost_increment generates the fastest growth in total salary earned in the simulation?
Remember to compare the plots of the functions over roughly the same number of days.
0
Correct
Correct. Lower cost for bribes leads to faster growth in total salary earned.


2. Question 2
One scenario that the greedy boss simulator does not cover is the situation when you refuse to accept a bribe. Which of the following arithmetic sums evaluates to your total salary earned after dd days?
100+100+⋯+100+100
(with d terms in sum)
Correct
Correct. You earn 100 dollars per day over d days.


3. Question 3
Reduce the arithmetic sum that you selected in Question 2 to a polynomial expression in the number of days d using the rules for arithmetic sums specified in the Math notes. This expression should evaluate to your total salary earned after dd days.
Enter the answer as a math expression below
100*d
Correct
Correct. Your salary earned grows linearly.


4. Question 4
For the next three problems, we will consider the case when  bribe_cost_increment == 1000. First, convert the output of  greedy_boss() into Log/Log form by taking the logarithm of both  current_day and the total salary earned using math.log() before they appended to the list days_vs_earnings.
The plot of the resulting graph approaches a straight line as the number of days increase. This observation signals that the function might be a polynomial function. Compute the slope of this line and round it to the nearest integer to estimate the degree of this polynomial.
2
Correct
Correct. The graph corresponds to a quadratic function.


5. Question 5
Examine the output of the simulation greedy_boss(50, 1000). Note you accumulate enough savings to pay a bribe once every 10 days.
Which of the arithmetic sums below evaluates to the total salary earned after nn bribes?
1000+2000+3000+...+1000n
Correct
Correct. The total salary earned grows at a quadratic rate.

6. Question 6
Reduce the arithmetic sum that you selected in Question 5 to a closed-form expression in nn using the rules for arithmetic sums specified in the Math notes. This expression should relate total salary earned to the number of bribes.
Finally, use the fact that each bribe happens once every 10 days to derive a polynomial expression that approximates the total salary earned in terms of the number of days dd. As a check, this expression in dd should evaluate exactly to the total salary earned by the end of the day of each bribe.
Enter this expression in dd as a math expression below.
500* (d/10+1)* d/10
Correct
Correct. Total salary earned grows quadratically as a function of the number of days.


7. Question7
The next two questions will examine the case when the cost of a bribe does not increase, bribe_cost_increment == 0. Our first task is to check whether the total salary earned is a polynomial function of the number of days in this case. To this end, create a Log/Log plot of the output of greedy_boss and examine the resulting graph.
Does the graph approach a straight line as the number of days increases?
No, the graph does not approach a straight line.
Correct
Correct. This observation means the function can not be a polynomial.


8. Question8
To conclude our analysis of this case, we will do some manual experimentation to locate an expression in dd that grows at a similar rate to total salary earned when bribe_cost_increment == 0.
Compare the growth rates of the expressions below to the growth rate of total salary earned using the plotting technique described in the Math notes. Which expression grows at approximately the same rate as total salary earned?
e ^ (0.095d)
Correct
Correct. The ratio of the two quantities approaches a constant (approximately) as d increases.


9. Question9
In the next two questions, we will consider a simple version of Cookie Clicker in which there is only one possible upgrade option. Instead of increasing the cost of an upgrade by some fixed amount after each upgrade as done in the greedy boss simulator, each upgrade in Cookie Clicker costs 15% more than the cost of the previous upgrade. (Note that this cost compounds in the same manner that interest does.)
If the first upgrade costs one unit, enter a math expression that models the cost of the nnth upgrade.
1 * (1 + 0.15) ^(n-1)
Correct
Correct.


10. Question10 
For the case when bribe_cost_increment == 1000, the cost of the nth bribe was exactly 1000n1000n. Which expression in nn grows faster (as defined in the Math notes), 1000n1000n or your answer to question 9?
You may want to plot some examples using SimplePlot for large values of nn to help in making this comparison.
The cost of an upgrade in Cookie Clicker grows faster than the cost of a bribe in the greedy boss scenario.
Correct
Correct. In this simplified version of Cooke Clicker, the cost of upgrades grows faster than in the greedy boss scenario. Therefore, the total cookies generated in this version grows at rate that is bounded by a quadratic function.

