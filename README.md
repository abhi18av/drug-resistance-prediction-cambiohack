# drug-resistance-prediction-hackathon

Predicting drug resistance using Machine Learning


## Overview of process


1. Download and prepare the variant calling and drug resistance results

2. Download all `VCF` files for samples

3. Download results of `tb-profiler` for these samples

4. Syncronize these files as per common genome IDs

5. Filter out SNP from the `synced VCFs`

6. Filter out resistance and lineage oriented fields from `synced tb-profiler`

7. Merge the `filtered SNP from VCF` files and do feature engineering

8. Split the final dataset into test-train data (30/70 split)

9. Train the `Random Forest` algorithm on the training dataset

10. Check the accuracy as per AUC metric

11. Iterate on steps 7 - 10 till satisfactory results are achieved
