
# FASTQ Sequence Statistics
# Project 03: NGS Read Quality Control

fastq_file = "data/SRR1553607.fastq"

total_reads = 0
total_bases = 0

a_count = 0
t_count = 0
g_count = 0
c_count = 0

with open(fastq_file, "r") as file:

    for line_number, line in enumerate(file):

        if line_number % 4 == 1:

            sequence = line.strip().upper()

            total_reads += 1
            total_bases += len(sequence)

            a_count += sequence.count("A")
            t_count += sequence.count("T")
            g_count += sequence.count("G")
            c_count += sequence.count("C")

gc_content = ((g_count + c_count) / total_bases) * 100

average_length = total_bases / total_reads

print("FASTQ SEQUENCE STATISTICS")
print("-------------------------")

print("Total reads:", total_reads)
print("Total bases:", total_bases)
print("Average read length:", average_length)

print("A:", a_count)
print("T:", t_count)
print("G:", g_count)
print("C:", c_count)

print("GC Content:", round(gc_content, 2), "%")
