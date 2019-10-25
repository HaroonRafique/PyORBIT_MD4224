import numpy as np

parameters = {}

parameters['tunex']						= '617'
parameters['tuney']						= '624'

parameters['lattice_start'] 			= 'BWSH65'
parameters['DistType'] 					= 'Tomo'
parameters['n_macroparticles']			= int(5E5)
parameters['lattice_version']			='Original'
parameters['TwissType'] 				= 'Lattice'
parameters['machine']					= 'PS'

# ~ parameters['lattice_start'] 		= 'BWSV64'
# ~ parameters['DistType'] 				= 'Gaussian'
# ~ parameters['DistType'] 				= 'Joho'
# ~ parameters['n_macroparticles']		= int(5E4)
# ~ parameters['lattice_version']		='Optimised'
# ~ parameters['TwissType'] 			= 'Manual'

parameters['bunch_label'] = parameters['machine'] + '_' + parameters['lattice_version'] + '_Lattice_Tune_' + parameters['tunex'] + '_' + parameters['tuney'] + '_' + parameters['lattice_start']
parameters['flat_file'] = str('../../00_Flat_Files/'+parameters['lattice_version']+'_Lattice/Flat_Files/'+parameters['lattice_start'][3]+'_'+parameters['tunex'][1:]+'_'+parameters['tuney'][1:]+'/PTC-PyORBIT_flat_file.flt')
parameters['tomo_file'] = 'PyORBIT_Tomo_file_MD4224_HB.mat'
# Full path for creating distns
# ~ parameters['input_distn'] = str('../../01_Input_Distns/' +parameters['lattice_start'][3]+'/'+parameters['DistType']+'/' + str(parameters['n_macroparticles']) + '/PyORBIT_' + parameters['DistType'] + '_Bunch_' + parameters['TwissType'] + '_Twiss_Nmp_' + str(parameters['n_macroparticles']) + '_' + parameters['machine'] + '_' + parameters['lattice_version'] + '_Lattice_Tune_' + parameters['tunex'] + '_'	+ parameters['tuney'] + '_' + parameters['lattice_start'] + '.mat')
# Fix tune to nominal for tune scans
parameters['input_distn'] = str('../../01_Input_Distns/' +parameters['lattice_start'][3]+'/'+parameters['DistType']+'/' + str(parameters['n_macroparticles']) + '/PyORBIT_'+parameters['DistType']+'_Bunch_' + parameters['TwissType'] + '_Twiss_Nmp_' + str(parameters['n_macroparticles']) + '_PS_' + parameters['lattice_version'] + '_Lattice_Tune_621_624_' + parameters['lattice_start'] + '.mat')

parameters['gamma']				= 2.49253731343
parameters['intensity']			= 72.5E+10
parameters['bunch_length']		= 140e-9
parameters['blength']			= 140e-9
parameters['epsn_x']			= 1E-6
parameters['epsn_y']			= 1.2E-6
parameters['dpp_rms']			= 8.7e-04
parameters['LongitudinalJohoParameter'] = 1.2
parameters['LongitudinalCut'] 	= 2.4
parameters['TransverseCut']		= 5
parameters['rf_voltage']		= 0.0212942055190595723
parameters['circumference']		= 2*np.pi*100
parameters['phi_s']				= 0
parameters['macrosize']			= parameters['intensity']/float(parameters['n_macroparticles'])

# PS Injection 1.4 GeV
parameters['gamma'] 	= 2.49253731343
parameters['beta'] 		= np.sqrt(parameters['gamma']**2-1)/parameters['gamma']
c 						= 299792458
parameters['sig_z'] 	= (parameters['beta'] * c * parameters['blength'])/4.

parameters['turns_max'] = int(2200)
tu1 = range(-1, parameters['turns_max'], 200)
tu2 = range(10, 100, 10) 
tu3 = range(1, 9)
tu = tu2 + tu1 + tu3 
tu.append(874) # WS 172s
tu.append(2185)# WS 175s

parameters['turns_print'] = sorted(tu)
parameters['turns_update'] = sorted(tu)

switches = {
	'SliceBySlice': 	True,
	'LongitudinalKick': True,
	'GridSizeX': 128,
	'GridSizeY': 128,
	'GridSizeZ': 64
}

# PTC RF Table Parameters
harmonic_factors = [1] # this times the base harmonic defines the RF harmonics (for SPS = 4620, PS 10MHz 7, 8, or 9)
time = np.array([0,1,2])
ones = np.ones_like(time)
Ekin_GeV = 1.4*ones
RF_voltage_MV = np.array([0.0212942055190595723*ones]).T # in MV
RF_phase = np.array([np.pi*ones]).T

RFparameters = {
	'harmonic_factors': harmonic_factors,
	'time': time,
	'Ekin_GeV': Ekin_GeV,
	'voltage_MV': RF_voltage_MV,
	'phase': RF_phase
}
