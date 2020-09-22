# drug-resistance-prediction-hackathon

Predicting drug resistance using Machine Learning


## Contribution ides

I've documented some ideas here 

https://github.com/abhi18av/drug-resistance-prediction-cambiohack/projects/1


## Overview of ML process


1. Download and prepare the variant calling and drug resistance results - DONE

2. Download all `VCF` files for samples - DONE
 
3. Download results of `tb-profiler` for these samples - DONE

4. Syncronize these files as per common genome IDs - DONE

5. Filter out SNP from the `synced VCFs` - DONE

6. Filter out resistance and lineage oriented fields from `synced tb-profiler`- DONE

7. Merge the `filtered SNP from VCF` files - DONE


You can get the results of this stage through this link

https://1drv.ms/u/s!AtDyzJXLzSCVgaBRAOeffZf3Zi6QtA?e=bwp8P5



8. Do feature engineering to obtain a format suitable for machine learning

9. Split the final dataset into test-train data (30/70 split)

10. Train the `Random Forest` algorithm on the training dataset

11. Check the accuracy as per AUC metric

12. Iterate on steps 7 - 10 till satisfactory results are achieved
