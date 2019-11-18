import os

Horizontal_Scan_NoSC = False
Horizontal_Scan = True
Vertical_Scan_NoSC = False
Vertical_Scan = True

master_dir = os.getcwd()

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

H_locations_NoSC = []
H_locations_NoSC.append('/02_NoSC_Tomo_Lattice_H_07')
H_locations_NoSC.append('/02_NoSC_Tomo_Lattice_H_09')
H_locations_NoSC.append('/02_NoSC_Tomo_Lattice_H_11')
H_locations_NoSC.append('/02_NoSC_Tomo_Lattice_H_13')
H_locations_NoSC.append('/02_NoSC_Tomo_Lattice_H_15')
H_locations_NoSC.append('/02_NoSC_Tomo_Lattice_H_17')
H_locations_NoSC.append('/02_NoSC_Tomo_Lattice_H_19')
H_locations_NoSC.append('/02_NoSC_Tomo_Lattice_H_21')

V_locations_NoSC = []
V_locations_NoSC.append('/01_NoSC_Tomo_Lattice_V_10')
V_locations_NoSC.append('/01_NoSC_Tomo_Lattice_V_12')
V_locations_NoSC.append('/01_NoSC_Tomo_Lattice_V_14')
V_locations_NoSC.append('/01_NoSC_Tomo_Lattice_V_16')
V_locations_NoSC.append('/01_NoSC_Tomo_Lattice_V_18')
V_locations_NoSC.append('/01_NoSC_Tomo_Lattice_V_20')
V_locations_NoSC.append('/01_NoSC_Tomo_Lattice_V_22')
V_locations_NoSC.append('/01_NoSC_Tomo_Lattice_V_24')

if Horizontal_Scan_NoSC:
	for loc in H_locations_NoSC:
		print '--------------------------------------------------------------------------------------------'
		print '\t Submitting HPC-Batch simulation: ',loc[22],' Scan, tune (6.',loc[24:26] ,', 6.24) NoSC'
		print '--------------------------------------------------------------------------------------------'
		dir_ = master_dir + loc
		make_command = 'python Make_SLURM_submission_script.py'
		submit_command = 'sbatch SLURM_submission_script.sh'
		os.chdir(dir_)
		os.system(make_command)
		os.system(submit_command)

if Vertical_Scan_NoSC:
	for loc in V_locations_NoSC:
		print '--------------------------------------------------------------------------------------------'
		print '\t Submitting HPC-Batch simulation: ',loc[22],' Scan, tune (6.21, 6.',loc[24:26] ,') NoSC'
		print '--------------------------------------------------------------------------------------------'
		dir_ = master_dir + loc
		make_command = 'python Make_SLURM_submission_script.py'
		submit_command = 'sbatch SLURM_submission_script.sh'
		os.chdir(dir_)
		os.system(make_command)
		os.system(submit_command)

if Horizontal_Scan:
	for loc in H_locations:
		print '--------------------------------------------------------------------------------------------'
		print '\t Submitting HPC-Batch simulation: ',loc[21],' Scan, tune (6.',loc[23:25] ,', 6.24) SbS'
		print '--------------------------------------------------------------------------------------------'
		dir_ = master_dir + loc
		make_command = 'python Make_SLURM_submission_script.py'
		submit_command = 'sbatch SLURM_submission_script.sh'
		os.chdir(dir_)
		os.system(make_command)
		os.system(submit_command)

if Vertical_Scan:
	for loc in V_locations:
		print '--------------------------------------------------------------------------------------------'
		print '\t Submitting HPC-Batch simulation: ',loc[21],' Scan, tune (6.21, 6.',loc[23:25] ,') SbS'
		print '--------------------------------------------------------------------------------------------'
		dir_ = master_dir + loc
		make_command = 'python Make_SLURM_submission_script.py'
		submit_command = 'sbatch SLURM_submission_script.sh'
		os.chdir(dir_)
		os.system(make_command)
		os.system(submit_command)
