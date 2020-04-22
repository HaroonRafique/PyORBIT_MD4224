#!/bin/bash

# Check if directories needed exist, if not, create them

if [ ! -d "MADX_Tables" ]; then
  mkdir MADX_Tables
fi
if [ ! -d "MADX_Twiss" ]; then
  mkdir MADX_Twiss
fi
if [ ! -d "PTC_Twiss" ]; then
  mkdir PTC_Twiss
fi
if [ ! -d "PTC-PyORBIT_Tables" ]; then
  mkdir PTC-PyORBIT_Tables
fi

mv TUNES.tfs MADX_Tables
mv KQDN36.tfs MADX_Tables
mv KQDN40.tfs MADX_Tables
mv KQDN46.tfs MADX_Tables
mv KQDW28.tfs MADX_Tables
mv KQDW32.tfs MADX_Tables
mv KQFN35.tfs MADX_Tables
mv KQFN39.tfs MADX_Tables
mv KQFN45.tfs MADX_Tables
mv KQFN49.tfs MADX_Tables
mv KQFW31.tfs MADX_Tables
mv mytable.tfs MADX_Tables
mv *.tfs MADX_Twiss
mv MADX_Twiss/madx_twiss.tfs .
mv *.ptc PTC_Twiss
mv PTC-PyORBIT_flat_file.flt PyORBIT
mv MADX_Twiss/optimised_flat_file.tfs .
mv MADX_Twiss/optimised_bare_simplified.tfs .
