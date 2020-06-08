#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 11:41:00 2020

@author: User
"""


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


generate_PC("RAW_test", "test", "~/runs/krohn/krohn/Main_0_Data/exclusion_regions_hg19.txt")    
