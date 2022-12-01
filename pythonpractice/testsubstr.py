substr="abaacacaacda"

#def checkLongestsub(substr):

#print(set(substr))
#print(len(substr))

dup = []
dupoccur = []

for i in range(1, len(substr)):
	if substr[i]==substr[i]:	
		#print("there are duplicate characters")
		dup.append(substr[i])







print(dup.count('a'))
#dup = {x for x in dup if dup.count(x) > 1}
#print(dup)

