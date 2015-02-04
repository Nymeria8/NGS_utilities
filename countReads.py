#Counts reads of several fastq files
#python countReads.py [coma separated list of fastq files] [fastq header]

from sys import argv


def conta (inputt,header):
	listas=inputt.split(",")
	for i in listas:
		lis= open (i)
		s=0
		for d in lis:
			if (d.startswith(header)==True):
				s+=1
		lis.close()
		print (s)
		
conta(argv[1], argv[2])
