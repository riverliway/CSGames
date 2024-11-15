# Easy 4: DNDice

Any die that is called a DN is a fair, N sided die which will produce a number between 1 and N when rolled. 

The minimum roll is the smallest number possible to get from rolling a set of dice.

The maximum roll is the largest number possible to get from rolling a set of dice.

The expected roll is the average number when rolling the set of dice over and over.

For example, rolling 1 D6 yields a min of 1, max of 6, and an expected value of 3.5

A D6 die is the traditional six sided die commonly used in board games.

I have a big bag of dice and I will roll them all and sum the numbers to get the roll of the set.

`3` D2

`1` D4

`2` D6

`2` D12

`5` D37

`1` D99

Format your answer in the form: X:Y:ZWhere X is the minimum roll from the set in the bag, Y is the maximum roll, and Z is the expected roll.

### Solution

The minimum roll is equal to the number of dice: $3+1+2+2+5+1=14$.

The maximum roll is equal to the highest roll for each dice: $3 * 2+1*4+2*6+2*12+5*37+1*99=330$.

The expected roll is equal to the highest roll plus one halved for each dice:

$3*\frac12(2+1)+1*\frac12(4+1)+2*\frac12(6+1)+2*\frac12(12+1)+5*\frac12(37+1)+1*\frac12(99+1)=172$

The solution is `14:330:172`.