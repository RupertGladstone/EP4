

from EP4_defaultParams import *
import EP4_utils

#inputDataset.PointArrayStatus = ['smbref', 'bmb', 'deltat_basin', 't_forcing', 'bed', 'fs lower', 'fs upper', 'thickness', 'depth', 'height', 'groundedmask', 'beta', 'vaf', 'haf', 'velocity', 'gm']
    

#EP4_params['fieldvar'] = 'bed'
#EP4_params['fieldvarLabel'] = 'Bed elevation, $m$'
EP4_params['fieldvars'].append('bed')

help(EP4_utils)

EP4_utils.EP4_plot(EP4_params)

