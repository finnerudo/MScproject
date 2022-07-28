import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
#weight, bins, name, logscale = None, y_err = None
#log_scale=logscale, labels = labels

def histogram_plot(MC_frame, variable, bins, name, scaling, plot_data = None, logscale = None, dataFrame = None):
    """
    MC_frame: pandas dataframe - MC dataframe
    variable: string - name of the variable
    bins: int - number of bins
    name: string - name of the plot. The plot is saved
    scaling: array/list - weights you want to apply on MC data
    plot_data: boolean - 
    """
    #x = 0.5*(bins[1:]+ bins[:-1])
    MC_frame = MC_frame[MC_frame['Subevent'] == 0]
    if (plot_data == None):
        fig = plt.figure(figsize=(15,10))
        
        labels=[r"$\nu$ NC", r"$\nu_{\mu}$ CC", r"$\nu_e$ CC", r"EXT", r"Out. fid. vol.", r"Cosmic"]
        sns.histplot(data=MC_frame, x= variable , hue="category", multiple="stack", palette = 'deep', weights = scaling, bins=bins, legend = False, log_scale=logscale)
        
        plt.legend(title='Run 3', loc='upper right', labels=[r"$\nu$ NC", r"$\nu_{\mu}$ CC", r"$\nu_e$ CC", r"EXT", r"Out. fid. vol.", r"Cosmic"])
        plt.xlabel(variable,fontsize = 20)
        plt.ylabel("Events",fontsize = 20)
        plt.xticks(fontsize=18)
        plt.yticks(fontsize=18)
        plt.savefig(name+'.jpg', dpi=300) 
        plt.show()
        

    else:
        dataFrame = dataFrame[dataFrame['Subevent'] == 0]
        fig_data = plt.figure(figsize=(15,10))
        
        Data_fig = sns.histplot(data=dataFrame, x=variable, bins=bins, legend = False, log_scale=logscale)
        bars = Data_fig.patches
        
        heights = [patch.get_height() for patch in bars]
        x = [patch.get_x() for patch in bars]
        w = [patch.get_width() for patch in bars]
        plt.close(fig_data)
        del x[-1]
        del heights[-1]
        new_bins = [start+w[0]/2 for start in x]
        #y_real = np.array(y_real)
        
        fig = plt.figure(figsize=(15,10))
        sns.histplot(data=MC_frame, x= variable , hue="category", multiple="stack", palette = 'deep', weights = scaling, bins = x, legend = False, log_scale=logscale)
        
        plt.errorbar(new_bins, heights , xerr=w[0]/2, fmt='.k')
        labels=[r"$\nu$ NC", r"$\nu_{\mu}$ CC", r"$\nu_e$ CC", r"EXT", r"Out. fid. vol.", r"Cosmic", r"Data"]
        plt.legend(title='Run 3', loc='upper right', labels=labels)
        
        if variable == 'trk_energy_tot':
            variable = "Reconstructed numu energy (Gev)"
         
        plt.xlabel(variable,fontsize = 20)
        plt.ylabel("Events",fontsize = 20)
        plt.xticks(fontsize=18)
        plt.yticks(fontsize=18)
        plt.savefig(name+'.jpg', dpi=300) 
        
        
    return 
   
