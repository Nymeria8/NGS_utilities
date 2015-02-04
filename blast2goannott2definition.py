#given a .annot file from blast2go output where the description of the gene is the acession number, this script substitute the acession with the description from ncbi database
#python blast2goannott2definition.py blast2go.annot output.annot "mail@example.com"

from Bio import Entrez
from sys import argv


fich= open (argv[1])
out=open(argv[2], "w")
dica={}

for i in fich:
	a=i.split()
	if len(a)>2:
		w=a[2].split("|")
		dica[a[0]]=w[1]

sss=set()
ddd={}
"""for y in gi:
	sss.add(y.strip("\n"))

for key, value in dica.items():
	if value in sss:
		out.write(key+"\n")
"""


for key, value in dica.items():
	print ("check!")
	Entrez.email = argv[3]
	handle = Entrez.efetch(db="protein", id=value, rettype="gb", retmode="text")
	entry=(handle.read().strip())
	complete=entry.split("\n")
	definition=complete[1][12:]
	definition2=definition.strip(".")
	handle.close()
	out.write(key+"\t"+value+"\t"+definition2+"\n")
		


fich.close()
gi.close()
out.close()
	
		
