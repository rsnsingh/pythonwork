x={"aa","bb","dd"}
x.add("cc")
for a in x:
    print(a)
print("aa" in x)
print("yes")
x.update(["ss","ll"])
    
for a in x:
        print(a)
x.remove("ss")
x.discard("ll")
print(x)


