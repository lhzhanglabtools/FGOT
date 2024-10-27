# FGOT-master

## Overview

Integrating single-cell or spatial transcriptomic and epigenomic data enables scrutinizing the transcriptional regulatory mechanisms controlling cell fate.  In current methods, multi-omics measurements are projected into a shared latent space, without connecting transcriptomic and epigenomic features, such as target genes and their regulatory elements, and in addition, the cell-type specific regulatory mechanism are often missing. To address both problems, we develop a Feature Guided Optimal Transport (FGOT) method, which allows incorporation prior knowledge of genes and their regulatory elements relationship, to simultaneously uncover cellular heterogeneity and their associated transcriptional regulatory links. Benchmarking on simulation data and validating via histone modification data or 3D genomics data for matched real data show good robustness and accuracy in integration and inference of regulatory links. From both paired and unpaired multi-omics data, it is found that for the same gene different type of cells have different regulatory relationship. Application of FGOT to paired spatial multi-omics data show spatial differences in regulatory links for the same gene. The method allows systematic screening of more specific regulatory elements in diseases at single-cell level.

## Requirements

* anndata==0.10.8
* gudhi==3.9.0
* hnswlib==0.8.0
* networkx==2.6.3
* numpy==2.0.0
* pandas==1.3.5
* scanpy==1.10.2
* scikit_learn==1.5.1
* scipy==1.14.0
* torch==2.2.0
* tqdm==4.65.0

## Data
All datasets used in this study are already published and were obtained from public data repositories. Simulated datasets 1 and 2 were two batches of scRNA-seq with batch effects generated by the R package 'Splatter'. The PBMC data was published on https://support.10xgenomics.com/single-cell-multiome-atac-gex/datasets/1.0.0/pbmc_granulocyte_sorted_10k?. The BMMC data was obtained from the GEO repository (accession no. GSE159417). The spatial-ATAC-RNA-seq mouse brain data was from https://cells.ucsc.edu/?ds=brain-spatial-omics.

The details of all datasets used are available in the Methods section. The data used in our experiments have been uploaded and are freely available at https://drive.google.com/drive/folders/1H3GLroILCYSaGjowwJUjaO4JlKcNDdvy.

## Tutorial
For the step-by-step tutorials, we have released them at https://github.com/YCH-bioinf/FGOT-master/tree/main/examples.




## Citation
