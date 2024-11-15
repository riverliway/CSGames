# Hard 1: Game of Life

A population of creatures is described as a string of ones and zeros. Each index of the string represents a single creature. If the index is 0, the creature is dead and if it is 1, the creature is alive. 

Each day creatures die and revive depending on their neighbors. If a creature’s neighbors are both dead, the creature dies from loneliness. If a creature’s neighbors are both alive, it dies from overcrowding. If there is one alive neighbor (on either side), the creature revives from friendship.

Examples:

`..101..` $\to$ `..101..` (overcrowding, but already dead)

`..111..` $\to$ `..101..` (dies from overcrowding)

`..100..` $\to$ `..110..` (revives from friendship)

`..110..` $\to$ `..110..` (friendship, but already alive)

`..010..` $\to$ `..000..` (dies from loneliness)

By continuing to observe this population’s evolution through time, the population will always eventually converge to cyclic behavior. The first day on which the population is the same as any previous day’s population is the day of stagnation.

Here is a population on day 0. Which day does this population reach stagnation?

`0101001101011010111101001011111110`

Note: Assume the neighbors outside the border for the creatures on each end are always zero.

Note: The day of stagnation is not necessarily the same as the period of the cycle.

### Solution

Create a function which will calculate the next day's population given the current day's. This function will iterate through the previous population, calculating the bit at each position. The resulting bit is the exclusive or (XOR) of the left and right bits. Example:
$$
abcde \to (0\oplus b)(a\oplus c)(b\oplus d)(c\oplus e)(d\oplus 0)
$$
Do not do this in-place, because all populations should be kept in a hashset to see when the next day matches any of the previous day's populations.

Run this in a while-true loop and break out once a duplicate population has been found. If implemented correctly, the program is guaranteed to halt because of the pigeonhole principal. The input population consists of $34$ bits, so there are only $2^{34}$ different bitstrings, a finite amount. Luckily, this population reaches stagnation far faster than $2^{34}$. This problem is a variant of John Conway's game of life, played on an infinite 2D grid; that version is not guaranteed to reach stagnation.

This population reaches stagnation on day 8190.

[Python Solution](../../resources/game_of_life.py)

