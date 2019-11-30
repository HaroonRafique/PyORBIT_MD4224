import os

master_dir = os.getcwd()

sbs_locations = []
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

for loc in sbs_locations:
	print '------------------------------------------------------------------------------------------------'
	print '\t Submitting HPC-Batch simulation: PFW scan, tunes (6.21, 6.10), Beta-beating ', loc[24:26] ,' %'
	print '------------------------------------------------------------------------------------------------'
	dir_ = master_dir + loc
	make_command = 'python Make_SLURM_submission_script.py'
	submit_command = 'sbatch SLURM_submission_script.sh'
	os.chdir(dir_)
	os.system(make_command)
	os.system(submit_command)
