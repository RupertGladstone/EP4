# trace generated using paraview version 5.10.0-RC1

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'XML Partitioned Unstructured Grid Reader'
pig_s4_l4_i_t0016pvtu = XMLPartitionedUnstructuredGridReader(registrationName='pig_s4_l4_i_t0016.pvtu', FileName=['C:/Users/XPS-15/Desktop/S4_I/pig_s4_l4_i_t0016.pvtu'])
pig_s4_l4_i_t0016pvtu.CellArrayStatus = ['GeometryIds']
pig_s4_l4_i_t0016pvtu.PointArrayStatus = ['emergencevelocity', 'bmb', 'alpha', 'beta', 'bed', 'height', 'depth', 'fs upper', 'fs lower', 'vx', 'vy', 'groundedmask', 'smbref', 'ef', 'bottom ef', 'mu', 'temperature', 'viscosity', 'velocity']

# Properties modified on pig_s4_l4_i_t0016pvtu
pig_s4_l4_i_t0016pvtu.TimeArray = 'None'

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# show data in view
pig_s4_l4_i_t0016pvtuDisplay = Show(pig_s4_l4_i_t0016pvtu, renderView1, 'UnstructuredGridRepresentation')

# get color transfer function/color map for 'emergencevelocity'
emergencevelocityLUT = GetColorTransferFunction('emergencevelocity')
emergencevelocityLUT.RGBPoints = [-1196.541819580664, 0.231373, 0.298039, 0.752941, 732.2768748457568, 0.865003, 0.865003, 0.865003, 2661.0955692721773, 0.705882, 0.0156863, 0.14902]
emergencevelocityLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'emergencevelocity'
emergencevelocityPWF = GetOpacityTransferFunction('emergencevelocity')
emergencevelocityPWF.Points = [-1196.541819580664, 0.0, 0.5, 0.0, 2661.0955692721773, 1.0, 0.5, 0.0]
emergencevelocityPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
pig_s4_l4_i_t0016pvtuDisplay.Representation = 'Surface'
pig_s4_l4_i_t0016pvtuDisplay.ColorArrayName = ['POINTS', 'emergencevelocity']
pig_s4_l4_i_t0016pvtuDisplay.LookupTable = emergencevelocityLUT
pig_s4_l4_i_t0016pvtuDisplay.SelectTCoordArray = 'None'
pig_s4_l4_i_t0016pvtuDisplay.SelectNormalArray = 'None'
pig_s4_l4_i_t0016pvtuDisplay.SelectTangentArray = 'None'
pig_s4_l4_i_t0016pvtuDisplay.OSPRayScaleArray = 'emergencevelocity'
pig_s4_l4_i_t0016pvtuDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
pig_s4_l4_i_t0016pvtuDisplay.SelectOrientationVectors = 'velocity'
pig_s4_l4_i_t0016pvtuDisplay.ScaleFactor = 78305.2202328
pig_s4_l4_i_t0016pvtuDisplay.SelectScaleArray = 'emergencevelocity'
pig_s4_l4_i_t0016pvtuDisplay.GlyphType = 'Arrow'
pig_s4_l4_i_t0016pvtuDisplay.GlyphTableIndexArray = 'emergencevelocity'
pig_s4_l4_i_t0016pvtuDisplay.GaussianRadius = 3915.26101164
pig_s4_l4_i_t0016pvtuDisplay.SetScaleArray = ['POINTS', 'emergencevelocity']
pig_s4_l4_i_t0016pvtuDisplay.ScaleTransferFunction = 'PiecewiseFunction'
pig_s4_l4_i_t0016pvtuDisplay.OpacityArray = ['POINTS', 'emergencevelocity']
pig_s4_l4_i_t0016pvtuDisplay.OpacityTransferFunction = 'PiecewiseFunction'
pig_s4_l4_i_t0016pvtuDisplay.DataAxesGrid = 'GridAxesRepresentation'
pig_s4_l4_i_t0016pvtuDisplay.PolarAxes = 'PolarAxesRepresentation'
pig_s4_l4_i_t0016pvtuDisplay.ScalarOpacityFunction = emergencevelocityPWF
pig_s4_l4_i_t0016pvtuDisplay.ScalarOpacityUnitDistance = 8702.974949111735
pig_s4_l4_i_t0016pvtuDisplay.OpacityArrayName = ['POINTS', 'emergencevelocity']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
pig_s4_l4_i_t0016pvtuDisplay.ScaleTransferFunction.Points = [-1196.541819580664, 0.0, 0.5, 0.0, 2661.0955692721773, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
pig_s4_l4_i_t0016pvtuDisplay.OpacityTransferFunction.Points = [-1196.541819580664, 0.0, 0.5, 0.0, 2661.0955692721773, 1.0, 0.5, 0.0]

# reset view to fit data
renderView1.ResetCamera(False)

# get the material library
materialLibrary1 = GetMaterialLibrary()

# show color bar/color legend
pig_s4_l4_i_t0016pvtuDisplay.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# Rescale transfer function
emergencevelocityLUT.RescaleTransferFunction(-1196.541819580664, 2661.0955692721777)

# Rescale transfer function
emergencevelocityPWF.RescaleTransferFunction(-1196.541819580664, 2661.0955692721777)

# create a new 'Threshold'
threshold1 = Threshold(registrationName='Threshold1', Input=pig_s4_l4_i_t0016pvtu)
threshold1.Scalars = ['POINTS', 'emergencevelocity']
threshold1.LowerThreshold = -1196.541819580664
threshold1.UpperThreshold = 2661.0955692721777

# rename source object
RenameSource('Threshold lower surface', threshold1)

# Properties modified on threshold1
threshold1.Scalars = ['CELLS', 'GeometryIds']
threshold1.LowerThreshold = 103.0
threshold1.UpperThreshold = 103.0

# show data in view
threshold1Display = Show(threshold1, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
threshold1Display.Representation = 'Surface'
threshold1Display.ColorArrayName = ['POINTS', 'emergencevelocity']
threshold1Display.LookupTable = emergencevelocityLUT
threshold1Display.SelectTCoordArray = 'None'
threshold1Display.SelectNormalArray = 'None'
threshold1Display.SelectTangentArray = 'None'
threshold1Display.OSPRayScaleArray = 'emergencevelocity'
threshold1Display.OSPRayScaleFunction = 'PiecewiseFunction'
threshold1Display.SelectOrientationVectors = 'velocity'
threshold1Display.ScaleFactor = 78305.2202328
threshold1Display.SelectScaleArray = 'emergencevelocity'
threshold1Display.GlyphType = 'Arrow'
threshold1Display.GlyphTableIndexArray = 'emergencevelocity'
threshold1Display.GaussianRadius = 3915.26101164
threshold1Display.SetScaleArray = ['POINTS', 'emergencevelocity']
threshold1Display.ScaleTransferFunction = 'PiecewiseFunction'
threshold1Display.OpacityArray = ['POINTS', 'emergencevelocity']
threshold1Display.OpacityTransferFunction = 'PiecewiseFunction'
threshold1Display.DataAxesGrid = 'GridAxesRepresentation'
threshold1Display.PolarAxes = 'PolarAxesRepresentation'
threshold1Display.ScalarOpacityFunction = emergencevelocityPWF
threshold1Display.ScalarOpacityUnitDistance = 22113.595860805817
threshold1Display.OpacityArrayName = ['POINTS', 'emergencevelocity']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
threshold1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
threshold1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# hide data in view
Hide(pig_s4_l4_i_t0016pvtu, renderView1)

# show color bar/color legend
threshold1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Calculator'
calculator1 = Calculator(registrationName='Calculator1', Input=threshold1)
calculator1.Function = ''

# rename source object
RenameSource('Calculator u_b_mag', calculator1)

# Properties modified on calculator1
calculator1.ResultArrayName = 'u_b_mag'
calculator1.Function = 'mag(velocity)'

# show data in view
calculator1Display = Show(calculator1, renderView1, 'UnstructuredGridRepresentation')

# get color transfer function/color map for 'u_b_mag'
u_b_magLUT = GetColorTransferFunction('u_b_mag')
u_b_magLUT.RGBPoints = [0.019261474795393495, 0.231373, 0.298039, 0.752941, 2104.8905693791758, 0.865003, 0.865003, 0.865003, 4209.761877283557, 0.705882, 0.0156863, 0.14902]
u_b_magLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'u_b_mag'
u_b_magPWF = GetOpacityTransferFunction('u_b_mag')
u_b_magPWF.Points = [0.019261474795393495, 0.0, 0.5, 0.0, 4209.761877283557, 1.0, 0.5, 0.0]
u_b_magPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
calculator1Display.Representation = 'Surface'
calculator1Display.ColorArrayName = ['POINTS', 'u_b_mag']
calculator1Display.LookupTable = u_b_magLUT
calculator1Display.SelectTCoordArray = 'None'
calculator1Display.SelectNormalArray = 'None'
calculator1Display.SelectTangentArray = 'None'
calculator1Display.OSPRayScaleArray = 'u_b_mag'
calculator1Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator1Display.SelectOrientationVectors = 'velocity'
calculator1Display.ScaleFactor = 78305.2202328
calculator1Display.SelectScaleArray = 'u_b_mag'
calculator1Display.GlyphType = 'Arrow'
calculator1Display.GlyphTableIndexArray = 'u_b_mag'
calculator1Display.GaussianRadius = 3915.26101164
calculator1Display.SetScaleArray = ['POINTS', 'u_b_mag']
calculator1Display.ScaleTransferFunction = 'PiecewiseFunction'
calculator1Display.OpacityArray = ['POINTS', 'u_b_mag']
calculator1Display.OpacityTransferFunction = 'PiecewiseFunction'
calculator1Display.DataAxesGrid = 'GridAxesRepresentation'
calculator1Display.PolarAxes = 'PolarAxesRepresentation'
calculator1Display.ScalarOpacityFunction = u_b_magPWF
calculator1Display.ScalarOpacityUnitDistance = 22113.595860805817
calculator1Display.OpacityArrayName = ['POINTS', 'u_b_mag']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
calculator1Display.ScaleTransferFunction.Points = [0.019261474795393495, 0.0, 0.5, 0.0, 4209.761877283557, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
calculator1Display.OpacityTransferFunction.Points = [0.019261474795393495, 0.0, 0.5, 0.0, 4209.761877283557, 1.0, 0.5, 0.0]

# hide data in view
Hide(threshold1, renderView1)

# show color bar/color legend
calculator1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Contour'
contour1 = Contour(registrationName='Contour1', Input=calculator1)
contour1.ContourBy = ['POINTS', 'u_b_mag']
contour1.Isosurfaces = [2104.890569379176]
contour1.PointMergeMethod = 'Uniform Binning'

# rename source object
RenameSource('Contour u_b_mag', contour1)

# set active source
SetActiveSource(pig_s4_l4_i_t0016pvtu)

# create a new 'Threshold'
threshold1_1 = Threshold(registrationName='Threshold1', Input=pig_s4_l4_i_t0016pvtu)
threshold1_1.Scalars = ['POINTS', 'emergencevelocity']
threshold1_1.LowerThreshold = -1196.541819580664
threshold1_1.UpperThreshold = 2661.0955692721777

# rename source object
RenameSource('Threshold upper surface', threshold1_1)

# show data in view
contour1Display = Show(contour1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
contour1Display.Representation = 'Surface'
contour1Display.ColorArrayName = ['POINTS', 'u_b_mag']
contour1Display.LookupTable = u_b_magLUT
contour1Display.SelectTCoordArray = 'None'
contour1Display.SelectNormalArray = 'None'
contour1Display.SelectTangentArray = 'None'
contour1Display.OSPRayScaleArray = 'u_b_mag'
contour1Display.OSPRayScaleFunction = 'PiecewiseFunction'
contour1Display.SelectOrientationVectors = 'velocity'
contour1Display.ScaleFactor = 12969.018945493905
contour1Display.SelectScaleArray = 'u_b_mag'
contour1Display.GlyphType = 'Arrow'
contour1Display.GlyphTableIndexArray = 'u_b_mag'
contour1Display.GaussianRadius = 648.4509472746952
contour1Display.SetScaleArray = ['POINTS', 'u_b_mag']
contour1Display.ScaleTransferFunction = 'PiecewiseFunction'
contour1Display.OpacityArray = ['POINTS', 'u_b_mag']
contour1Display.OpacityTransferFunction = 'PiecewiseFunction'
contour1Display.DataAxesGrid = 'GridAxesRepresentation'
contour1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
contour1Display.ScaleTransferFunction.Points = [2104.890569379176, 0.0, 0.5, 0.0, 2105.390625, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
contour1Display.OpacityTransferFunction.Points = [2104.890569379176, 0.0, 0.5, 0.0, 2105.390625, 1.0, 0.5, 0.0]

# hide data in view
Hide(calculator1, renderView1)

# show color bar/color legend
contour1Display.SetScalarBarVisibility(renderView1, True)

# Properties modified on threshold1_1
threshold1_1.Scalars = ['CELLS', 'GeometryIds']
threshold1_1.LowerThreshold = 104.0
threshold1_1.UpperThreshold = 104.0

# show data in view
threshold1_1Display = Show(threshold1_1, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
threshold1_1Display.Representation = 'Surface'
threshold1_1Display.ColorArrayName = ['POINTS', 'emergencevelocity']
threshold1_1Display.LookupTable = emergencevelocityLUT
threshold1_1Display.SelectTCoordArray = 'None'
threshold1_1Display.SelectNormalArray = 'None'
threshold1_1Display.SelectTangentArray = 'None'
threshold1_1Display.OSPRayScaleArray = 'emergencevelocity'
threshold1_1Display.OSPRayScaleFunction = 'PiecewiseFunction'
threshold1_1Display.SelectOrientationVectors = 'velocity'
threshold1_1Display.ScaleFactor = 78305.2202328
threshold1_1Display.SelectScaleArray = 'emergencevelocity'
threshold1_1Display.GlyphType = 'Arrow'
threshold1_1Display.GlyphTableIndexArray = 'emergencevelocity'
threshold1_1Display.GaussianRadius = 3915.26101164
threshold1_1Display.SetScaleArray = ['POINTS', 'emergencevelocity']
threshold1_1Display.ScaleTransferFunction = 'PiecewiseFunction'
threshold1_1Display.OpacityArray = ['POINTS', 'emergencevelocity']
threshold1_1Display.OpacityTransferFunction = 'PiecewiseFunction'
threshold1_1Display.DataAxesGrid = 'GridAxesRepresentation'
threshold1_1Display.PolarAxes = 'PolarAxesRepresentation'
threshold1_1Display.ScalarOpacityFunction = emergencevelocityPWF
threshold1_1Display.ScalarOpacityUnitDistance = 22113.433058322593
threshold1_1Display.OpacityArrayName = ['POINTS', 'emergencevelocity']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
threshold1_1Display.ScaleTransferFunction.Points = [-1196.541819580664, 0.0, 0.5, 0.0, 2661.0955692721773, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
threshold1_1Display.OpacityTransferFunction.Points = [-1196.541819580664, 0.0, 0.5, 0.0, 2661.0955692721773, 1.0, 0.5, 0.0]

# hide data in view
Hide(pig_s4_l4_i_t0016pvtu, renderView1)

# show color bar/color legend
threshold1_1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# Rescale transfer function
emergencevelocityLUT.RescaleTransferFunction(-1196.541819580664, 2661.0955692721777)

# Rescale transfer function
emergencevelocityPWF.RescaleTransferFunction(-1196.541819580664, 2661.0955692721777)

# set active source
SetActiveSource(contour1)

# set active source
SetActiveSource(threshold1_1)

# create a new 'Calculator'
calculator1_1 = Calculator(registrationName='Calculator1', Input=threshold1_1)
calculator1_1.Function = ''

# rename source object
RenameSource('Calculator u_obs_mag', calculator1_1)

# Properties modified on contour1
contour1.Isosurfaces = [100.0, 1000.0]

# Properties modified on calculator1_1
calculator1_1.ResultArrayName = 'u_obs_mag'
calculator1_1.Function = 'sqrt(vx^2+vy^2)'

# show data in view
calculator1_1Display = Show(calculator1_1, renderView1, 'UnstructuredGridRepresentation')

# get color transfer function/color map for 'u_obs_mag'
u_obs_magLUT = GetColorTransferFunction('u_obs_mag')
u_obs_magLUT.RGBPoints = [0.07436254671408091, 0.231373, 0.298039, 0.752941, 2111.467092623259, 0.865003, 0.865003, 0.865003, 4222.859822699804, 0.705882, 0.0156863, 0.14902]
u_obs_magLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'u_obs_mag'
u_obs_magPWF = GetOpacityTransferFunction('u_obs_mag')
u_obs_magPWF.Points = [0.07436254671408091, 0.0, 0.5, 0.0, 4222.859822699804, 1.0, 0.5, 0.0]
u_obs_magPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
calculator1_1Display.Representation = 'Surface'
calculator1_1Display.ColorArrayName = ['POINTS', 'u_obs_mag']
calculator1_1Display.LookupTable = u_obs_magLUT
calculator1_1Display.SelectTCoordArray = 'None'
calculator1_1Display.SelectNormalArray = 'None'
calculator1_1Display.SelectTangentArray = 'None'
calculator1_1Display.OSPRayScaleArray = 'u_obs_mag'
calculator1_1Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator1_1Display.SelectOrientationVectors = 'velocity'
calculator1_1Display.ScaleFactor = 78305.2202328
calculator1_1Display.SelectScaleArray = 'u_obs_mag'
calculator1_1Display.GlyphType = 'Arrow'
calculator1_1Display.GlyphTableIndexArray = 'u_obs_mag'
calculator1_1Display.GaussianRadius = 3915.26101164
calculator1_1Display.SetScaleArray = ['POINTS', 'u_obs_mag']
calculator1_1Display.ScaleTransferFunction = 'PiecewiseFunction'
calculator1_1Display.OpacityArray = ['POINTS', 'u_obs_mag']
calculator1_1Display.OpacityTransferFunction = 'PiecewiseFunction'
calculator1_1Display.DataAxesGrid = 'GridAxesRepresentation'
calculator1_1Display.PolarAxes = 'PolarAxesRepresentation'
calculator1_1Display.ScalarOpacityFunction = u_obs_magPWF
calculator1_1Display.ScalarOpacityUnitDistance = 22113.433058322593
calculator1_1Display.OpacityArrayName = ['POINTS', 'u_obs_mag']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
calculator1_1Display.ScaleTransferFunction.Points = [0.07436254671408091, 0.0, 0.5, 0.0, 4222.859822699804, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
calculator1_1Display.OpacityTransferFunction.Points = [0.07436254671408091, 0.0, 0.5, 0.0, 4222.859822699804, 1.0, 0.5, 0.0]

# hide data in view
Hide(threshold1_1, renderView1)

# show color bar/color legend
calculator1_1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Calculator'
calculator1_2 = Calculator(registrationName='Calculator1', Input=calculator1_1)
calculator1_2.Function = ''

# rename source object
RenameSource('Calculator flow discrepancy', calculator1_2)

# Properties modified on calculator1_2
calculator1_2.ResultArrayName = 'FlowDis'
calculator1_2.Function = 'abs(sqrt(velocity_X^2+velocity_Y^2)-u_obs_mag)/u_obs_mag'

# show data in view
calculator1_2Display = Show(calculator1_2, renderView1, 'UnstructuredGridRepresentation')

# get color transfer function/color map for 'FlowDis'
flowDisLUT = GetColorTransferFunction('FlowDis')
flowDisLUT.RGBPoints = [3.92701862125696e-07, 0.231373, 0.298039, 0.752941, 15.790834615987965, 0.865003, 0.865003, 0.865003, 31.581668839274066, 0.705882, 0.0156863, 0.14902]
flowDisLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'FlowDis'
flowDisPWF = GetOpacityTransferFunction('FlowDis')
flowDisPWF.Points = [3.92701862125696e-07, 0.0, 0.5, 0.0, 31.581668839274066, 1.0, 0.5, 0.0]
flowDisPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
calculator1_2Display.Representation = 'Surface'
calculator1_2Display.ColorArrayName = ['POINTS', 'FlowDis']
calculator1_2Display.LookupTable = flowDisLUT
calculator1_2Display.SelectTCoordArray = 'None'
calculator1_2Display.SelectNormalArray = 'None'
calculator1_2Display.SelectTangentArray = 'None'
calculator1_2Display.OSPRayScaleArray = 'FlowDis'
calculator1_2Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator1_2Display.SelectOrientationVectors = 'velocity'
calculator1_2Display.ScaleFactor = 78305.2202328
calculator1_2Display.SelectScaleArray = 'FlowDis'
calculator1_2Display.GlyphType = 'Arrow'
calculator1_2Display.GlyphTableIndexArray = 'FlowDis'
calculator1_2Display.GaussianRadius = 3915.26101164
calculator1_2Display.SetScaleArray = ['POINTS', 'FlowDis']
calculator1_2Display.ScaleTransferFunction = 'PiecewiseFunction'
calculator1_2Display.OpacityArray = ['POINTS', 'FlowDis']
calculator1_2Display.OpacityTransferFunction = 'PiecewiseFunction'
calculator1_2Display.DataAxesGrid = 'GridAxesRepresentation'
calculator1_2Display.PolarAxes = 'PolarAxesRepresentation'
calculator1_2Display.ScalarOpacityFunction = flowDisPWF
calculator1_2Display.ScalarOpacityUnitDistance = 22113.433058322593
calculator1_2Display.OpacityArrayName = ['POINTS', 'FlowDis']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
calculator1_2Display.ScaleTransferFunction.Points = [3.92701862125696e-07, 0.0, 0.5, 0.0, 31.581668839274066, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
calculator1_2Display.OpacityTransferFunction.Points = [3.92701862125696e-07, 0.0, 0.5, 0.0, 31.581668839274066, 1.0, 0.5, 0.0]

# hide data in view
Hide(calculator1_1, renderView1)

# show color bar/color legend
calculator1_2Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(contour1)

# set active source
SetActiveSource(calculator1_2)

# reset view to fit data
renderView1.ResetCamera(False)

# Rescale transfer function
flowDisLUT.RescaleTransferFunction(0.0, 1.0)

# Rescale transfer function
flowDisPWF.RescaleTransferFunction(0.0, 1.0)

# set active source
SetActiveSource(contour1)

# Properties modified on contour1Display
contour1Display.Scale = [1.0, 1.0, 0.0]

# Properties modified on contour1Display.DataAxesGrid
contour1Display.DataAxesGrid.Scale = [1.0, 1.0, 0.0]

# Properties modified on contour1Display.PolarAxes
contour1Display.PolarAxes.Scale = [1.0, 1.0, 0.0]

# set active source
SetActiveSource(calculator1_2)

# Properties modified on calculator1_2Display
calculator1_2Display.Scale = [1.0, 1.0, 0.0]

# Properties modified on calculator1_2Display.DataAxesGrid
calculator1_2Display.DataAxesGrid.Scale = [1.0, 1.0, 0.0]

# Properties modified on calculator1_2Display.PolarAxes
calculator1_2Display.PolarAxes.Scale = [1.0, 1.0, 0.0]

# set active source
SetActiveSource(contour1)

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
u_b_magLUT.ApplyPreset('Cool to Warm (Extended)', True)

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
u_b_magLUT.ApplyPreset('X Ray', True)

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
u_b_magLUT.ApplyPreset('Black-Body Radiation', True)

# invert the transfer function
u_b_magLUT.InvertTransferFunction()

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
u_b_magLUT.ApplyPreset('Cool to Warm', True)

# invert the transfer function
u_b_magLUT.InvertTransferFunction()

# invert the transfer function
u_b_magLUT.InvertTransferFunction()

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
u_b_magLUT.ApplyPreset('Black-Body Radiation', True)

# invert the transfer function
u_b_magLUT.InvertTransferFunction()

# Properties modified on contour1Display
contour1Display.LineWidth = 2.0

# set active source
SetActiveSource(calculator1_2)

# reset view to fit data
renderView1.ResetCamera(False)

# set active source
SetActiveSource(contour1)

# hide color bar/color legend
contour1Display.SetScalarBarVisibility(renderView1, False)

# get color legend/bar for flowDisLUT in view renderView1
flowDisLUTColorBar = GetScalarBar(flowDisLUT, renderView1)
flowDisLUTColorBar.WindowLocation = 'Upper Right Corner'
flowDisLUTColorBar.Title = 'FlowDis'
flowDisLUTColorBar.ComponentTitle = ''
flowDisLUTColorBar.TitleColor = [0.0, 0.0, 0.0]
flowDisLUTColorBar.TitleBold = 1
flowDisLUTColorBar.LabelColor = [0.0, 0.0, 0.0]
flowDisLUTColorBar.LabelBold = 1
flowDisLUTColorBar.AutomaticLabelFormat = 0
flowDisLUTColorBar.LabelFormat = '%-#6.1f'
flowDisLUTColorBar.RangeLabelFormat = '%-#6.1f'
flowDisLUTColorBar.ScalarBarThickness = 15
flowDisLUTColorBar.ScalarBarLength = 0.39

# change scalar bar placement
flowDisLUTColorBar.WindowLocation = 'Any Location'
flowDisLUTColorBar.Position = [0.7981060606060605, 0.07320099255583128]
flowDisLUTColorBar.ScalarBarLength = 0.3899999999999999

# change scalar bar placement
flowDisLUTColorBar.Position = [0.7981060606060605, 0.0]
flowDisLUTColorBar.ScalarBarLength = 0.39

# change scalar bar placement
flowDisLUTColorBar.Position = [0.7920454545454544, 0.05583126550868486]

# change scalar bar placement
flowDisLUTColorBar.Position = [0.7930555555555553, 0.04838709677419353]

# set active source
SetActiveSource(calculator1_2)

# Properties modified on flowDisLUTColorBar
flowDisLUTColorBar.AutoOrient = 0
flowDisLUTColorBar.Orientation = 'Horizontal'
flowDisLUTColorBar.Title = 'Flow Discrepancy'

# change scalar bar placement
flowDisLUTColorBar.Position = [0.5992171717171711, 0.03307692307692319]
flowDisLUTColorBar.ScalarBarLength = 0.38999999999999946

# change scalar bar placement
flowDisLUTColorBar.Position = [0.7032575757575752, 0.03307692307692319]
flowDisLUTColorBar.ScalarBarLength = 0.2859595959595954

# change scalar bar placement
flowDisLUTColorBar.Position = [0.6982070707070701, 0.03183622828784131]

# Properties modified on renderView1
renderView1.OrientationAxesVisibility = 0

# change scalar bar placement
flowDisLUTColorBar.Position = [0.6982070707070701, 0.018188585607940566]

# get layout
layout1 = GetLayout()

# layout/tab size in pixels
layout1.SetSize(990, 806)

# current camera placement for renderView1
renderView1.CameraPosition = [-1527543.6649195766, -208453.33568981462, 685182.7160805691]
renderView1.CameraFocalPoint = [-1527543.6649195766, -208453.33568981462, 0.0]
renderView1.CameraParallelScale = 459969.9726563078

# save screenshot
SaveScreenshot('C:/Users/XPS-15/Desktop/PIG_flowdis.png', renderView1, ImageResolution=[1980, 1612],
    OverrideColorPalette='WhiteBackground', 
    # PNG options
    CompressionLevel='3')

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout1.SetSize(990, 806)

#-----------------------------------
# saving camera placements for views

# current camera placement for renderView1
renderView1.CameraPosition = [-1527543.6649195766, -208453.33568981462, 685182.7160805691]
renderView1.CameraFocalPoint = [-1527543.6649195766, -208453.33568981462, 0.0]
renderView1.CameraParallelScale = 459969.9726563078

#--------------------------------------------
# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).