# drug-resistance-prediction-hackathon

Predicting drug resistance using Machine Learning


## Overview of process


1. Download and prepare the variant calling and drug resistance results
  1. Download all `VCF` files for samples
  2. Download results of `tb-profiler` for these samples
  3. Syncronize these files as per common genome IDs
  4. Filter out SNP from the `synced VCFs`
  5. Filter out resistance and lineage oriented fields from `synced tb-profiler`


2. Merge the `filtered SNP from VCF` files and do feature engineering

3. Split the final dataset into test-train data (30/70 split)

4. Train the `Random Forest` algorithm on the training dataset

5. Check the accuracy as per AUC metric

6. Iterate on steps 2 - 5 till satisfactory results are achieved
