# Given: A file containing at most 1000 lines
# Return: A file contaiing all the even-numbered lines from the original file. Assume 1-based numbering of lines. 

f = open('dataset.txt', 'r')

count = 0
for line in f: 
    count = count + 1
    if count % 2 == 0: 
        f.write(line.strip() + \n)
        print(line)


f.close()