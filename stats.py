#make basic stats for a group of fasta files
#python stats.py fastafile

from sys import argv


sequencefile= open (argv[1])

Nomes=[]
dic={}
for x in sequencefile:
	if x.startswith(">"):
		dic[x]=("")
		d=x
	else:
		dic[d]+=x.strip("\n")

n=0
numlist=[]
superior=[]
bp=0
for key, value in dic.items():
	numero=(len(value))
	numlist.append (numero)
	bp+=numero
	if (numero>=1000):
		superior.append (numero)


numlist.sort() #ORDENAR
print ("Total of sequences: " + str(len(dic)))
maiorcontig=numlist[n-1]
print ("longest sequence: " + str(maiorcontig))
totalsuperior=float(len(superior))
print ("total of sequences with more than 1000bp: " + str(totalsuperior))

print ("%>1000bp: " + str(totalsuperior/(len(dic))*100))
print ("average length: " + str(float(bp)/len(dic)))

newlist = []
for x in numlist :
    newlist += [x]*x

# take the mean of the two middle elements if there are an even number
# of elements. otherwise, take the middle element
if len(newlist) % 2 == 0:
    medianpos = len(newlist)/2 
    N50= float(newlist[medianpos] + newlist[medianpos-1]) /2
else:
    medianpos = len(newlist)/2
    N50= newlist[medianpos]

print ("N50: " + str(N50))

sequencefile.close()


