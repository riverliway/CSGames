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

[Solution](../../sol/m1)