# program to evaluate a polynomial of the variable (e.g. p(X)= -2X**0+X**2+3X**3)
def eval_poly(p,x):
    sum=0
    for power in p:
        sum+=p[power]*x**power   #  -2*1 + 1*(2**2)+ 3*(2**3) =  -2+4+24 = 26
    print(' Value of polynomial after evaluation: ', sum)
p={0:-2,2:1,3:3}
x=2
eval_poly(p,x)
