# Script to read single or double columned MADX tfs tables containing 
# magnet ramp data, and converting this to a PTC-PyORBIT readable PTC 
# table. Note that we ignore the timing column as in MAD-X this is not 
# defined as a time but as a step. We therefore create our own timing.
#
# Haroon Rafique CERN BE-ABP-HSI 28.06.19
#
import numpy as np
import os
from math import log10, floor
from scipy.misc import factorial

def turn_to_time(x):
    return x*2.287E-6

def time_to_turn(x):
    return x/2.287E-6

# From Hannes Bartosik CERN BE-ABP-HSI
def write_PTCtable(filename, multipole_orders, time, normal_components, skew_components):
	print '\n Create table ', filename
	multipole_orders = np.atleast_1d(multipole_orders)
	factors = 1./factorial(multipole_orders-1) # the factorial factor is needed to be consistent with MADX
	if factors.shape[0] <= 1:
		normal_components = (factors * (normal_components))
		skew_components   = (factors * (skew_components))
		arr = np.empty((normal_components.shape[0], 3), dtype=normal_components.dtype)
		arr[:,0] = time
		arr[:,1] = normal_components
		arr[:,2] = skew_components
		n_lines = len(time)
		n_multipoles = len(multipole_orders) # number of multipole orders to be changed

	else:
		normal_components = (factors.T * np.atleast_2d(normal_components))
		skew_components   = (factors.T * np.atleast_2d(skew_components))
		arr = np.empty((normal_components.shape[0], 1+normal_components.shape[1]*2), dtype=normal_components.dtype)
		arr[:,0] = time
		arr[:,1::2] = normal_components
		arr[:,2::2] = skew_components
		n_lines = len(time)
		n_multipoles = len(multipole_orders) # number of multipole orders to be changed
		
	with open(filename, 'w') as fid:
		fid.write('%d  1  %d\n'%(n_lines, n_multipoles))
		fid.write(' '.join(map(lambda i: '%d'%i, multipole_orders)) + '\n')
		for j in xrange(n_lines):
			fid.write('\t'.join(map(lambda i: '%+1.11f'%i, arr[j, :]))+'\n')
	return

# Read TFS table to obtain our dipole kick or quadrupole gradient
# We ignore the time column
def Read_Single_Column_TFS_Return_Data(file_in):
	print '\n Reading single column file ', file_in
	fi = open(file_in, 'r')
	contents = fi.readlines()	
	x=[]
	data =np.ndarray(shape=(1,1))
	data = np.delete(data, 0, 0)

	for l in contents:
		if ('@' in l) or ('$' in l) or ('*' in l):
			pass
		else:
			x = [float(l.split()[1])]
			data = np.vstack([data, x])

	data = np.delete(data, 0, 0)
	return data

# Read TFS table to obtain our dipole kick or quadrupole gradient
# We ignore the time column
def Read_Double_Column_TFS_Return_Data(file_in, f1=1., f2=1.):
	print '\n Reading double column file', file_in
	fi = open(file_in, 'r')
	contents = fi.readlines()
	x=[]
	data =np.ndarray(shape=(2,2))
	data = np.delete(data, 1, 0)
	
	for l in contents:
		if ('@' in l) or ('$' in l) or ('*' in l):
			pass
		else:
			x = [f1*float(l.split()[1]), f2*float(l.split()[2])]
			data = np.vstack([data, x])

	data = np.delete(data, 0, 0)
	return data
        
def Create_ZeroDispersion_Timing(turns, data):
    print '\n Create timing'
    data_2 = data

    # create sequence for time
    d_len = len(data)
    try:
        d_shape = data_2.shape[1]
    except AttributeError as error:
        d_shape = 1

    ramp_stop_time = turn_to_time(turns)
    
    time = np.linspace(0, ramp_stop_time, d_len)

    # Calculate interval to complete data until the end of the simulation
    interval = ramp_stop_time / (d_len-1)

    result = np.column_stack([time, data_2])

    return result

# Create the input files for the closure (2nd half) of the injection bump

# Table time is in seconds
# 1 turn = 2.287E-6 seconds
# Start with a 500 turn quarter cycle
# total 2000 turns = 2000 * 2.287E-6 = 4.574 ms

KQDW28 = Read_Single_Column_TFS_Return_Data('./MADX_Tables/KQDW28.tfs')
KQDW28_final = Create_ZeroDispersion_Timing(2000, KQDW28)
write_PTCtable('./PTC-PyORBIT_Tables/KQDW28.dat', (2), KQDW28_final[:,0],  KQDW28_final[:,1], KQDW28_final[:,0]*0)

KQFW31 = Read_Single_Column_TFS_Return_Data('./MADX_Tables/KQFW31.tfs')
KQFW31_final = Create_ZeroDispersion_Timing(2000, KQFW31)
write_PTCtable('./PTC-PyORBIT_Tables/KQFW31.dat', (2), KQFW31_final[:,0],  KQFW31_final[:,1], KQFW31_final[:,0]*0)

KQDW32 = Read_Single_Column_TFS_Return_Data('./MADX_Tables/KQDW32.tfs')
KQDW32_final = Create_ZeroDispersion_Timing(2000, KQDW32)
write_PTCtable('./PTC-PyORBIT_Tables/KQDW32.dat', (2), KQDW32_final[:,0],  KQDW32_final[:,1], KQDW32_final[:,0]*0)

KQFN35 = Read_Single_Column_TFS_Return_Data('./MADX_Tables/KQFN35.tfs')
KQFN35_final = Create_ZeroDispersion_Timing(2000, KQFN35)
write_PTCtable('./PTC-PyORBIT_Tables/KQFN35.dat', (2), KQFN35_final[:,0],  KQFN35_final[:,1], KQFN35_final[:,0]*0)

KQDN36 = Read_Single_Column_TFS_Return_Data('./MADX_Tables/KQDN36.tfs')
KQDN36_final = Create_ZeroDispersion_Timing(2000, KQDN36)
write_PTCtable('./PTC-PyORBIT_Tables/KQDN36.dat', (2), KQDN36_final[:,0],  KQDN36_final[:,1], KQDN36_final[:,0]*0)

KQFN39 = Read_Single_Column_TFS_Return_Data('./MADX_Tables/KQFN39.tfs')
KQFN39_final = Create_ZeroDispersion_Timing(2000, KQFN39)
write_PTCtable('./PTC-PyORBIT_Tables/KQFN39.dat', (2), KQFN39_final[:,0],  KQFN39_final[:,1], KQFN39_final[:,0]*0)

KQDN40 = Read_Single_Column_TFS_Return_Data('./MADX_Tables/KQDN40.tfs')
KQDN40_final = Create_ZeroDispersion_Timing(2000, KQDN40)
write_PTCtable('./PTC-PyORBIT_Tables/KQDN40.dat', (2), KQDN40_final[:,0],  KQDN40_final[:,1], KQDN40_final[:,0]*0)

KQFN45 = Read_Single_Column_TFS_Return_Data('./MADX_Tables/KQFN45.tfs')
KQFN45_final = Create_ZeroDispersion_Timing(2000, KQFN45)
write_PTCtable('./PTC-PyORBIT_Tables/KQFN45.dat', (2), KQFN45_final[:,0],  KQFN45_final[:,1], KQFN45_final[:,0]*0)

KQDN46 = Read_Single_Column_TFS_Return_Data('./MADX_Tables/KQDN46.tfs')
KQDN46_final = Create_ZeroDispersion_Timing(2000, KQDN46)
write_PTCtable('./PTC-PyORBIT_Tables/KQDN46.dat', (2), KQDN46_final[:,0],  KQDN46_final[:,1], KQDN46_final[:,0]*0)

KQFN49 = Read_Single_Column_TFS_Return_Data('./MADX_Tables/KQFN49.tfs')
KQFN49_final = Create_ZeroDispersion_Timing(2000, KQFN49)
write_PTCtable('./PTC-PyORBIT_Tables/KQFN49.dat', (2), KQFN49_final[:,0],  KQFN49_final[:,1], KQFN49_final[:,0]*0)
