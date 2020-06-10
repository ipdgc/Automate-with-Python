from bioinfokit import analys, visuz
import pandas as pd
import argparse

def plot_manhattan(df):
    visuz.marker.mhat(df=df, chr='CHR', pv='P', gwas_sign_line=True, markernames = True, markeridcol= 'SNP', figtype='png')

def main():
    #the input file should be the output of plink GWAS which is an association file such as:
    #CHR   SNP              BP        A1       TEST    NMISS         OR       SE      L95      U95         STAT            P
    #1   1:20991002:C:T   20991002    T        ADD     2000     0.9922    1.424  0.06088    16.17    -0.005522       0.9956
    #1   1:21009211:C:T   21009211    T        ADD     2000         NA       NA       NA       NA           NA           NA
    #1   1:21009279:C:T   21009279    T        ADD     2000      1.224    1.416  0.07634    19.63        0.143       0.8863
    #python Manhattan_Plot.py -file_name Demo_plinkgwas_test1.assoc.logistic -out_file_name DemoManhattan
    #this will produce the image: manhatten.png
    parser = argparse.ArgumentParser()
    parser.add_argument("-file_name", "--file_name",  help="Provide association filename with p-values")
    args = parser.parse_args()
    print('input file:', args.file_name)

    #Read association file from GWAS analysis
    df = pd.read_csv(args.file_name, delim_whitespace=True)
    print('shape:', df.shape)

    plot_manhattan(df)

main()
