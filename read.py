data = []
count = 0 
with open('reviews.txt', 'r') as f:
    for line in f:
    	data.append(line)
    	count += 1
    	if count % 1000 == 0:
       		print(len(data))
print('file reading completed , there are a total  of ' , len(data) , 'records')

print(data[0])

sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
print('average of the records is ' , sum_len/len(data))

new = []
for d in data:
	if len(d) <  100:
		new.append(d)
print('there are a total of ', len(new) , 'records length less then 100')
print(new[0])
print(new[1])

good = []
for d in data:
	if good in d:
		good.append(d)
print('there are total of ' , len(good), 'records')

#word_count
wc = {} #word_count
for d in data:
	words = d.split()
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] =  1

for word in wc:
	if wc[word] > 1000000:
	    print(word, wc[word])

print(len(wc))

while True:
	word = input('please enter the word you would like to search: ')
	if word == 'q':
		break
	if word in wc:
	    print(word, 'appear',wc[word] ,'times')
	else:
		print('the word is not found')


print('thank for used this function')