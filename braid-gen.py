import maya.cmds as cmds

leftStrand = cmds.curve(p=[(-1,0,-0.125),(-0.875,0,-0.25),(-0.75,0,-0.25),(-0.625,0.03,-0.25),(-0.5,0,-0.125),(-0.375,-0.03,0),(-0.25,0,0),(-0.125,0.03,0),(0,0,-0.125),(0.125,-0.03,-0.25),(0.25,0,-0.25),(0.375,0.03,-0.25),(0.5,0,-0.125),(0.625,-0.03,0),(0.75,0,0),(0.875,0.03,0),(1,0,-0.125)], k=[0,0,0,1,2,3,4,5,6,6,6,7,8,9,10,11,12,12,12], name='leftStrand')
cmds.rotate(0,0,-90,leftStrand)
cmds.move(-0.0072805614748225056,0.62530322953737649,0.12630761389650735,leftStrand)

for i in xrange (0,10):
    copyLS = cmds.duplicate('leftStrand', name=leftStrand + '_copy#')
    copyName = 'leftStrand_copy'+str(i+1)
    #move left chunks out toward left
    cmds.move(0,0,i*0.01, copyName+'.cv[5:7]', relative=True)
    cmds.move(0,0,i*0.01, copyName+'.cv[13:15]', relative=True)
    #move right chunks toward right
    cmds.move(0,0,i*-0.01, copyName+'.cv[1:3]', relative=True)
    cmds.move(0,0,i*-0.01, copyName+'.cv[9:11]', relative=True)
    '''
'''
#fill middle
for i in xrange (0,10):
    copyLS = cmds.duplicate('leftStrand', name=leftStrand + '_copy#')
    copyName = 'leftStrand_copy'+str(i+11)
    cmds.move(0,0,i*0.01, copyName, relative=True)
for i in xrange (0,10):
    copyLS = cmds.duplicate('leftStrand', name=leftStrand + '_copy#')
    copyName = 'leftStrand_copy'+str(i+21)
    cmds.move(0,0,i*-0.01, copyName, relative=True)
    
middleStrand = cmds.curve(p=[(-1,0,-0.125),(-0.875,-0.03,-0.25),(-0.75,0,-0.25),(-0.625,0.03,-0.25),(-0.5,0,-0.125),(-0.375,-0.03,0),(-0.25,0,0),(-0.125,0.03,0),(0,0,-0.125),(0.125,-0.03,-0.25),(0.25,0,-0.25),(0.375,0.03,-0.25),(0.5,0,-0.125),(0.625,-0.03,0),(0.75,0,0),(0.875,0.03,0),(1,0,-0.125)], k=[0,0,0,1,2,3,4,5,6,6,6,7,8,9,10,11,12,12,12], name='middleStrand')
cmds.rotate(0,0,-90,middleStrand)
cmds.move(-0.0072805614748224301,0.28597074587880578,0.12123025620918559)

for i in xrange (0,10):
    copyMS = cmds.duplicate('middleStrand', name=middleStrand + '_copy#')
    copyName = 'middleStrand_copy'+str(i+1)
    #move out toward left
    cmds.move(0,0,i*0.01, copyName+'.cv[5:7]', relative=True)
    cmds.move(0,0,i*0.01, copyName+'.cv[13:15]', relative=True)
    #move right chunks toward right
    cmds.move(0,0,i*-0.01, copyName+'.cv[1:3]', relative=True)
    cmds.move(0,0,i*-0.01, copyName+'.cv[9:11]', relative=True)
#fill middle
for i in xrange (0,10):
    copyMS = cmds.duplicate('middleStrand', name=middleStrand + '_copy#')
    copyName = 'middleStrand_copy'+str(i+11)
    cmds.move(0,0,i*0.01, copyName, relative=True)
for i in xrange (0,10):
    copyMS = cmds.duplicate('middleStrand', name=middleStrand + '_copy#')
    copyName = 'middleStrand_copy'+str(i+21)
    cmds.move(0,0,i*-0.01, copyName, relative=True)


rightStrand = cmds.curve(p=[(0,0,-0.125),(-0.125,0,0),(-0.25,0,0),(-0.375,-0.03,0),(-0.5,0,-0.125),(-0.625,0.03,-0.25),(-0.75,0,-0.25),(-0.875,-0.03,-0.25),(-1,0,-0.125),(-1.125,0.03,0),(-1.25,0,0),(-1.375,-0.03,0),(-1.5,0,-0.125),(-1.625,0.03,-0.25),(-1.75,0,-0.25),(-1.875,-0.03,-0.25),(-2,0,-0.125)], k=[0,0,0,1,2,3,4,5,6,6,6,7,8,9,10,11,12,12,12], name='rightStrand')
cmds.rotate(0,0,-90,rightStrand)
cmds.move(0,-1.0353652835420843,0.12560945545540347)

for i in xrange (0,10):
    copyRS = cmds.duplicate('rightStrand', name=rightStrand + '_copy#')
    copyName = 'rightStrand_copy'+str(i+1)
    #move toward left
    cmds.move(0,0,i*0.01, copyName+'.cv[1:3]', relative=True)
    cmds.move(0,0,i*0.01, copyName+'.cv[9:11]', relative=True)
    #move out toward right
    cmds.move(0,0,i*-0.01, copyName+'.cv[5:7]', relative=True)
    cmds.move(0,0,i*-0.01, copyName+'.cv[13:15]', relative=True)

#fill middle
for i in xrange (0,10):
    copyRS = cmds.duplicate('rightStrand', name=rightStrand + '_copy#')
    copyName = 'rightStrand_copy'+str(i+11)
    cmds.move(0,0,i*0.01, copyName, relative=True)
for i in xrange (0,10):
    copyRS = cmds.duplicate('rightStrand', name=rightStrand + '_copy#')
    copyName = 'rightStrand_copy'+str(i+21)
    cmds.move(0,0,i*-0.01, copyName, relative=True)