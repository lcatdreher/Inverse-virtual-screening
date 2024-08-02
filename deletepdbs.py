#deletes original pdb files
file_names = [fn for fn in os.listdir(".") if fn.endswith(".pdb")]
for fn in file_names:
    if fn.endswith("pdbqt"):
	cmd = 'rm ' + fn
	subprocess.run(cmd, shell=True)