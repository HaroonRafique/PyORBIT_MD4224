import os

master_dir = os.getcwd()

locations = []

locations.append('/0_0_0')
locations.append('/0_0_1')
locations.append('/0_0_2')
locations.append('/0_0_3')
locations.append('/0_0_4')

locations.append('/1_0_0')
locations.append('/1_0_1')
locations.append('/1_0_2')
locations.append('/1_0_3')
locations.append('/1_0_4')

locations.append('/1_1_0')
locations.append('/1_1_1')
locations.append('/1_1_2')
locations.append('/1_1_3')
locations.append('/1_1_4')

for loc in locations:
	print '---------------------------------------------------------------------------'
	print '\t Submitting SLURM Job: PS Injection Sim ', loc
	print '---------------------------------------------------------------------------'
	dir_ = master_dir + loc
	make_command = 'python Make_SLURM_submission_script.py'
	submit_command = 'sbatch SLURM_submission_script.sh'
	os.chdir(dir_)
	os.system(make_command)
	os.system(submit_command)
