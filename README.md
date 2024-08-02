# Inverse-virtual-screening
Automated docking process

Required to run:\n
Python versions 2 and 3\n
AutoDock Vina (downloadable here: https://vina.scripps.edu/downloads/)\n
ADFR suite (downloadable here: https://ccsb.scripps.edu/adfr/downloads/)\n
ChimeraX 1.8 (downloadable here: https://www.cgl.ucsf.edu/chimerax/download.html)\n

Before running:\n
Place all protein files, python files, Vina.exe, an ADFR suite in a single directory (I will fix this so it can be more organized but for now thisll do)

To run:
1. Open 'chimera.py' in ChimeraX
     This will prep each protein for docking, creating a new .pdb file whose name begins with 'prep_'

2. In the terminal, run 'python2.7 adt.py'
     This will further prep each protein using autdock tools and generate a new pbqt file, then run vina.

4. In the terminal, run 'getresults.py'
     This will format the docking results from the vina log files in a .csv spreadsheet.
