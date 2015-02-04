#!/usr/bin/python3
# This scripts was used as part of a redundancy pipeline. It forms groups of homologies, when a homologie search of sequences against themselves is made. It clusters the sequences by their mutual hits
#The output is a list of fasta headers, where each cluster is divided by "---\n"
#python categorize.py tabular_blast_output_outfmt6 outfile


infile = open(argv[1],'r')
outfile=open(argv[2],"w")


title = ""
scaf = set()
scafs = []
for lines in infile:
	lines = lines.split()
	if lines[0] != title:
		title = lines[0]
		scafs.append(scaf)
		scaf = set()
		x=0
		size=lines[0].split("e")
		if float(size[1])/float(lines[3])<=2.0 and x<=1:
			scaf.add(lines[1])
			x+=1
		
	else:
		size=lines[0].split("e")
		if float(size[1])/float(lines[3])<=2.0 and x<=1:
			scaf.add(lines[1])
			x+=1
scafs.append(scafs)
del scafs[0]
del scafs[-1]

infile.close()

def consolidate(sets):
    setlist = [s for s in sets if s]
    for i, s1 in enumerate(setlist):
        if s1:
            for s2 in setlist[i+1:]:
                intersection = s1.intersection(s2)
                if intersection:
                    s2.update(s1)
                    s1.clear()
                    s1 = s2
    return [s for s in setlist if s]



for i in consolidate(scafs):
	for a in i:
		outfile.write(a+"\n")
	outfile.write("---\n")

outfile.close()
