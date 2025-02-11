# User guide

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


3. Install celescope

Make sure you have activated the `SingleCell_VDJ` conda environment before running `pip install celescope`. 
```
conda activate SingleCell_VDJ
pip install .
```

## Usage

CeleScope contains interfaces `multi_{assay}` to generate pipeline scripts for all assays. Assays can be one of:
|assay|data|kit|
|---|------|--------------|
|[vdj](./assay/multi_vdj.md)|single-cell VDJ|GEXSCOPE<sup>TM</sup> IR|
|[flv_CR](./assay/multi_flv_CR.md)|single-cell full length VDJ|sCircle<sup>TM</sup>|
|[flv_trust4](./assay/multi_flv_trust4.md)|single-cell full length VDJ|sCircle<sup>TM</sup>|
|[bulk_vdj](assay/multi_bulk_vdj.md)|bulk_vdj|NA|
|[convert10X](assay/multi_convert10X.md)|convert10X|NA|


Click on the hyperlinks above to view the uasge for each assay. Run `multi_{assay} -h` in the command line to display available arguments. For example：
```
$ multi_rna -h

usage: rna multi-samples [-h] --mapfile MAPFILE [--mod {sjm,shell}] [--queue QUEUE] [--rm_files] [--steps_run STEPS_RUN]
...
```

## [Test scripts and data](https://github.com/singleron-RD/celescope_test_script)

## [Change log](./CHANGELOG.md)


 
