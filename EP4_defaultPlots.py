

import EP4_utils

#help(EP4_utils)


# Params for PIG shelf only view:
#
## current camera placement for renderView1
#renderView1.CameraPosition = [-1614019.783372834, -302285.4088466101, 276620.37228006445]
#renderView1.CameraFocalPoint = [-1614019.783372834, -302285.4088466101, 54.256739617548874]
#renderView1.CameraParallelScale = 483070.79314165615
#ImageResolution=[478, 502])


# params for PIG shelf and first part of fast flow region
#
## layout/tab size in pixels
#layout1.SetSize(540, 785)
## current camera placement for renderView1
#renderView1.CameraPosition = [-1605788.984079296, -255363.88241205012, 426583.7883110717]
#renderView1.CameraFocalPoint = [-1605788.984079296, -255363.88241205012, -118.14914196244786]
#renderView1.CameraParallelScale = 623627.5113294333
#ImageResolution=[540, 785])

# thickness change rate for PIG at start of modified transient run (more basal drag)
EP4_params = {
    'mode':'difference',
    'surface':'lower',
    'fieldvars' : ['depth', 'groundedmask', 'velocity', 'fs lower'],
    'fieldvar' : 'depth',
    'fieldvarLabel' : 'Ice thickness change rate, $m a^{-1}$',
    'fieldrange' : [-100.0, 100.0],
    'cameraHeight' : 500000.0,
    'camerax' : -1585790.0,
    'cameray' : -231939.0,
    'xres' : 600,
    'yres' : 800,
    'LSgeomID' : 103,
    'USgeomID' : 104,
    'imgname' : './PIGthckRate1ts_m.png',
    'inputfname' : '/scratch/project_2000339/gladston/PIG_S4_I/vtuoutputs/pig_s4_l4_i_t0016.pvtu',
    'inputfname2' : '/scratch/project_2000339/gladston/PIG_S8_2/vtuoutputs/geomtrans_s8_t0001.pvtu',
#    'inputfname2' : '/scratch/project_2000339/gladston/PIG_S8/vtuoutputs/geomtrans_s8_t0002.pvtu',
#    'inputfname' : '/media/sf_VBshare/PIG8/8b/geomtrans_s8b_r2_t0006.pvtu',
#    'inputfname2' : '/media/sf_VBshare/PIG8/8b/geomtrans_s8b_r2_t0018.pvtu',
    'dt' : '0.05',
    'velocityContours' : [100.0, 1000.0],
    'presetColor' : 'Blue Orange (divergent)',
    'fontSize' : 15
}
EP4_utils.EP4_plot(EP4_params)

# thickness change rate for PIG at start of transient run
EP4_params = {
    'mode':'difference',
    'surface':'lower',
    'fieldvars' : ['depth', 'groundedmask', 'velocity', 'fs lower'],
    'fieldvar' : 'depth',
    'fieldvarLabel' : 'Ice thickness change rate, $m a^{-1}$',
    'fieldrange' : [-100.0, 100.0],
    'cameraHeight' : 500000.0,
    'camerax' : -1585790.0,
    'cameray' : -231939.0,
    'xres' : 600,
    'yres' : 800,
    'LSgeomID' : 103,
    'USgeomID' : 104,
    'imgname' : './PIGthckRate1ts.png',
    'inputfname' : '/scratch/project_2000339/gladston/PIG_S4_I/vtuoutputs/pig_s4_l4_i_t0016.pvtu',
    'inputfname2' : '/scratch/project_2000339/gladston/PIG_S8/vtuoutputs/geomtrans_s8_t0001.pvtu',
#    'inputfname2' : '/scratch/project_2000339/gladston/PIG_S8/vtuoutputs/geomtrans_s8_t0002.pvtu',
#    'inputfname' : '/media/sf_VBshare/PIG8/8b/geomtrans_s8b_r2_t0006.pvtu',
#    'inputfname2' : '/media/sf_VBshare/PIG8/8b/geomtrans_s8b_r2_t0018.pvtu',
    'dt' : '0.05',
    'velocityContours' : [100.0, 1000.0],
    'presetColor' : 'Blue Orange (divergent)',
    'fontSize' : 15
}
#EP4_utils.EP4_plot(EP4_params)


# thickness change rate for PIG after 4 years of transient run
EP4_params = {
    'mode':'difference',
    'surface':'lower',
    'fieldvars' : ['depth', 'groundedmask', 'velocity', 'fs lower'],
    'fieldvar' : 'depth',
    'fieldvarLabel' : 'Ice thickness change rate, $m a^{-1}$',
    'fieldrange' : [-100.0, 100.0],
    'cameraHeight' : 500000.0,
    'camerax' : -1585790.0,
    'cameray' : -231939.0,
    'xres' : 600,
    'yres' : 800,
    'LSgeomID' : 103,
    'USgeomID' : 104,
    'imgname' : './PIGthckRate80ts.png',
    'inputfname' : '/scratch/project_2000339/gladston/PIG_S8/vtuoutputs/geomtrans_s8_t0079.pvtu',
    'inputfname2' : '/scratch/project_2000339/gladston/PIG_S8/vtuoutputs/geomtrans_s8_t0080.pvtu',
    'dt' : '0.05',
    'velocityContours' : [100.0, 1000.0],
    'presetColor' : 'Blue Orange (divergent)',
    'fontSize' : 15
}
#EP4_utils.EP4_plot(EP4_params)

# thickness change rate for PIG over 4 years of transient run
EP4_params = {
    'mode':'difference',
    'surface':'lower',
    'fieldvars' : ['depth', 'groundedmask', 'velocity', 'fs lower'],
    'fieldvar' : 'depth',
    'fieldvarLabel' : 'Ice thickness change rate, $m a^{-1}$',
    'fieldrange' : [-100.0, 100.0],
    'cameraHeight' : 500000.0,
    'camerax' : -1585790.0,
    'cameray' : -231939.0,
    'xres' : 600,
    'yres' : 800,
    'LSgeomID' : 103,
    'USgeomID' : 104,
    'imgname' : './PIGthckRate4a.png',
    'inputfname' : '/scratch/project_2000339/gladston/PIG_S4_I/vtuoutputs/pig_s4_l4_i_t0016.pvtu',
    'inputfname2' : '/scratch/project_2000339/gladston/PIG_S8/vtuoutputs/geomtrans_s8_t0080.pvtu',
    'dt' : '4.0',
    'velocityContours' : [100.0, 1000.0],
    'presetColor' : 'Blue Orange (divergent)',
    'fontSize' : 15
}
#EP4_utils.EP4_plot(EP4_params)

# some kind of PIG thickness change rate...
EP4_params = {
    'mode':'difference',
    'surface':'lower',
    'fieldvars' : ['depth', 'groundedmask', 'velocity', 'fs lower'],
    'fieldvar' : 'depth',
    'fieldvarLabel' : 'Ice thickness change rate, $m a^{-1}$',
    'fieldrange' : [-200.0, 200.0],
    'cameraHeight' : 500000.0,
    'camerax' : -1585790.0,
    'cameray' : -231939.0,
    'xres' : 600,
    'yres' : 800,
    'LSgeomID' : 103,
    'USgeomID' : 104,
    'imgname' : './PIGthckChange2.png',
    'inputfname' : '/scratch/project_2000339/gladston/PIG_S8/vtuoutputs/geomtrans_s8_t0001.pvtu',
    'inputfname2' : '/scratch/project_2000339/gladston/PIG_S8/vtuoutputs/geomtrans_s8_t0100.pvtu',
#    'inputfname' : '/media/sf_VBshare/PIG8/8b/geomtrans_s8b_r2_t0006.pvtu',
#    'inputfname2' : '/media/sf_VBshare/PIG8/8b/geomtrans_s8b_r2_t0018.pvtu',
    'dt' : '1.0',
    'velocityContours' : [100.0, 1000.0],
    'fontSize' : 15
}
#EP4_utils.EP4_plot(EP4_params)


# PIG bmb
EP4_params = {
    'mode':'singlefield',
    'surface':'lower',
    'fieldvars' : ['depth', 'groundedmask', 'velocity','bmb'],
    'fieldvar' : 'bmb',
    'fieldvarLabel' : 'Basal mass balance, $m a^{-1}$',
    'fieldrange' : [-70.0, 0.0],
    'cameraHeight' : 276620., 
    'camerax' : -1614019.0,
    'cameray' : -302285.0,
    'xres' : 478,
    'yres' : 502,
    'LSgeomID' : 103,
    'USgeomID' : 104,
    'imgname' : './PIGbmb.png',
    'inputfname' : '/scratch/project_2000339/gladston/PIG_S4_I/vtuoutputs/pig_s4_l4_i_t0016.pvtu',
#    'inputfname' : '/scratch/project_2000339/gladston/PIG_S8/vtuoutputs/geomtrans_s8_t0001.pvtu',
#    'inputfname2' : '/scratch/project_2000339/gladston/PIG_S8/vtuoutputs/geomtrans_s8_t0002.pvtu',
    'dt' : '0.05',
    'velocityContours' : [100.0, 1000.0],
    'presetColor' : 'Black-Body Radiation',
    'fontSize' : 15
}
#EP4_utils.EP4_plot(EP4_params)


# PIG lower surface
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


