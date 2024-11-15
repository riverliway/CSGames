# Easy 2: DFA

Below is a picture of a DFA (Deterministic Finite Automaton). It is a flowchart which shows how each circle is related to every other circle. The solid blue arrows correspond to the symbol `1` and the dashed red arrows correspond to the symbol `0`. Begin at the orange circle in the top left. The example bitstring `110` takes you from circle $1$ to circle $6$ by following the arrows for ‘1’ ‘1’ and ‘0’. 

![DFA](../../resources/DFA.png)

Here is a bitstring which will take you from circle $1$ to circle $X$:

`0000100110111111`

Your goal is to reach the green circle $16$ from circle $X$ using the smallest number of arrows. What is the bitstring that corresponds to that path?

[Solution](../../sol/e2)