## Download and unpack cellranger soft and reference file.
```
Soft:
wget -O cellranger-8.0.1.tar.gz "https://cf.10xgenomics.com/releases/cell-exp/cellranger-8.0.1.tar.gz?Expires=1738964769&Key-Pair-Id=APKAI7S6A5RYOXBWRPDA&Signature=amrSZeLDPqCjpbjb7Yek7kyj~7zVlibyIFBx-wDdmiZLloujnDEEfI9iNEcUDXP7qhOT39vBtuqx8qrJ0WbstCERfyAY4n5U7hrd2Go-NxYOseTFk8vawTRlCxrGEy7nyS76JrvwT27V08xgQJCD5uxob0pnxIBtcKJYmSxPZ8x6KslsSX1OTsJy8MPXMJaEepUsDkpgcJOo0L3gKAoMD9NQVA-6ehJ6mtjoDET-StLfNxCTGbm3p2AoyHbuYuhSB1imxhNQwMB7dVpIYRu7AHO8EfkcrVvL4CErKDY-Vvty4sZIyLTtOQGcAx-K78h0m3-8v0dT8Awj53S0TVxZGA__"
tar -xzvf cellranger-8.0.1.tar.gz

If the link is invalid, you can download it from the official website
https://www.10xgenomics.com/support/software/cell-ranger/downloads/previous-versions

Reference: human and mouse
wget "https://cf.10xgenomics.com/supp/cell-vdj/refdata-cellranger-vdj-GRCh38-alts-ensembl-7.1.0.tar.gz"
wget "https://cf.10xgenomics.com/supp/cell-vdj/refdata-cellranger-vdj-GRCm38-alts-ensembl-7.0.0.tar.gz"

tar -xzvf refdata-cellranger-vdj-GRCh38-alts-ensembl-7.1.0.tar.gz
tar -xzvf refdata-cellranger-vdj-GRCm38-alts-ensembl-7.0.0.tar.gz

Reference: Other species
Should provide customized reference and primer sequence file.
Rabbit: 
https://github.com/Chenjunjie1996/vdj_reference/tree/main/Rabbit
```

## Usage

```
Human or mouse:
conda activate SingleCell_VDJ
multi_flv_CR \
    --mapfile ./mapfile \
    --thread 8 \
    --seqtype BCR \
    --allowNoLinker \
    --ref_path "/path/refdata-cellranger-vdj-GRCh38-alts-ensembl-7.1.0" \
    --soft_path "/path/cellranger/cellranger-8.0.1/cellranger" \
    --not_refine\
    --mod shell

Other species: 
conda activate SingleCell_VDJ
multi_flv_CR \
    --mapfile ./mapfile \
    --thread 8 \
    --seqtype BCR \
    --allowNoLinker \
    --ref_path "/path/ref/vdj_IMGT_rabbit" \
    --soft_path "/path/cellranger/cellranger-8.0.1/cellranger" \
    --other_param " --inner-enrichment-primers=/path/ref/primer.txt " \
    --not_refine \
    --mod shell
```

## Arguments
`--mapfile` Mapfile is a tab-delimited text file with as least three columns. Each line of mapfile represents paired-end fastq files.

1st column: Fastq file prefix.  
2nd column: Fastq file directory path.  
3rd column: Sample name, which is the prefix of all output files.  
4th column: The single cell rna directory after running CeleScope is called `matched_dir`.

Example

Sample1 has 2 paired-end fastq files located in 2 different directories(fastq_dir1 and fastq_dir2). Sample2 has 1 paired-end fastq file located in fastq_dir1.
```
$cat ./my.mapfile
fastq_prefix1	fastq_dir1	sample1 sample1_matched_rna
fastq_prefix2	fastq_dir2	sample1 sample1_matched_rna
fastq_prefix3	fastq_dir1	sample2 sample2_matched_rna

$ls fastq_dir1
fastq_prefix1_1.fq.gz	fastq_prefix1_2.fq.gz
fastq_prefix3_1.fq.gz	fastq_prefix3_2.fq.gz

$ls fastq_dir2
fastq_prefix2_1.fq.gz	fastq_prefix2_2.fq.gz
```

## Features
### barcode

- Demultiplex barcodes.
- Filter invalid R1 reads, which includes:
    - Reads without linker: the mismatch between linkers and all linkers in the whitelist is greater than 2.  
    - Reads without correct barcode: the mismatch between barcodes and all barcodes in the whitelist is greater than 1.  
    - Reads without polyT: the number of T bases in the defined polyT region is less than 10.
    - Low quality reads: low sequencing quality in barcode and UMI regions.


### convert

- Convert barcodes and UMI to 10X format.

Output

- `02.convert/barcode_correspond.txt` Recording barcodes correspondence.

- `02.convert/{sample}_S1_L001_R1_001.fastq.gz` New R1 reads as cellranger input.

- `02.convert/{sample}_S1_L001_R2_001.fastq.gz` New R2 reads as cellranger input.

### assemble

- TCR/BCR Assemble by Cellranger.

- Generate Mapping, Cells, V(D)J annotations metrics in html.


### summarize

- Convert 10X barcode of assemble result back to SGR barcode.

- Generate Productive contigs sequences and annotation files.

- Generate VDJ-annotation metrics in html.


### match

- Assembled results match with sc-RNA library.

- Generate matched VDJ-annotation metrics, clonetypes table and bar-plot of clonetypes distribution in html.


### mapping

- Output TSNE-plot of Assembled T/B Cells.


### refine_vdj

- Refine barcodes where "is_cell=False" and have multi productive chains.

- There are three methods to filter noise: SNR, AUTO, NOT_FILTER

## Output files
### barcode

- `01.barcode/{sample}_2.fq(.gz)` Demultiplexed R2 reads. Barcode and UMI are contained in the read name. The format of 
the read name is `{barcode}_{UMI}_{read ID}`.

### assemble

- `03.assemble/{sample}` Cellranger vdj results.

### summarize

- `filtered_contig_annotations.csv` High-level annotations of each high-confidence contigs from cell-associated barcodes.

- `filtered_contig.fasta` High-confidence contig sequences annotated in the filtered_contig_annotations.csv.

- `productive_contig_annotations.csv` Annotations of each productive contigs from cell-associated barcodes. This is a subset of filtered_contig_annotations.csv.

- `productive_contig.fasta` Productive contig sequences annotated in the productive_contig_annotations.csv.

- `clonotypes.csv` High-level descriptions of each clonotype.

### match

- `matched_contig_annotations.csv` High-level annotations of each high-confidence contigs from matched cell-associated barcodes.

- `matched_contig.fasta` High-confidence contig sequences annotated in the matched_contig_annotations.csv.

- `matched_productive_contig_annotations.csv` Annotations of each productive contigs from matched cell-associated barcodes. This is a subset of matched_contig_annotations.csv.

- `matched_productive_contig.fasta` Productive contig sequences annotated in the matched_productive_contig_annotations.csv.

- `clonotypes.csv` High-level descriptions of each clonotype where barcodes match with scRNA-Seq.

### mapping
- `06.mapping/{sample}_mapping.pdf` TSNE-plot of Assembled Cells.

