#arr = [100,200,5,6,10,1]
arr = ['a','z','b','x']

for i in range(len(arr)-1):
	for j in range(0,len(arr)-i-1):
		if arr[j] > arr[j + 1]:
			temp = arr[j]
			arr[j] = arr[j+1]
			arr[j+1] = temp
	
print(arr)


