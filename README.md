# Introduction
SingCell-VDJ and Bulk-VDJ analysis pipeline.

## Installation
1. Clone repo
```
git clone https://github.com/Chenjunjie1996/SingleCell_VDJ.git
```

2. Create conda environment and install conda packages. 
It is recommended to use [mamba](https://github.com/mamba-org/mamba) (which is a faster replacement for Conda):
```
conda install mamba
cd SingleCell_VDJ
mamba create -n SingleCell_VDJ -y --file conda_pkgs.txt
```

3. Install
Make sure you have activated the `SingleCell_VDJ` conda environment before running `pip install celescope`. 
```
conda activate SingleCell_VDJ
pip install celescope
```

## Usage
CeleScope contains interfaces `multi_{assay}` to generate pipeline scripts for all assays. Assays can be one of:
|assay|data|
|---|------
|[vdj](doc/assay/multi_vdj.md)|single-cell VDJ
|[flv_trust4](doc/assay/multi_flv_trust4.md)|single-cell full length VDJ
|[flv_CR](doc/assay/multi_flv_CR.md)|single-cell full length VDJ
|[bulk_vdj](doc/assay/multi_bulk_vdj.md)|bulk_vdj
|[rna](doc/assay/multi_convert10X.md)|single-cell RNA-Seq
