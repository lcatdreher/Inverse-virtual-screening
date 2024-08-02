import subprocess
import os

#set directory
os.chdir("/home/ld/Desktop/IVS")
#os.chdir("/Users/lcatd/OneDrive/Desktop/IVS")


#iterate through chimera prepped files
file_names = [fn for fn in os.listdir(".") if fn.startswith("prep_")]
for fn in file_names:
    qtfn = fn.replace(".pdb", ".pdbqt")
    #prep = "python ADFRsuite-1.0\\Lib\\site-packages\\AutoDockTools\\Utilities24\\prepare_receptor4.py"+" -r " +fn
    prep = "python2.7 prepare_receptor4.py"+" -r " +fn
    print "prep:\n" + prep
    subprocess.call(prep, shell = True)


    oldfn = fn.replace("prep_", "")
    conffn = oldfn.replace(".pdb", "")
    conffn = conffn + "conf.txt"
   
   
    dock = "vina --config \""+conffn+"\""


    print "prepped. running vina."

    subprocess.call(dock, shell = True)
