input = "[abc][zyx][e]"
input = input.split("][")
print(input)

input = [s.strip("[") for s in input] 
print(input)
input = [s.strip("]") for s in input] 
print(input)
#result = [min(s) for s in input]
#print(result)

for i in input:
	s = min(i)
	print(s.strip("%"), end="")
