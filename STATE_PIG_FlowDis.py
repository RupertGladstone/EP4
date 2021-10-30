# state file generated using paraview version 5.10.0-RC1

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

# get the material library
materialLibrary1 = GetMaterialLibrary()

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.ViewSize = [990, 806]
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.OrientationAxesVisibility = 0
renderView1.CenterOfRotation = [-1389421.5833959999, -144609.38397855, 0.0]
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [-1527543.6649195766, -208453.33568981462, 685182.7160805691]
renderView1.CameraFocalPoint = [-1527543.6649195766, -208453.33568981462, 0.0]
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 459969.9726563078
renderView1.BackEnd = 'OSPRay raycaster'
renderView1.OSPRayMaterialLibrary = materialLibrary1

SetActiveView(None)

# ----------------------------------------------------------------
# setup view layouts
# ----------------------------------------------------------------

# create new layout object 'Layout #1'
layout1 = CreateLayout(name='Layout #1')
layout1.AssignView(0, renderView1)
layout1.SetSize(990, 806)

# ----------------------------------------------------------------
# restore active view
SetActiveView(renderView1)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'XML Partitioned Unstructured Grid Reader'
pig_s4_l4_i_t0016pvtu = XMLPartitionedUnstructuredGridReader(registrationName='pig_s4_l4_i_t0016.pvtu', FileName=['C:/Users/XPS-15/Desktop/S4_I/pig_s4_l4_i_t0016.pvtu'])
pig_s4_l4_i_t0016pvtu.CellArrayStatus = ['GeometryIds']
pig_s4_l4_i_t0016pvtu.PointArrayStatus = ['emergencevelocity', 'bmb', 'alpha', 'beta', 'bed', 'height', 'depth', 'fs upper', 'fs lower', 'vx', 'vy', 'groundedmask', 'smbref', 'ef', 'bottom ef', 'mu', 'temperature', 'viscosity', 'velocity']
pig_s4_l4_i_t0016pvtu.TimeArray = 'None'

# create a new 'Threshold'
thresholduppersurface = Threshold(registrationName='Threshold upper surface', Input=pig_s4_l4_i_t0016pvtu)
thresholduppersurface.Scalars = ['CELLS', 'GeometryIds']
thresholduppersurface.LowerThreshold = 104.0
thresholduppersurface.UpperThreshold = 104.0

# create a new 'Threshold'
thresholdlowersurface = Threshold(registrationName='Threshold lower surface', Input=pig_s4_l4_i_t0016pvtu)
thresholdlowersurface.Scalars = ['CELLS', 'GeometryIds']
thresholdlowersurface.LowerThreshold = 103.0
thresholdlowersurface.UpperThreshold = 103.0

# create a new 'Calculator'
calculatoru_b_mag = Calculator(registrationName='Calculator u_b_mag', Input=thresholdlowersurface)
calculatoru_b_mag.ResultArrayName = 'u_b_mag'
calculatoru_b_mag.Function = 'mag(velocity)'

# create a new 'Contour'
contouru_b_mag = Contour(registrationName='Contour u_b_mag', Input=calculatoru_b_mag)
contouru_b_mag.ContourBy = ['POINTS', 'u_b_mag']
contouru_b_mag.Isosurfaces = [100.0, 1000.0]
contouru_b_mag.PointMergeMethod = 'Uniform Binning'

# create a new 'Calculator'
calculatoru_obs_mag = Calculator(registrationName='Calculator u_obs_mag', Input=thresholduppersurface)
calculatoru_obs_mag.ResultArrayName = 'u_obs_mag'
calculatoru_obs_mag.Function = 'sqrt(vx^2+vy^2)'

# create a new 'Calculator'
calculatorflowdiscrepancy = Calculator(registrationName='Calculator flow discrepancy', Input=calculatoru_obs_mag)
calculatorflowdiscrepancy.ResultArrayName = 'FlowDis'
calculatorflowdiscrepancy.Function = 'abs(sqrt(velocity_X^2+velocity_Y^2)-u_obs_mag)/u_obs_mag'

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from pig_s4_l4_i_t0016pvtu
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

# show data from thresholdlowersurface
thresholdlowersurfaceDisplay = Show(thresholdlowersurface, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
thresholdlowersurfaceDisplay.Representation = 'Surface'
thresholdlowersurfaceDisplay.ColorArrayName = ['POINTS', 'emergencevelocity']
thresholdlowersurfaceDisplay.LookupTable = emergencevelocityLUT
thresholdlowersurfaceDisplay.SelectTCoordArray = 'None'
thresholdlowersurfaceDisplay.SelectNormalArray = 'None'
thresholdlowersurfaceDisplay.SelectTangentArray = 'None'
thresholdlowersurfaceDisplay.OSPRayScaleArray = 'emergencevelocity'
thresholdlowersurfaceDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
thresholdlowersurfaceDisplay.SelectOrientationVectors = 'velocity'
thresholdlowersurfaceDisplay.ScaleFactor = 78305.2202328
thresholdlowersurfaceDisplay.SelectScaleArray = 'emergencevelocity'
thresholdlowersurfaceDisplay.GlyphType = 'Arrow'
thresholdlowersurfaceDisplay.GlyphTableIndexArray = 'emergencevelocity'
thresholdlowersurfaceDisplay.GaussianRadius = 3915.26101164
thresholdlowersurfaceDisplay.SetScaleArray = ['POINTS', 'emergencevelocity']
thresholdlowersurfaceDisplay.ScaleTransferFunction = 'PiecewiseFunction'
thresholdlowersurfaceDisplay.OpacityArray = ['POINTS', 'emergencevelocity']
thresholdlowersurfaceDisplay.OpacityTransferFunction = 'PiecewiseFunction'
thresholdlowersurfaceDisplay.DataAxesGrid = 'GridAxesRepresentation'
thresholdlowersurfaceDisplay.PolarAxes = 'PolarAxesRepresentation'
thresholdlowersurfaceDisplay.ScalarOpacityFunction = emergencevelocityPWF
thresholdlowersurfaceDisplay.ScalarOpacityUnitDistance = 22113.595860805817
thresholdlowersurfaceDisplay.OpacityArrayName = ['POINTS', 'emergencevelocity']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
thresholdlowersurfaceDisplay.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
thresholdlowersurfaceDisplay.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# show data from calculatoru_b_mag
calculatoru_b_magDisplay = Show(calculatoru_b_mag, renderView1, 'UnstructuredGridRepresentation')

# get color transfer function/color map for 'u_b_mag'
u_b_magLUT = GetColorTransferFunction('u_b_mag')
u_b_magLUT.RGBPoints = [0.019261474795393495, 1.0, 1.0, 1.0, 841.9677846365474, 0.901960784314, 0.901960784314, 0.0, 2525.8648309600517, 0.901960784314, 0.0, 0.0, 4209.761877283557, 0.0, 0.0, 0.0]
u_b_magLUT.ColorSpace = 'RGB'
u_b_magLUT.NanColor = [0.0, 0.498039215686, 1.0]
u_b_magLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'u_b_mag'
u_b_magPWF = GetOpacityTransferFunction('u_b_mag')
u_b_magPWF.Points = [0.019261474795393495, 0.0, 0.5, 0.0, 4209.761877283557, 1.0, 0.5, 0.0]
u_b_magPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
calculatoru_b_magDisplay.Representation = 'Surface'
calculatoru_b_magDisplay.ColorArrayName = ['POINTS', 'u_b_mag']
calculatoru_b_magDisplay.LookupTable = u_b_magLUT
calculatoru_b_magDisplay.SelectTCoordArray = 'None'
calculatoru_b_magDisplay.SelectNormalArray = 'None'
calculatoru_b_magDisplay.SelectTangentArray = 'None'
calculatoru_b_magDisplay.OSPRayScaleArray = 'u_b_mag'
calculatoru_b_magDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
calculatoru_b_magDisplay.SelectOrientationVectors = 'velocity'
calculatoru_b_magDisplay.ScaleFactor = 78305.2202328
calculatoru_b_magDisplay.SelectScaleArray = 'u_b_mag'
calculatoru_b_magDisplay.GlyphType = 'Arrow'
calculatoru_b_magDisplay.GlyphTableIndexArray = 'u_b_mag'
calculatoru_b_magDisplay.GaussianRadius = 3915.26101164
calculatoru_b_magDisplay.SetScaleArray = ['POINTS', 'u_b_mag']
calculatoru_b_magDisplay.ScaleTransferFunction = 'PiecewiseFunction'
calculatoru_b_magDisplay.OpacityArray = ['POINTS', 'u_b_mag']
calculatoru_b_magDisplay.OpacityTransferFunction = 'PiecewiseFunction'
calculatoru_b_magDisplay.DataAxesGrid = 'GridAxesRepresentation'
calculatoru_b_magDisplay.PolarAxes = 'PolarAxesRepresentation'
calculatoru_b_magDisplay.ScalarOpacityFunction = u_b_magPWF
calculatoru_b_magDisplay.ScalarOpacityUnitDistance = 22113.595860805817
calculatoru_b_magDisplay.OpacityArrayName = ['POINTS', 'u_b_mag']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
calculatoru_b_magDisplay.ScaleTransferFunction.Points = [0.019261474795393495, 0.0, 0.5, 0.0, 4209.761877283557, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
calculatoru_b_magDisplay.OpacityTransferFunction.Points = [0.019261474795393495, 0.0, 0.5, 0.0, 4209.761877283557, 1.0, 0.5, 0.0]

# show data from contouru_b_mag
contouru_b_magDisplay = Show(contouru_b_mag, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
contouru_b_magDisplay.Representation = 'Surface'
contouru_b_magDisplay.ColorArrayName = ['POINTS', 'u_b_mag']
contouru_b_magDisplay.LookupTable = u_b_magLUT
contouru_b_magDisplay.LineWidth = 2.0
contouru_b_magDisplay.SelectTCoordArray = 'None'
contouru_b_magDisplay.SelectNormalArray = 'None'
contouru_b_magDisplay.SelectTangentArray = 'None'
contouru_b_magDisplay.Scale = [1.0, 1.0, 0.0]
contouru_b_magDisplay.OSPRayScaleArray = 'u_b_mag'
contouru_b_magDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
contouru_b_magDisplay.SelectOrientationVectors = 'velocity'
contouru_b_magDisplay.ScaleFactor = 12969.018945493905
contouru_b_magDisplay.SelectScaleArray = 'u_b_mag'
contouru_b_magDisplay.GlyphType = 'Arrow'
contouru_b_magDisplay.GlyphTableIndexArray = 'u_b_mag'
contouru_b_magDisplay.GaussianRadius = 648.4509472746952
contouru_b_magDisplay.SetScaleArray = ['POINTS', 'u_b_mag']
contouru_b_magDisplay.ScaleTransferFunction = 'PiecewiseFunction'
contouru_b_magDisplay.OpacityArray = ['POINTS', 'u_b_mag']
contouru_b_magDisplay.OpacityTransferFunction = 'PiecewiseFunction'
contouru_b_magDisplay.DataAxesGrid = 'GridAxesRepresentation'
contouru_b_magDisplay.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
contouru_b_magDisplay.ScaleTransferFunction.Points = [2104.890569379176, 0.0, 0.5, 0.0, 2105.390625, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
contouru_b_magDisplay.OpacityTransferFunction.Points = [2104.890569379176, 0.0, 0.5, 0.0, 2105.390625, 1.0, 0.5, 0.0]

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
contouru_b_magDisplay.PolarAxes.Scale = [1.0, 1.0, 0.0]

# show data from thresholduppersurface
thresholduppersurfaceDisplay = Show(thresholduppersurface, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
thresholduppersurfaceDisplay.Representation = 'Surface'
thresholduppersurfaceDisplay.ColorArrayName = ['POINTS', 'emergencevelocity']
thresholduppersurfaceDisplay.LookupTable = emergencevelocityLUT
thresholduppersurfaceDisplay.SelectTCoordArray = 'None'
thresholduppersurfaceDisplay.SelectNormalArray = 'None'
thresholduppersurfaceDisplay.SelectTangentArray = 'None'
thresholduppersurfaceDisplay.OSPRayScaleArray = 'emergencevelocity'
thresholduppersurfaceDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
thresholduppersurfaceDisplay.SelectOrientationVectors = 'velocity'
thresholduppersurfaceDisplay.ScaleFactor = 78305.2202328
thresholduppersurfaceDisplay.SelectScaleArray = 'emergencevelocity'
thresholduppersurfaceDisplay.GlyphType = 'Arrow'
thresholduppersurfaceDisplay.GlyphTableIndexArray = 'emergencevelocity'
thresholduppersurfaceDisplay.GaussianRadius = 3915.26101164
thresholduppersurfaceDisplay.SetScaleArray = ['POINTS', 'emergencevelocity']
thresholduppersurfaceDisplay.ScaleTransferFunction = 'PiecewiseFunction'
thresholduppersurfaceDisplay.OpacityArray = ['POINTS', 'emergencevelocity']
thresholduppersurfaceDisplay.OpacityTransferFunction = 'PiecewiseFunction'
thresholduppersurfaceDisplay.DataAxesGrid = 'GridAxesRepresentation'
thresholduppersurfaceDisplay.PolarAxes = 'PolarAxesRepresentation'
thresholduppersurfaceDisplay.ScalarOpacityFunction = emergencevelocityPWF
thresholduppersurfaceDisplay.ScalarOpacityUnitDistance = 22113.433058322593
thresholduppersurfaceDisplay.OpacityArrayName = ['POINTS', 'emergencevelocity']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
thresholduppersurfaceDisplay.ScaleTransferFunction.Points = [-1196.541819580664, 0.0, 0.5, 0.0, 2661.0955692721773, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
thresholduppersurfaceDisplay.OpacityTransferFunction.Points = [-1196.541819580664, 0.0, 0.5, 0.0, 2661.0955692721773, 1.0, 0.5, 0.0]

# show data from calculatoru_obs_mag
calculatoru_obs_magDisplay = Show(calculatoru_obs_mag, renderView1, 'UnstructuredGridRepresentation')

# get color transfer function/color map for 'u_obs_mag'
u_obs_magLUT = GetColorTransferFunction('u_obs_mag')
u_obs_magLUT.RGBPoints = [0.07436254671408091, 0.231373, 0.298039, 0.752941, 2111.467092623259, 0.865003, 0.865003, 0.865003, 4222.859822699804, 0.705882, 0.0156863, 0.14902]
u_obs_magLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'u_obs_mag'
u_obs_magPWF = GetOpacityTransferFunction('u_obs_mag')
u_obs_magPWF.Points = [0.07436254671408091, 0.0, 0.5, 0.0, 4222.859822699804, 1.0, 0.5, 0.0]
u_obs_magPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
calculatoru_obs_magDisplay.Representation = 'Surface'
calculatoru_obs_magDisplay.ColorArrayName = ['POINTS', 'u_obs_mag']
calculatoru_obs_magDisplay.LookupTable = u_obs_magLUT
calculatoru_obs_magDisplay.SelectTCoordArray = 'None'
calculatoru_obs_magDisplay.SelectNormalArray = 'None'
calculatoru_obs_magDisplay.SelectTangentArray = 'None'
calculatoru_obs_magDisplay.OSPRayScaleArray = 'u_obs_mag'
calculatoru_obs_magDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
calculatoru_obs_magDisplay.SelectOrientationVectors = 'velocity'
calculatoru_obs_magDisplay.ScaleFactor = 78305.2202328
calculatoru_obs_magDisplay.SelectScaleArray = 'u_obs_mag'
calculatoru_obs_magDisplay.GlyphType = 'Arrow'
calculatoru_obs_magDisplay.GlyphTableIndexArray = 'u_obs_mag'
calculatoru_obs_magDisplay.GaussianRadius = 3915.26101164
calculatoru_obs_magDisplay.SetScaleArray = ['POINTS', 'u_obs_mag']
calculatoru_obs_magDisplay.ScaleTransferFunction = 'PiecewiseFunction'
calculatoru_obs_magDisplay.OpacityArray = ['POINTS', 'u_obs_mag']
calculatoru_obs_magDisplay.OpacityTransferFunction = 'PiecewiseFunction'
calculatoru_obs_magDisplay.DataAxesGrid = 'GridAxesRepresentation'
calculatoru_obs_magDisplay.PolarAxes = 'PolarAxesRepresentation'
calculatoru_obs_magDisplay.ScalarOpacityFunction = u_obs_magPWF
calculatoru_obs_magDisplay.ScalarOpacityUnitDistance = 22113.433058322593
calculatoru_obs_magDisplay.OpacityArrayName = ['POINTS', 'u_obs_mag']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
calculatoru_obs_magDisplay.ScaleTransferFunction.Points = [0.07436254671408091, 0.0, 0.5, 0.0, 4222.859822699804, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
calculatoru_obs_magDisplay.OpacityTransferFunction.Points = [0.07436254671408091, 0.0, 0.5, 0.0, 4222.859822699804, 1.0, 0.5, 0.0]

# show data from calculatorflowdiscrepancy
calculatorflowdiscrepancyDisplay = Show(calculatorflowdiscrepancy, renderView1, 'UnstructuredGridRepresentation')

# get color transfer function/color map for 'FlowDis'
flowDisLUT = GetColorTransferFunction('FlowDis')
flowDisLUT.AutomaticRescaleRangeMode = 'Never'
flowDisLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'FlowDis'
flowDisPWF = GetOpacityTransferFunction('FlowDis')
flowDisPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
calculatorflowdiscrepancyDisplay.Representation = 'Surface'
calculatorflowdiscrepancyDisplay.ColorArrayName = ['POINTS', 'FlowDis']
calculatorflowdiscrepancyDisplay.LookupTable = flowDisLUT
calculatorflowdiscrepancyDisplay.SelectTCoordArray = 'None'
calculatorflowdiscrepancyDisplay.SelectNormalArray = 'None'
calculatorflowdiscrepancyDisplay.SelectTangentArray = 'None'
calculatorflowdiscrepancyDisplay.Scale = [1.0, 1.0, 0.0]
calculatorflowdiscrepancyDisplay.OSPRayScaleArray = 'FlowDis'
calculatorflowdiscrepancyDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
calculatorflowdiscrepancyDisplay.SelectOrientationVectors = 'velocity'
calculatorflowdiscrepancyDisplay.ScaleFactor = 78305.2202328
calculatorflowdiscrepancyDisplay.SelectScaleArray = 'FlowDis'
calculatorflowdiscrepancyDisplay.GlyphType = 'Arrow'
calculatorflowdiscrepancyDisplay.GlyphTableIndexArray = 'FlowDis'
calculatorflowdiscrepancyDisplay.GaussianRadius = 3915.26101164
calculatorflowdiscrepancyDisplay.SetScaleArray = ['POINTS', 'FlowDis']
calculatorflowdiscrepancyDisplay.ScaleTransferFunction = 'PiecewiseFunction'
calculatorflowdiscrepancyDisplay.OpacityArray = ['POINTS', 'FlowDis']
calculatorflowdiscrepancyDisplay.OpacityTransferFunction = 'PiecewiseFunction'
calculatorflowdiscrepancyDisplay.DataAxesGrid = 'GridAxesRepresentation'
calculatorflowdiscrepancyDisplay.PolarAxes = 'PolarAxesRepresentation'
calculatorflowdiscrepancyDisplay.ScalarOpacityFunction = flowDisPWF
calculatorflowdiscrepancyDisplay.ScalarOpacityUnitDistance = 22113.433058322593
calculatorflowdiscrepancyDisplay.OpacityArrayName = ['POINTS', 'FlowDis']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
calculatorflowdiscrepancyDisplay.ScaleTransferFunction.Points = [3.92701862125696e-07, 0.0, 0.5, 0.0, 31.581668839274066, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
calculatorflowdiscrepancyDisplay.OpacityTransferFunction.Points = [3.92701862125696e-07, 0.0, 0.5, 0.0, 31.581668839274066, 1.0, 0.5, 0.0]

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
calculatorflowdiscrepancyDisplay.PolarAxes.Scale = [1.0, 1.0, 0.0]

# setup the color legend parameters for each legend in this view

# get color legend/bar for emergencevelocityLUT in view renderView1
emergencevelocityLUTColorBar = GetScalarBar(emergencevelocityLUT, renderView1)
emergencevelocityLUTColorBar.WindowLocation = 'Upper Right Corner'
emergencevelocityLUTColorBar.Title = 'emergencevelocity'
emergencevelocityLUTColorBar.ComponentTitle = ''
emergencevelocityLUTColorBar.TitleColor = [0.0, 0.0, 0.0]
emergencevelocityLUTColorBar.TitleBold = 1
emergencevelocityLUTColorBar.LabelColor = [0.0, 0.0, 0.0]
emergencevelocityLUTColorBar.LabelBold = 1
emergencevelocityLUTColorBar.AutomaticLabelFormat = 0
emergencevelocityLUTColorBar.LabelFormat = '%-#6.1f'
emergencevelocityLUTColorBar.RangeLabelFormat = '%-#6.1f'
emergencevelocityLUTColorBar.ScalarBarThickness = 15
emergencevelocityLUTColorBar.ScalarBarLength = 0.39

# set color bar visibility
emergencevelocityLUTColorBar.Visibility = 0

# get color legend/bar for u_b_magLUT in view renderView1
u_b_magLUTColorBar = GetScalarBar(u_b_magLUT, renderView1)
u_b_magLUTColorBar.WindowLocation = 'Any Location'
u_b_magLUTColorBar.Title = 'u_b_mag'
u_b_magLUTColorBar.ComponentTitle = ''
u_b_magLUTColorBar.TitleColor = [0.0, 0.0, 0.0]
u_b_magLUTColorBar.TitleBold = 1
u_b_magLUTColorBar.LabelColor = [0.0, 0.0, 0.0]
u_b_magLUTColorBar.LabelBold = 1
u_b_magLUTColorBar.AutomaticLabelFormat = 0
u_b_magLUTColorBar.LabelFormat = '%-#6.1f'
u_b_magLUTColorBar.RangeLabelFormat = '%-#6.1f'
u_b_magLUTColorBar.ScalarBarThickness = 15
u_b_magLUTColorBar.ScalarBarLength = 0.39

# set color bar visibility
u_b_magLUTColorBar.Visibility = 0

# get color legend/bar for u_obs_magLUT in view renderView1
u_obs_magLUTColorBar = GetScalarBar(u_obs_magLUT, renderView1)
u_obs_magLUTColorBar.WindowLocation = 'Upper Right Corner'
u_obs_magLUTColorBar.Title = 'u_obs_mag'
u_obs_magLUTColorBar.ComponentTitle = ''
u_obs_magLUTColorBar.TitleColor = [0.0, 0.0, 0.0]
u_obs_magLUTColorBar.TitleBold = 1
u_obs_magLUTColorBar.LabelColor = [0.0, 0.0, 0.0]
u_obs_magLUTColorBar.LabelBold = 1
u_obs_magLUTColorBar.AutomaticLabelFormat = 0
u_obs_magLUTColorBar.LabelFormat = '%-#6.1f'
u_obs_magLUTColorBar.RangeLabelFormat = '%-#6.1f'
u_obs_magLUTColorBar.ScalarBarThickness = 15
u_obs_magLUTColorBar.ScalarBarLength = 0.39

# set color bar visibility
u_obs_magLUTColorBar.Visibility = 0

# get color legend/bar for flowDisLUT in view renderView1
flowDisLUTColorBar = GetScalarBar(flowDisLUT, renderView1)
flowDisLUTColorBar.AutoOrient = 0
flowDisLUTColorBar.Orientation = 'Horizontal'
flowDisLUTColorBar.WindowLocation = 'Any Location'
flowDisLUTColorBar.Position = [0.6982070707070701, 0.018188585607940566]
flowDisLUTColorBar.Title = 'Flow Discrepancy'
flowDisLUTColorBar.ComponentTitle = ''
flowDisLUTColorBar.TitleColor = [0.0, 0.0, 0.0]
flowDisLUTColorBar.TitleBold = 1
flowDisLUTColorBar.LabelColor = [0.0, 0.0, 0.0]
flowDisLUTColorBar.LabelBold = 1
flowDisLUTColorBar.AutomaticLabelFormat = 0
flowDisLUTColorBar.LabelFormat = '%-#6.1f'
flowDisLUTColorBar.RangeLabelFormat = '%-#6.1f'
flowDisLUTColorBar.ScalarBarThickness = 15
flowDisLUTColorBar.ScalarBarLength = 0.2859595959595954

# set color bar visibility
flowDisLUTColorBar.Visibility = 1

# hide data in view
Hide(pig_s4_l4_i_t0016pvtu, renderView1)

# hide data in view
Hide(thresholdlowersurface, renderView1)

# hide data in view
Hide(calculatoru_b_mag, renderView1)

# hide data in view
Hide(thresholduppersurface, renderView1)

# hide data in view
Hide(calculatoru_obs_mag, renderView1)

# show color legend
calculatorflowdiscrepancyDisplay.SetScalarBarVisibility(renderView1, True)

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# restore active source
SetActiveSource(calculatorflowdiscrepancy)
# ----------------------------------------------------------------


if __name__ == '__main__':
    # generate extracts
    SaveExtracts(ExtractsOutputDirectory='extracts')
