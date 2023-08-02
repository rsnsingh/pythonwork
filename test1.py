def Change(P ,Q=30):    # P=150 Q=100
    P=P+Q 
    Q=P-Q 
    print( P,"#",Q)     # 250 # 150
    return (P) 
R=150 
S=100 
R=Change(R,S)       #  R=150, S= 100  
print(R,"#",S)
S=Change(S)
print(S)

