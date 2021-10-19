# Elmer/Ice's Paraview Python Post Processor (EP4) utils.
# 
# Development version. No error handling. Not licensed. Share at will. Guaranteed to fail one way or another.
# Contact: RupertGladstone1972@gmail.com
# 
# Initially created based on trace generated using paraview version 5.7.0
#


#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

def EP4_plot(EP4_params):
    "A standard plot from a pvtu file showing a lower or upper surface field variable, or difference between two variables, with grounding line and upper surface velocity contours"
    
    # create a new 'XML Partitioned Unstructured Grid Reader'
    inputDataset = XMLPartitionedUnstructuredGridReader(FileName=EP4_params['inputfname'])
    inputDataset.CellArrayStatus = ['GeometryIds']
    inputDataset.PointArrayStatus = EP4_params['fieldvars']
    
    # get active view
    renderView1 = GetActiveViewOrCreate('RenderView')
    # set a specific view size
    renderView1.ViewSize = [EP4_params['xres'], EP4_params['yres'] ]
    
    # remove axes and set background to white
    renderView1.OrientationAxesVisibility = 0    
    renderView1.Background = [1.0, 1.0, 1.0]

    [lowerSurface,lowerSurfaceDisplay] = extractSurface(EP4_params,inputDataset,renderView1,'lower')
    [upperSurface,upperSurfaceDisplay] = extractSurface(EP4_params,inputDataset,renderView1,'upper')

    if (EP4_params['surface']=='lower'):
        [fieldvarLUTColorBar, fieldvarLUT, fieldvarPWF] = plotField(EP4_params,renderView1,lowerSurfaceDisplay)
        Hide(upperSurface, renderView1)
    elif (EP4_params['surface']=='upper'):
        [fieldvarLUTColorBar, fieldvarLUT, fieldvarPWF] = plotField(EP4_params,renderView1,upperSurfaceDisplay)
        Hide(lowerSurface, renderView1)
    else:
        sys.exit("ERROR in extractSurface: surface should be lower or upper")

    contour1Display = addGL(EP4_params, lowerSurface, renderView1)    
    calculator1 = velocityMagnitude(upperSurface)
    Hide(calculator1, renderView1)
    contour2Display = addVelContours(EP4_params, calculator1, renderView1)    

#    Hide(lowerSurface, renderView1)
#    Hide(upperSurface, renderView1)
#    Hide(lowerSurfaceDisplay, renderView1)
#    Hide(upperSurfaceDisplay, renderView1)

#    ColorBy(upperSurface, ('POINTS', EP4_params['fieldvar']))

    
    # current camera placement for renderView1
    renderView1.CameraPosition = [EP4_params['camerax'], EP4_params['cameray'], EP4_params['cameraHeight']]
    renderView1.CameraFocalPoint = [EP4_params['camerax'], EP4_params['cameray'], 0.0]
    renderView1.CameraParallelScale = 459975.77514285187
    
    # save screenshot
    SaveScreenshot(EP4_params['imgname'], renderView1, ImageResolution=[EP4_params['xres'],EP4_params['yres']])
    
    # set active source
    SetActiveSource(None)
    
    # set active view
    SetActiveView(None)





def extractSurface(EP4_params,inputDataset,renderView1,surface):
    "Select and extract the lower or upper surface using threshold filter based on geometry ID"

    if (surface=='lower'):
        thresholdValue = EP4_params['LSgeomID']
    elif (surface=='upper'):
        thresholdValue = EP4_params['USgeomID']
    else:
        sys.exit("ERROR in extractSurface: surface should be lower or upper")
        
    # create a new 'Threshold'
    threshold1 = Threshold(Input=inputDataset)
    threshold1.Scalars = ['CELLS', 'GeometryIds']
    threshold1.ThresholdRange = [ thresholdValue, thresholdValue ]

    # show data in view
    threshold1Display = Show(threshold1, renderView1)

    # trace defaults for the display properties.
    threshold1Display.Representation = 'Surface'
    threshold1Display.ColorArrayName = [None, '']
    threshold1Display.OSPRayScaleArray = EP4_params['fieldvar']
    threshold1Display.OSPRayScaleFunction = 'PiecewiseFunction'
    threshold1Display.SelectOrientationVectors = 'None'
    threshold1Display.ScaleFactor = 78305.2202328
    threshold1Display.SelectScaleArray = 'None'
    threshold1Display.GlyphType = 'Arrow'
    threshold1Display.GlyphTableIndexArray = 'None'
    threshold1Display.GaussianRadius = 3915.26101164
    threshold1Display.SetScaleArray = ['POINTS', EP4_params['fieldvar']]
    threshold1Display.ScaleTransferFunction = 'PiecewiseFunction'
    threshold1Display.OpacityArray = ['POINTS', EP4_params['fieldvar']]
    threshold1Display.OpacityTransferFunction = 'PiecewiseFunction'
    threshold1Display.DataAxesGrid = 'GridAxesRepresentation'
    threshold1Display.PolarAxes = 'PolarAxesRepresentation'
    threshold1Display.ScalarOpacityUnitDistance = 22113.595860805814
    
    # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
    threshold1Display.ScaleTransferFunction.Points = [-2256.1485977394705, 0.0, 0.5, 0.0, 2019.8503138145743, 1.0, 0.5, 0.0]
    
    # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
    threshold1Display.OpacityTransferFunction.Points = [-2256.1485977394705, 0.0, 0.5, 0.0, 2019.8503138145743, 1.0, 0.5, 0.0]
    
    # update the view to ensure updated data information
    renderView1.Update()

    # set scalar coloring
    ColorBy(threshold1Display, ('POINTS', EP4_params['fieldvar']))
    
    # rescale color and/or opacity maps used to include current data range
    threshold1Display.RescaleTransferFunctionToDataRange(True, False)

    # show color bar/color legend
    threshold1Display.SetScalarBarVisibility(renderView1, True)

    # reduce vertical scaling
    threshold1Display.Scale = [1.0, 1.0, 0.1]
    threshold1Display.DataAxesGrid.Scale = [1.0, 1.0, 0.1]
    threshold1Display.PolarAxes.Scale = [1.0, 1.0, 0.1]

    return [threshold1,threshold1Display]





def addGL(EP4_params,lowerSurface,renderView1):
    "Use contour filter on grounded mask to add grounding line to current view"

    # get color transfer function/color map for 'groundedmask'
    groundedmaskLUT = GetColorTransferFunction('groundedmask')
    groundedmaskLUT.RGBPoints = [0.0, 0.231373, 0.298039, 0.752941, 5.878906683738906e-39, 0.865003, 0.865003, 0.865003, 1.1757813367477812e-38, 0.705882, 0.0156863, 0.14902]
    groundedmaskLUT.ScalarRangeInitialized = 1.0
    
    # create a new 'Contour'
    contour1 = Contour(Input=lowerSurface)
    contour1.ContourBy = ['POINTS', 'groundedmask']
    contour1.Isosurfaces = [0.0]
    contour1.PointMergeMethod = 'Uniform Binning'
    
    # show data in view
    contour1Display = Show(contour1, renderView1)
    
    # trace defaults for the display properties.
    contour1Display.Representation = 'Surface'
    contour1Display.ColorArrayName = ['POINTS', 'groundedmask']
    contour1Display.LookupTable = groundedmaskLUT
    contour1Display.OSPRayScaleArray = 'groundedmask'
    contour1Display.OSPRayScaleFunction = 'PiecewiseFunction'
    contour1Display.SelectOrientationVectors = 'velocity'
    contour1Display.ScaleFactor = 13185.17195599999
    contour1Display.SelectScaleArray = 'groundedmask'
    contour1Display.GlyphType = 'Arrow'
    contour1Display.GlyphTableIndexArray = 'groundedmask'
    contour1Display.GaussianRadius = 659.2585977999994
    contour1Display.SetScaleArray = ['POINTS', 'groundedmask']
    contour1Display.ScaleTransferFunction = 'PiecewiseFunction'
    contour1Display.OpacityArray = ['POINTS', 'groundedmask']
    contour1Display.OpacityTransferFunction = 'PiecewiseFunction'
    contour1Display.DataAxesGrid = 'GridAxesRepresentation'
    contour1Display.PolarAxes = 'PolarAxesRepresentation'
    
    # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
    contour1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]
    
    # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
    contour1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]
    
    # turn off scalar coloring
    ColorBy(contour1Display, None)
    
    # Hide the scalar bar for this color map if no visible data is colored by it.
    HideScalarBarIfNotNeeded(groundedmaskLUT, renderView1)
    
    # change solid color
    contour1Display.AmbientColor = [0.0, 0.0, 0.0]
    contour1Display.DiffuseColor = [0.0, 0.0, 0.0]
    
    # Properties modified on contour1Display
    contour1Display.LineWidth = 3.0
    
    # Compress vertically
    contour1Display.Scale = [1.0, 1.0, 0.1]
    contour1Display.DataAxesGrid.Scale = [1.0, 1.0, 0.1]
    contour1Display.PolarAxes.Scale = [1.0, 1.0, 0.1]
    
    # Lift GL contour a bit so that it is above 2d lower surface display
    contour1Display.Position = [0.0, 0.0, 100.0]
    contour1Display.DataAxesGrid.Position = [0.0, 0.0, 100.0]
    contour1Display.PolarAxes.Translation = [0.0, 0.0, 100.0]
    



def velocityMagnitude(upperSurface):
    "Use calculator filter to get the magnitude of the velocity vector"

    # create a new 'Calculator'
    calculator1 = Calculator(Input=upperSurface)
    calculator1.ResultArrayName = 'Ice velocity, $m a{-1^}$'
    calculator1.Function = 'mag(velocity)'
    
    return calculator1



def addVelContours(EP4_params,calculator1,renderView1):
    "Use contour filter to add velocity contours"

    # get color transfer function/color map for 'Icevelocityma1'
    icevelocityma1LUT = GetColorTransferFunction('Icevelocityma1')
    
    # get opacity transfer function/opacity map for 'Icevelocityma1'
    icevelocityma1PWF = GetOpacityTransferFunction('Icevelocityma1')

    # create a new 'Contour'
    contour2 = Contour(Input=calculator1)
    contour2.ContourBy = ['POINTS', 'Ice velocity, $m a{-1^}$']
    contour2.Isosurfaces = EP4_params['velocityContours']
    contour2.PointMergeMethod = 'Uniform Binning'

    # show data in view
    contour2Display = Show(contour2, renderView1)
    
    # trace defaults for the display properties.
    contour2Display.Representation = 'Surface'
    contour2Display.ColorArrayName = ['POINTS', 'Ice velocity, $m a{-1^}$']
    contour2Display.LookupTable = icevelocityma1LUT
    contour2Display.OSPRayScaleArray = 'Ice velocity, $m a{-1^}$'
    contour2Display.OSPRayScaleFunction = 'PiecewiseFunction'
    contour2Display.SelectOrientationVectors = 'velocity'
    contour2Display.ScaleFactor = 41739.81971939511
    contour2Display.SelectScaleArray = 'Ice velocity, $m a{-1^}$'
    contour2Display.GlyphType = 'Arrow'
    contour2Display.GlyphTableIndexArray = 'Ice velocity, $m a{-1^}$'
    contour2Display.GaussianRadius = 2086.9909859697555
    contour2Display.SetScaleArray = ['POINTS', 'Ice velocity, $m a{-1^}$']
    contour2Display.ScaleTransferFunction = 'PiecewiseFunction'
    contour2Display.OpacityArray = ['POINTS', 'Ice velocity, $m a{-1^}$']
    contour2Display.OpacityTransferFunction = 'PiecewiseFunction'
    contour2Display.DataAxesGrid = 'GridAxesRepresentation'
    contour2Display.PolarAxes = 'PolarAxesRepresentation'
    
    # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
    contour2Display.ScaleTransferFunction.Points = [100.0, 0.0, 0.5, 0.0, 1000.0, 1.0, 0.5, 0.0]
    
    # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
    contour2Display.OpacityTransferFunction.Points = [100.0, 0.0, 0.5, 0.0, 1000.0, 1.0, 0.5, 0.0]

    # show color bar/color legend
    contour2Display.SetScalarBarVisibility(renderView1, True)
    
    # update the view to ensure updated data information
    renderView1.Update()
    
    # turn off scalar coloring
    ColorBy(contour2Display, None)
    
    # Hide the scalar bar for this color map if no visible data is colored by it.
    HideScalarBarIfNotNeeded(icevelocityma1LUT, renderView1)
    
    # change solid color
    contour2Display.AmbientColor = [1.0, 1.0, 1.0]
    contour2Display.DiffuseColor = [1.0, 1.0, 1.0]
    
    # Properties modified on contour1Display
    contour2Display.LineWidth = 2.0

    return contour2Display



def plotField(EP4_params,renderView1,plottingSurface):
    "Add a field variable to the current view"
    
    # set scalar coloring
    ColorBy(plottingSurface, ('POINTS', EP4_params['fieldvar']))
    
    # rescale color and/or opacity maps used to include current data range
    plottingSurface.RescaleTransferFunctionToDataRange(True, False)
    
    # show color bar/color legend
    plottingSurface.SetScalarBarVisibility(renderView1, True)
    
    # get color transfer function/color map for 'fieldvar'
    fieldvarLUT = GetColorTransferFunction(EP4_params['fieldvar'])
    
    # get opacity transfer function/opacity map for fieldvar
    fieldvarPWF = GetOpacityTransferFunction(EP4_params['fieldvar'])

    # get color legend/bar for fieldvarLUT in view renderView1
    fieldvarLUTColorBar = GetScalarBar(fieldvarLUT, renderView1)
    fieldvarLUTColorBar.Title = EP4_params['fieldvarLabel']
    fieldvarLUTColorBar.ComponentTitle = ''
    
    # Properties modified on fieldvarLUTColorBar
    # (setting size, font etc for colorbar)
    fieldvarLUTColorBar.ScalarBarThickness = 10
    fieldvarLUTColorBar.ScalarBarLength = 0.2
    fieldvarLUTColorBar.AddRangeLabels = 0
    fieldvarLUTColorBar.TitleFontSize = EP4_params['fontSize']
    fieldvarLUTColorBar.LabelFontSize = EP4_params['fontSize']
    # Set colorbar text to black
    fieldvarLUTColorBar.TitleColor = [0.0, 0.0, 0.0]
    fieldvarLUTColorBar.LabelColor = [0.0, 0.0, 0.0]

    # Hide the scalar bar for this color map if no visible data is colored by it.
    HideScalarBarIfNotNeeded(fieldvarLUT, renderView1)
    
    # User defined value range
    if 'fieldrange' in EP4_params.keys():
        fieldvarLUT.RescaleTransferFunction(EP4_params['fieldrange'])
        fieldvarPWF.RescaleTransferFunction(EP4_params['fieldrange'])
        
    return [fieldvarLUTColorBar, fieldvarLUT, fieldvarPWF]
