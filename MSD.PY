P,Q,R=raw_input().split()
P=int(P)
Q=int(Q)
R=int(R)
if(P>Q) and (P>R):
	print(P)
elif(Q>R) and (Q>P):
	print(Q)
else :
	print(R)
