This short Python script transforms your ZetaView txt file into a nice PDF file of the concentration.
The PDF file is generated in the same folder as your script and the same name as your txt file.

These are the inputs from the user:

filename    = The name of your file. Usually something like: '20240605_0000_11postestzeta_size_520'
dia_range   = The diameter range. I have set it at 0 - 1000 nm, but if it leaves too much white space it can be altered. 
filt_length = Length of the filter. A higher number results in a smoother curve.

Just so you know, this uses filtering which makes the figure an approximation. this is fine, as we should not use the NTA data as absolute truths.
