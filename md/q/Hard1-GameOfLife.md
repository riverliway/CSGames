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

[Solution](../../sol/h1)