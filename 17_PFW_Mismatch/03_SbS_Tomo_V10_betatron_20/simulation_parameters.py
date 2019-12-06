import numpy as np

analytic_e = [1, 2, 3, 4, 5, 10, 15, 20, 25] # percentage emittance growth for below factors
mismatches = [1.152, 1.221, 1.277, 1.326, 1.371, 1.559, 1.718, 1.864, 2.]

parameters = {}

parameters['beta_mismatch']				= mismatches[7]

parameters['tunex']						= '621'
parameters['tuney']						= '610'

parameters['lattice_start'] 			= 'BWSH65'
parameters['n_macroparticles']			= int(5E5)

# Fix tune to nominal for tune scans
parameters['input_distn'] = str('../../12_PFW_Test/Generate_Distns/Bunches/PyORBIT_Tomo_Bunch_Manual_Twiss_Nmp_'+str(parameters['n_macroparticles'])+'_PS_Optimised_Lattice_Tune_621_624_'+parameters['lattice_start']+'.mat')
parameters['tomo_file']			='PyORBIT_Tomo_file_BCMS_PreLIU.mat'

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
tu2 = range(50, 100, 10) 
tu3 = range(1, 50)
tu = tu2 + tu1 + tu3 
tu.append(874) # WS 172s
tu.append(2185)# WS 175s

parameters['turns_print'] = sorted(tu)
parameters['turns_update'] = sorted(tu)

switches = {
	'CreateDistn':		True,
	'Update_Twiss':		False,
	'Space_Charge': 	True,
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
