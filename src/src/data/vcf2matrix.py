import allel
# see http://alimanfoo.github.io/2017/06/14/read-vcf.html for allel tutorial
import pandas as pd

vcf = allel.read_vcf("_resources/synced/snpFiles/cohort.bqsr.filter.snps.vcf")

def vcf_get_index(vcf):
    """Return index as "CHR.POS"."""
    return [
        ".".join([chrom, str(pos)]) for chrom, pos in zip(
            vcf["variants/CHROM"],
            vcf["variants/POS"]
        )
    ]

def vcf_get_columns(vcf):
    """Return columns as "SAMPLE_ID"."""
    return vcf["samples"]

def vcf_to_snp_count(vcf):
    """Yield snp counts per sample, iterating over the snps in vcf."""
    for gt in vcf["calldata/GT"]:
        # GT value per allele is 0 if ref, >0 if alt.
        # see https://samtools.github.io/hts-specs/VCFv4.2.pdf section 1.4.2.
        n_snps = [sum(allele > 0) for allele in gt]
        yield n_snps

snps = pd.DataFrame(
    vcf_to_snp_count(vcf),
    index=vcf_get_index(vcf),
    columns=vcf_get_columns(vcf)
)
print(snps)
