# Hard 3: Letter Train 2

This is a continuation of the letter train problem from the 1st round. In addition to the first 6 letters, we will define the following actions:

G - Perform the last 3 characters in reverse order. Ex: ABCG -> perform CBA	

​	^ Note it only performs their actions in reverse order. It does not actually move any letters around in the string.

H - Create a new train using the last 5 characters on a fresh counter initialized to zero. Add the result of the new train to this train’s counter

I - Perform A, B, or C depending on the counter modulus 3. 0 - A, 1 - B, 2 - C

J - Increment the counter by the sum of the ascii values of the previous 4 characters

K - Perform the previous character, but shift the letter up by one. Ex: if A, perform B; if B, perform C; ... ; if K, perform A

What is the counter after the following train?

`ABCEBGGJAGABBICHIIIGGGGDABCKBGGFABAAIGJHGAKBGGHEKAKIGGCKC`

Note: Your counter may overflow if you don’t use a programming language equipped to deal with large integers.

### Solution

This problem builds on the solution from the first letter train, but global variables are much harder to utilize in this version because of the recursion and building new trains. 

The counter ends at 731.

[Python Solution](../../resources/letter_train.py) 