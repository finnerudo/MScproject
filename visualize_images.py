#!/usr/bin/env python

##########################################################
#	Event display for larcv-root files 
#       This script should be run with Larcv1   
##########################################################



import os, sys, ROOT                                                    
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from larcv import larcv
import cv2
import gc


def EvDisp(input_file, entry, plane, producer="wire"):
    iom = larcv.IOManager(larcv.IOManager.kREAD)
    iom.add_in_file(input_file)
    iom.initialize()
    print("Number of entries in this file: " + str(iom.get_n_entries()))
    # Access entry
    # entries 4, 5 are interesting candidates
    img_plane= plane 
    iom.read_entry(entry)
    # Access a product instance (type,label) = (image2d,data)
    image2d_data = iom.get_data(larcv.kProductImage2D,producer)
    print("Selected entry: " + str(entry))
    print("Run: " + str(image2d_data.run()))
    print("Subrun: " + str(image2d_data.subrun()))
    print("Event: " + str(image2d_data.event()))
    whole_img = image2d_data.at(img_plane)
    whole_image=larcv.as_ndarray(whole_img)
    fig, ax1 = plt.subplots(1,1,figsize=(50,20))
    ax1.imshow(whole_image.transpose(), cmap="jet",origin="lower")
    #plt.axis("off")
    plt.show()
    iom.finalize()
    gc.collect()


