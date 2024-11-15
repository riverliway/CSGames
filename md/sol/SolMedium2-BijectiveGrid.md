# Medium 2: Bijective Grid

A bijective function is one that produces a unique output for every input. We have provided a snippet of python code which implements a bijective function named `transform()` operating on a 2D grid of letters. The output of the function has been saved and stored in the “output” variable, but the input to the function was overwritten with Xs.

[Python Snippet](../../resources/bijective_grid.py)

Compute the inverse of the transform function and feed it the output to get the input.

### Solution

The bijective function `transform()` is a composition of 6 other bijective functions. The inverse of a composition is the reversed ordering of each inverse:
$$
f=g_1\circ g_2\circ \ ...\ \circ g_{n-1}\circ g_n \\
f^{-1}=g_n^{-1}\circ g_{n-1}^{-1}\circ\ ...\ \circ g_2^{-1}\circ g_1^{-1}
$$
The shift and cycle functions will compute the inverse by simply passing in a negative parameter because it will shift/cycle the other direction when computing a modulus with a negative input. The swap function's inverse can be found by exchanging the swap's order.

The message found when undoing the output is:

`HEYBROGUESSWHATTHISSAYSACOOLMESSAGEWHENYOUUNDOIT`

[Python Solution](../../resources/bijective_grid_sol.py)