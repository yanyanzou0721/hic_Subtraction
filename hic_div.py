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
import pandas
import h5py
import cooler
import click
import os
from math import celi

def read_in(file_path):
    return cooler.Cooler(file_path)


def get_div(c1,c2,range_s,range_e):
    mat1 = c1.matrix(balance=False, sparse=True)[range_s:range_e,range_s:range_e]
    mat2 = c2.matrix(balance=False, sparse=True)[range_s:range_e,range_s:range_e]
    arr1 = mat1.toarray()
    arr2 = mat2.toarray()
    arr = arr1-arr2
    return arr

def process(input1,input2,area_s,area_e,outdir):
    c1 = read_in(input1)
    c2 = read_in(input2)
    arr = get_div(c1,c2,area_s,area_e)
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111)
    im = ax.matshow(np.log10(arr), cmap='YlOrRd')
    fig.colorbar(im)
    fig.savefig(outdir+"sample_div.png")    
    
    
@click.command(name="hic_div")
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