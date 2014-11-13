"""
    Create 3-strand hair braid in Maya

    Michelle Lee
    5-26-14
"""

import maya.cmds as cmds
import math

#Radius of each hair section
radius = 0.07
#Number of strands on outer boundary on each hair section's cross section
range = 10
#Number of times to append to braid length (adds to bottom)
append = 1
#Keep track of number of strands in each section
counter1 = 1
counter2 = 1
counter3 = 1
#Helps determine spacing between woven sections
#weave = radius + 0.035


"""
    Build left hair section
"""

#Start with template curve
leftStrand = cmds.curve(p=[(-1,0,-0.125),(-0.9375,-0.0875,-0.1875),(-0.84375,-0.06375,-0.26),(-0.7578125,-0.0053125,-0.275),(-0.6875,0.0425,-0.26),(-0.625,0.06375,-0.234375),(-0.5625,0.0425,-0.1875),(-0.5,0,-0.125),(-0.4375,-0.0875221,-0.0625),(-0.375,-0.06375,-0.015625),(-0.3125,-0.0425,0),(-0.2421875,0.0053125,0),(-0.15625,0.06375,0),(-0.0625,0.0425,-0.0625),(0,0,-0.125),(0.0625,-0.08752214296547417,-0.1875),(0.15625,-0.06375,-0.26),(0.2421875,-0.0053125,-0.275),(0.3125,0.0425,-0.26),(0.375,0.06375,-0.234375),(0.4375,0.0425,-0.1875),(0.5,0,-0.125),(0.5625,-0.0875221,-0.0625),(0.625,-0.06375,-0.015625),(0.6875,-0.0425,0),(0.7578125,0.0053125,0),(0.84375,0.06375,0),(0.9375,0.0425,-0.0625),(1,0,-0.125)], k=[0,0,0,0.5,1,1.5,2,2.5,3,3.5,4,4.5,5,5.5,6,6,6,6.5,7,7.5,8,8.5,9,9.5,10,10.5,11,11.5,12,12,12], name='leftStrand')
lsTemplate = cmds.duplicate('leftStrand', name='lsTemplate')

#Append length if necessary
cutbottom = 12 #Curve point at which to detach curve
for i in xrange(0, append):
    toAppend = cmds.duplicate('lsTemplate', name='leftStrand2')
    cmds.move(2*(i+1),0,0,'leftStrand2', relative=True)
    cmds.attachCurve('leftStrand', 'leftStrand2')
    cmds.delete('leftStrand2')
    cutbottom = 12*(i+2) - 6*(i+1)

#Cut bottom of curve
cmds.detachCurve('leftStrand.u['+str(cutbottom)+']', k=(1,0), replaceOriginal=True)
cmds.delete('leftStranddetachedCurve2')

#Position strand upright, set color to red
cmds.rotate(0, 0, -90, leftStrand)
cmds.move(-0.0072805614748225056, 0.62530322953737649, 0.12630761389650735, leftStrand, relative=True)
cmds.setAttr(leftStrand+'.overrideEnabled', 1)
cmds.setAttr(leftStrand+'.overrideColor', 4)

#Duplicate curves concentrically around template
r = radius
while r > 0:
    theta = 0
    while theta <= 360:
        copyLS = cmds.duplicate('leftStrand', name=leftStrand+'_copy#')
        copyName = 'leftStrand_copy'+str(counter1)
        cmds.setAttr(copyName+'.overrideEnabled', 1)
        cmds.setAttr(copyName+'.overrideColor', 4)
        x = r*math.cos(theta)
        z = r*math.sin(theta)
        cmds.move(x, 0, z-radius, copyName, relative=True)
        theta += (360/range)
        counter1 += 1
    r = r-(radius/4.0)

leftSection = cmds.group('leftStrand*', name='leftSection')
cmds.delete(lsTemplate)


"""
    Build middle hair section
"""

#Start with template curve
middleStrand = cmds.curve(p=[(-1,0,-0.125),(-0.9375,-0.0875,-0.1875),(-0.84375,-0.06375,-0.26),(-0.7578125,-0.0053125,-0.275),(-0.6875,0.0425,-0.26),(-0.625,0.06375,-0.234375),(-0.5625,0.0425,-0.1875),(-0.5,0,-0.125),(-0.4375,-0.0875221,-0.0625),(-0.375,-0.06375,-0.015625),(-0.3125,-0.0425,0),(-0.2421875,0.0053125,0),(-0.15625,0.06375,0),(-0.0625,0.0425,-0.0625),(0,0,-0.125),(0.0625,-0.08752214296547417,-0.1875),(0.15625,-0.06375,-0.26),(0.2421875,-0.0053125,-0.275),(0.3125,0.0425,-0.26),(0.375,0.06375,-0.234375),(0.4375,0.0425,-0.1875),(0.5,0,-0.125),(0.5625,-0.0875221,-0.0625),(0.625,-0.06375,-0.015625),(0.6875,-0.0425,0),(0.7578125,0.0053125,0),(0.84375,0.06375,0),(0.9375,0.0425,-0.0625),(1,0,-0.125)], k=[0,0,0,0.5,1,1.5,2,2.5,3,3.5,4,4.5,5,5.5,6,6,6,6.5,7,7.5,8,8.5,9,9.5,10,10.5,11,11.5,12,12,12], name='middleStrand')
msTemplate = cmds.duplicate('middleStrand', name='msTemplate')

#Add length to top
appendMSTop = cmds.duplicate('msTemplate', name='middleStrand2')
cmds.move(-2,0,0,'middleStrand2', relative=True)
cmds.attachCurve('middleStrand', 'middleStrand2')
cmds.delete('middleStrand2')
if append == 0:
    cmds.reverseCurve('middleStrand', rpo=True)
    
#Append length if necessary
cutbottom = 24 - 1.71725261027258 #Curve point at which to detach curve
for i in xrange(0, append):
    toAppend = cmds.duplicate('msTemplate', name='middleStrand2')
    cmds.move(2*(i+1),0,0,'middleStrand2', relative=True)
    cmds.attachCurve('middleStrand','middleStrand2')
    cmds.delete('middleStrand2')
    cutbottom = (24+12*(i+1)) - 1.71725261027258 - 6*(i+1)

#Cut top of curve
cmds.detachCurve('middleStrand.u[10.2827459692]', k=(0,1), replaceOriginal=True)
cmds.delete('middleStrand')
cmds.rename('middleStranddetachedCurve2', 'middleStrand')

#Cut bottom of curve
cmds.detachCurve('middleStrand.u['+str(cutbottom)+']', k=(1,0), replaceOriginal=True)
cmds.delete('middleStranddetachedCurve2')

#Position upright, set color to blue
cmds.rotate(0, 0, -90, middleStrand)
cmds.move(-0.0072805614748224301, 0.28597074587880578, 0.12123025620918559, middleStrand, relative=True)
cmds.setAttr(middleStrand+'.overrideEnabled', 1)
cmds.setAttr(middleStrand+'.overrideColor', 5)

#Duplicate curves concentrically around template
r = radius
while r > 0:
    theta = 0
    while theta <= 360:
        copyMS = cmds.duplicate('middleStrand', name=middleStrand+'_copy#')
        copyName = 'middleStrand_copy'+str(counter2)
        cmds.setAttr(copyName+'.overrideEnabled',1)
        cmds.setAttr(copyName+'.overrideColor', 5)  
        x = r*math.cos(theta)    
        z = r*math.sin(theta)
        cmds.move(x, 0, z-radius, copyName, relative=True)  
        theta += (360/range)
        counter2 += 1
    r = r-(radius/4.0)

middleSection = cmds.group('middleStrand*', name='middleSection')
cmds.delete(msTemplate)


"""
    Build right hair section
"""

#Start with template curve
rightStrand = cmds.curve(p=[(0,0,-0.125),( -0.0625,0.0425,-0.062),( -0.15625,0.06375,0),( -0.242188,0.0053125,0),(-0.3125,-0.0425,0),(-0.375,-0.06375,-0.015625),(-0.4375,-0.0875221,-0.0625),(-0.5,0,-0.125),(-0.5625,0.0425,-0.1875),(-0.625,0.06375,-0.234375),(-0.6875,0.0425,-0.26),(-0.7578125,-0.0053125,-0.275),(-0.84375,-0.06375,-0.26),(-0.9375,-0.08752214296547417,-0.1875),(-1,0,-0.125),(-1.0625,0.0425,-0.0625),(-1.15625,0.06375,0),(-1.2421875,0.0053125,0),(-1.3125,-0.0425,0),(-1.375,-0.06375,-0.015625),(-1.4375,-0.0875221,-0.0625),(-1.5,0,-0.125),(-1.5625,0.0425,-0.1875),(-1.625,0.06375,-0.234375),(-1.6875,0.0425,-0.26),(-1.7578125,-0.0053125,-0.275),(-1.84375,-0.06375,-0.26),(-1.9375,-0.08752214296547417,-0.1875),(-2,0,-0.125)], k=[0,0,0,0.5,1,1.5,2,2.5,3,3.5,4,4.5,5,5.5,6,6,6,6.5,7,7.5,8,8.5,9,9.5,10,10.5,11,11.5,12,12,12], name='rightStrand')
rsTemplate = cmds.duplicate('rightStrand', name='rsTemplate')

#Add length to top
appendRSTop = cmds.duplicate('rsTemplate', name='rightStrand2')
cmds.move(-2,0,0,'rightStrand2', relative=True)
cmds.attachCurve('rightStrand', 'rightStrand2')
cmds.delete('rightStrand2')
if append == 0:
    cmds.reverseCurve('rightStrand', rpo=True)

#Append length if necessary
cutbottom = 24 - 4.27956282558987
for i in xrange(0, append):
    toAppend = cmds.duplicate('rsTemplate', name='rightStrand2')
    cmds.move(2*(i+1), 0, 0, 'rightStrand2', relative=True)
    cmds.attachCurve('rightStrand', 'rightStrand2')
    cmds.delete('rightStrand2')
    cutbottom = (24+12*(i+1)) - 4.27956282558987 - 6*(i+1)
    
#Cut top of curve
cmds.detachCurve('rightStrand.u[7.72117911584729]', k=(0,1), replaceOriginal=True)
cmds.delete('rightStrand')
cmds.rename('rightStranddetachedCurve2', 'rightStrand')

#Cut bottom of curve
cmds.detachCurve('rightStrand.u['+str(cutbottom)+']', k=(1,0), replaceOriginal=True)
cmds.delete('rightStranddetachedCurve2')

#Position upright, set color to green
cmds.rotate(0, 0, -90, rightStrand)
cmds.move(0, -1.0353652835420843, 0.12560945545540347, rightStrand, relative=True)
cmds.setAttr(rightStrand+'.overrideEnabled', 1)
cmds.setAttr(rightStrand+'.overrideColor', 7)

#Duplicate curves concentrically around template
r = radius
while r > 0:
    theta = 0    
    while theta <= 360:
        copyRS = cmds.duplicate('rightStrand', name=rightStrand+'_copy#')
        copyName = 'rightStrand_copy'+str(counter3)
        cmds.setAttr(copyName+'.overrideEnabled', 1)
        cmds.setAttr(copyName+'.overrideColor', 7)  
        x = r*math.cos(theta)
        z = r*math.sin(theta)
        cmds.move(x, 0, z-radius, copyName, relative=True)    
        theta += (360/range)    
        counter3 += 1
    r = r-(radius/4.0)

rightSection = cmds.group('rightStrand*', name='rightSection')
cmds.delete(rsTemplate)
cmds.select(clear=True)