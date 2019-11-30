import shutil

pyorbit = False
simulation_parameters = False
flat_files = True
tune_files = False

master_directory = './00_Master'
pyorbit_file = master_directory + '/pyOrbit.py'
sim_params_file = master_directory + '/simulation_parameters.py'
flat_file = master_directory + '/Flat_file.madx'
tune_file = master_directory + '/tunes.str'

sbs_locations = []
noSC_locations = []

sbs_locations.append('./01_SbS_Tomo_V10_dBeta_25/')
sbs_locations.append('./01_SbS_Tomo_V10_dBeta_20/')
sbs_locations.append('./01_SbS_Tomo_V10_dBeta_15/')
sbs_locations.append('./01_SbS_Tomo_V10_dBeta_10/')
sbs_locations.append('./01_SbS_Tomo_V10_dBeta_05/')
sbs_locations.append('./01_SbS_Tomo_V10_dBeta_04/')
sbs_locations.append('./01_SbS_Tomo_V10_dBeta_03/')
sbs_locations.append('./01_SbS_Tomo_V10_dBeta_02/')
sbs_locations.append('./01_SbS_Tomo_V10_dBeta_01/')
sbs_locations.append('./01_SbS_Tomo_V10_dBeta_00/')

if pyorbit:
	for loc in sbs_locations:
		newPath = shutil.copy(pyorbit_file, loc)
		print pyorbit_file, ' copied to ', loc

if simulation_parameters:
	for loc in sbs_locations:
		newPath = shutil.copy(sim_params_file, loc)
		print sim_params_file, ' copied to ', loc

if flat_files:
	for loc in sbs_locations:
		newPath = shutil.copy(flat_file, loc)
		print flat_file, ' copied to ', loc

if tune_files:
	for loc in sbs_locations:
		newPath = shutil.copy(tune_file, loc)
		print flat_file, ' copied to ', loc
