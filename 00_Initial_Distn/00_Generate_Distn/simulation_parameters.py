import numpy as np

parameters = {}

p['n_macroparticles']	= int(0.5E6)


# Include machine (PS), tunes, lattice start position (BWS65H) for bunch output file label
p['tunex']				= '621'
p['tuney']				= '624'
p['machine']			= 'PS'
p['lattice_start'] 		= 'BWSH65'
# ~ p['lattice_start'] 	= 'BWSV64'
p['bunch_label'] 		= p['machine'] + '_Tune_' + p['tunex'] + '_' + p['tuney'] + '_' + p['lattice_start']

p['flat_file']			= str('../Original_Lattice/Flat_Files/'+p['lattice_start'][3]+'_'+p['tunex'][1:]+'_'+p['tunex'][1:]+'/PTC-PyORBIT_flat_file.flt')
# ~ p['flat_file']			= str('../Optimised_Lattice/Flat_Files/V_'+p['tunex'][1:]+'_'+p['tunex'][1:]+'/PTC-PyORBIT_flat_file.flt')

p['tomo_file']			= 'PyORBIT_Tomo_file_MD4224_HB.mat'

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
