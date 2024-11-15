# Hard 4: Oracle

An oracle is any black-box function where you don't know how the function works on the inside. We have queried this oracle 250 times and placed the results in an array. Each element is the output of the oracle whose input was the index. It looks like: [f(0), f(1), f(2), ...]

We have also found out that the oracle takes on the following structure:

`f(x) = ((x * A) % B * C) % D * E + x % F * G`

This structure has seven prime constants which define it (A,B,C,D,E,F,G). Below are the first 250 outputs of an oracle. What are the seven constants that define this oracle? Format your answer as A:B:C:D:E:F:G

```
[0,149,89,187,127,276,165,61,254,99,39,188,77,17,166,55,204,144,242,182,78,220,116,56,154,94,34,132,72,221,110,259,199,44,237,133,22,171,111,0,149,89,187,127,276,165,61,254,99,39,188,77,17,166,55,204,144,242,182,78,220,116,56,154,94,34,132,72,221,110,259,199,44,237,133,22,171,111,0,149,89,187,127,276,165,61,254,99,39,188,77,17,166,55,204,144,242,182,78,220,116,56,154,94,34,132,72,221,110,259,199,44,237,133,22,171,111,0,149,89,187,127,276,165,61,254,99,39,188,77,17,166,55,204,144,242,182,78,220,116,56,154,94,34,132,72,221,110,259,199,44,237,133,22,171,111,0,149,89,187,127,276,165,61,254,99,39,188,77,17,166,55,204,144,242,182,78,220,116,56,154,94,34,132,72,221,110,259,199,44,237,133,22,171,111,0,149,89,187,127,276,165,61,254,99,39,188,77,17,166,55,204,144,242,182,78,220,116,56,154,94,34,132,72,221,110,259,199,44,237,133,22,171,111,0,149,89,187,127,276,165,61,254,99,39,188,77,17,166,55,204]
```

[Solution](../../sol/h4)