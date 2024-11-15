# Medium 1: Letter Train

There is a counter initialized to zero. These letters perform the following actions:

A - Increments the counter by 5

B - Doubles the counter

C - Sums the digits of the counter, then adds the sum to the counter. Ex: 125 += 1 + 2 + 5 = 8

D - Performs the action of the letter 3 characters back. Ex: ABCD -> perform A

E - Subtracts 13 then performs ABA

F - Overwrites the counter with the number of digits in the counter. Ex: 3459 -> 4

Here is a string of letters, read left to right. What is the counter after all letters have been performed?

`ABCDEFBBBCCABECDDDDEEDFADAADBBCBEEDEEBBFAAAABBEECDABABABCC`

### Solution

Have a program keep track of the counter as it processes each letter. It also needs to know the position in the string because the letter D will move 3 letters back, and it can find another D, which will repeat the process. 

The counter ends at 6134.

It is feasible to compute this by hand.