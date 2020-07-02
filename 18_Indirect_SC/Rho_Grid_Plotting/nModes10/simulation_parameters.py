import os
import numpy as np
c = 299792458

# Folder flags
########################################################################
cwd = os.getcwd() # Get the present directory
folder = cwd.split('/')[-1] # Last part of cwd is folder name
# name folder like 1_0_3, or 01_00_03
dir_sc = 1 # int(folder.split('_')[0]) # First number is sc flag
indir_sc = 1 # int(folder.split('_')[1]) # Second number is indirect sc flag
case = 1 # int(folder.split('_')[2]) # Last number is case flag

#### Cases
# 0 PFW
# 1 LEQ
# 2 PFW + Single quadrupolar error
# 3 PFW + Distributed quadrupolar error
# 4 PFW + non-linear PFW field components

parameters = {}

if case is 0:
        print 'simulation_parameters.py:: file read for PFW simulation'
        parameters['MADX_File']	= 'PFW_Flat_file.madx'

elif case is 1:
        print 'simulation_parameters.py:: file read for LEQ simulation'
        parameters['MADX_File']	= 'LEQ_Flat_file.madx'

elif case is 2:
        print 'simulation_parameters.py:: file read for PFW Single Quad Error simulation'
        parameters['MADX_File']	= 'PFW_Single_Quad_Error_Flat_file.madx'

elif case is 3:
        print 'simulation_parameters.py:: file read for PFW Distributed Quad Error simulation'
        parameters['MADX_File']	= 'PFW_Distributed_Quad_Error_Flat_file.madx'

elif case is 4:
        print 'simulation_parameters.py:: file read for PFW Non-Linear simulation'
        parameters['MADX_File']	= 'PFW_Nonlinear_Flat_file.madx'

parameters['tunex']						= '621'
parameters['tuney']						= '610'

parameters['lattice_start'] 			= 'BWSH65'
parameters['n_macroparticles']			= int(5E5)

# Currently use measured MD4224 tomo file to generate distribution
parameters['input_distn'] = str('../../12_PFW_Test/Generate_Distns/Bunches/PyORBIT_Tomo_Bunch_Manual_Twiss_Nmp_'+str(parameters['n_macroparticles'])+'_PS_Optimised_Lattice_Tune_621_624_'+parameters['lattice_start']+'.mat')
parameters['tomo_file']			='PyORBIT_Tomo_file_MD4224_HB.mat'

parameters['intensity']			= 72.5E+10
parameters['bunch_length']		= 140e-9
parameters['blength']			= 140e-9
parameters['epsn_x']			= 1E-6
parameters['epsn_y']			= 1E-6
parameters['dpp_rms']			= 8.7e-04
parameters['LongitudinalJohoParameter'] = 1.2
parameters['LongitudinalCut'] 	        = 2.4
parameters['TransverseCut']		= 5
parameters['rf_voltage']		= 0.0212942055190595723
parameters['circumference']		= 2*np.pi*100
parameters['phi_s']			= 0
parameters['macrosize']			= parameters['intensity']/float(parameters['n_macroparticles'])

# PS Injection 1.4 GeV
parameters['gamma'] 	= 2.49253731343
parameters['beta'] 	= np.sqrt(parameters['gamma']**2-1)/parameters['gamma']
parameters['sig_z'] 	= (parameters['beta'] * c * parameters['blength'])/4.

parameters['turns_max'] = int(1)
# ~ tu1 = range(-1, parameters['turns_max'], 200)
# ~ tu2 = range(50, 100, 10)
# ~ tu3 = range(1, 50)
# ~ tu = tu2 + tu1 + tu3 
# ~ tu.append(874) # WS 172s
# ~ tu.append(2185)# WS 175s

tu = range(-1, parameters['turns_max']) # every turn
parameters['turns_print'] = tu
parameters['turns_update'] = tu

switches = {
	'CreateDistn':		True,
	'Update_Twiss':		False,
	'Print_SC_Grid':	True,
	'GridSizeX': 128,
	'GridSizeY': 128,
	'GridSizeZ': 64
}

if dir_sc:
        switches['Space_Charge'] = True
        parameters['Space_Charge_Flag'] = True
else:
        switches['Space_Charge'] = False
        parameters['Space_Charge_Flag'] = False

if indir_sc:
        switches['Indirect_Space_Charge'] = True
        parameters['Indirect_Space_Charge_Flag'] = True
        switches['GridSizeX'] = 312
        switches['GridSizeY'] = 206
else:
        switches['Indirect_Space_Charge'] = False
        parameters['Indirect_Space_Charge_Flag'] = False

parameters['Space_Charge_GridSizeX'] = switches['GridSizeX']
parameters['Space_Charge_GridSizeY'] = switches['GridSizeY']
parameters['Space_Charge_GridSizeZ'] = switches['GridSizeZ']

# PTC RF Table Parameters
harmonic_factors = [1] # this times the base harmonic defines the RF harmonics (for SPS = 4620, PS 10MHz 7, 8, or 9)
time = np.array([0,1,2])
ones = np.ones_like(time)
Ekin_GeV = 1.4*ones
RF_voltage_MV = np.array([parameters['rf_voltage']*ones]).T # in MV
RF_phase = np.array([np.pi*ones]).T

RFparameters = {
	'harmonic_factors': harmonic_factors,
	'time': time,
	'Ekin_GeV': Ekin_GeV,
	'voltage_MV': RF_voltage_MV,
	'phase': RF_phase
}
