#It retrives a subset of fasta sequences, given a list of headers and a a set of fasta sequences.
#python fastalist.py setOfFasta.fasta headersList output.fasta


from sys import argv

fasta=open(argv[1])
lista=open(argv[2])
out=open(argv[3],"w")

dicfasta={}

for i in fasta:
	if i.startswith(">"):
		e=i.strip("\n")
	else:
		if e in dicfasta:
			dicfasta[e]+=i.strip("\n")
		else:
			dicfasta[e]=i.strip("\n")

for t in lista:
	w=">"+t.strip("\n")
	if w in dicfasta:
		out.write(w+"\n")
		out.write(dicfasta[w]+"\n")

fasta.close()
lista.close()
out.close()
			
