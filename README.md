# prusa_slicer_remove_start_code
A plugin for prusa slicer which removes the starting code


To use this code, you'll have to save the remove_starting_code.py somewhere on your computer.

In Prusa Slicer, you'll have to add the code via Print Settings > Output options > Post-processing scripts. The documentation told me to use ! before spaces, but that didn't work.

The setting that works for me is
"C:\Program Files (x86)\Python37-32\python.exe" C:\Users\username\Documents\3Dprinter\PrusaPostProcess\remove_starting_gcode.py
