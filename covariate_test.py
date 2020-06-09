# Generate a covariate file

import pandas as pd

# Read .eigenvec file (from plink) and rename columns
pcs = pd.read_csv("FILTERED.eigenvec", names=('FID', 'IID', 'PC1', 'PC2', 'PC3', 'PC4', 'PC5', 'PC6', 'PC7', 'PC8', 'PC9', 'PC10', 'PC11', 'PC12', 'PC13', 'PC14', 'PC15', 'PC16', 'PC17', 'PC18', 'PC19', 'PC20'), delimiter = '\s+')
print(pcs.head(5))

# Read .fam file and rename columns
pheno = pd.read_csv("/Users/raquelreal/Desktop/Hackthon_IPDGC_2020/RAW_test/RAW_test.fam", names=('FID', 'IID', 'PAT', 'MAT', 'SEX', 'PHENO'), sep = '\t')
print(pheno.head(5))

# Combine the .fam file with the .eigenvec file
pheno_pcs = pd.merge(pheno, pcs, on=('FID', 'IID'), how='left')
print(pheno_pcs.head(5))

# Save the combined file
pheno_pcs.to_csv(r'/Users/raquelreal/Desktop/Hackthon_IPDGC_2020/covar.txt', header=True, index=False, sep='\t', mode='a')
