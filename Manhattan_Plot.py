from bioinfokit import analys, visuz
import pandas as pd 

#Read association file from GWAS analysis
df = pd.read_csv("GWAS.txt", delimiter = '\t')
print(df.head(5))

#Create duplicate of column "SNP" and split column by ":" 
df['chr'] = df.SNP.str.split(":",expand=True) [0]

#Delete "chr" prefix 
df['chr'] = df.chr.str.replace("chr","")

#Make Manhattan Plot
visuz.marker.mhat(df=df, chr='chr', pv='p', gwas_sign_line=True, markernames = True, markeridcol= 'SNP')


