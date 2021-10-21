

import EP4_utils

#help(EP4_utils)

EP4_params = {
    'mode':'difference',
    'surface':'lower',
    'fieldvars' : ['depth', 'groundedmask', 'velocity', 'fs lower'],
    'fieldvar' : 'depth',
    'fieldvarLabel' : 'Ice thickness change rate, $m a^{-1}$',
    'fieldrange' : [-300.0, 300.0],
    'cameraHeight' : 500000.0,
    'camerax' : -1585790.0,
    'cameray' : -231939.0,
    'xres' : 600,
    'yres' : 800,
    'LSgeomID' : 103,
    'USgeomID' : 104,
    'imgname' : './PIGtst.png',
#    'inputfname' : '/scratch/project_2000339/gladston/PIG_S8/vtuoutputs/geomtrans_s8_t0001.pvtu',
#    'inputfname2' : '/scratch/project_2000339/gladston/PIG_S8/vtuoutputs/geomtrans_s8_t0002.pvtu',
    'inputfname' : '/media/sf_VBshare/PIG8/8b/geomtrans_s8b_r2_t0006.pvtu',
    'inputfname2' : '/media/sf_VBshare/PIG8/8b/geomtrans_s8b_r2_t0018.pvtu',
    'dt' : '0.05',
    'velocityContours' : [100.0, 1000.0],
    'fontSize' : 15
}

EP4_utils.EP4_plot(EP4_params)


EP4_params = {
    'mode':'singlefield',
    'surface':'lower',
    'fieldvars' : ['depth', 'groundedmask', 'velocity'],
    'fieldvar' : 'depth',
    'fieldvarLabel' : 'Depth, $m$',
    'fieldrange' : [-1000.0, 1000.0],
    'cameraHeight' : 500000.0,
    'camerax' : -1585790.0,
    'cameray' : -231939.0,
    'xres' : 600,
    'yres' : 800,
    'LSgeomID' : 103,
    'USgeomID' : 104,
    'imgname' : './PIGtst.png',
    'inputfname' : '/scratch/project_2000339/gladston/PIG_S8/vtuoutputs/geomtrans_s8_t0001.pvtu',
    'inputfname2' : '/scratch/project_2000339/gladston/PIG_S8/vtuoutputs/geomtrans_s8_t0002.pvtu',
    'dt' : '0.05',
    'velocityContours' : [100.0, 1000.0],
    'fontSize' : 15
}

#EP4_utils.EP4_plot(EP4_params)


