# Easy 1: Magic Square

A magic square is a grid of numbers whose rows, columns, and diagonals must sum to the same number. Enter the number for $X$ which satisfies this magic square:
$$
\begin{matrix}
100 & 93 & 98 \\
95 & X & 99 \\
96 & 101 & 94
\end{matrix}
$$

### Solution

Add any row or column which does not contain $X$ to find the sum: $100 + 93 + 98=291$.

Subtract the two elements on either side of a row or column containing $X$ from the sum: $X=291-93-101=97$.

Although this simple $3\times3$ magic square was simple to solve, there are more advanced magic squares that have rewards for solving them or proving a solution is impossible!