#Create ply file for hair braid

import maya.cmds as cmds
#make sure you rebuild all curves to linear, then select them all

numCVs = 150

print '''ply
format ascii 1.0
comment created by Michelle
element vertex '''+str(len(allCurves)*numCVs)+'''
property float x
property float y
property float z
property int segment
element face 0
property list int int vertex_indices
end_header'''

allCurves = cmds.ls(selection=True)
for i in xrange(0,len(allCurves)):
    #print allCurves[i]
    #print len(allCurves)*numCVs
    for j in xrange(0,numCVs):
        result = cmds.pointPosition(allCurves[i]+'.cv['+str(j)+']', w=True)
        print str(result[0])+' '+str(result[1])+' '+str(result[2])+' '+str(i)