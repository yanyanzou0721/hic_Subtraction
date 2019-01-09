# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 11:29:04 2019

@author: yyzou

this script to get the division of two hic matrix

input : .cool file with a certain resolution

---------

"""

import matplotlib.pyplot as plt
import numpy as np
import cooler
import click
import os
from os.path import exists
from math import log

def read_in(file_path):
    return cooler.Cooler(file_path)

"""
  get matrix data then calculate input1 - input2
  
  normalized by log10() with positive and negative signs unchanged
  

"""

def get_Subtraction(c1,c2,range_s,range_e):
    mat1 = c1.matrix(balance=False, sparse=True)[range_s:range_e,range_s:range_e]
    mat2 = c2.matrix(balance=False, sparse=True)[range_s:range_e,range_s:range_e]
    arr1 = mat1.toarray()
    arr2 = mat2.toarray()
    arr_sub = arr1-arr2
    arr_list = np.array([[x*log(x+1 if x>=0 else -x+1,10)/abs(x) for x in row ] for row in arr_sub])
    arr = arr_list.reshape(arr_list.shape[0],arr_list.shape[1])
    return arr

def get_fig(data,outdir):
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111)
    im = ax.matshow(data, cmap='YlOrRd')
    fig.colorbar(im)
    fig.savefig(outdir+"sample_div.png")

def process(input1,input2,area_s,area_e,outdir):
    c1 = read_in(input1)
    c2 = read_in(input2)
    arr = get_Subtraction(c1,c2,area_s,area_e)
    get_fig(arr,outdir)
            
    
@click.command(name="hic_Subtraction")
@click.argument("input1")
@click.argument("input2")
@click.option("area_s","-s",
              default=0,
              help="comparasion starts area")
@click.option("area_e","-e",
              default=2000,
              help="comparasion starts area")
@click.option("--outdir", "-O",
    default="./",
    help="path to output files.")

def main_(input1,input2,area_s,area_e,outdir):
    if not exists(outdir):
        os.mkdir(outdir)
    process(input1,input2,area_s,area_e,outdir)
    
if __name__ == "__main__":
    main_()