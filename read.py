data  = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print('file reading completed , there are a total  of ' , len(data) , 'records')

sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
	
print('average of the records is ' , sum_len/len(data))