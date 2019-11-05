#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.84.2), 2017_03_14_1129
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, core, data, event, logging, sound, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'aqv'  # from the Builder filename that created this script
expInfo = {u'session': u'001', u'participant': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)
#save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(size=(1440, 900), fullscr=True, screen=0, allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[-1, -1, -1], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    )
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
title = visual.TextStim(win=win, ori=0, name='title',
    text=u'Avalia\xe7\xe3o de Qualidade Visual',    font=u'Times New Roman',
    pos=(0, 0.8), height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)
question = visual.TextStim(win=win, ori=0, name='question',
    text=u'H\xe1 alguma informa\xe7\xe3o indispens\xe1vel ao diagn\xf3stico na imagem de refer\xeancia que est\xe1 ausente na imagem de teste?',    font=u'Times New Roman',
    pos=(0, 0), height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-1.0)
answer = visual.TextStim(win=win, ori=0, name='answer',
    text=u'Se sim, selecione 1. Caso contr\xe1rio, selecione 0.',    font=u'Times New Roman',
    pos=(0, -0.4), height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-2.0)
goon = visual.TextStim(win=win, ori=0, name='goon',
    text=u'Aperte qualquer tecla para continuar...;',    font=u'Times New Roman',
    pos=(0, -0.9), height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-4.0)

# Initialize components for Routine "trial"
trialClock = core.Clock()
image = visual.ImageStim(win=win, name='image',units='pix', 
    image='sin', mask=None,
    ori=0, pos=(-325, 0), size=(512, 512),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
image_2 = visual.ImageStim(win=win, name='image_2',units='pix', 
    image='sin', mask=None,
    ori=0, pos=(325, 0), size=(512, 512),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
text = visual.TextStim(win=win, ori=0, name='text',
    text='Imagem de Teste',    font='Times New Roman',
    pos=(0.45, 0.8), height=0.08, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0)
text_2 = visual.TextStim(win=win, ori=0, name='text_2',
    text=u'Imagem de refer\xeancia',    font='Times New Roman',
    pos=(-0.45, 0.8), height=0.08, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0)
rating_2 = visual.RatingScale(win=win, name='rating_2', marker='triangle', size=1.0, pos=[0.0, -0.7], low=0, high=1, labels=[''], scale='')
text_3 = visual.TextStim(win=win, ori=0, name='text_3',
    text='Fase de teste',    font='Times New Roman',
    pos=(0, 0.9), height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-5.0)

# Initialize components for Routine "lets"
letsClock = core.Clock()
text_4 = visual.TextStim(win=win, ori=0, name='text_4',
    text=u'Aperte qualquer tecla para come\xe7ar o experimento...',    font=u'Times New Roman',
    pos=(0, 0), height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-1.0)

# Initialize components for Routine "experiment"
experimentClock = core.Clock()
image_ref = visual.ImageStim(win=win, name='image_ref',units='pix', 
    image='sin', mask=None,
    ori=0, pos=(-325, 0), size=(512, 512),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
image_test = visual.ImageStim(win=win, name='image_test',units='pix', 
    image='sin', mask=None,
    ori=0, pos=(325, 0), size=(512, 512),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
rating = visual.RatingScale(win=win, name='rating', marker='triangle', size=1.0, pos=[0.0, -0.7], low='0', high='1', labels=[''], scale='')
label_ref = visual.TextStim(win=win, ori=0, name='label_ref',
    text=u'Imagem de Refer\xeancia',    font=u'Times New Roman',
    pos=(-0.45, 0.8), height=0.08, wrapWidth=10,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-3.0)
label_teste = visual.TextStim(win=win, ori=0, name='label_teste',
    text=u'Imagem de Teste',    font=u'Times New Roman',
    pos=(0.45, 0.8), height=0.08, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-4.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

#------Prepare to start Routine "instructions"-------
t = 0
instructionsClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_2.status = NOT_STARTED
# keep track of which components have finished
instructionsComponents = []
instructionsComponents.append(title)
instructionsComponents.append(question)
instructionsComponents.append(answer)
instructionsComponents.append(key_resp_2)
instructionsComponents.append(goon)
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "instructions"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = instructionsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *title* updates
    if t >= 0.0 and title.status == NOT_STARTED:
        # keep track of start time/frame for later
        title.tStart = t  # underestimates by a little under one frame
        title.frameNStart = frameN  # exact frame index
        title.setAutoDraw(True)
    
    # *question* updates
    if t >= 0.0 and question.status == NOT_STARTED:
        # keep track of start time/frame for later
        question.tStart = t  # underestimates by a little under one frame
        question.frameNStart = frameN  # exact frame index
        question.setAutoDraw(True)
    
    # *answer* updates
    if t >= 0.0 and answer.status == NOT_STARTED:
        # keep track of start time/frame for later
        answer.tStart = t  # underestimates by a little under one frame
        answer.frameNStart = frameN  # exact frame index
        answer.setAutoDraw(True)
    
    # *key_resp_2* updates
    if t >= 0.0 and key_resp_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_2.tStart = t  # underestimates by a little under one frame
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        key_resp_2.clock.reset()  # now t=0
        event.clearEvents(eventType='keyboard')
    if key_resp_2.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_2.keys = theseKeys[-1]  # just the last key pressed
            key_resp_2.rt = key_resp_2.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # *goon* updates
    if t >= 0.0 and goon.status == NOT_STARTED:
        # keep track of start time/frame for later
        goon.tStart = t  # underestimates by a little under one frame
        goon.frameNStart = frameN  # exact frame index
        goon.setAutoDraw(True)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "instructions"-------
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
   key_resp_2.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.nextEntry()
# the Routine "instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions(u'trial.xlsx'),
    seed=None, name='trials_2')
thisExp.addLoop(trials_2)  # add the loop to the experiment
thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrial_2.rgb)
if thisTrial_2 != None:
    for paramName in thisTrial_2.keys():
        exec(paramName + '= thisTrial_2.' + paramName)

for thisTrial_2 in trials_2:
    currentLoop = trials_2
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2.keys():
            exec(paramName + '= thisTrial_2.' + paramName)
    
    #------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    image.setImage(Imagemoriginal)
    image_2.setImage(Imagemteste)
    rating_2.reset()
    # keep track of which components have finished
    trialComponents = []
    trialComponents.append(image)
    trialComponents.append(image_2)
    trialComponents.append(text)
    trialComponents.append(text_2)
    trialComponents.append(rating_2)
    trialComponents.append(text_3)
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "trial"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image* updates
        if t >= 0.0 and image.status == NOT_STARTED:
            # keep track of start time/frame for later
            image.tStart = t  # underestimates by a little under one frame
            image.frameNStart = frameN  # exact frame index
            image.setAutoDraw(True)
        
        # *image_2* updates
        if t >= 0.0 and image_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_2.tStart = t  # underestimates by a little under one frame
            image_2.frameNStart = frameN  # exact frame index
            image_2.setAutoDraw(True)
        
        # *text* updates
        if t >= 0.0 and text.status == NOT_STARTED:
            # keep track of start time/frame for later
            text.tStart = t  # underestimates by a little under one frame
            text.frameNStart = frameN  # exact frame index
            text.setAutoDraw(True)
        
        # *text_2* updates
        if t >= 0.0 and text_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_2.tStart = t  # underestimates by a little under one frame
            text_2.frameNStart = frameN  # exact frame index
            text_2.setAutoDraw(True)
        # *rating_2* updates
        if t >= 0.0 and rating_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            rating_2.tStart = t  # underestimates by a little under one frame
            rating_2.frameNStart = frameN  # exact frame index
            rating_2.setAutoDraw(True)
        continueRoutine &= rating_2.noResponse  # a response ends the trial
        
        # *text_3* updates
        if t >= 0.0 and text_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_3.tStart = t  # underestimates by a little under one frame
            text_3.frameNStart = frameN  # exact frame index
            text_3.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials_2 (TrialHandler)
    trials_2.addData('rating_2.response', rating_2.getRating())
    trials_2.addData('rating_2.rt', rating_2.getRT())
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_2'


#------Prepare to start Routine "lets"-------
t = 0
letsClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_3 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_3.status = NOT_STARTED
# keep track of which components have finished
letsComponents = []
letsComponents.append(key_resp_3)
letsComponents.append(text_4)
for thisComponent in letsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "lets"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = letsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp_3* updates
    if t >= 0.0 and key_resp_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_3.tStart = t  # underestimates by a little under one frame
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        key_resp_3.clock.reset()  # now t=0
        event.clearEvents(eventType='keyboard')
    if key_resp_3.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_3.keys = theseKeys[-1]  # just the last key pressed
            key_resp_3.rt = key_resp_3.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # *text_4* updates
    if t >= 0.0 and text_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_4.tStart = t  # underestimates by a little under one frame
        text_4.frameNStart = frameN  # exact frame index
        text_4.setAutoDraw(True)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in letsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "lets"-------
for thisComponent in letsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_3.keys in ['', [], None]:  # No response was made
   key_resp_3.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('key_resp_3.keys',key_resp_3.keys)
if key_resp_3.keys != None:  # we had a response
    thisExp.addData('key_resp_3.rt', key_resp_3.rt)
thisExp.nextEntry()
# the Routine "lets" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('arquivo (1).xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial.keys():
        exec(paramName + '= thisTrial.' + paramName)

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial.keys():
            exec(paramName + '= thisTrial.' + paramName)
    
    #------Prepare to start Routine "experiment"-------
    t = 0
    experimentClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    image_ref.setImage(Imagemoriginal)
    image_test.setImage(Imagemteste)
    rating.reset()
    # keep track of which components have finished
    experimentComponents = []
    experimentComponents.append(image_ref)
    experimentComponents.append(image_test)
    experimentComponents.append(rating)
    experimentComponents.append(label_ref)
    experimentComponents.append(label_teste)
    for thisComponent in experimentComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "experiment"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = experimentClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_ref* updates
        if t >= 0.0 and image_ref.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_ref.tStart = t  # underestimates by a little under one frame
            image_ref.frameNStart = frameN  # exact frame index
            image_ref.setAutoDraw(True)
        
        # *image_test* updates
        if t >= 0.0 and image_test.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_test.tStart = t  # underestimates by a little under one frame
            image_test.frameNStart = frameN  # exact frame index
            image_test.setAutoDraw(True)
        # *rating* updates
        if t >= 0.0 and rating.status == NOT_STARTED:
            # keep track of start time/frame for later
            rating.tStart = t  # underestimates by a little under one frame
            rating.frameNStart = frameN  # exact frame index
            rating.setAutoDraw(True)
        continueRoutine &= rating.noResponse  # a response ends the trial
        
        # *label_ref* updates
        if t >= 0.0 and label_ref.status == NOT_STARTED:
            # keep track of start time/frame for later
            label_ref.tStart = t  # underestimates by a little under one frame
            label_ref.frameNStart = frameN  # exact frame index
            label_ref.setAutoDraw(True)
        
        # *label_teste* updates
        if t >= 0.0 and label_teste.status == NOT_STARTED:
            # keep track of start time/frame for later
            label_teste.tStart = t  # underestimates by a little under one frame
            label_teste.frameNStart = frameN  # exact frame index
            label_teste.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in experimentComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "experiment"-------
    for thisComponent in experimentComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials (TrialHandler)
    trials.addData('rating.response', rating.getRating())
    trials.addData('rating.rt', rating.getRT())
    # the Routine "experiment" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'

win.close()
core.quit()
