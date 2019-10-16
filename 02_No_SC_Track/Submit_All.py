import os

sbs = True

master_dir = os.getcwd()

sbs_locations = []

sbs_locations.append('/00_Original_V_624_Tomo')
sbs_locations.append('/01_Original_V_624_Gaussian')
sbs_locations.append('/02_Original_V_624_Joho')
sbs_locations.append('/03_Original_H_621_Tomo')
sbs_locations.append('/04_Original_H_621_Gaussian')
sbs_locations.append('/05_Original_H_621_Joho')
sbs_locations.append('/06_Optimised_V_624_Tomo')
sbs_locations.append('/07_Optimised_V_624_Gaussian')
sbs_locations.append('/08_Optimised_V_624_Joho')
sbs_locations.append('/09_Optimisd_H_621_Tomo')
sbs_locations.append('/10_Optimised_H_621_Gaussian')
sbs_locations.append('/11_Optimised_H_621_Joho')

if sbs:
	for loc in sbs_locations:
		dir_ = master_dir + loc
		make_command = 'python Make_SLURM_submission_script.py'		
		submit_command = 'sbatch SLURM_submission_script.sh'
		os.chdir(dir_)
		os.system(make_command)		
		os.system(submit_command)
