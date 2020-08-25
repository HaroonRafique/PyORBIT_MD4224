import shutil

pyorbit = False
simulation_parameters = False
flat_files = True

sbs = True
noSC = False

master_directory = './00_Master'
pyorbit_file = master_directory + '/pyOrbit.py'
sim_params_file = master_directory + '/simulation_parameters.py'
flat_file = master_directory + '/Flat_file.madx'
# ~ flat_file = master_directory + '/tunes.str'

sbs_locations = []
noSC_locations = []

sbs_locations.append('./03_SbS_Tomo_Lattice_V_10/')
sbs_locations.append('./03_SbS_Tomo_Lattice_V_11/')
sbs_locations.append('./03_SbS_Tomo_Lattice_V_12/')
sbs_locations.append('./03_SbS_Tomo_Lattice_V_13/')
sbs_locations.append('./03_SbS_Tomo_Lattice_V_14/')
sbs_locations.append('./03_SbS_Tomo_Lattice_V_15/')
sbs_locations.append('./03_SbS_Tomo_Lattice_V_16/')
sbs_locations.append('./03_SbS_Tomo_Lattice_V_17/')
sbs_locations.append('./03_SbS_Tomo_Lattice_V_18/')
sbs_locations.append('./03_SbS_Tomo_Lattice_V_19/')
sbs_locations.append('./03_SbS_Tomo_Lattice_V_20/')
sbs_locations.append('./03_SbS_Tomo_Lattice_V_21/')
sbs_locations.append('./03_SbS_Tomo_Lattice_V_22/')
sbs_locations.append('./03_SbS_Tomo_Lattice_V_23/')
sbs_locations.append('./03_SbS_Tomo_Lattice_V_24/')

sbs_locations.append('./04_SbS_Tomo_Lattice_H_07/')
sbs_locations.append('./04_SbS_Tomo_Lattice_H_08/')
sbs_locations.append('./04_SbS_Tomo_Lattice_H_09/')
sbs_locations.append('./04_SbS_Tomo_Lattice_H_10/')
sbs_locations.append('./04_SbS_Tomo_Lattice_H_11/')
sbs_locations.append('./04_SbS_Tomo_Lattice_H_12/')
sbs_locations.append('./04_SbS_Tomo_Lattice_H_13/')
sbs_locations.append('./04_SbS_Tomo_Lattice_H_14/')
sbs_locations.append('./04_SbS_Tomo_Lattice_H_15/')
sbs_locations.append('./04_SbS_Tomo_Lattice_H_16/')
sbs_locations.append('./04_SbS_Tomo_Lattice_H_17/')
sbs_locations.append('./04_SbS_Tomo_Lattice_H_18/')
sbs_locations.append('./04_SbS_Tomo_Lattice_H_19/')
sbs_locations.append('./04_SbS_Tomo_Lattice_H_20/')
sbs_locations.append('./04_SbS_Tomo_Lattice_H_21/')

noSC_locations.append('./01_NoSC_Tomo_Lattice_V_10/')
noSC_locations.append('./01_NoSC_Tomo_Lattice_V_12/')
noSC_locations.append('./01_NoSC_Tomo_Lattice_V_14/')
noSC_locations.append('./01_NoSC_Tomo_Lattice_V_16/')
noSC_locations.append('./01_NoSC_Tomo_Lattice_V_18/')
noSC_locations.append('./01_NoSC_Tomo_Lattice_V_20/')
noSC_locations.append('./01_NoSC_Tomo_Lattice_V_22/')
noSC_locations.append('./01_NoSC_Tomo_Lattice_V_24/')

noSC_locations.append('./02_NoSC_Tomo_Lattice_H_07/')
noSC_locations.append('./02_NoSC_Tomo_Lattice_H_09/')
noSC_locations.append('./02_NoSC_Tomo_Lattice_H_11/')
noSC_locations.append('./02_NoSC_Tomo_Lattice_H_13/')
noSC_locations.append('./02_NoSC_Tomo_Lattice_H_15/')
noSC_locations.append('./02_NoSC_Tomo_Lattice_H_17/')
noSC_locations.append('./02_NoSC_Tomo_Lattice_H_19/')
noSC_locations.append('./02_NoSC_Tomo_Lattice_H_21/')

if pyorbit:
	if sbs:
		for loc in sbs_locations:
			newPath = shutil.copy(pyorbit_file, loc)
			print pyorbit_file, ' copied to ', loc
	if noSC:
		for loc in noSC_locations:
			newPath = shutil.copy(pyorbit_file, loc)
			print pyorbit_file, ' copied to ', loc

if simulation_parameters:
	if sbs:
		for loc in sbs_locations:
			newPath = shutil.copy(sim_params_file, loc)
			print sim_params_file, ' copied to ', loc
	if noSC:
		for loc in noSC_locations:
			newPath = shutil.copy(sim_params_file, loc)
			print sim_params_file, ' copied to ', loc

if flat_files:
	if sbs:
		for loc in sbs_locations:
			newPath = shutil.copy(flat_file, loc)
			print flat_file, ' copied to ', loc
	if noSC:
		for loc in noSC_locations:
			newPath = shutil.copy(flat_file, loc)
			print flat_file, ' copied to ', loc
