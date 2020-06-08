# Automate-with-Python
“Automate the boring stuff with Python” for Population Genetics



## Running the GWAS analysis

To run the GWAS itself, just edit the below commands and execute!

```
export BFILE=“Type in the prefix of the input file for plink”
export REGRESSION_MODEL=“Type in the regression model you would like to use, e.g. for binary outcomes please write logistic”
export COVARIATES_LIST=“Type in the covariates you would like to use, separated by commas e.g. Sex,Age,PC1,PC2,PC3,PC4,PC5”
export OUTPUT_FILE_NAME=“Type in the name you want your output file to have”
which plink | PLINK_PATH=$(</dev/stdin)

python3 call_plink_gwas.py -conf_file plink_gwas_config_1.txt
```
