import shutil

pyorbit = True
simulation_parameters = False
lib_bunch_gather = True

Horizontal_Scan_NoSC = True
Horizontal_Scan = True
Vertical_Scan_NoSC = True
Vertical_Scan = True

master_directory = './00_Master'
pyorbit_file = master_directory + '/pyOrbit.py'
sim_params_file = master_directory + '/simulation_parameters.py'
flat_file = master_directory + '/lib/pyOrbit_Bunch_Gather.py'

H_locations = []

H_locations.append('./04_SbS_Tomo_Lattice_H_07')
H_locations.append('./04_SbS_Tomo_Lattice_H_08')
H_locations.append('./04_SbS_Tomo_Lattice_H_09')
H_locations.append('./04_SbS_Tomo_Lattice_H_10')
H_locations.append('./04_SbS_Tomo_Lattice_H_11')
H_locations.append('./04_SbS_Tomo_Lattice_H_12')
H_locations.append('./04_SbS_Tomo_Lattice_H_13')
H_locations.append('./04_SbS_Tomo_Lattice_H_14')
H_locations.append('./04_SbS_Tomo_Lattice_H_15')
H_locations.append('./04_SbS_Tomo_Lattice_H_16')
H_locations.append('./04_SbS_Tomo_Lattice_H_17')
H_locations.append('./04_SbS_Tomo_Lattice_H_18')
H_locations.append('./04_SbS_Tomo_Lattice_H_19')
H_locations.append('./04_SbS_Tomo_Lattice_H_20')
H_locations.append('./04_SbS_Tomo_Lattice_H_21')

V_locations = []
V_locations.append('./03_SbS_Tomo_Lattice_V_10')
V_locations.append('./03_SbS_Tomo_Lattice_V_11')
V_locations.append('./03_SbS_Tomo_Lattice_V_12')
V_locations.append('./03_SbS_Tomo_Lattice_V_13')
V_locations.append('./03_SbS_Tomo_Lattice_V_14')
V_locations.append('./03_SbS_Tomo_Lattice_V_15')
V_locations.append('./03_SbS_Tomo_Lattice_V_16')
V_locations.append('./03_SbS_Tomo_Lattice_V_17')
V_locations.append('./03_SbS_Tomo_Lattice_V_18')
V_locations.append('./03_SbS_Tomo_Lattice_V_19')
V_locations.append('./03_SbS_Tomo_Lattice_V_20')
V_locations.append('./03_SbS_Tomo_Lattice_V_21')
V_locations.append('./03_SbS_Tomo_Lattice_V_22')
V_locations.append('./03_SbS_Tomo_Lattice_V_23')
V_locations.append('./03_SbS_Tomo_Lattice_V_24')

H_locations_NoSC = []
H_locations_NoSC.append('./02_NoSC_Tomo_Lattice_H_07')
H_locations_NoSC.append('./02_NoSC_Tomo_Lattice_H_09')
H_locations_NoSC.append('./02_NoSC_Tomo_Lattice_H_11')
H_locations_NoSC.append('./02_NoSC_Tomo_Lattice_H_13')
H_locations_NoSC.append('./02_NoSC_Tomo_Lattice_H_15')
H_locations_NoSC.append('./02_NoSC_Tomo_Lattice_H_17')
H_locations_NoSC.append('./02_NoSC_Tomo_Lattice_H_19')
H_locations_NoSC.append('./02_NoSC_Tomo_Lattice_H_21')

V_locations_NoSC = []
V_locations_NoSC.append('./01_NoSC_Tomo_Lattice_V_10')
V_locations_NoSC.append('./01_NoSC_Tomo_Lattice_V_12')
V_locations_NoSC.append('./01_NoSC_Tomo_Lattice_V_14')
V_locations_NoSC.append('./01_NoSC_Tomo_Lattice_V_16')
V_locations_NoSC.append('./01_NoSC_Tomo_Lattice_V_18')
V_locations_NoSC.append('./01_NoSC_Tomo_Lattice_V_20')
V_locations_NoSC.append('./01_NoSC_Tomo_Lattice_V_22')
V_locations_NoSC.append('./01_NoSC_Tomo_Lattice_V_24')

if pyorbit:
	if Vertical_Scan:
		for loc in V_locations:
			newPath = shutil.copy(pyorbit_file, loc)
			print sim_params_file, ' copied to ', loc
	if Horizontal_Scan:
		for loc in H_locations:
			newPath = shutil.copy(pyorbit_file, loc)
			print sim_params_file, ' copied to ', loc
	if Vertical_Scan_NoSC:
		for loc in V_locations_NoSC:
			newPath = shutil.copy(pyorbit_file, loc)
			print sim_params_file, ' copied to ', loc
	if Horizontal_Scan_NoSC:
		for loc in H_locations_NoSC:
			newPath = shutil.copy(pyorbit_file, loc)
			print sim_params_file, ' copied to ', loc

if simulation_parameters:
	if Vertical_Scan:
		for loc in V_locations:
			newPath = shutil.copy(sim_params_file, loc)
			print sim_params_file, ' copied to ', loc
	if Horizontal_Scan:
		for loc in H_locations:
			newPath = shutil.copy(sim_params_file, loc)
			print sim_params_file, ' copied to ', loc
	if Vertical_Scan_NoSC:
		for loc in V_locations_NoSC:
			newPath = shutil.copy(sim_params_file, loc)
			print sim_params_file, ' copied to ', loc
	if Horizontal_Scan_NoSC:
		for loc in H_locations_NoSC:
			newPath = shutil.copy(sim_params_file, loc)
			print sim_params_file, ' copied to ', loc

if lib_bunch_gather:
	if Vertical_Scan:
		for loc in V_locations:
			loc_2 = loc + '/lib'
			newPath = shutil.copy(flat_file, loc_2)
			print sim_params_file, ' copied to ', loc_2
	if Horizontal_Scan:
		for loc in H_locations:
			loc_2 = loc + '/lib'
			newPath = shutil.copy(flat_file, loc_2)
			print sim_params_file, ' copied to ', loc_2
	if Vertical_Scan_NoSC:
		for loc in V_locations_NoSC:
			loc_2 = loc + '/lib'
			newPath = shutil.copy(flat_file, loc_2)
			print sim_params_file, ' copied to ', loc_2
	if Horizontal_Scan_NoSC:
		for loc in H_locations_NoSC:
			loc_2 = loc + '/lib'
			newPath = shutil.copy(flat_file, loc_2)
			print sim_params_file, ' copied to ', loc_2
