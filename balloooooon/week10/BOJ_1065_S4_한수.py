k=input()
countd=0
for a in range(1,int(k)+1):
	if len(str(a))<=2:
		countd += 1
	else:
		for i in range(len(str(a))-2):
			midcount=0
			a=str(a)
			if int(a[i+1])-int(a[i])==int(a[i+2])-int(a[i+1]):
				midcount += 1
			if midcount == len(a)-2:
				countd += 1
				
print(countd)