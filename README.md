# FGOT

![FGOT_Overview](https://github.com/lhzhanglabtools/FGOT/blob/main/Fig1_overview.tiff)

## Overview

Interpretable transcriptional regulatory analysis by integrating single cell and spatial multi-omics data 

## Installation
The FGOT package is developed based on the Python libraries [Scanpy](https://scanpy.readthedocs.io/en/stable/) and [PyTorch](https://pytorch.org/) framework.
First clone the repository. 
```
git clone https://github.com/lhzhanglabtools/FGOT.git
cd FGOT-main
```
It's recommended to create a separate conda environment for running FGOT:
```
#create an environment called env_FGOT
conda create -n env_FGOT python=3.11

#activate your environment
conda activate env_FGOT
```

Install all the required packages:
```
pip install -r requirements.txt
```

Install FGOT:
```
python setup.py build
python setup.py install
```
The detailed information for installation can be found [here] (https://github.com/YCH-bioinf/FGOT-master)
## Tutorial
For the step-by-step tutorials are included in the 'Tutorial' folder to show how to use FGOT.

- [Tutorial 1a: Running FGOT on paired scRNA-seq and scATAC-seq data of PBMC](https://github.com/lhzhanglabtools/FGOT/blob/main/Tutorial/run_FGOT_on_PBMC.ipynb)
- [Tutorial 1b: Ploting the result of FGOT](https://github.com/lhzhanglabtools/FGOT/blob/main/Analysis/plot_regulatory_links_with_FGOT.html)
- [Tutorial 2: Running FGOT on unpaired scRNA-seq and scATAC-seq data of BMMC](https://github.com/lhzhanglabtools/FGOT/blob/main/Tutorial/run_FGOT_on_BMMC.ipynb)
- [Tutorial 3: Running FGOT on spatial ATAC-RNA data of P22 mouse brain](https://github.com/lhzhanglabtools/FGOT/blob/main/Tutorial/run_FGOT_on_P22.ipynb)

## Support
If you have any questions, please feel free to contact us [zhanglh@whu.edu.cn](mailto:zhanglh@whu.edu.cn). 

