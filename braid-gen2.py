import maya.cmds as cmds
import math

#Radius of each hair chunk
r = 0.05
#Number of strands on outermost circle on each section's cross section
range = 10
#Number of times to append braid to bottom
append = 0
#Keep track of number of strands in each section
counter1 = 1
counter2 = 1
counter3 = 1
#Helps determine spacing between woven s$ections
weave = r + 0.035




leftStrand = cmds.curve(p=[(-1,0,-0.125),(-0.875,0,-0.25),(-0.75,0,-0.25),(-0.625,weave,-0.25),(-0.5,0,-0.125),(-0.375,-weave,0),(-0.25,0,0),(-0.125,weave,0),(0,0,-0.125),(0.125,-weave,-0.25),(0.25,0,-0.25),(0.375,weave,-0.25),(0.5,0,-0.125),(0.625,-weave,0),(0.75,0,0),(0.875,weave,0),(1,0,-0.125)], k=[0,0,0,1,2,3,4,5,6,6,6,7,8,9,10,11,12,12,12], name='leftStrand')
lsTemplate = cmds.duplicate('leftStrand', name='lsTemplate')

#Append length if necessary
cutbottom = 12
for i in xrange(0,append):
    toAppend = cmds.duplicate('lsTemplate', name='leftStrand2')
    cmds.move(2*(i+1),0,0,'leftStrand2', relative=True)
    cmds.attachCurve('leftStrand','leftStrand2')
    cmds.delete('leftStrand2')
    cutbottom = 12*(i+2) - 6*(i+1)

#Cut bottom
cmds.detachCurve('leftStrand.u['+str(cutbottom)+']', k=(1,0), replaceOriginal=True)
cmds.delete('leftStranddetachedCurve2')

cmds.rotate(0,0,-90,leftStrand)
cmds.move(-0.0072805614748225056,0.62530322953737649,0.12630761389650735,leftStrand, relative=True)

#Create tubes of curves around original
theta = 0
while theta <= 360:
    copyLS = cmds.duplicate('leftStrand', name=leftStrand + '_copy#')
    copyName = 'leftStrand_copy'+str(counter1)
    x = r*math.cos(theta)
    z = r*math.sin(theta)
    cmds.move(x,0,z-r, copyName, relative=True)
    theta += (360/range)
    counter1 += 1
    
   
    

middleStrand = cmds.curve(p=[(-1,0,-0.125),(-0.875,-weave,-0.25),(-0.75,0,-0.25),(-0.625,weave,-0.25),(-0.5,0,-0.125),(-0.375,-weave,0),(-0.25,0,0),(-0.125,weave,0),(0,0,-0.125),(0.125,-weave,-0.25),(0.25,0,-0.25),(0.375,weave,-0.25),(0.5,0,-0.125),(0.625,-weave,0),(0.75,0,0),(0.875,weave,0),(1,0,-0.125)], k=[0,0,0,1,2,3,4,5,6,6,6,7,8,9,10,11,12,12,12], name='middleStrand')
msTemplate = cmds.duplicate('middleStrand', name='msTemplate')

#Add length to top
appendMSTop = cmds.duplicate('msTemplate', name='middleStrand2')
cmds.move(-2,0,0,'middleStrand2', relative=True)
cmds.attachCurve('middleStrand','middleStrand2')
cmds.delete('middleStrand2')
if append == 0:
    cmds.reverseCurve('middleStrand', rpo=True)
    

#Append length if necessary
cutbottom = 24 - 1.71725261027258
for i in xrange(0,append):
    toAppend = cmds.duplicate('msTemplate', name='middleStrand2')
    cmds.move(2*(i+1),0,0,'middleStrand2', relative=True)
    cmds.attachCurve('middleStrand','middleStrand2')
    cmds.delete('middleStrand2')
    cutbottom = (24+12*(i+1)) - 1.71725261027258 - 6*(i+1)

#Cut top
cmds.detachCurve('middleStrand.u[10.2827459692]', k=(0,1), replaceOriginal=True)
cmds.delete('middleStrand')
cmds.rename('middleStranddetachedCurve2', 'middleStrand')

#Cut bottom
cmds.detachCurve('middleStrand.u['+str(cutbottom)+']', k=(1,0), replaceOriginal=True)
cmds.delete('middleStranddetachedCurve2')

cmds.rotate(0,0,-90,middleStrand)
cmds.move(-0.0072805614748224301,0.28597074587880578,0.12123025620918559, middleStrand, relative=True)

theta = 0
while theta <= 360:
    copyMS = cmds.duplicate('middleStrand', name=middleStrand + '_copy#')
    copyName = 'middleStrand_copy'+str(counter2)
    x = r*math.cos(theta)
    z = r*math.sin(theta)
    cmds.move(x,0,z-r, copyName, relative=True)
    theta += (360/range)
    counter2 += 1
    
   
   


rightStrand = cmds.curve(p=[(0,0,-0.125),(-0.125,0,0),(-0.25,0,0),(-0.375,-weave,0),(-0.5,0,-0.125),(-0.625,weave,-0.25),(-0.75,0,-0.25),(-0.875,-weave,-0.25),(-1,0,-0.125),(-1.125,weave,0),(-1.25,0,0),(-1.375,-weave,0),(-1.5,0,-0.125),(-1.625,weave,-0.25),(-1.75,0,-0.25),(-1.875,-weave,-0.25),(-2,0,-0.125)], k=[0,0,0,1,2,3,4,5,6,6,6,7,8,9,10,11,12,12,12], name='rightStrand')
rsTemplate = cmds.duplicate('rightStrand', name='rsTemplate')

#Add length to top
appendRSTop = cmds.duplicate('rsTemplate', name='rightStrand2')
cmds.move(-2,0,0,'rightStrand2', relative=True)
cmds.attachCurve('rightStrand','rightStrand2')
cmds.delete('rightStrand2')
if append == 0:
    cmds.reverseCurve('rightStrand', rpo=True)

#Append length if necessary
cutbottom = 24 - 4.27956282558987
for i in xrange(0,append):
    toAppend = cmds.duplicate('rsTemplate', name='rightStrand2')
    cmds.move(2*(i+1),0,0,'rightStrand2', relative=True)
    cmds.attachCurve('rightStrand','rightStrand2')
    cmds.delete('rightStrand2')
    cutbottom = (24+12*(i+1)) - 4.27956282558987 - 6*(i+1)
    
#Cut top
cmds.detachCurve('rightStrand.u[7.72117911584729]', k=(0,1), replaceOriginal=True)
cmds.delete('rightStrand')
cmds.rename('rightStranddetachedCurve2', 'rightStrand')

#Cut bottom
cmds.detachCurve('rightStrand.u['+str(cutbottom)+']', k=(1,0), replaceOriginal=True)
cmds.delete('rightStranddetachedCurve2')

cmds.rotate(0,0,-90,rightStrand)
cmds.move(0,-1.0353652835420843,0.12560945545540347, rightStrand, relative=True)

theta = 0
while theta <= 360:
    copyRS = cmds.duplicate('rightStrand', name=rightStrand + '_copy#')
    copyName = 'rightStrand_copy'+str(counter3)
    x = r*math.cos(theta)
    z = r*math.sin(theta)
    cmds.move(x,0,z-r, copyName, relative=True)
    theta += (360/range)
    counter3 += 1
    

cmds.delete(lsTemplate)
cmds.delete(msTemplate)
cmds.delete(rsTemplate)