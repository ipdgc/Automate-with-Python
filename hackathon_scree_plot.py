#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 12:57:24 2020

@author: User
"""

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
    
    
# scree_plot("~/Desktop/IPDGC_pre-impute")
