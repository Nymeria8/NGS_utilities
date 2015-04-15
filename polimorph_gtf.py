from sys import argv

def read_gtf(infile):
	gtf=open(infile)
	gtf_dic={}
	for i in gtf:
		line=i.split("\t")
		if line[2]=='exon':
			gene=line[8].split('"')[1]
			if line[0] not in gtf_dic:
				gtf_dic[line[0]]=[]
				for h in range(int(line[3])):
					gtf_dic[line[0]].append(' ')
				for f in range(int(line[3]),int(line[4])):
					gtf_dic[line[0]].append(gene+'_E')
				corrent_gene=gene
			else:
				if corrent_gene==gene:
					for h in range(len(gtf_dic[line[0]]),int(line[3])):
						gtf_dic[line[0]].append(gene+'_I')
					for f in range(int(line[3]),int(line[4])):
						gtf_dic[line[0]].append(gene+'_E')
				else:
					corrent_gene=gene			
					for h in range(len(gtf_dic[line[0]]),int(line[3])):
						gtf_dic[line[0]].append(' ')
					for f in range(int(line[3]),int(line[4])):
						gtf_dic[line[0]].append(gene+'_E')
	gtf.close()
	return gtf_dic


def read_vcf(infile):
	vcf=open(infile)
	vcf_dic={}
	pol=0
	for i in vcf:
		if i.startswith("#")==False:
			pol+=1
			d=i.split()
			if d[0] not in vcf_dic:
				vcf_dic[d[0]]=[int(d[1])]
			else:
				vcf_dic[d[0]].append(int(d[1]))
	print("total polimorfisms")
	print(pol)
	vcf.close()
	return vcf_dic


def stats (dic,vcf):
	polE=0
	polI=0
	polU=0
	genesE=set()
	genesI=set()
	for key, value in vcf.items():
		for snp in value:
			if dic[key][snp-1]==' ':
				polU+=1
			elif dic[key][snp-1].endswith('_E'):
				polE+=1
				genesE.add(dic[key][snp-1][:-3])
			elif dic[key][snp-1].endswith('_I'):
				polI+=1
				genesI.add(dic[key][snp-1][:-3])
	print('polimorphisms in coding regions')
	print(str(polE))
	print('polimorphisms in Introns')
	print(str(polI))
	print('polimorphisms in uncaracterized regions')
	print(str(polU))
	print('genes with polimorphisms in exons')
	print(str(len(genesE)))	
	print('genes with polimorphisms in introns')
	print(str(len(genesI)))
	print('genes with polimorphisms')
	print(str(len(genesE|genesI)))

stats(read_gtf(argv[1]),read_vcf(argv[2]))
