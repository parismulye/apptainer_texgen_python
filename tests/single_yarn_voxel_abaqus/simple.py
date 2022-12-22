from TexGen.Core import *

textile = CTextile( )
yarn = CYarn( )
yarn.AddNode( CNode(XYZ(0, 0.0, 0)) )
yarn.AddNode( CNode(XYZ(1, 3.5, 0)) )
yarn.AddNode( CNode(XYZ(0, 7.0, 0)) )

# Add repeats
yarn.AddRepeat( XYZ(3, 0, 0) )
yarn.AddRepeat( XYZ(0, 7, 0) )
yarn.AddRepeat( XYZ(0.5, 0, 1) )
textile.AddYarn(yarn)
# Assign a domain using a min/max box
textile.AssignDomain(CDomainPlanes(XYZ(-0.5, 0, -0.5), XYZ(1.5, 7, 0.5)))
# AddTextile is not required if don't need to visualise yarns
AddTextile( "SingleYarn", textile)
#create a voxel mesh with the default boundaries 'CPeriodicBoundaries'
VoxMesh = CRectangularVoxelMesh()
vx=20
vy=50
vz=20
VoxMesh.SaveVoxelMesh(textile, "test_out.inp", vx, vy, vz, False, True,
MATERIAL_CONTINUUM, 0 )