################################################################
# -*- coding: utf-8 -*-
#(1) Tahir Hafeez
#(2) Hardware platform: PC (HP), Intel Core i7-4600U CPU @ 2.10 GHz 2.70 GHz, RAM 16 GB
#(3) OS: Windows 10, 64-bit
#(4) Python 3.7.3, 64-bit | Qt 5.9.6 | PyQt5 5.9.2 (Anaconda 3 distribution)
#(5) Special instructions: Run in Spyder 3.6 IDE (Anaconda 3 distribution)
#
# Authors: Tahir Hafeez, Peter Bishay
# Date Due: 5/20/2020
# Purpose: GMU CSS 610: Final Project: Simulation Model of Team Resilience
# Program Description:  
# Submission: 
# (1) Code Submission: The code is to be submitted to the online folder and must include (see 1-5 header items). 
#       Code Comments: Extensive comments throughout code, ~50% of keystrokes.
# (2) Writeup Submission: Please submit either in PDF online the day before class or in hardcopy at the start of class. 
################################################################

#set working directory where my scripts are locally saved
#import os
#os.getcwd()
#os.chdir("C:\\Users\\user\\Documents\\GMU CSS\\CSS 610\\Final Project\\Code")
#os.chdir("PETER INSERT YOUR FILEPATH FOR THE CODE FILES")

#import libraries
from TR_Main_v11 import xModel
import random
import matplotlib.pyplot as plt
from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
import numpy as np 

# declare global variables
g_fBelief = 4
g_fBelongsafe = 4
g_fContribute = 4
g_fHope = 4
g_fResilience = 4
g_fStrength = 4
g_fTrusted = 4
g_fStressTeam = 0
g_fStressAgent = 0

## declare model settings
g_iN = 7                                                                        # number of agents
g_iSteps = 1000                                                                    # number of steps
g_iTogether = 4                                                                 # Team Togetherness [1.7] -- 4 has no impact on the model

# create a model with (n agents)
aModel = xModel(a_iNAgents = g_iN, a_fTogether = g_iTogether )

# declare variables to help with data visualizations
g_lSteps = list(range(g_iSteps))                                                #creating a list [0,1...n] for n steps in the model
Total_Stress = []                                                               #declare empty list for plotting total stress
lists = []                                                                      #declare empty list for plotting lists

#run the model (for the declared # of steps)
for i in range(g_iSteps):                                                       #loop through the specified number of steps
    print ('===================================STEP #' + str(i))                #print for debugging
    aModel.step(i)                                                              #run the next step for the model
    

for i in aModel.m_oScheduler.agents:                                            #loop thruogh all agents in the model
     print("This is Agent #" + str(i.unique_id))                                #print for debugging
     print("RESILIENCE = " + str(i.m_fResilience))
     print("Agent #" + str(i.unique_id) + " stress event memory (m_fStressMem) is")
     print(i.m_fStressMem)
     lists.append(i.m_fStressAgg)                                               #store value for plotting later

lists = sum(map(np.array, lists))                                               #Calculating for plot: Sum of Agents' Perceived Stress (m_fStressAgg) Over Time
print (lists)                                                                   #print for debugging
print("test")
print(aModel.m_fStressTeam)

## plotting
# declare plot counter
g_iPlot = 0

# plot: Unadjusted Team stress events (m_fStressTeam) over time
g_iPlot += g_iPlot
plt.clf()
plt.figure(g_iPlot)
plt.plot(g_lSteps, aModel.m_fStressTeam)
plt.xlabel('Steps')
plt.ylabel('Team Stress Events')
plt.title('Unadjusted Team Stress Events (m_fStressTeam) Over Time', y=1.05)
plt.show()

# plot: Unadjusted Team stress magnitude (10^m_fStressTeam) over time (linear scale)
g_iPlot += g_iPlot
plt.clf()
plt.figure(g_iPlot)
plt.plot(g_lSteps, [10**x for x in aModel.m_fStressTeam])
plt.xlabel('Steps')
plt.ylabel('Team Stress Events')
plt.title('Unadjusted Team Stress Magnitude (10^m_fStressTeam) Over Time', y=1.05)
plt.show()

# plot: Unadjusted Team stress magnitude (10^m_fStressTeam) over time (log scale)
g_iPlot += g_iPlot
plt.clf()
plt.figure(g_iPlot)
plt.plot(g_lSteps, [10**x for x in aModel.m_fStressTeam])
plt.xlabel('Steps')
plt.ylabel('Team Stress Events')
plt.title('Unadjusted Team Stress Magnitude (10^m_fStressTeam) Over Time (log scale)', y=1.05)
plt.yscale('log')
plt.show()

# plot: Adjusted (m_fTogether) Team stress events (m_fStressTeam) over time
g_iPlot += g_iPlot
plt.clf()
plt.figure(g_iPlot)
temp = []
yTeamModify = aModel.m_fTogether - 4                                            #rescale team togetherness value from [1,7] to [-3,3]
for i in aModel.m_fStressTeam:                                                  #loop through m_fStressTeam (one value for each step in the model)
    temp.append(max(0,i-yTeamModify))                                           #storing modified team stress value for plotting
plt.plot(g_lSteps, temp)
plt.xlabel('Steps')
plt.ylabel('Adjusted Team Stress Events')
plt.title('Adjusted (m_fTogether) Team Stress Events (m_fStressTeam) Over Time', y=1.05)
plt.show()

# plot: Adjusted (m_fTogether) Team stress magnitude (10^m_fStressTeam) over time (linear scale)
g_iPlot += g_iPlot
plt.clf()
plt.figure(g_iPlot)
plt.plot(g_lSteps, [10**x for x in temp])
plt.xlabel('Steps')
plt.ylabel('Team Stress Events')
plt.title('Adjusted (m_fTogether) Team Stress Magnitude (10^m_fStressTeam) Over Time', y=1.05)
plt.show()

# plot: Adjusted (m_fTogether) Team stress magnitude (10^m_fStressTeam) over time (log scale)
g_iPlot += g_iPlot
plt.clf()
plt.figure(g_iPlot)
plt.plot(g_lSteps, [10**x for x in temp])
plt.xlabel('Steps')
plt.ylabel('Team Stress Events')
plt.title('Adjusted (m_fTogether) Team Stress Magnitude (10^m_fStressTeam) Over Time (log scale)', y=1.05)
plt.yscale('log')
plt.show()


# plot: Sum of Agents' Perceived Stress (m_fStressAgg) Over Time
g_iPlot += g_iPlot
plt.clf()
plt.figure(g_iPlot)
plt.plot(g_lSteps,lists)
plt.xlabel('Steps')
plt.ylabel('Total Stress Magnitude')
plt.title("Sum of Agents' Perceived Stress (m_fStressAgg) Over Time", y=1.05)
plt.show()

# plot: Subplots of each agent's Perceived Stress (m_fStressAgg) Over Time (shared x and y axes)
g_iPlot += g_iPlot
plt.clf()
fig, axs = plt.subplots(g_iN, sharex=True, sharey=True, figsize=(8, 20))        #creating subplots with shared y-axes
fig.suptitle("Subplot of each agent's Perceived Stress (m_fStressAgg) Over Time", y=0.9)
for i in aModel.m_oScheduler.agents:                                            #loop through agents
    axs[i.unique_id].plot(g_lSteps, i.m_fStressAgg)                             #plot each agent's perceived stress
    plt.ylabel('Team Stress')
    if (i.unique_id == len(aModel.m_oScheduler.agents)):                        #if this is the last subplot
        plt.xlabel('Steps')                                                     #add the x axis label
plt.show()


# plot: Subplot of each agent's Perceived Stress (m_fStressAgg) Over Time (shared x axis only)
g_iPlot += g_iPlot
plt.clf()
fig, axs = plt.subplots(g_iN, sharex=True, sharey=False, figsize=(8, 20))       #creating subplots with independent y-axes
fig.suptitle("Subplot of each agent's Perceived Stress (m_fStressAgg) Over Time", y=0.9)
for i in aModel.m_oScheduler.agents:                                            #loop through agents
    axs[i.unique_id].plot(g_lSteps, i.m_fStressAgg)                             #plot each agent's perceived stress
    plt.ylabel('Team Stress')
    if (i.unique_id == len(aModel.m_oScheduler.agents)):                        #if this is the last subplot
        plt.xlabel('Steps')                                                     #add the x axis label
plt.show()

