# NGS Read Quality Control and FASTQ Analysis

## Project Overview

This project demonstrates a beginner-friendly NGS quality-control workflow using a publicly available sequencing dataset from the NCBI Sequence Read Archive (SRA).

The project covers FASTQ inspection, sequence statistics using Linux/AWK and Python, and quality assessment using FastQC and MultiQC.

## Dataset Information

- Dataset:SRR1553607
- Study: PRJNA257197
- Experiment: SRX674270
- Organism: Zaire ebolavirus
- Sample description: Genome sequencing from the 2014 Sierra Leone outbreak
- Library strategy: RNA-Seq
- Library source: Transcriptomic
- Library selection: cDNA
- Platform: Illumina
- Layout:Paired-end
- Original read layout: 2 × 101 bp

Dataset source: [NCBI SRA SRR1553607](https://www.ncbi.nlm.nih.gov/sra/?term=SRR1553607)

### Data Subset

This project initially downloaded 10,000 spots from the public SRA accession for educational quality-control analysis.

The FASTQ records produced by the download were 202 bp long. The SRA metadata describes two 101 bp reads per spot. Therefore, the downloaded representation should not be confused with separately assessed paired-end reads.

Raw sequencing data is not included in this repository. The accession is provided for reproducibility.

## Tools and Technologies

- Linux / macOS Terminal
- AWK
- Python 3
- SRA Toolkit
- FastQC v0.13.0
- MultiQC
- Git and GitHub

## Analysis Performed

### 1. FASTQ Inspection

Inspected FASTQ records to understand:
- Read identifiers
- Nucleotide sequences
- Quality score lines
- FASTQ record structure

### 2. Linux/AWK Statistics

Calculated:
- Number of downloaded records
- Total nucleotide bases
- Average sequence length
- A, T, G and C counts
- GC content

### 3. Python Sequence Statistics

Developed a Python script to calculate sequence statistics independently and cross-check the AWK results.

### 4. FastQC Quality Assessment

Evaluated:
- Basic Statistics
- Per Base Sequence Quality
- Per Sequence Quality Scores
- Per Base Sequence Content
- Per Sequence GC Content
- Per Base N Content
- Sequence Length Distribution
- Sequence Duplication Levels
- Overrepresented Sequences
- Adapter Content
- K-mer Content

### 5. MultiQC

Generated an aggregated quality-control report from FastQC output.

## Results

| Metric | Result |
|---|---:|
| Downloaded spots | 10,000 |
| FASTQ records | 10,000 |
| Total bases | 2,020,000 |
| Combined record length | 202 bp |
| Average record length | 202 bp |
| A count | 409,551 |
| T count | 411,720 |
| G count | 598,545 |
| C count | 600,184 |
| GC content | 59.34% |

### FastQC Findings

- Per Base Sequence Quality: PASS
- Per Sequence Quality Scores: PASS
- Per Base Sequence Content: FAIL
- Per Sequence GC Content: FAIL
- Remaining reported modules: PASS

The two failed modules indicate unusual nucleotide composition and GC distribution relative to FastQC's expectations. These findings require biological and technical context and do not independently establish contamination or poor sequencing quality.


## Key Learning Outcomes

- Understanding the FASTQ format
- Using Linux commands for sequencing data inspection
- Writing Python scripts for sequence statistics
- Calculating GC content and nucleotide frequencies
- Understanding Phred quality scores
- Interpreting FastQC modules
- Recognising sequence composition bias
- Generating aggregated quality reports with MultiQC
- Documenting a reproducible bioinformatics workflow

## Limitations

- Only 10,000 spots were used in this initial exercise.
- The downloaded records represent paired-end reads in a combined 202 bp format.
- The two failed FastQC modules have not been attributed to a definitive biological or technical cause.
- No conclusions about the complete original sequencing experiment should be drawn from this subset alone.

## Author

Dipshikha Yadav

