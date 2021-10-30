##################################################################
# Script to save the screenshot 
##################################################################

# get active view
renderView2 = GetActiveViewOrCreate('RenderView')

# get layout
layout1 = GetLayout()

# layout/tab size in pixels
layout1.SetSize(990, 806)

# current camera placement for renderView2
renderView2.CameraPosition = [-1541356.6899384311, -213500.47319195943, 695780.6775417095]
renderView2.CameraFocalPoint = [-1541356.6899384311, -205651.43476640512, -1.5967825998247633]
renderView2.CameraViewUp = [0.0, 0.9999363769118055, 0.011280165268815222]
renderView2.CameraParallelScale = 217912.72592683224

# save screenshot
SaveScreenshot('C:/Users/XPS-15/Desktop/Filename.png', renderView2, ImageResolution=[1980, 1612],
    OverrideColorPalette='WhiteBackground')
