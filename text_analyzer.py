input_file = open("text.txt", "r")
output_file = open("output.txt", "w")

r = input_file.read()

words = r.replace('#',' ').replace('(',' ').replace(')',' ').replace('/',' ').replace(',',' ').replace('.',' ').replace('?',' ').replace('-',' ').replace('!',' ').split()
num = len(words)

d = {}

for i in range(num):
    k = words[i]
    if k in d.keys():
        d[words[i]] += 1
    else :
        d[words[i]] = 1

sort_1 = sorted(d.items())
sort_2 = sorted(sort_1, key = lambda x:x[1], reverse=True)


for key in sort_2:
    print (key)
    output_file.write (str(key) + '\n')

output_file.close()
