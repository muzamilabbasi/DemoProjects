str="muzamil abbasi"
new_str = {}
Totalcount=0

for i in range(len(str)):
	count=1
	for j in range(i+1, len(str)):
		#print(f"outer loop is {i} ,inner loop is {j}")
		if str[i]==str[j] and str[j] !='0':
			#print(f"value of str in i is: {str[i]}, value of str in j is :{str[j]}")
			count +=1
			print(f"the value of count is {count}") 
			new_str[str[j]]=count
			#Totalcount += 1
			str = str[:j] + '0' + str[j+1:]
			#if count > 0 and str[i] != '0':
			#print(str[i])  
print(new_str)
