# This is a script for reading NTA data and make it prettier
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter    
import re


# Input from the user:
# These are the things you need to insert yourself
filename = '20240605_0000_11postestzeta_size_520'
dia_range = (0,1000)
filt_length= 7 # Greater value = more smoothing. 7 works OK





df = pd.read_csv(filename+'.txt',encoding='iso-8859-1',on_bad_lines='skip')

# Extract the dilution factor from the program
dilution_cell = df[df[df.columns[0]].str.contains('Dilution::', na=False)].iloc[0, 0]
dilution_value = float(re.sub("[^\d\.]","",dilution_cell.split('Dilution::')[1]))

## Get rid of metadata and whatever the last rows are
idx = df.index[df[df.columns[0]].eq("Size Distribution")].min()
df = df[idx+2:]
df[['Size','Number','Concentration','Volume', 'Area']] = df[df.columns[0]].str.split('\t',expand=True)
del df[df.columns[0]]
df=df.apply(pd.to_numeric)
df= df.reset_index(drop=True)
idx = df.index[df[df.columns[0]].eq(-1)].min()
df = df[0:idx]

# filter to set the data pretty
x_filtered = df[["Size","Concentration"]].apply(savgol_filter,  window_length=filt_length, polyorder=2)
x_width = x_filtered['Size'].diff();

# Plotting the data
fig,ax=plt.subplots(figsize=(3,3))

ax.plot(x_filtered.Size, x_filtered.Concentration*dilution_value , '-', linewidth=1,color="#708090")
ax.set(ylim=(0,max(x_filtered.Concentration)*dilution_value*1.1), xlim = dia_range,xlabel="Diameter (nm)", ylabel="Concentration (part/ml)")
ax.fill_between(x_filtered.Size, 0, x_filtered.Concentration*dilution_value,color="#708090")
fig.savefig(filename+'.pdf', format="pdf", bbox_inches="tight")
