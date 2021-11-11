# trace generated using paraview version 5.10.0-RC1

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'XML Partitioned Unstructured Grid Reader'
pig_s4_l4_i_t0016pvtu = XMLPartitionedUnstructuredGridReader(registrationName='pig_s4_l4_i_t0016.pvtu', FileName=['C:/Users/XPS-15/Desktop/S4_I/pig_s4_l4_i_t0016.pvtu'])
pig_s4_l4_i_t0016pvtu.CellArrayStatus = ['GeometryIds']
pig_s4_l4_i_t0016pvtu.PointArrayStatus = ['emergencevelocity', 'bmb', 'alpha', 'beta', 'bed', 'height', 'depth', 'fs upper', 'fs lower', 'vx', 'vy', 'groundedmask', 'smbref', 'ef', 'bottom ef', 'mu', 'temperature', 'viscosity', 'velocity']

# set active source
SetActiveSource(pig_s4_l4_i_t0016pvtu)

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

# show color bar/color legend
pig_s4_l4_i_t0016pvtuDisplay.SetScalarBarVisibility(renderView1, True)

# get the material library
materialLibrary1 = GetMaterialLibrary()

# reset view to fit data
renderView1.ResetCamera(False)

# Properties modified on pig_s4_l4_i_t0016pvtu
pig_s4_l4_i_t0016pvtu.TimeArray = 'None'

# show data in view
pig_s4_l4_i_t0016pvtuDisplay = Show(pig_s4_l4_i_t0016pvtu, renderView1, 'UnstructuredGridRepresentation')

# reset view to fit data
renderView1.ResetCamera(False)

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

# create a new 'Threshold'
threshold1_1 = Threshold(registrationName='Threshold1', Input=threshold1)
threshold1_1.Scalars = ['POINTS', 'emergencevelocity']

# rename source object
RenameSource('Threshold grounded area', threshold1_1)

# Properties modified on threshold1_1
threshold1_1.Scalars = ['POINTS', 'groundedmask']
threshold1_1.LowerThreshold = 1.0
threshold1_1.UpperThreshold = 1.0

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
threshold1_1Display.ScalarOpacityUnitDistance = 23951.826940350908
threshold1_1Display.OpacityArrayName = ['POINTS', 'emergencevelocity']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
threshold1_1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
threshold1_1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# hide data in view
Hide(threshold1, renderView1)

# show color bar/color legend
threshold1_1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Calculator'
calculator1 = Calculator(registrationName='Calculator1', Input=threshold1_1)
calculator1.Function = ''

# rename source object
RenameSource('Calculator tau_b', calculator1)

# Properties modified on calculator1
calculator1.ResultArrayName = 'tau_b'
calculator1.Function = '10^alpha*mag(velocity)'

# show data in view
calculator1Display = Show(calculator1, renderView1, 'UnstructuredGridRepresentation')

# get color transfer function/color map for 'tau_b'
tau_bLUT = GetColorTransferFunction('tau_b')
tau_bLUT.RGBPoints = [1.512062715270901e-06, 0.231373, 0.298039, 0.752941, 4.542437911964192, 0.865003, 0.865003, 0.865003, 9.084874311865669, 0.705882, 0.0156863, 0.14902]
tau_bLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'tau_b'
tau_bPWF = GetOpacityTransferFunction('tau_b')
tau_bPWF.Points = [1.512062715270901e-06, 0.0, 0.5, 0.0, 9.084874311865669, 1.0, 0.5, 0.0]
tau_bPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
calculator1Display.Representation = 'Surface'
calculator1Display.ColorArrayName = ['POINTS', 'tau_b']
calculator1Display.LookupTable = tau_bLUT
calculator1Display.SelectTCoordArray = 'None'
calculator1Display.SelectNormalArray = 'None'
calculator1Display.SelectTangentArray = 'None'
calculator1Display.OSPRayScaleArray = 'tau_b'
calculator1Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator1Display.SelectOrientationVectors = 'velocity'
calculator1Display.ScaleFactor = 78305.2202328
calculator1Display.SelectScaleArray = 'tau_b'
calculator1Display.GlyphType = 'Arrow'
calculator1Display.GlyphTableIndexArray = 'tau_b'
calculator1Display.GaussianRadius = 3915.26101164
calculator1Display.SetScaleArray = ['POINTS', 'tau_b']
calculator1Display.ScaleTransferFunction = 'PiecewiseFunction'
calculator1Display.OpacityArray = ['POINTS', 'tau_b']
calculator1Display.OpacityTransferFunction = 'PiecewiseFunction'
calculator1Display.DataAxesGrid = 'GridAxesRepresentation'
calculator1Display.PolarAxes = 'PolarAxesRepresentation'
calculator1Display.ScalarOpacityFunction = tau_bPWF
calculator1Display.ScalarOpacityUnitDistance = 23951.826940350908
calculator1Display.OpacityArrayName = ['POINTS', 'tau_b']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
calculator1Display.ScaleTransferFunction.Points = [1.512062715270901e-06, 0.0, 0.5, 0.0, 9.084874311865669, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
calculator1Display.OpacityTransferFunction.Points = [1.512062715270901e-06, 0.0, 0.5, 0.0, 9.084874311865669, 1.0, 0.5, 0.0]

# hide data in view
Hide(threshold1_1, renderView1)

# show color bar/color legend
calculator1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# rename source object
RenameSource('Calculator u_b', calculator1)

# rename source object
RenameSource('Calculator u_b_mag', calculator1)

# Properties modified on calculator1
calculator1.ResultArrayName = 'u_b_mag'
calculator1.Function = 'mag(velocity)'

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Calculator'
calculator1_1 = Calculator(registrationName='Calculator1', Input=calculator1)
calculator1_1.Function = ''

# rename source object
RenameSource('Calculator tau_b', calculator1_1)

# Properties modified on calculator1_1
calculator1_1.ResultArrayName = 'tau_b'
calculator1_1.Function = '10^alpha*u_b_mag'

# show data in view
calculator1_1Display = Show(calculator1_1, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
calculator1_1Display.Representation = 'Surface'
calculator1_1Display.ColorArrayName = ['POINTS', 'tau_b']
calculator1_1Display.LookupTable = tau_bLUT
calculator1_1Display.SelectTCoordArray = 'None'
calculator1_1Display.SelectNormalArray = 'None'
calculator1_1Display.SelectTangentArray = 'None'
calculator1_1Display.OSPRayScaleArray = 'tau_b'
calculator1_1Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator1_1Display.SelectOrientationVectors = 'velocity'
calculator1_1Display.ScaleFactor = 78305.2202328
calculator1_1Display.SelectScaleArray = 'tau_b'
calculator1_1Display.GlyphType = 'Arrow'
calculator1_1Display.GlyphTableIndexArray = 'tau_b'
calculator1_1Display.GaussianRadius = 3915.26101164
calculator1_1Display.SetScaleArray = ['POINTS', 'tau_b']
calculator1_1Display.ScaleTransferFunction = 'PiecewiseFunction'
calculator1_1Display.OpacityArray = ['POINTS', 'tau_b']
calculator1_1Display.OpacityTransferFunction = 'PiecewiseFunction'
calculator1_1Display.DataAxesGrid = 'GridAxesRepresentation'
calculator1_1Display.PolarAxes = 'PolarAxesRepresentation'
calculator1_1Display.ScalarOpacityFunction = tau_bPWF
calculator1_1Display.ScalarOpacityUnitDistance = 23951.826940350908
calculator1_1Display.OpacityArrayName = ['POINTS', 'tau_b']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
calculator1_1Display.ScaleTransferFunction.Points = [1.512062715270901e-06, 0.0, 0.5, 0.0, 9.084874311865669, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
calculator1_1Display.OpacityTransferFunction.Points = [1.512062715270901e-06, 0.0, 0.5, 0.0, 9.084874311865669, 1.0, 0.5, 0.0]

# hide data in view
Hide(calculator1, renderView1)

# show color bar/color legend
calculator1_1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Contour'
contour1 = Contour(registrationName='Contour1', Input=calculator1_1)
contour1.ContourBy = ['POINTS', 'tau_b']
contour1.Isosurfaces = [4.542437911964192]
contour1.PointMergeMethod = 'Uniform Binning'

# rename source object
RenameSource('Contour u_b_mag', contour1)

# show data in view
contour1Display = Show(contour1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
contour1Display.Representation = 'Surface'
contour1Display.ColorArrayName = ['POINTS', 'tau_b']
contour1Display.LookupTable = tau_bLUT
contour1Display.SelectTCoordArray = 'None'
contour1Display.SelectNormalArray = 'None'
contour1Display.SelectTangentArray = 'None'
contour1Display.OSPRayScaleArray = 'tau_b'
contour1Display.OSPRayScaleFunction = 'PiecewiseFunction'
contour1Display.SelectOrientationVectors = 'velocity'
contour1Display.ScaleFactor = 8274.669639047162
contour1Display.SelectScaleArray = 'tau_b'
contour1Display.GlyphType = 'Arrow'
contour1Display.GlyphTableIndexArray = 'tau_b'
contour1Display.GaussianRadius = 413.73348195235815
contour1Display.SetScaleArray = ['POINTS', 'tau_b']
contour1Display.ScaleTransferFunction = 'PiecewiseFunction'
contour1Display.OpacityArray = ['POINTS', 'tau_b']
contour1Display.OpacityTransferFunction = 'PiecewiseFunction'
contour1Display.DataAxesGrid = 'GridAxesRepresentation'
contour1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
contour1Display.ScaleTransferFunction.Points = [4.542437911964192, 0.0, 0.5, 0.0, 4.54341459274292, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
contour1Display.OpacityTransferFunction.Points = [4.542437911964192, 0.0, 0.5, 0.0, 4.54341459274292, 1.0, 0.5, 0.0]

# hide data in view
Hide(calculator1_1, renderView1)

# show color bar/color legend
contour1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on contour1
contour1.ContourBy = ['POINTS', 'u_b_mag']
contour1.Isosurfaces = [100.0, 1000.0]

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(calculator1_1)

# show data in view
calculator1_1Display = Show(calculator1_1, renderView1, 'UnstructuredGridRepresentation')

# show color bar/color legend
calculator1_1Display.SetScalarBarVisibility(renderView1, True)

# set active source
SetActiveSource(threshold1)

# show data in view
threshold1Display = Show(threshold1, renderView1, 'UnstructuredGridRepresentation')

# show color bar/color legend
threshold1Display.SetScalarBarVisibility(renderView1, True)

# Properties modified on threshold1Display
threshold1Display.Scale = [1.0, 1.0, 0.0]

# Properties modified on threshold1Display.DataAxesGrid
threshold1Display.DataAxesGrid.Scale = [1.0, 1.0, 0.0]

# Properties modified on threshold1Display.PolarAxes
threshold1Display.PolarAxes.Scale = [1.0, 1.0, 0.0]

# set active source
SetActiveSource(calculator1_1)

# Properties modified on calculator1_1Display
calculator1_1Display.Scale = [1.0, 1.0, 0.0]

# Properties modified on calculator1_1Display.DataAxesGrid
calculator1_1Display.DataAxesGrid.Scale = [1.0, 1.0, 0.0]

# Properties modified on calculator1_1Display.PolarAxes
calculator1_1Display.PolarAxes.Scale = [1.0, 1.0, 0.0]

# set active source
SetActiveSource(contour1)

# Properties modified on contour1Display
contour1Display.Scale = [1.0, 1.0, 0.0]

# Properties modified on contour1Display.DataAxesGrid
contour1Display.DataAxesGrid.Scale = [1.0, 1.0, 0.0]

# Properties modified on contour1Display.PolarAxes
contour1Display.PolarAxes.Scale = [1.0, 1.0, 0.0]

# set active source
SetActiveSource(calculator1_1)

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
tau_bLUT.ApplyPreset('Viridis (matplotlib)', True)

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
tau_bLUT.ApplyPreset('Viridis (matplotlib)', True)

# invert the transfer function
tau_bLUT.InvertTransferFunction()

# get color legend/bar for tau_bLUT in view renderView1
tau_bLUTColorBar = GetScalarBar(tau_bLUT, renderView1)
tau_bLUTColorBar.WindowLocation = 'Any Location'
tau_bLUTColorBar.Title = 'tau_b'
tau_bLUTColorBar.ComponentTitle = ''
tau_bLUTColorBar.TitleColor = [0.0, 0.0, 0.0]
tau_bLUTColorBar.TitleBold = 1
tau_bLUTColorBar.LabelColor = [0.0, 0.0, 0.0]
tau_bLUTColorBar.LabelBold = 1
tau_bLUTColorBar.AutomaticLabelFormat = 0
tau_bLUTColorBar.LabelFormat = '%-#6.1f'
tau_bLUTColorBar.RangeLabelFormat = '%-#6.1f'
tau_bLUTColorBar.ScalarBarThickness = 15
tau_bLUTColorBar.ScalarBarLength = 0.39

# change scalar bar placement
tau_bLUTColorBar.Position = [0.8324242424242424, 0.06466501240694793]

# Rescale transfer function
tau_bLUT.RescaleTransferFunction(0.0, 1.0)

# Rescale transfer function
tau_bPWF.RescaleTransferFunction(0.0, 1.0)

# Rescale transfer function
tau_bLUT.RescaleTransferFunction(0.0001, 1.0)

# Rescale transfer function
tau_bPWF.RescaleTransferFunction(0.0001, 1.0)

# convert to log space
tau_bLUT.MapControlPointsToLogSpace()

# Properties modified on tau_bLUT
tau_bLUT.UseLogScale = 1

# set active source
SetActiveSource(threshold1)

# turn off scalar coloring
ColorBy(threshold1Display, None)

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(emergencevelocityLUT, renderView1)

# set active source
SetActiveSource(calculator1_1)

# set active source
SetActiveSource(contour1)

# Properties modified on contour1Display
contour1Display.LineWidth = 2.0

# set scalar coloring
ColorBy(contour1Display, ('POINTS', 'velocity', 'Magnitude'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(tau_bLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
contour1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
contour1Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'velocity'
velocityLUT = GetColorTransferFunction('velocity')
velocityLUT.RGBPoints = [0.011403976794966693, 0.231373, 0.298039, 0.752941, 2106.6925802016617, 0.865003, 0.865003, 0.865003, 4213.373756426528, 0.705882, 0.0156863, 0.14902]
velocityLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'velocity'
velocityPWF = GetOpacityTransferFunction('velocity')
velocityPWF.Points = [0.011403976794966693, 0.0, 0.5, 0.0, 4213.373756426528, 1.0, 0.5, 0.0]
velocityPWF.ScalarRangeInitialized = 1

# get color legend/bar for velocityLUT in view renderView1
velocityLUTColorBar = GetScalarBar(velocityLUT, renderView1)
velocityLUTColorBar.WindowLocation = 'Upper Right Corner'
velocityLUTColorBar.Title = 'velocity'
velocityLUTColorBar.ComponentTitle = 'Magnitude'
velocityLUTColorBar.TitleColor = [0.0, 0.0, 0.0]
velocityLUTColorBar.TitleBold = 1
velocityLUTColorBar.LabelColor = [0.0, 0.0, 0.0]
velocityLUTColorBar.LabelBold = 1
velocityLUTColorBar.AutomaticLabelFormat = 0
velocityLUTColorBar.LabelFormat = '%-#6.1f'
velocityLUTColorBar.RangeLabelFormat = '%-#6.1f'
velocityLUTColorBar.ScalarBarThickness = 15
velocityLUTColorBar.ScalarBarLength = 0.39

# change scalar bar placement
velocityLUTColorBar.Position = [0.8970959595959596, 0.5942928039702233]

# hide color bar/color legend
contour1Display.SetScalarBarVisibility(renderView1, False)

# set active source
SetActiveSource(calculator1_1)

# Properties modified on tau_bLUTColorBar
tau_bLUTColorBar.AutoOrient = 0
tau_bLUTColorBar.Orientation = 'Horizontal'
tau_bLUTColorBar.Title = 'Basal resistance, Mpa'

# Properties modified on tau_bLUTColorBar
tau_bLUTColorBar.UseCustomLabels = 1
tau_bLUTColorBar.CustomLabels = [0.001, 0.01, 0.1]

# Properties modified on tau_bLUTColorBar
tau_bLUTColorBar.AutomaticLabelFormat = 1

# change scalar bar placement
tau_bLUTColorBar.Position = [0.5901010101010098, 0.08161290322580665]
tau_bLUTColorBar.ScalarBarLength = 0.3900000000000007

# change scalar bar placement
tau_bLUTColorBar.Position = [0.5890909090909088, 0.10766749379652625]

# Properties modified on calculator1_1Display
calculator1_1Display.ShowTexturesOnBackface = 0

# Properties modified on calculator1_1Display
calculator1_1Display.ShowTexturesOnBackface = 1

# Properties modified on renderView1
renderView1.OrientationAxesVisibility = 0

# change scalar bar placement
tau_bLUTColorBar.Position = [0.6850505050505047, 0.10766749379652625]
tau_bLUTColorBar.ScalarBarLength = 0.29404040404040477

# change scalar bar placement
tau_bLUTColorBar.Position = [0.6951515151515147, 0.010893300248139153]

# change scalar bar placement
tau_bLUTColorBar.Position = [0.6789898989898986, 0.014615384615384811]

# get layout
layout1 = GetLayout()

# layout/tab size in pixels
layout1.SetSize(990, 806)

# current camera placement for renderView1
renderView1.CameraPosition = [-1567557.0726364802, -225823.5174728783, 675373.0855179759]
renderView1.CameraFocalPoint = [-1532787.6654349628, -209804.5894552741, -8748.095445001694]
renderView1.CameraViewUp = [-0.0006924865340347511, 0.9997265569918664, 0.023373739700542757]
renderView1.CameraParallelScale = 459975.8283875806

# save screenshot
SaveScreenshot('C:/Users/XPS-15/Desktop/PIG_tau_b.png', renderView1, ImageResolution=[1980, 1612],
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
renderView1.CameraPosition = [-1567557.0726364802, -225823.5174728783, 675373.0855179759]
renderView1.CameraFocalPoint = [-1532787.6654349628, -209804.5894552741, -8748.095445001694]
renderView1.CameraViewUp = [-0.0006924865340347511, 0.9997265569918664, 0.023373739700542757]
renderView1.CameraParallelScale = 459975.8283875806

#--------------------------------------------
# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).