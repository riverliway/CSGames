message = "MYSECRET"
key = "BOROWSKI"

m = list(message)
k = list(key)
c = list(message)
for i in range(len(m)):
    r = (ord(m[i]) - ord('A') + ord(k[i]) - ord('A')) % 26
    c[i] = chr(r + ord('A'))
    
print("".join(c))