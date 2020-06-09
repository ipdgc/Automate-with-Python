# Automate-with-Python
“Automate the boring stuff with Python” for Population Genetics

## Generate principal components
Filter and prune pre-imputed data to generate principal components.  
*geno_path = quality controlled bfiles pre-impution*  
*out_path = name/location of principal component output*  
*exclusion_region = problematic area in the genome. Hg19 regions file included in github files.*  

```python
import subprocess

def generate_PC(geno_path, out_path, exclusion_region):

#    step= "GENERATING PCs"
#    print(step)

    #Make sure to use high-quality SNPs 
    bash1 = 'plink --bfile ' + geno_path + ' --maf 0.01 --geno 0.05 --hwe 1E-6 --exclude range ' + exclusion_region + ' --make-bed --out filter'

    # Prune out unnecessary SNPs (only need to do this to generate PCs)
    bash2 = 'plink --bfile filter --indep-pairwise 1000 10 0.02 --out prune'

    # Keep only pruned SNPs (only need to do this to generate PCs)
    bash3 = 'plink --bfile filter --extract prune.prune.in --make-bed --out prune' 

    # Generate PCs 
    bash4 = 'plink --bfile prune --pca 20 --out ' + out_path

    bash5 = 'rm filter* prune*'

    cmds = [bash1, bash2, bash3, bash4, bash5]
    
    for cmd in cmds:
        subprocess.run(cmd, shell = True)
```
## Make scree plot  
To determine optimal number of PCs to use as covariates.  
*out_path = same out_path used in the generate PCs step.*
```python
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def scree_plot(out_path):
    
    df = pd.read_csv(out_path + ".eigenval", delimiter="\t", names=['eigenvalues'])
    df['pc'] = df.index+1
    
    plt.plot(df.pc, df.eigenvalues, 'ro-', linewidth=2)
    plt.title('Scree Plot')
    plt.xlabel('Principal Components')
    plt.ylabel('Percent (%) Variance Explained')
    plt.xticks(np.arange(0, max(df.pc)+1, step=1)) 

    plt.savefig('scree_plot.png')
```
![Example scree plot](scree_plot.png)

## Generate a covariate file

```python

# Generate a covariate file
import pandas as pd

# Read .eigenvec file (from plink) and rename columns
pcs = pd.read_csv("FILTERED.eigenvec", names=('FID', 'IID', 'PC1', 'PC2', 'PC3', 'PC4', 'PC5', 'PC6', 'PC7', 'PC8', 'PC9', 'PC10', 'PC11', 'PC12', 'PC13', 'PC14', 'PC15', 'PC16', 'PC17', 'PC18', 'PC19', 'PC20'), delimiter = '\s+')

# Read .fam file and rename columns
pheno = pd.read_csv("/Users/raquelreal/Desktop/Hackthon_IPDGC_2020/RAW_test/RAW_test.fam", names=('FID', 'IID', 'PAT', 'MAT', 'SEX', 'PHENO'), sep = '\t')

# Combine the .fam file with the .eigenvec file
pheno_pcs = pd.merge(pheno, pcs, on=('FID', 'IID'), how='left')

# Save the combined file
pheno_pcs.to_csv(r'/Users/raquelreal/Desktop/Hackthon_IPDGC_2020/covar.txt', header=True, index=False, sep='\t', mode='a')

```
To run the script:
```
python3 covariate_test.py 

```

## Running the GWAS analysis

To run the GWAS itself, just edit the below commands and execute!

```
export BFILE=“Type in the prefix of the input file for plink”
export REGRESSION_MODEL=“Type in the regression model you would like to use, e.g. for binary outcomes please write logistic”
export COVARIATES_LIST=“Type in the covariates you would like to use, separated by commas e.g. Sex,Age,PC1,PC2,PC3,PC4,PC5”
export OUTPUT_FILE_NAME=“Type in the name you want your output file to have”
export PLINK_PATH=“$(dirname $(which plink))/”

python3 call_plink_gwas.py -conf_file plink_gwas_config_1.txt
```
