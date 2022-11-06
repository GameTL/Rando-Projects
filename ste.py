
#%%
x = "12 a-a".split() # split on whitespace
print(x)
opplus = x[1].split("+") # split on -
opminus = x[1].split("-") # split on -

print(opplus)
print(opminus)
if len(opplus) > 1:
    front = len(opplus[0])
    back = len(opplus[1])
    a = int(x[0][0:front])
    b = int(x[0][front:front+back])
    print(a+b)
elif len(opminus) > 1:
    front = len(opminus[0])
    back = len(opminus[1])
    a = int(x[0][0:front])
    b = int(x[0][front:front+back])
    print(a-b)
# %%
