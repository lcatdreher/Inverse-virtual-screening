# Inverse-virtual-screening
Automated docking process

Required to run:
1. Python versions 2 and 3
2. AutoDock Vina (downloadable here: https://vina.scripps.edu/downloads/)
3. ADFR suite (downloadable here: https://ccsb.scripps.edu/adfr/downloads/)
4. ChimeraX 1.8 (downloadable here: https://www.cgl.ucsf.edu/chimerax/download.html)

     
     

Before running:
Place all protein files in a single directory, and place all python files, Vina.exe, an ADFR suite in a subfolder of this directory (runfiles)

To run:
1. Open 'chimera.py' in ChimeraX
     This will prep each protein for docking, creating a new .pdb file whose name begins with 'prep_'

2. In the terminal, run 'python2.7 adt.py'
     This will further prep each protein using the prepare_receptor4 script from autdock tools and generate a new pbqt file, then run vina.

4. In the terminal, run 'python3 getresults.py'
     This will format the docking results from the vina log files in a .csv spreadsheet.

5. If desired, run 'python3 deletepdbs.py' to delete the original pdb files
