import h5py
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.anchored_artists import AnchoredSizeBar
import matplotlib.font_manager as fm 
import numpy as np



##########################################################
#
#      Script to visualize larcv images in hdf5 format
#               Author: Luis Mora Lepin
#          luis.moralepin@postgrad.manchester.ac.uk
#
###########################################################


'''
Things to do: 
* Add text with run,subrun,event 
* Where the images will be stored? 
'''

# Function to get the entry of an event given its labels (run,subrun and event)
def SearchID(run,subrun,event,id_list):
    id = 0 
    # First entry in hdf5 metadata is event number and 3rd entry is run number  
    for element in id_list:
        if(element[1]==event and element[2]==subrun and element[3]==run):
            id = element[0]
        else:
            pass
    # fail case
    if (id==0):
        print("No such event found! Please check that such an event exists.")
        print("Displaying event: {}, subrun: {}, run: {}".format(id_list[0][1], id_list[0][2], id_list[0][3]) )
    return id 

def PlaneLabel(plane):
    plane_label = 'none'
    if(plane == 0):
        plane_label='U'
    elif(plane==1):
        plane_label='V'
    elif(plane==2):
        plane_label='Y'
    else:
        print("Error, plane number out of range")
    return plane_label 

def DatasetSelector(dataset):
    file='none'
    if(dataset == 'mc'):
        file='bnb_run3_mc_larcv.h5'
    elif(dataset == 'data'):
        file='bnb_run3_open_data_larcv.h5'
    elif(dataset == 'dirt'):
        file='bnb_run3_dirt_larcv.h5'
    elif(dataset == 'ext'):
        file='bnb_run3_ext_larcv.h5'
    else:
        print('Error, wrong dataset input')
    return file 


def EvDisp(run,subrun,event,plane,dataset,debug=False):
    #base_dir = "/hepgpu4-data2/lmlepin/Ole_files/"
    # adjust based on where you're saving the data files
    base_dir = "data/"
    input_file=base_dir+DatasetSelector(dataset)
    producer = 'wire'
    f = h5py.File(input_file,'r')
    event_id_list = f['eventid']
    entry = SearchID(run,subrun,event,event_id_list)
    # restating values of dataset, event, entry, as they can be modified if incorrect value is selected.
    event = event_id_list[entry][1]
    subrun = event_id_list[entry][2]
    run = event_id_list[entry][3]
    #if(debug):
    #	entry = 1000
    #else: 
    #	entry = SearchID(run,subrun,event,event_id_list)
    plane_label = PlaneLabel(plane)
    #print(list(f['image2d'].keys()))
    #print(list(f['image2d']['metadata']))
    #print(list(f['image2d']['wire'].keys()))
    wire_set = f['image2d'][producer]
    print(wire_set)
    image=wire_set[list(wire_set.keys())[0]]
    fontprops=fm.FontProperties(size=10)
    plot_title = "BNB Run 3, Dataset: " + dataset + ", Plane : " + plane_label + ", Event: " + str(event) + ", Entry: " + str(entry)
    fig, ax1= plt.subplots(1,1,figsize=(8.5,3.5))
    plt.title(plot_title)
    plt.xlabel("Wire number")
    plt.ylabel("Time tick")
    ax1.imshow(image[entry,plane,:,:],cmap='turbo',origin="lower")
    scalebar1= AnchoredSizeBar(ax1.transData,
                                100,'30 cm','lower left',
                                color='white',
                                frameon=False,
                                size_vertical=1,
                                fontproperties=fontprops)
    ax1.add_artist(scalebar1)
    plt.show()

    
def list_entries(dataset, sliced=False, slice_val = 0):
    base_dir = "data/"
    input_file=base_dir+DatasetSelector(dataset) 
    
    f = h5py.File(input_file,'r')
    event_id_list = f['eventid']
    
    # can remove entries from your printed list, as there are many
    
    if sliced == True:    
        i = 0
        for element in event_id_list:
            if i > slice_val:
                break;
            print("Event: {}, Subrun: {}, Run: {}".format(element[1], element[2], element[3]))
            i += 1
    else:
        print("Caution: You are printing every event in the file (there are {}).".format(len(event_id_list)))
        for element in event_id_list:
            print("Event: {}, Subrun: {}, Run: {}".format(element[1], element[2], element[3]))
    
            