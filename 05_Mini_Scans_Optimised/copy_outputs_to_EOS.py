#!/usr/bin/python
# Python script to copy various outputs from HPC-Batch to SWAN (EOS)
import os

print '\nSTARTED copy_outputs_to_EOS.py'

master_dir = os.getcwd()

def make_output_copy_command(loc, case):
	return 'cp output.mat /afs/cern.ch/user/h/harafiqu/EOS/SWAN_projects/PS/From_Scratch/MD4224_Repo_Outputs/'+ str(case) + '/Simulation_Outputs/' + str(loc) + '_output.mat'

def make_bunch_copy_commands(loc, case):
	return ['cp mainbunch_000874.mat /afs/cern.ch/user/h/harafiqu/EOS/SWAN_projects/PS/From_Scratch/MD4224_Repo_Outputs/'+ str(case) + '/Simulation_Profiles/' + str(loc) + '_c172.mat', 'cp mainbunch_002185.mat /afs/cern.ch/user/h/harafiqu/EOS/SWAN_projects/PS/From_Scratch/MD4224_Repo_Outputs/'+ str(case) + '/Simulation_Profiles' + str(loc) + '_c175.mat']

H_locations = []
H_locations.append('/04_SbS_Tomo_Lattice_H_07')
H_locations.append('/04_SbS_Tomo_Lattice_H_08')
H_locations.append('/04_SbS_Tomo_Lattice_H_09')
H_locations.append('/04_SbS_Tomo_Lattice_H_10')
H_locations.append('/04_SbS_Tomo_Lattice_H_11')
H_locations.append('/04_SbS_Tomo_Lattice_H_12')
H_locations.append('/04_SbS_Tomo_Lattice_H_13')
H_locations.append('/04_SbS_Tomo_Lattice_H_14')
H_locations.append('/04_SbS_Tomo_Lattice_H_15')
H_locations.append('/04_SbS_Tomo_Lattice_H_16')
H_locations.append('/04_SbS_Tomo_Lattice_H_17')
H_locations.append('/04_SbS_Tomo_Lattice_H_18')
H_locations.append('/04_SbS_Tomo_Lattice_H_19')
H_locations.append('/04_SbS_Tomo_Lattice_H_20')
H_locations.append('/04_SbS_Tomo_Lattice_H_21')

V_locations = []
V_locations.append('/03_SbS_Tomo_Lattice_V_10')
V_locations.append('/03_SbS_Tomo_Lattice_V_11')
V_locations.append('/03_SbS_Tomo_Lattice_V_12')
V_locations.append('/03_SbS_Tomo_Lattice_V_13')
V_locations.append('/03_SbS_Tomo_Lattice_V_14')
V_locations.append('/03_SbS_Tomo_Lattice_V_15')
V_locations.append('/03_SbS_Tomo_Lattice_V_16')
V_locations.append('/03_SbS_Tomo_Lattice_V_17')
V_locations.append('/03_SbS_Tomo_Lattice_V_18')
V_locations.append('/03_SbS_Tomo_Lattice_V_19')
V_locations.append('/03_SbS_Tomo_Lattice_V_20')
V_locations.append('/03_SbS_Tomo_Lattice_V_21')
V_locations.append('/03_SbS_Tomo_Lattice_V_22')
V_locations.append('/03_SbS_Tomo_Lattice_V_23')
V_locations.append('/03_SbS_Tomo_Lattice_V_24')


for loc in V_locations:
	case = 'V_Mini_Optimised'

	print '\nStarted loop for folder', loc

	# Create a full path to output folder
	out_dir = master_dir + loc + '/output'
	print '\n\tcd ', out_dir

	# change directory to output folder
	os.chdir(out_dir)

	# To get correct name we need to do some string gymnastics
	tune = loc[-2:]
	lab = '6' + tune + '_SbS'

	# copy output file with correct naming convention
	print '\n\t' + str(make_output_copy_command(lab, case))
	os.system(make_output_copy_command(lab, case))
	
	# change directory to bunch output folder
	bunch_dir = master_dir + loc + '/bunch_output'
	print '\n\tcd ', bunch_dir
	os.chdir(bunch_dir)

	# copy output files with correct naming convention
	comm_172, comm_175= make_bunch_copy_commands(lab, case)
	print '\n\t' + str(comm_172)
	os.system(comm_172)
	# ~ print '\n\t' + str(comm_175)
	# ~ os.system(comm_175)

	print '\nFinished loop for folder\n', loc

for loc in H_locations:
	case = 'H_Mini_Optimised'

	print '\nStarted loop for folder', loc

	# Create a full path to output folder
	out_dir = master_dir + loc + '/output'
	print '\n\tcd ', out_dir

	# change directory to output folder
	os.chdir(out_dir)

	# To get correct name we need to do some string gymnastics
	tune = loc[-2:]
	lab = '6' + tune + '_SbS'

	# copy output file with correct naming convention
	print '\n\t' + str(make_output_copy_command(lab, case))
	os.system(make_output_copy_command(lab, case))
	
	# change directory to bunch output folder
	bunch_dir = master_dir + loc + '/bunch_output'
	print '\n\tcd ', bunch_dir
	os.chdir(bunch_dir)

	# copy output files with correct naming convention
	comm_172, comm_175= make_bunch_copy_commands(lab, case)
	print '\n\t' + str(comm_172)
	os.system(comm_172)
	# ~ print '\n\t' + str(comm_175)
	# ~ os.system(comm_175)

	print '\nFinished loop for folder\n', loc


print '\nFINISHED copy_outputs_to_EOS.py'
