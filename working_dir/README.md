## 3rd year undergraduate lab focusing on MicroBooNE experiment
### Developed by O.G. Finnerud, A. Kedziora, & J. Waiton

This folder contains almost everything that is needed to run the lab, including:

#### /data/
2 files included:
- DataSet_LSND.csv: Dataset for LSND used as comparison (42.9KB).
- DataSet_MiniBooNE.csv: Dataset for MiniBoone used as comparison (17.0KB).

Missing 3 essential files due to github's restrictions on file sizes.
- bnb_run3_mc_larcv.h5: Event display file (8.8GB).
- data_flattened.pkl: True data from MicroBooNE flattened (24.2MB).
- MC_EXT_flattened.pkl: MC and EXT data from simulations & MicroBooNE (111.4MB).


#### /lab docs/
Contains the lab sheet and the solutions


#### MainAnalysis_template.ipynb
Template for student's usage throughout the lab.


#### MainAnalysis_solns.ipynb
Solutions for the lab to be used by tutors for guidance.


#### Neutrino_functions.py
Useful functions that are used throughout the lab.


#### event_display.ipynb & EventDisplay.py
Currently a work in progress, but allows you to visualise the Events.
- Need to allow for listing of all events as they are not linearly spread throughout the .h5 file

#### keras_example.ipynb
An example of a simple NN in action for interest of the reader.
