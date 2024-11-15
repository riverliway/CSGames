# Easy 2: DFA

Below is a picture of a DFA (Deterministic Finite Automaton). It is a flowchart which shows how each circle is related to every other circle. The solid blue arrows correspond to the symbol `1` and the dashed red arrows correspond to the symbol `0`. Begin at the orange circle in the top left. The example bitstring `110` takes you from circle $1$ to circle $6$ by following the arrows for ‘1’ ‘1’ and ‘0’. 

![DFA](../../resources/DFA.png)

Here is a bitstring which will take you from circle $1$ to circle $X$:

`0000100110111111`

Your goal is to reach the green circle $16$ from circle $X$ using the smallest number of arrows. What is the bitstring that corresponds to that path?

### Solution

Following the path from circle $1$ to circle $X$ yields the following:
$$
1\xrightarrow0 2\xrightarrow0 3\xrightarrow0 7 \xrightarrow0 2\xrightarrow1 5\xrightarrow0 5\xrightarrow0 5
\xrightarrow1 9 \xrightarrow1 13\xrightarrow0 14\xrightarrow1 15\xrightarrow1 10 \xrightarrow1 11\xrightarrow1 12 \xrightarrow18 \xrightarrow17
$$
Circle $X$ is circle $7$. The shortest path to circle $16$ has length 6:
$$
7\xrightarrow1 4\xrightarrow0 12\xrightarrow0 6\xrightarrow0 10\xrightarrow1 11\xrightarrow0 16
$$
The shortest path is `100010`.

