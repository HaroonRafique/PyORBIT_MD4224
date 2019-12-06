import os

master_dir = os.getcwd()

Sims_01 = False
Sims_02 = True
Sims_03 = False

sbs_locations = []
sbs_locations.append('/01_SbS_Tomo_V10_dBeta_25/')
sbs_locations.append('/01_SbS_Tomo_V10_dBeta_20/')
sbs_locations.append('/01_SbS_Tomo_V10_dBeta_15/')
sbs_locations.append('/01_SbS_Tomo_V10_dBeta_10/')
sbs_locations.append('/01_SbS_Tomo_V10_dBeta_05/')
sbs_locations.append('/01_SbS_Tomo_V10_dBeta_04/')
sbs_locations.append('/01_SbS_Tomo_V10_dBeta_03/')
sbs_locations.append('/01_SbS_Tomo_V10_dBeta_02/')
sbs_locations.append('/01_SbS_Tomo_V10_dBeta_01/')
sbs_locations.append('/01_SbS_Tomo_V10_dBeta_00/')

if Sims_01:
	for loc in sbs_locations:
		print '------------------------------------------------------------------------------------------------'
		print '\t Submitting HPC-Batch simulation: PFW scan, tunes (6.21, 6.10), Beta-beating ', loc[21:22] ,' %'
		print '------------------------------------------------------------------------------------------------'
		dir_ = master_dir + loc
		make_command = 'python Make_SLURM_submission_script.py'
		submit_command = 'sbatch SLURM_submission_script.sh'
		os.chdir(dir_)
		os.system(make_command)
		os.system(submit_command)

sims02_locations = []
sims02_locations.append('/02_NoSC_Tomo_V10_betatron_01/')
sims02_locations.append('/02_NoSC_Tomo_V10_betatron_02/')
sims02_locations.append('/02_NoSC_Tomo_V10_betatron_03/')
sims02_locations.append('/02_NoSC_Tomo_V10_betatron_04/')
sims02_locations.append('/02_NoSC_Tomo_V10_betatron_05/')
sims02_locations.append('/02_NoSC_Tomo_V10_betatron_10/')
sims02_locations.append('/02_NoSC_Tomo_V10_betatron_15/')
sims02_locations.append('/02_NoSC_Tomo_V10_betatron_20/')
sims02_locations.append('/02_NoSC_Tomo_V10_betatron_25/')

if Sims_02:
	for loc in sims02_locations:
		print '------------------------------------------------------------------------------------------------'
		print '\t Submitting HPC-Batch sim: PFW scan, tunes (6.21, 6.10), Beta mismatch, expected emittance growth ', loc[27:29] ,' %'
		print '------------------------------------------------------------------------------------------------'
		dir_ = master_dir + loc
		make_command = 'python Make_SLURM_submission_script.py'
		submit_command = 'sbatch SLURM_submission_script.sh'
		os.chdir(dir_)
		os.system(make_command)
		os.system(submit_command)

sims03_locations = []
sims03_locations.append('/03_SbS_Tomo_V10_betatron_01/')
sims03_locations.append('/03_SbS_Tomo_V10_betatron_02/')
sims03_locations.append('/03_SbS_Tomo_V10_betatron_03/')
sims03_locations.append('/03_SbS_Tomo_V10_betatron_04/')
sims03_locations.append('/03_SbS_Tomo_V10_betatron_05/')
sims03_locations.append('/03_SbS_Tomo_V10_betatron_10/')
sims03_locations.append('/03_SbS_Tomo_V10_betatron_15/')
sims03_locations.append('/03_SbS_Tomo_V10_betatron_20/')
sims03_locations.append('/03_SbS_Tomo_V10_betatron_25/')

if Sims_03:
	for loc in sims03_locations:
		print '------------------------------------------------------------------------------------------------'
		print '\t Submitting HPC-Batch sim: PFW scan, tunes (6.21, 6.10), Beta mismatch, expected emittance growth ', loc[24:26] ,' %'
		print '------------------------------------------------------------------------------------------------'
		dir_ = master_dir + loc
		make_command = 'python Make_SLURM_submission_script.py'
		submit_command = 'sbatch SLURM_submission_script.sh'
		os.chdir(dir_)
		os.system(make_command)
		os.system(submit_command)
