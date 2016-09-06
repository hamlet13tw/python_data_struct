fname = input('Enter the file name : ')
try:
	fhand = open(fname)
except:
    print('Can Not Open The File:' + fname)
    exit()
    
count = 0
for line in fhand:
    if line.startswith('Subject'):
        count = count + 1
        
print('There were ' + str(count) + ',subject lines in:' + fname)