x = "[YOUR ASCII]"
x = x.split()
s = ""

for i in range(len(x)):
    s+=chr(int(x[i]))
    
print(s)