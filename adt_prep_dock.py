import subprocess
import os

#set directory
os.chdir("/home/ld/Desktop/IVS")
#os.chdir("/Users/lcatd/OneDrive/Desktop/IVS")

#set up molkit
pckgs_cmd = "export PYTHONPATH=\"${PYTHONPATH}:/home/ld/Desktop/ADFRsuite/CCSBpckgs\""
subprocess.call(pckgs_cmd, shell = True)

#iterate through chimera prepped files
file_names = [fn for fn in os.listdir(".") if fn.startswith("prep_")]
for fn in file_names:
    qtfn = fn.replace(".pdb", ".pdbqt")
    #run prepare_receptor
    #prep = "python ADFRsuite-1.0\\Lib\\site-packages\\AutoDockTools\\Utilities24\\prepare_receptor4.py"+" -r " +fn
    prep = "python2.7 runfiles/prepare_receptor4.py"+" -r " +fn
    subprocess.call(prep, shell = True)


    oldfn = fn.replace("prep_", "")
    conffn = oldfn.replace(".pdb", "")
    conffn = conffn + "conf.txt"

   
    dock = "./runfiles/vina --config \""+conffn+"\""


    print "prepped. running vina."

    subprocess.call(dock, shell = True)

