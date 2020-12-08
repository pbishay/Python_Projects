

import random
class Agents (object):
    def __init__(self,type):
        self.type = type
        self.payoff = 0
        
    def set_payoff (self, payoff):
        self.payoff = payoff 
        
    def get_payoff (self):
        return self.payoff 

class NormalFormAgent (object):
    def __init__(self):
        self.max_player_1 = 10
        self.max_player_2 = 10
        self.max_interact = 10
        
        self.payoff_data_1 = []
        self.payoff_data_2 = []
    
    def generate_agents (self):
        self.player_1 = []
        self.player_2 = []
        for i in range (self.max_player_1):
            self.player_1.append (Agents("Player_1"))
        for i in range (self.max_player_2):
            self.player_2.append (Agents("Player_1"))
            
    def play (self):
        for i in range (self.max_interact):
            player_1_ = self.player_1[i]
            player_1_strat = random.randint(1,3)
            
            player_2_ = self.player_2[i]
            player_2_strat = random.randint(1,3)
        
            if player_1_strat == 1 and player_2_strat == 1:
                player_1_.set_payoff(1)
                player_2_.set_payoff(1)
                self.payoff_data_1.append(1)
                self.payoff_data_2.append(1)
                
            if player_1_strat == 2 and player_2_strat == 1:
                player_1_.set_payoff(2)
                player_2_.set_payoff(0)
                self.payoff_data_1.append(2)
                self.payoff_data_2.append(0)
                
            if player_1_strat == 3 and player_2_strat == 1:
                player_1_.set_payoff(0)
                player_2_.set_payoff(2)
                self.payoff_data_1.append(0)
                self.payoff_data_2.append(2)
                
            if player_1_strat == 1 and player_2_strat == 2:
                player_1_.set_payoff(0)
                player_2_.set_payoff(2)
                self.payoff_data_1.append(0)
                self.payoff_data_2.append(2)
                
            if player_1_strat == 2 and player_2_strat == 2:
                player_1_.set_payoff(1)
                player_2_.set_payoff(1)
                self.payoff_data_1.append(1)
                self.payoff_data_2.append(1)
                
            if player_1_strat == 3 and player_2_strat == 2:
                player_1_.set_payoff(2)
                player_2_.set_payoff(0)
                self.payoff_data_1.append(2)
                self.payoff_data_2.append(0)
                
            if player_1_strat == 1 and player_2_strat == 3:
                player_1_.set_payoff(2)
                player_2_.set_payoff(0)
                self.payoff_data_1.append(2)
                self.payoff_data_2.append(0)
                
            if player_1_strat == 2 and player_2_strat == 3:
                player_1_.set_payoff(2)
                player_2_.set_payoff(0)
                self.payoff_data_1.append(2)
                self.payoff_data_2.append(0)
                
            if player_1_strat == 3 and player_2_strat == 3:
                player_1_.set_payoff(1)
                player_2_.set_payoff(1)
                self.payoff_data_1.append(1)
                self.payoff_data_2.append(1)
           
        
    def Average1 (self):
        return float(sum(self.payoff_data_1)/len(self.payoff_data_1))
    def Average2 (self):
        return float(sum(self.payoff_data_2)/len(self.payoff_data_2))
    def get_data_1 (self):
        return self.payoff_data_1
    def get_data_2 (self):
        return self.payoff_data_2
    def player (self):
        return self.player_1




run = NormalFormAgent()
run.generate_agents()
run.play()
print (run.Average1())
print(run.get_data_1())
print (run.Average2())
print(run.get_data_2())


                
                