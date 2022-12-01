s='muzamil'
print(s[::-1])

r = reversed(s)
print(''.join(r))


output=''
i=len(s)-1
while i >=0:
	output = output + s[i]
	i=i-1

print(output)

