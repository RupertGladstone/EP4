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
renderView1.CenterOfRotation = [-1389421.5833959999, -144609.38397855, 64.8329610983003]
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [-1567557.0726364802, -225823.5174728783, 675373.0855179759]
renderView1.CameraFocalPoint = [-1532787.6654349628, -209804.5894552741, -8748.095445001694]
renderView1.CameraViewUp = [-0.0006924865340347511, 0.9997265569918664, 0.023373739700542757]
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 459975.8283875806
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
thresholdlowersurface = Threshold(registrationName='Threshold lower surface', Input=pig_s4_l4_i_t0016pvtu)
thresholdlowersurface.Scalars = ['CELLS', 'GeometryIds']
thresholdlowersurface.LowerThreshold = 103.0
thresholdlowersurface.UpperThreshold = 103.0

# create a new 'Threshold'
thresholdgroundedarea = Threshold(registrationName='Threshold grounded area', Input=thresholdlowersurface)
thresholdgroundedarea.Scalars = ['POINTS', 'groundedmask']
thresholdgroundedarea.LowerThreshold = 1.0
thresholdgroundedarea.UpperThreshold = 1.0

# create a new 'Calculator'
calculatoru_b_mag = Calculator(registrationName='Calculator u_b_mag', Input=thresholdgroundedarea)
calculatoru_b_mag.ResultArrayName = 'u_b_mag'
calculatoru_b_mag.Function = 'mag(velocity)'

# create a new 'Calculator'
calculatortau_b = Calculator(registrationName='Calculator tau_b', Input=calculatoru_b_mag)
calculatortau_b.ResultArrayName = 'tau_b'
calculatortau_b.Function = '10^alpha*u_b_mag'

# create a new 'Contour'
contouru_b_mag = Contour(registrationName='Contour u_b_mag', Input=calculatortau_b)
contouru_b_mag.ContourBy = ['POINTS', 'u_b_mag']
contouru_b_mag.Isosurfaces = [100.0, 1000.0]
contouru_b_mag.PointMergeMethod = 'Uniform Binning'

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
thresholdlowersurfaceDisplay.ColorArrayName = ['POINTS', '']
thresholdlowersurfaceDisplay.SelectTCoordArray = 'None'
thresholdlowersurfaceDisplay.SelectNormalArray = 'None'
thresholdlowersurfaceDisplay.SelectTangentArray = 'None'
thresholdlowersurfaceDisplay.Scale = [1.0, 1.0, 0.0]
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
thresholdlowersurfaceDisplay.ScalarOpacityUnitDistance = 22113.595860805817
thresholdlowersurfaceDisplay.OpacityArrayName = ['POINTS', 'emergencevelocity']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
thresholdlowersurfaceDisplay.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
thresholdlowersurfaceDisplay.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
thresholdlowersurfaceDisplay.PolarAxes.Scale = [1.0, 1.0, 0.0]

# show data from thresholdgroundedarea
thresholdgroundedareaDisplay = Show(thresholdgroundedarea, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
thresholdgroundedareaDisplay.Representation = 'Surface'
thresholdgroundedareaDisplay.ColorArrayName = ['POINTS', 'emergencevelocity']
thresholdgroundedareaDisplay.LookupTable = emergencevelocityLUT
thresholdgroundedareaDisplay.SelectTCoordArray = 'None'
thresholdgroundedareaDisplay.SelectNormalArray = 'None'
thresholdgroundedareaDisplay.SelectTangentArray = 'None'
thresholdgroundedareaDisplay.OSPRayScaleArray = 'emergencevelocity'
thresholdgroundedareaDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
thresholdgroundedareaDisplay.SelectOrientationVectors = 'velocity'
thresholdgroundedareaDisplay.ScaleFactor = 78305.2202328
thresholdgroundedareaDisplay.SelectScaleArray = 'emergencevelocity'
thresholdgroundedareaDisplay.GlyphType = 'Arrow'
thresholdgroundedareaDisplay.GlyphTableIndexArray = 'emergencevelocity'
thresholdgroundedareaDisplay.GaussianRadius = 3915.26101164
thresholdgroundedareaDisplay.SetScaleArray = ['POINTS', 'emergencevelocity']
thresholdgroundedareaDisplay.ScaleTransferFunction = 'PiecewiseFunction'
thresholdgroundedareaDisplay.OpacityArray = ['POINTS', 'emergencevelocity']
thresholdgroundedareaDisplay.OpacityTransferFunction = 'PiecewiseFunction'
thresholdgroundedareaDisplay.DataAxesGrid = 'GridAxesRepresentation'
thresholdgroundedareaDisplay.PolarAxes = 'PolarAxesRepresentation'
thresholdgroundedareaDisplay.ScalarOpacityFunction = emergencevelocityPWF
thresholdgroundedareaDisplay.ScalarOpacityUnitDistance = 23951.826940350908
thresholdgroundedareaDisplay.OpacityArrayName = ['POINTS', 'emergencevelocity']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
thresholdgroundedareaDisplay.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
thresholdgroundedareaDisplay.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# show data from calculatoru_b_mag
calculatoru_b_magDisplay = Show(calculatoru_b_mag, renderView1, 'UnstructuredGridRepresentation')

# get color transfer function/color map for 'tau_b'
tau_bLUT = GetColorTransferFunction('tau_b')
tau_bLUT.AutomaticRescaleRangeMode = 'Never'
tau_bLUT.RGBPoints = [0.0001, 0.993248, 0.906157, 0.143936, 0.0001036783316283538, 0.983868, 0.904867, 0.136897, 0.00010749097445936855, 0.974417, 0.90359, 0.130215, 0.00011144484897053321, 0.964894, 0.902323, 0.123941, 0.00011554309590224598, 0.9553, 0.901065, 0.118128, 0.00011979315414319746, 0.945636, 0.899815, 0.112838, 0.0001241983997058467, 0.935904, 0.89857, 0.108131, 0.00012876682872413637, 0.926106, 0.89733, 0.104071, 0.00013350329971192445, 0.916242, 0.896091, 0.100717, 0.000138412718976, 0.906311, 0.894855, 0.098125, 0.00014350399779575898, 0.89632, 0.893616, 0.096335, 0.0001487811804030094, 0.886271, 0.892374, 0.095374, 0.00015425384561881176, 0.876168, 0.891125, 0.09525, 0.00015992634062734573, 0.866013, 0.889868, 0.095953, 0.0001658089617967104, 0.85581, 0.888601, 0.097452, 0.00017190796528112424, 0.845561, 0.887322, 0.099702, 0.00017822966877624596, 0.83527, 0.886029, 0.102646, 0.00018478554705395303, 0.82494, 0.88472, 0.106217, 0.0001915808077432913, 0.814576, 0.883393, 0.110347, 0.0001986277851883687, 0.804182, 0.882046, 0.114965, 0.00020593207712039281, 0.79376, 0.880678, 0.120005, 0.0002135069418460386, 0.783315, 0.879285, 0.125405, 0.0002213604352166926, 0.772852, 0.877868, 0.131109, 0.00022950069232870375, 0.762373, 0.876424, 0.137064, 0.00023794248888192213, 0.751884, 0.874951, 0.143228, 0.0002466925305751204, 0.741388, 0.873449, 0.149561, 0.000255766699952052, 0.730889, 0.871916, 0.156029, 0.00026517220503367265, 0.720391, 0.87035, 0.162603, 0.00027492611812102944, 0.709898, 0.868751, 0.169257, 0.00028503618718608885, 0.699415, 0.867117, 0.175971, 0.0002955207634116085, 0.688944, 0.865448, 0.182725, 0.0003063909971205313, 0.678489, 0.863742, 0.189503, 0.0003176581483209031, 0.668054, 0.861999, 0.196293, 0.0003293426684606342, 0.657642, 0.860219, 0.203082, 0.00034145383907972467, 0.647257, 0.8584, 0.209861, 0.0003540136436388228, 0.636902, 0.856542, 0.21662, 0.0003670320589557195, 0.626579, 0.854645, 0.223353, 0.0003805327152664863, 0.616293, 0.852709, 0.230052, 0.00039452997048836775, 0.606045, 0.850733, 0.236712, 0.00040903832377663996, 0.595839, 0.848717, 0.243329, 0.0004240841098122048, 0.585678, 0.846661, 0.249897, 0.0004396792801397769, 0.575563, 0.844566, 0.256415, 0.00045585214216447705, 0.565498, 0.84243, 0.262877, 0.0004726155427181821, 0.555484, 0.840254, 0.269281, 0.0004899999097065014, 0.545524, 0.838039, 0.275626, 0.0005080237313641418, 0.535621, 0.835785, 0.281908, 0.0005267056777935439, 0.525776, 0.833491, 0.288127, 0.0005460796593281597, 0.515992, 0.831158, 0.294279, 0.0005661610655931017, 0.506271, 0.828786, 0.300362, 0.0005869863471362382, 0.496615, 0.826376, 0.306377, 0.0006085720464155685, 0.487026, 0.823929, 0.312321, 0.000630957344480193, 0.477504, 0.821444, 0.318195, 0.0006541660480436306, 0.468053, 0.818921, 0.323998, 0.0006782221980047136, 0.458674, 0.816363, 0.329727, 0.000703169459624438, 0.449368, 0.813768, 0.335384, 0.0007290276496350139, 0.440137, 0.811138, 0.340967, 0.0007558437042509838, 0.430983, 0.808473, 0.346476, 0.0007836389246709061, 0.421908, 0.805774, 0.35191, 0.0008124637630891685, 0.412913, 0.803041, 0.357269, 0.0008423488746557926, 0.404001, 0.800275, 0.362552, 0.0008733252160738017, 0.395174, 0.797475, 0.367757, 0.0009054490137150345, 0.386433, 0.794644, 0.372886, 0.0009387457849571144, 0.377779, 0.791781, 0.377939, 0.0009732759680750312, 0.369214, 0.788888, 0.382914, 0.0010090669919466486, 0.360741, 0.785964, 0.387814, 0.0010461838222627017, 0.35236, 0.783011, 0.392636, 0.0010846659326877136, 0.344074, 0.780029, 0.397381, 0.001124553185186445, 0.335885, 0.777018, 0.402049, 0.0011659179806748194, 0.327796, 0.77398, 0.40664, 0.0012087931770707761, 0.319809, 0.770914, 0.411152, 0.0012532565988243544, 0.311925, 0.767822, 0.415586, 0.0012993435652317348, 0.304148, 0.764704, 0.419943, 0.001347137730552635, 0.296479, 0.761561, 0.424223, 0.0013966899237730418, 0.288921, 0.758394, 0.428426, 0.0014480514738808485, 0.281477, 0.755203, 0.432552, 0.0015013156092394528, 0.274149, 0.751988, 0.436601, 0.001556524639947771, 0.266941, 0.748751, 0.440573, 0.0016137787780820918, 0.259857, 0.745492, 0.444467, 0.0016731235031800335, 0.252899, 0.742211, 0.448284, 0.0017346665341789276, 0.24607, 0.73891, 0.452024, 0.0017984567574769405, 0.239374, 0.735588, 0.455688, 0.0018646099612094828, 0.232815, 0.732247, 0.459277, 0.0019331964991580889, 0.226397, 0.728888, 0.462789, 0.002004287417170523, 0.220124, 0.725509, 0.466226, 0.002078011755159426, 0.214, 0.722114, 0.469588, 0.002154428075683102, 0.20803, 0.718701, 0.472873, 0.00223367508500109, 0.202219, 0.715272, 0.476084, 0.0023158157325779863, 0.196571, 0.711827, 0.479221, 0.002400999115123798, 0.19109, 0.708366, 0.482284, 0.0024893158249718944, 0.185783, 0.704891, 0.485273, 0.0025808573456073815, 0.180653, 0.701402, 0.488189, 0.002675789837633556, 0.175707, 0.6979, 0.491033, 0.0027741887101995644, 0.170948, 0.694384, 0.493803, 0.002876232570957059, 0.166383, 0.690856, 0.496502, 0.002982002477935297, 0.162016, 0.687316, 0.499129, 0.003091690418239488, 0.157851, 0.683765, 0.501686, 0.0032054130447443786, 0.153894, 0.680203, 0.504172, 0.003323288157832546, 0.150148, 0.676631, 0.506589, 0.003445529717243444, 0.146616, 0.67305, 0.508936, 0.003572234824946998, 0.143303, 0.669459, 0.511215, 0.0037036334683520963, 0.14021, 0.665859, 0.513427, 0.0038398300233124425, 0.137339, 0.662252, 0.515571, 0.003981071705534973, 0.134692, 0.658636, 0.517649, 0.004127508725227115, 0.132268, 0.655014, 0.519661, 0.004279292770205737, 0.130067, 0.651384, 0.521608, 0.0044366993496420815, 0.128087, 0.647749, 0.523491, 0.004599853498663449, 0.126326, 0.644107, 0.525311, 0.004769051364762731, 0.12478, 0.640461, 0.527068, 0.004944427349416694, 0.123444, 0.636809, 0.528763, 0.005126299784451269, 0.122312, 0.633153, 0.530398, 0.005314862090786979, 0.12138, 0.629492, 0.531973, 0.0055103095920151675, 0.120638, 0.625828, 0.533488, 0.005712997052558486, 0.120081, 0.622161, 0.534946, 0.005923085476185147, 0.119699, 0.61849, 0.536347, 0.0061409562026301075, 0.119483, 0.614817, 0.537692, 0.006366782296412751, 0.119423, 0.611141, 0.538982, 0.006600973663330131, 0.119512, 0.607464, 0.540218, 0.006843779365367716, 0.119738, 0.603785, 0.5414, 0.0070954509145198215, 0.120092, 0.600104, 0.54253, 0.0073564451296829385, 0.120565, 0.596422, 0.543611, 0.007626969330303526, 0.121148, 0.592739, 0.544641, 0.007907514555464932, 0.121831, 0.589055, 0.545623, 0.008198303654860427, 0.122606, 0.585371, 0.546557, 0.008499864451185652, 0.123463, 0.581687, 0.547445, 0.008812517653660824, 0.124395, 0.578002, 0.548287, 0.009136587126304888, 0.125394, 0.574318, 0.549086, 0.009472661100323881, 0.126453, 0.570633, 0.549841, 0.009821006534394352, 0.127568, 0.566949, 0.550556, 0.010182255723971663, 0.128729, 0.563265, 0.551229, 0.010556695625538718, 0.129933, 0.559582, 0.551864, 0.01094500589964196, 0.131172, 0.555899, 0.552459, 0.011347494998601087, 0.132444, 0.552216, 0.553018, 0.011764893496160509, 0.133743, 0.548535, 0.553541, 0.012197645294671934, 0.135066, 0.544853, 0.554029, 0.012646198663129792, 0.136408, 0.541173, 0.554483, 0.013111367788340164, 0.13777, 0.537492, 0.554906, 0.013593522175065823, 0.139147, 0.533812, 0.555298, 0.014093537000638586, 0.140536, 0.530132, 0.555659, 0.01461180944932859, 0.141935, 0.526453, 0.555991, 0.015149280257778048, 0.143343, 0.522773, 0.556295, 0.01570652102496789, 0.144759, 0.519093, 0.556572, 0.01628410897266635, 0.14618, 0.515413, 0.556823, 0.016883092503403568, 0.147607, 0.511733, 0.557049, 0.01750394741674449, 0.149039, 0.508051, 0.55725, 0.01814780065078504, 0.150476, 0.504369, 0.55743, 0.0188151636471141, 0.151918, 0.500685, 0.557587, 0.019507247762472445, 0.153364, 0.497, 0.557724, 0.02022478902674083, 0.154815, 0.493313, 0.55784, 0.02096853071008498, 0.15627, 0.489624, 0.557936, 0.021739822807195136, 0.157729, 0.485932, 0.558013, 0.022539277990082273, 0.159194, 0.482237, 0.558073, 0.02336834738119408, 0.160665, 0.47854, 0.558115, 0.024227689547645363, 0.162142, 0.474838, 0.55814, 0.025118864315095794, 0.163625, 0.471133, 0.558148, 0.026042819445881295, 0.165117, 0.467423, 0.558141, 0.027000512025423036, 0.166617, 0.463708, 0.558119, 0.02799368039907167, 0.168126, 0.459988, 0.558082, 0.02902311348514615, 0.169646, 0.456262, 0.55803, 0.03009067984800333, 0.171176, 0.45253, 0.557965, 0.031197227503631964, 0.172719, 0.448791, 0.557885, 0.03234476499006758, 0.174274, 0.445044, 0.557792, 0.03353451271081398, 0.175841, 0.44129, 0.557685, 0.03476770307441629, 0.177423, 0.437527, 0.557565, 0.03604657449305472, 0.179019, 0.433756, 0.55743, 0.03737214283182987, 0.180629, 0.429975, 0.557282, 0.038746814181806664, 0.182256, 0.426184, 0.55712, 0.0401716805062809, 0.183898, 0.422383, 0.556944, 0.04164932813598471, 0.185556, 0.41857, 0.556753, 0.043181328545807585, 0.187231, 0.414746, 0.556547, 0.044769268669149834, 0.188923, 0.41091, 0.556326, 0.04641603083838996, 0.190631, 0.407061, 0.556089, 0.04812292315080188, 0.192357, 0.403199, 0.555836, 0.04989304385354627, 0.1941, 0.399323, 0.555565, 0.051727799033129955, 0.19586, 0.395433, 0.555276, 0.05363051902561692, 0.197636, 0.391528, 0.554969, 0.05560322736938655, 0.19943, 0.387607, 0.554642, 0.057647967508252615, 0.201239, 0.38367, 0.554294, 0.05976845093021186, 0.203063, 0.379716, 0.553925, 0.061966362030640834, 0.204903, 0.375746, 0.553533, 0.06424569032415418, 0.206756, 0.371758, 0.553117, 0.06660824638375586, 0.208623, 0.367752, 0.552675, 0.06905831857758145, 0.210503, 0.363727, 0.552206, 0.07159785310819614, 0.212395, 0.359683, 0.55171, 0.07423145958429729, 0.214298, 0.355619, 0.551184, 0.07696193884037532, 0.21621, 0.351535, 0.550627, 0.0797921192625734, 0.21813, 0.347432, 0.550038, 0.08272713802234251, 0.220057, 0.343307, 0.549413, 0.08576932653712158, 0.221989, 0.339161, 0.548752, 0.08892420680256266, 0.223925, 0.334994, 0.548053, 0.09219428488198968, 0.225863, 0.330805, 0.547314, 0.09558549642233861, 0.227802, 0.326594, 0.546532, 0.09910144796936059, 0.229739, 0.322361, 0.545706, 0.10274578154619642, 0.231674, 0.318106, 0.544834, 0.1065251121256097, 0.233603, 0.313828, 0.543914, 0.11044244179990048, 0.235526, 0.309527, 0.542944, 0.11450488106775258, 0.237441, 0.305202, 0.541921, 0.11871565690743377, 0.239346, 0.300855, 0.540844, 0.12308241246326801, 0.241237, 0.296485, 0.539709, 0.12760979176984555, 0.243113, 0.292092, 0.538516, 0.13230248454486593, 0.244972, 0.287675, 0.53726, 0.13716900867897777, 0.246811, 0.283237, 0.535941, 0.14221322987123172, 0.248629, 0.278775, 0.534556, 0.14744430408528889, 0.250425, 0.27429, 0.533103, 0.15286638659872862, 0.252194, 0.269783, 0.531579, 0.15848931924611143, 0.253935, 0.265254, 0.529983, 0.16431908200350392, 0.255645, 0.260703, 0.528312, 0.17036171367166436, 0.257322, 0.25613, 0.526563, 0.1766281824682549, 0.258965, 0.251537, 0.524736, 0.1831234661313511, 0.260571, 0.246922, 0.522828, 0.18985935450499858, 0.262138, 0.242286, 0.520837, 0.19684119820836066, 0.263663, 0.237631, 0.518762, 0.2040816702596896, 0.265145, 0.232956, 0.516599, 0.2115884708845249, 0.26658, 0.228262, 0.514349, 0.21936937605509546, 0.267968, 0.223549, 0.512008, 0.22743850919745265, 0.269308, 0.218818, 0.509577, 0.23580227998705855, 0.270595, 0.214069, 0.507052, 0.24447586983220218, 0.271828, 0.209303, 0.504434, 0.2534661685554973, 0.273006, 0.20452, 0.501721, 0.2627894948006513, 0.274128, 0.199721, 0.498911, 0.2724557639038951, 0.275191, 0.194905, 0.496005, 0.2824749887380711, 0.276194, 0.190074, 0.493001, 0.29286535559101273, 0.277134, 0.185228, 0.489898, 0.30363511799854387, 0.278012, 0.180367, 0.486697, 0.31480382457867406, 0.278826, 0.17549, 0.483397, 0.3263803471374877, 0.279574, 0.170599, 0.479997, 0.3383856986749779, 0.280255, 0.165693, 0.476498, 0.35083264685516563, 0.280868, 0.160771, 0.472899, 0.3637340849368756, 0.281412, 0.155834, 0.469201, 0.37711343082621196, 0.281887, 0.150881, 0.465405, 0.390981312339514, 0.28229, 0.145912, 0.46151, 0.40536290161225197, 0.282623, 0.140926, 0.457517, 0.4202696225877697, 0.282884, 0.13592, 0.453427, 0.43572853303978015, 0.283072, 0.130895, 0.449241, 0.4517519126763041, 0.283187, 0.125848, 0.44496, 0.46836884616197033, 0.283229, 0.120777, 0.440584, 0.48559700556770286, 0.283197, 0.11568, 0.436115, 0.5034542368036022, 0.283091, 0.110553, 0.431554, 0.5219729532302368, 0.28291, 0.105393, 0.426902, 0.5411678650971677, 0.282656, 0.100196, 0.42216, 0.5610738138415245, 0.282327, 0.094955, 0.417331, 0.5817066116539055, 0.281924, 0.089666, 0.412415, 0.6031037099345976, 0.281446, 0.08432, 0.407414, 0.6252878644488977, 0.280894, 0.078907, 0.402329, 0.6482820548093011, 0.280267, 0.073417, 0.397163, 0.672128018672295, 0.279566, 0.067836, 0.391917, 0.696844697959734, 0.278791, 0.062145, 0.386592, 0.722476956885295, 0.277941, 0.056324, 0.381191, 0.7490451563053616, 0.277018, 0.050344, 0.375715, 0.7765975212003939, 0.276022, 0.044167, 0.370164, 0.8051633534477213, 0.274952, 0.037752, 0.364543, 0.8347722431656047, 0.273809, 0.031497, 0.358853, 0.8654779346106837, 0.272594, 0.025563, 0.353093, 0.8973048186950362, 0.271305, 0.019942, 0.347269, 0.9303106656438385, 0.269944, 0.014625, 0.341379, 0.9645216934861647, 0.26851, 0.009605, 0.335427, 1.0, 0.267004, 0.004874, 0.329415]
tau_bLUT.UseLogScale = 1
tau_bLUT.NanColor = [1.0, 0.0, 0.0]
tau_bLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'tau_b'
tau_bPWF = GetOpacityTransferFunction('tau_b')
tau_bPWF.Points = [0.0001, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
tau_bPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
calculatoru_b_magDisplay.Representation = 'Surface'
calculatoru_b_magDisplay.ColorArrayName = ['POINTS', 'tau_b']
calculatoru_b_magDisplay.LookupTable = tau_bLUT
calculatoru_b_magDisplay.SelectTCoordArray = 'None'
calculatoru_b_magDisplay.SelectNormalArray = 'None'
calculatoru_b_magDisplay.SelectTangentArray = 'None'
calculatoru_b_magDisplay.OSPRayScaleArray = 'tau_b'
calculatoru_b_magDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
calculatoru_b_magDisplay.SelectOrientationVectors = 'velocity'
calculatoru_b_magDisplay.ScaleFactor = 78305.2202328
calculatoru_b_magDisplay.SelectScaleArray = 'tau_b'
calculatoru_b_magDisplay.GlyphType = 'Arrow'
calculatoru_b_magDisplay.GlyphTableIndexArray = 'tau_b'
calculatoru_b_magDisplay.GaussianRadius = 3915.26101164
calculatoru_b_magDisplay.SetScaleArray = ['POINTS', 'tau_b']
calculatoru_b_magDisplay.ScaleTransferFunction = 'PiecewiseFunction'
calculatoru_b_magDisplay.OpacityArray = ['POINTS', 'tau_b']
calculatoru_b_magDisplay.OpacityTransferFunction = 'PiecewiseFunction'
calculatoru_b_magDisplay.DataAxesGrid = 'GridAxesRepresentation'
calculatoru_b_magDisplay.PolarAxes = 'PolarAxesRepresentation'
calculatoru_b_magDisplay.ScalarOpacityFunction = tau_bPWF
calculatoru_b_magDisplay.ScalarOpacityUnitDistance = 23951.826940350908
calculatoru_b_magDisplay.OpacityArrayName = ['POINTS', 'tau_b']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
calculatoru_b_magDisplay.ScaleTransferFunction.Points = [1.512062715270901e-06, 0.0, 0.5, 0.0, 9.084874311865669, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
calculatoru_b_magDisplay.OpacityTransferFunction.Points = [1.512062715270901e-06, 0.0, 0.5, 0.0, 9.084874311865669, 1.0, 0.5, 0.0]

# show data from calculatortau_b
calculatortau_bDisplay = Show(calculatortau_b, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
calculatortau_bDisplay.Representation = 'Surface'
calculatortau_bDisplay.ColorArrayName = ['POINTS', 'tau_b']
calculatortau_bDisplay.LookupTable = tau_bLUT
calculatortau_bDisplay.SelectTCoordArray = 'None'
calculatortau_bDisplay.SelectNormalArray = 'None'
calculatortau_bDisplay.SelectTangentArray = 'None'
calculatortau_bDisplay.Scale = [1.0, 1.0, 0.0]
calculatortau_bDisplay.OSPRayScaleArray = 'tau_b'
calculatortau_bDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
calculatortau_bDisplay.SelectOrientationVectors = 'velocity'
calculatortau_bDisplay.ScaleFactor = 78305.2202328
calculatortau_bDisplay.SelectScaleArray = 'tau_b'
calculatortau_bDisplay.GlyphType = 'Arrow'
calculatortau_bDisplay.GlyphTableIndexArray = 'tau_b'
calculatortau_bDisplay.GaussianRadius = 3915.26101164
calculatortau_bDisplay.SetScaleArray = ['POINTS', 'tau_b']
calculatortau_bDisplay.ScaleTransferFunction = 'PiecewiseFunction'
calculatortau_bDisplay.OpacityArray = ['POINTS', 'tau_b']
calculatortau_bDisplay.OpacityTransferFunction = 'PiecewiseFunction'
calculatortau_bDisplay.DataAxesGrid = 'GridAxesRepresentation'
calculatortau_bDisplay.PolarAxes = 'PolarAxesRepresentation'
calculatortau_bDisplay.ScalarOpacityFunction = tau_bPWF
calculatortau_bDisplay.ScalarOpacityUnitDistance = 23951.826940350908
calculatortau_bDisplay.OpacityArrayName = ['POINTS', 'tau_b']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
calculatortau_bDisplay.ScaleTransferFunction.Points = [1.512062715270901e-06, 0.0, 0.5, 0.0, 9.084874311865669, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
calculatortau_bDisplay.OpacityTransferFunction.Points = [1.512062715270901e-06, 0.0, 0.5, 0.0, 9.084874311865669, 1.0, 0.5, 0.0]

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
calculatortau_bDisplay.PolarAxes.Scale = [1.0, 1.0, 0.0]

# show data from contouru_b_mag
contouru_b_magDisplay = Show(contouru_b_mag, renderView1, 'GeometryRepresentation')

# get color transfer function/color map for 'velocity'
velocityLUT = GetColorTransferFunction('velocity')
velocityLUT.RGBPoints = [0.011403976794966693, 0.231373, 0.298039, 0.752941, 2106.6925802016617, 0.865003, 0.865003, 0.865003, 4213.373756426528, 0.705882, 0.0156863, 0.14902]
velocityLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
contouru_b_magDisplay.Representation = 'Surface'
contouru_b_magDisplay.ColorArrayName = ['POINTS', 'velocity']
contouru_b_magDisplay.LookupTable = velocityLUT
contouru_b_magDisplay.LineWidth = 2.0
contouru_b_magDisplay.SelectTCoordArray = 'None'
contouru_b_magDisplay.SelectNormalArray = 'None'
contouru_b_magDisplay.SelectTangentArray = 'None'
contouru_b_magDisplay.Scale = [1.0, 1.0, 0.0]
contouru_b_magDisplay.OSPRayScaleArray = 'tau_b'
contouru_b_magDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
contouru_b_magDisplay.SelectOrientationVectors = 'velocity'
contouru_b_magDisplay.ScaleFactor = 8274.669639047162
contouru_b_magDisplay.SelectScaleArray = 'tau_b'
contouru_b_magDisplay.GlyphType = 'Arrow'
contouru_b_magDisplay.GlyphTableIndexArray = 'tau_b'
contouru_b_magDisplay.GaussianRadius = 413.73348195235815
contouru_b_magDisplay.SetScaleArray = ['POINTS', 'tau_b']
contouru_b_magDisplay.ScaleTransferFunction = 'PiecewiseFunction'
contouru_b_magDisplay.OpacityArray = ['POINTS', 'tau_b']
contouru_b_magDisplay.OpacityTransferFunction = 'PiecewiseFunction'
contouru_b_magDisplay.DataAxesGrid = 'GridAxesRepresentation'
contouru_b_magDisplay.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
contouru_b_magDisplay.ScaleTransferFunction.Points = [4.542437911964192, 0.0, 0.5, 0.0, 4.54341459274292, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
contouru_b_magDisplay.OpacityTransferFunction.Points = [4.542437911964192, 0.0, 0.5, 0.0, 4.54341459274292, 1.0, 0.5, 0.0]

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
contouru_b_magDisplay.PolarAxes.Scale = [1.0, 1.0, 0.0]

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

# get color legend/bar for tau_bLUT in view renderView1
tau_bLUTColorBar = GetScalarBar(tau_bLUT, renderView1)
tau_bLUTColorBar.AutoOrient = 0
tau_bLUTColorBar.Orientation = 'Horizontal'
tau_bLUTColorBar.WindowLocation = 'Any Location'
tau_bLUTColorBar.Position = [0.6789898989898986, 0.014615384615384811]
tau_bLUTColorBar.Title = 'Basal resistance, Mpa'
tau_bLUTColorBar.ComponentTitle = ''
tau_bLUTColorBar.TitleColor = [0.0, 0.0, 0.0]
tau_bLUTColorBar.TitleBold = 1
tau_bLUTColorBar.LabelColor = [0.0, 0.0, 0.0]
tau_bLUTColorBar.LabelBold = 1
tau_bLUTColorBar.LabelFormat = '%-#6.1f'
tau_bLUTColorBar.UseCustomLabels = 1
tau_bLUTColorBar.CustomLabels = [0.001, 0.01, 0.1]
tau_bLUTColorBar.RangeLabelFormat = '%-#6.1f'
tau_bLUTColorBar.ScalarBarThickness = 15
tau_bLUTColorBar.ScalarBarLength = 0.29404040404040477

# set color bar visibility
tau_bLUTColorBar.Visibility = 1

# get color legend/bar for velocityLUT in view renderView1
velocityLUTColorBar = GetScalarBar(velocityLUT, renderView1)
velocityLUTColorBar.WindowLocation = 'Upper Right Corner'
velocityLUTColorBar.Position = [0.8970959595959596, 0.5942928039702233]
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

# set color bar visibility
velocityLUTColorBar.Visibility = 0

# hide data in view
Hide(pig_s4_l4_i_t0016pvtu, renderView1)

# hide data in view
Hide(thresholdgroundedarea, renderView1)

# show color legend
calculatoru_b_magDisplay.SetScalarBarVisibility(renderView1, True)

# hide data in view
Hide(calculatoru_b_mag, renderView1)

# show color legend
calculatortau_bDisplay.SetScalarBarVisibility(renderView1, True)

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get opacity transfer function/opacity map for 'velocity'
velocityPWF = GetOpacityTransferFunction('velocity')
velocityPWF.Points = [0.011403976794966693, 0.0, 0.5, 0.0, 4213.373756426528, 1.0, 0.5, 0.0]
velocityPWF.ScalarRangeInitialized = 1

# ----------------------------------------------------------------
# restore active source
SetActiveSource(calculatortau_b)
# ----------------------------------------------------------------


if __name__ == '__main__':
    # generate extracts
    SaveExtracts(ExtractsOutputDirectory='extracts')
