

from EP4_defaultParams import *
import EP4_utils

EP4_params['fieldvar'] = 'bed'
EP4_params['fieldvarLabel'] = 'Bed elevation, $m$'
EP4_params['fieldvars'].append('bed')

help(EP4_utils)

EP4_utils.PlotLSfield(EP4_params)

