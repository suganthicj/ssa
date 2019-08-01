x11=int(input())
l=list(map(int,input().split()))
y11=0
for p in l:
	y11=y11+p
for p in l:
	if y11%2==0:
		if p%2==0:
			print(p)
	else:
		if p%2==1:
			print(p)
