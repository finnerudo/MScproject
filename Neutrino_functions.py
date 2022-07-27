import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
#weight, bins, name, logscale = None, y_err = None
#log_scale=logscale, labels = labels

def histogram_plot(MC_frame, variable, bins, name, scaling, plot_data = None, logscale = None, dataFrame = None):
    #x = 0.5*(bins[1:]+ bins[:-1])
    
    if (plot_data == None):
        fig = plt.figure(figsize=(15,10))
        labels=[r"$\nu$ NC", r"$\nu_{\mu}$ CC", r"$\nu_e$ CC", r"EXT", r"Out. fid. vol.", r"Cosmic"]
        sns.histplot(data=MC_frame, x= variable , hue="category", multiple="stack", palette = 'deep', weights = scaling, bins=bins, legend = False, log_scale=logscale)
        plt.legend(title='Run 30', loc='upper right', labels=[r"$\nu$ NC", r"$\nu_{\mu}$ CC", r"$\nu_e$ CC", r"EXT", r"Out. fid. vol.", r"Cosmic"])
        plt.savefig('name.jpg', dpi=300) 
        plt.show()
        

    else:
        fig_data = plt.figure(figsize=(15,10))
        Data_fig = sns.histplot(data=dataFrame, x=variable, bins=bins, legend = False, log_scale=logscale)
        bars = Data_fig.patches
        
        heights = [patch.get_height() for patch in bars]
        x = [patch.get_x() for patch in bars]
        w = [patch.get_width() for patch in bars]
        plt.close(fig_data)
        #y_real = np.array(y_real)
        fig = plt.figure(figsize=(15,10))
        labels=[r"$\nu$ NC", r"$\nu_{\mu}$ CC", r"$\nu_e$ CC", r"EXT", r"Out. fid. vol.", r"Cosmic", r"Data"]
        sns.histplot(data=MC_frame, x= variable , hue="category", multiple="stack", palette = 'deep', weights = scaling, bins = x, legend = False, log_scale=logscale)
        del x[-1]
        del heights[-1]
        new_bins = [start+w[0]/2 for start in x]
        plt.errorbar(new_bins, heights , xerr=w[0]/2, fmt='.k');
        plt.legend(title='Run 30', loc='upper right', labels=[r"$\nu$ NC", r"$\nu_{\mu}$ CC", r"$\nu_e$ CC", r"EXT", r"Out. fid. vol.", r"Cosmic"])
        plt.xlabel("Reconstructed numu energy (Gev)")
        plt.ylabel("Events")
        plt.savefig('name.jpg', dpi=300) 
        
        
    return 
    
    
#Return element from index
def element_index(vector,index,defval=9999.):
    import awkward 
    #print ('vector check....')
    #print (idx)
    #print (len(pidv))
    return awkward.fromiter([pidv[tid] if ( (tid<len(pidv) ) & (tid>=0)) else defval for pidv,tid in zip(vector,index)])

#Return index from element
def index(argidx,vecsort,mask):
    import awkward 
    vid = vecsort[mask]
    sizecheck = argidx if argidx>=0 else abs(argidx)-1
    # find the position in the array after masking
    mskd_pos = [v.argsort()[argidx] if len(v)>sizecheck else -1 for v in vid]
    # go back to the corresponding position in the origin array before masking
    result = [[i for i, n in enumerate(m) if n == 1][p] if (p)>=0 else -1 for m,p in zip(mask,mskd_pos)]
    return result