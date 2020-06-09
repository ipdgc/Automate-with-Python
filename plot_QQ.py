import numpy as np
import statsmodels.api as sm
import pylab as py
import argparse
import pandas as pd
import matplotlib.pyplot as plt
import math

def plot_QQ(pvals, out_file_name):
    observed=np.sort(pvals)

    lobs=-1*(np.log10(observed))
    expected=np.array( range(1,len(observed)+1) )

    tmp = [x / (len(expected)+1) for x in expected]
    lexp=-1*(np.log10(tmp))

    maxNum=max(max(lexp),max(lobs))
    maxLimit=math.ceil(maxNum)+1

    #plot
    label_font=12
    plot_title='QQ plot'
    plt.scatter(lexp,lobs, s=12,c='black')
    plt.plot( [0,maxLimit],[0,maxLimit],c='red' )
    plt.xlim(0,maxLimit)
    plt.ylim(0,maxLimit)
    plt.title(plot_title)
    plt.xlabel('Expected (−logP)',fontsize=label_font)
    plt.ylabel('Observed (-logP)',fontsize=label_font)
    out_file_name=out_file_name+ '.png'
    plt.savefig(out_file_name)

def main():
    #QQ calcualtion is based on: https://github.com/GP2-TNC-WG/GP2-Bioinformatics-course/blob/master/Module_III.md#3
    #the input file should be the output of plink GWAS which is an association file such as:
    #CHR   SNP              BP        A1       TEST    NMISS         OR       SE      L95      U95         STAT            P
    #1   1:20991002:C:T   20991002    T        ADD     2000     0.9922    1.424  0.06088    16.17    -0.005522       0.9956
    #1   1:21009211:C:T   21009211    T        ADD     2000         NA       NA       NA       NA           NA           NA
    #1   1:21009279:C:T   21009279    T        ADD     2000      1.224    1.416  0.07634    19.63        0.143       0.8863
    #python plot_QQ.py -file_name Demo_plinkgwas_test1.assoc.logistic -out_file_name DemoQQ
    #read user arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-file_name", "--file_name",  help="Provide filename with p-values")
    parser.add_argument("-out_file_name", "--out_file_name",  help="Provide name for output file")
    args = parser.parse_args()
    print('input file:', args.file_name)
    print('output_file:', args.out_file_name)

    df = pd.read_csv(args.file_name, delim_whitespace=True)
    pvals = df['P']
    plot_QQ(pvals, args.out_file_name)

main()
