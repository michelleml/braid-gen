import maya.cmds as cmds
#make sure you rebuild all curves to linear, then select them all

allCurves = cmds.ls(selection=True)
for i in xrange(0,len(allCurves)):
    #print allCurves[i]
    #print len(allCurves)*150
    for j in xrange(0,150):
        result = cmds.pointPosition(allCurves[i]+'.cv['+str(j)+']', w=True)
        print str(result[0])+' '+str(result[1])+' '+str(result[2])+' '+str(i)