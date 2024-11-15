# Medium 4: Regex Golf

Regex (Regular Expressions) is a tool used for pattern matching in strings. There is an expression which describes a set of rules and a given string which will either match the set of rules or not match it. For example, consider the expression “hello”. It will accept the string “hello world!”, but reject the string “goodbye world!”. This is because the expression is inside the first string, but not in the second string.

An expression which consists only of letters will accept inputs which have the expression as a substring and reject others. A single letter in the expression is called a token. Multiple letters can be grouped together with parentheses into a single token.

There are a number of special characters which will change what the expression accepts/rejects:

\* (Asterisk): Accepts inputs which match 0 or more of the previous token. Ex: “a*b” matches “b”, “ab”, “aab”, “xyaaaaaaab”, etc. but not “hello”

. (Period): This token is a wildcard for any character except the end of string. Ex: “a.b” matches “acb”, “axb”, doesn’t match “ab”

$ (Dollar sign): This token matches the end of string. Ex: “db\$” matches “db”, “xxccjsjdb”, but not “dba” because the db is not at the end of the string.

There are many more special characters, regex can be a very powerful tool!

The goal of Regex Golf is to create the smallest expression that accepts all of the good inputs and rejects all of the bad inputs. For these inputs, what is the smallest expression?

Good:

`helloran`

`hellobae`

`hellodad`

`bread`

Bad:

`hellored`

`hellobed`

`helloraid`

`breed`

[Solution](../../sol/m4)