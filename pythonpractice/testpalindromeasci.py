stri = "baba"
tl = []
temp = []


for i in stri:
	tl.append(i)
print(tl)
tl.sort()
print(tl)

for i in range(len(tl)):
	if tl[i] > stri:
		print(tl[i])

	else:
		print("not greater")	
