# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 11:29:04 2019

@author: yyzou

this script to get the subtraction of two hic matrix

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

def get_Subtraction(c1,c2,area_s,area_e):
    mat1 = (c1.matrix(balance=False, sparse=True)[area_s:area_e,area_s:area_e]).toarray()
    mat2 = (c2.matrix(balance=False, sparse=True)[area_s:area_e,area_s:area_e]).toarray()
    arr1 = (mat1/mat1.sum())*(mat1.sum()+mat2.sum())
    arr2 = (mat2/mat2.sum())*(mat1.sum()+mat2.sum())
    arr_sub = arr1-arr2
    arr_list = np.array([[x*log(x+1 if x>=0 else -x+1,10)/(abs(x)+1) for x in row ] for row in arr_sub])
    arr = arr_list.reshape(arr_list.shape[0],arr_list.shape[1])
    return arr


def get_fig(data,area_s,area_e,outdir,outfig):
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111)
    im = ax.matshow(data,cmap='seismic',interpolation='none') ## vmin vmax determin the range of colorbar
#    im = ax.matshow(data,cmap='YlOrRd',vmin=-1, vmax=1,interpolation='none')
    fig.colorbar(im)
    fig.savefig(outdir+outfig)

def process(input1,input2,area_s,area_e,outdir,outfig):
    c1 = read_in(input1)
    c2 = read_in(input2)
    arr = get_Subtraction(c1,c2,area_s,area_e)
    get_fig(arr,area_s,area_e,outdir,outfig)


@click.command(name="hic_Subtraction")
@click.argument("input1")
@click.argument("input2")
@click.option("area_s","-s",
              default=0,
              help="comparasion starts area")
@click.option("area_e","-e",
              default=None,
              help="comparasion starts area")
@click.option("--outdir", "-O",
    default="./",
    help="path to output files.")
@click.option("--outfig", "-fig",
    default="test.png",
    help="name of output figure.")

def main_(input1,input2,area_s,area_e,outdir,outfig):
    if not exists(outdir):
        os.mkdir(outdir)
    process(input1,input2,area_s,area_e,outdir,outfig)

if __name__ == "__main__":
    main_()
