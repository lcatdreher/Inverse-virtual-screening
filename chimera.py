from chimerax.core.commands import run
from chimerax.std_commands import measure_center
import subprocess
import os


#set directory
os.chdir("/home/ld/Desktop/IVS")
#os.chdir("/Users/lcatd/OneDrive/Desktop/IVS")


#iterate through protein files in directory
file_names = [fn for fn in os.listdir(".") if fn.endswith(".pdb")]
for fn in file_names:
    models = run(session, 'open '+fn)
    #run(session, 'open ' + fn)
    #delete c chains
    run(session, 'select /c')
    run(session, 'delete sel')
    #delete non-standard residues
    run(session, 'select :ala,arg,asn,asp,cys,glu,gln,gly,his,ile,leu,lys,met,phe,pro,ser,thr,trp,tyr,val')
    run(session, 'select ~sel')
    run(session, 'delete sel')
    #measure center
    center = measure_center.atoms_center_of_mass(models[0].atoms)
    print(center)
    centerx = str(center[0])
    centery = str(center[1])
    centerz = str(center[2])


    #configure config file
    conffn = fn.replace('.pdb', 'conf.txt')
    qtfn = fn.replace('.pdb', '.pdbqt')
    qtfn = "prep_" + qtfn
    outfn = fn.replace('.pdb', '_out.txt')
    logfn = fn.replace('.pdb', '_log.txt')
    f = open(conffn, 'w')
    f.write('receptor = ' + qtfn + '\nligand = NDM_opt2.pdbqt\ncenter_x = '+centerx+'\ncenter_y = '+centery+'\ncenter_z = ' +centerz+ '\nsize_x = 126\nsize_y = 126\nsize_z = 126\nexhaustiveness = 16\nout = '+outfn+'\nnum_modes = 5\nlog = '+logfn)    
    f.close()
    #save prepped molecule and close
    run(session, 'save /Users/lcatd/OneDrive/Desktop/IVS/prep_'+fn)
    run(session, 'save /home/ld/Desktop/IVS/prep_'+fn)
    run(session, 'close #1')


