# NGS utilities

Several simple scripts for simple bioinformatics tasks


##Usage:

In the command line:

1. **countReads.py**: count the fastq reads in a set of file, given a read header template
<pre><code>python countReads.py [coma separated list of fastq files] [fastq header]
</code></pre>

2. **blast2goannott2definition.py**: given a .annot file from blast2go output where the description of the gene is the acession number, this script substitute the acession with the description from ncbi database
<pre><code>python blast2goannott2definition.py blast2go.annot output.annot "mail@example.com"
</code></pre>

3. **categorize.py**: This scripts was used as part of a redundancy pipeline. It forms groups of homologies, when a homologie search of sequences against themselves is made. It clusters the sequences by their mutual hits
<pre><code>python categorize.py tabular_blast_output_outfmt6 outfile
</code></pre>

4. **fastalist.py**: It retrives a subset of fasta sequences, given a list of headers and a a set of fasta sequences.
<pre><code>python fastalist.py setOfFasta.fasta headersList output.fasta
</code></pre>

5. **stats.py**: make basic stats for a group of fasta files
<pre><code>python stats.py fastafile
</code></pre>


##License:

GPLv2


