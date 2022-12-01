arr = [1,2,5,6,10,100]
arr2 = []
print(arr)

for i in range(len(arr)-1):
	#print(arr[i], arr[i+1])
	if arr[i] <  arr[i+1]:
		temp = arr[i]
		arr[i] = arr[i+1]
		arr[i+1] = temp
		arr2.append(arr[i])
#print(arr2)
