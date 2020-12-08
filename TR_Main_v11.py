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

from mesa import Agent, Model                                                   #import Agent and Model from mesa library
from mesa.time import RandomActivation                                          #import RandomActivation from mesa library
import random
import math
import numpy as np

g_lZipfValues = [1, 2, 3, 4, 5, 6, 7]
g_lZipfWeights = [0.818, 0.143, 0.020, 0.010, 0.005, 0.003, 0.001]

class xMember(Agent):                                                           #class to create an "xMember" agent (breed in NetLogo) 
    def __init__(self, 
                 unique_id, 
                 model, 
                 #a_iNAgents = 5, 
                 a_fBelief = 4, 
                 a_fBelongsafe = 4, 
                 a_fContribute = 4, 
                 a_fGratitude = 4,
                 a_fHope = 4, 
                 a_fResilience = 4, 
                 a_fStrength = 4, 
                 a_fTrusted = 4):                                               #define class constructor to initialize the agent's attributes, given the arguments
        super().__init__(unique_id, model)                                      #inheriting mesa.Agent's superclass methods
        
        self.m_fBelief = a_fBelief
        self.m_fBelongsafe = a_fBelongsafe
        self.m_fContribute = a_fContribute
        self.m_fGratitude = a_fGratitude
        self.m_fHope = a_fHope
        self.m_fResilience = a_fResilience
        self.m_fStrength = a_fStrength
        self.m_fTrusted = a_fTrusted
        self.m_iUniqueID = unique_id
        self.m_fStressAgent = []
        self.m_fStressAgg = []
        self.m_fStressMem = []
        
        #create memory for member directioned relationship attributes
        self.m_fTrust = self.create_dict()                                      #create agent attribute (asdict) of trust in relationship with every agent
        
    def create_dict(self):                                                      #function to create a dict for directed links
        newdict = {}                                                            #declare empty python dict
        for i in range(self.model.m_iNAgents):                                  #this agent loop through all other agents
            if i == self.unique_id:                                             #skips making a link with itself
                pass
            else:
                newdict[i] = []                                                 #adds an empty list in the dict representing the directed link with the other agent.
        return newdict

    def step(self):                                                             #define agent's actions during each step
        # Agent Stress updating (event generation, accumulation and decay)
        self.m_fStressAgent.append(random.choices(population=g_lZipfValues,
                                            weights=g_lZipfWeights)[0])         #generate stress event for agent
        
        #############################################################################################
        # Aggregating stress from stress memory (m_fStressMem) using the hyperbolic tangent
        # 
        # m_fStressAgg[x] = (1 - tanh(αx)) * 10**m_fStressAgent
        # (1 - tanh(αx)) --> yields (0,1] starting at 1 (or 100%) for events in recent memory, approaching 0 (or 0%)
        #                   for events far in memory and with low event values 
        #                --> Think of this as uing the y-value between 1 and tanh curve to make a percent value
        #                   and we use that percent value to decay/reduce old stress event values 
        #                   such that 100% means it happened today, and 0% meeans it happened a long time ago
        # x = (steps ago)/(steps total) --> Yields a % [0%, 100%] i.e., bounded [0,1]
        # α = m_fResilience --> m_fResilience is integer [1,7]...
        #                   --> higher Resilience makes the tanh curve increase faster)
        # Note: Reference this visual to understand why bounding the 
        # https://www.researchgate.net/figure/Hyperbolic-tangent-function-Plot-of-the-hyperbolic-tangent-function-y-tanhax-for_fig9_6266085
        #############################################################################################

        ##using m_fStressMem to store today's stress value for all stress events in memory
        self.m_fStressMem.append(0)                                             #extending the list by 1 to have equal length to the stress event lists
        α = self.m_fResilience                                                  #storing alpha variable
        yTeamModify = self.model.m_fTogether - 4                                #rescale [1,7] to [-3,3]
        for i in range(len(self.m_fStressAgent)):                               #looping through agent's entire event memory
            #updating current feeling of history of stress events, starting from today/current step/end of the memory lists 
            x = i / len(self.m_fStressAgent)                                    #x is recency of stress event memory 
            yTeam = self.model.m_fStressTeam[-(i + 1)] - yTeamModify            #reduce team stress event magnitude exponent by rescaled model.m_fTogether
            yAgent = self.m_fStressAgent[-(i + 1)]
            y = 10**max(0,yTeam) + 10**yAgent
            d = (1 - np.tanh(α * x))
            self.m_fStressMem[-(i + 1)] = (d * y)
            # #PRINTING for debugging
            # print ("@Step " + str(self.model.m_iStep) + 
            #        " @Agent " + str(self.unique_id) + 
            #        ": α=self.m_fResilience=" + str(α) + 
            #        " x=i/len(self.m_fStressAgent)=" + str(x) +
            #        " yTeamModify=self.model.m_fTogether-4=" + str(yTeamModify) +
            #        " self.model.m_fStressTeam[-(i+1)]=" + str(self.model.m_fStressTeam[-(i + 1)]) +
            #        " yTeam=self.model.m_fStressTeam[-(i+1)]-yTeamModify=" + str(yTeam) +
            #        " yAgent=self.m_fStressAgent[-(i+1)]=" + str(yAgent) +
            #        " y=10**max(0,yTeam)+10**yAgent=" + str(y) +
            #        " d=(1-np.tanh(α*x))=" + str(d) +
            #        " self.m_fStressMem[-(i+1)]=(d*y)=" + str(self.m_fStressMem[-(i + 1)])
            #        )
        #sum today's feeling of stress event history, and add to today's stress felt
        self.m_fStressAgg.append(sum(self.m_fStressMem))


        # #PRINTING for debugging
        # print ("========================= Step #" + str(self.model.m_iStep))
        # print("Agent#" + str(self.unique_id) + " with α = Resilience = " + str(self.m_fResilience))
        # print("self.m_fStressMem || m_fStressAgent || m_fStressTeam || m_fStressAgg")
        # print(self.m_fStressMem)
        # print(self.m_fStressAgent)
        # print(self.model.m_fStressTeam)
        # print(self.m_fStressAgg)
        
        
        # Agent Trust updating (using python DICT for agent memory)
        for i in range(self.model.m_iNAgents):                                  #current agent loops through all agents...
            if i == self.unique_id:                                             #...skips itself...
                pass
            else:
                self.m_fTrust[i].append(i)                                      #append the new value to the "memory" of trust in the relationship
        
        #PLACEHOLDER for retrieving values in a python DICT        
        #self.m_fTrust[#agent_id][:4]

        #PRINTING for debugging
        print ("Agent " + str(self.m_iUniqueID) +
               " memory of trust in relations:" + str(self.m_fTrust) +
               " BELIEF VALUE=" + str(self.m_fBelief))
        if self.unique_id == 0:
            pass
        else:
            print ("Agent " + str(self.m_iUniqueID) +
               " first memory of trust in relation with Agent 0 = " +
               str(self.m_fTrust[0][0]) +
               " last memory of trust in relation with Agent 0 = " +
               str(self.m_fTrust[0][-1]) )
        def unique(self):
            return self.m_iUniqueID


class xModel(Model):                                                            #class to create an instance of the simulation model
    def __init__(self, a_iNAgents = 5,
                 a_fTogether = 4):                                         #define class constructor to initialize the model's attributes, given the arguments
        #Check if Arguments are valid 
        if not 1 <= a_fTogether <= 7 :
            raise ValueError("Argument a_fTogether not in [1,7]")
        if not 3 <= a_iNAgents <= 10 :
            raise ValueError("Argument a_iNAgents not in [3,10]")
        
        #specify model attributes
        self.m_iNAgents = a_iNAgents                                            #set number of agents
        self.m_iStep = 0                                                        #set step of model
        self.m_oScheduler = RandomActivation(self)                              #set agent scheduler object (stores agent object list) as MESA's random activation (shuffles the order)
        self.m_fStressTeam = []                                                 #declare team stress event variable 
        self.m_fTogether = a_fTogether 
        #create agents and add the MESA's scheduler object
        for i in range(a_iNAgents):                                             #create N agents
            r = i + 1
            a = xMember(i, self, a_fResilience = r)                             #create new agent using customized MESA agent class
            self.m_oScheduler.add(a)                                            #add agents to the Scheduler's agent list
    
    def step(self, a_iStep):                                                    #define model's actions during each step
        self.m_iStep = a_iStep 
        self.m_fStressTeam.append(random.choices(population=g_lZipfValues,
                                            weights=g_lZipfWeights)[0])         #generate stress event for the team 
        self.m_oScheduler.step()                                                #advance the model one step
       
       

        #PRINTING for debugging
        for a in self.m_oScheduler.agents:                                      #loop through all agents
            print ('Agent' + str(a.m_iUniqueID) + ' stress event memory is ' 
                   + str(a.m_fStressAgent))                                     #print all agent's individual stress event
            

    def getAgents(self):
        return self.m_oScheduler.agents