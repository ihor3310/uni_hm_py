'''
Generates a sequence of numbers 
where each subsequent number is the sum of the two previous ones.
'''

def gen_sum(s, n, c):
	m = n
	i = 0
	b = s
	while i < c:
		k = b + m
		yield m
		b = m
		m = k
		i += 1

res_arr = [1]
result = gen_sum(1, 2, 10)

for i in result:
	res_arr.append(i)
print(res_arr)
