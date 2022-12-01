
str="eeeee"
new_str = []
dic = {}

#print(len(str))

for i in range(len(str)-1):
	count=0
	for j in range(i+1, len(str)):
		if str[i]==str[j]:
			new_str.append(str[i])
			#count = count + 1
			#str=str[:j]+'0'+str[j+1:]
			#print(count)
	#if count>0 and str[i]!='0':
	#	print(str[i])

print(new_str)

