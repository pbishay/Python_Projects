# 2 functions define individual preferences who are risk taking and risk averse
def risk_averse(x):
    
    if x <23:
        return -.03*(x+4)*(x-50)
    else:
        print("Error")


def risk_taking(z):
    if z >= 0:
        return .1*((z**2)+20)
    else:
        print("Error")
        
def make_random_lotteries_2():
#Makes a lottery based on input and only provides two options 
    prob_dict = [{} for i in range (2)]
     
    list = []
    for a in range (2):
        list.append('out')
    list_1 = []   
    for b in range (2):
        list_1.append('prob')
        
    g = float(input("Enter value between 0 and 1:"))
    prob_dict[0]['prob'] = g
    prob_dict[1]['prob'] = 1-g
    prob_dict[0]["out"]= int(input("Enter min pay:"))
    prob_dict[1]["out"]= int(input("Enter max pay:"))
    
    print(prob_dict)
    
    return prob_dict 

def make_random_lotteries_3(prob,min_pay, max_pay):
# Makes lottery with two ouputs (program input instead of user input)    
    prob_dict = [{} for i in range (2)]
     
    list = []
    for a in range (2):
        list.append('out')
    list_1 = []   
    for b in range (2):
        list_1.append('prob')
        
    
    prob_dict[0]['prob'] = prob
    prob_dict[1]['prob'] = 1-prob
    prob_dict[0]["out"]= min_pay
    prob_dict[1]["out"]= max_pay
    
    return prob_dict 

def make_random_lotteries(number, max_pay, compound):
#Makes lottery with n number of events and last event has the max pay. if compound = True, there are two events and     
#the second event contains am aggregate of all events that would normally be included, minus the first event    
    prob_dict = [{} for i in range (number)]

 

    list = []
    for a in range (number):
        list.append('out')
    list_1 = []   
    for b in range (number):
        list_1.append('prob')

    
    for a in range (number):
        for i in list_1:
            prob_dict[a][i] = (1/number)


    for a in range(number-1):
        for i in list:
            prob_dict[a][i] = a*10
    
        prob_dict[number-1]["out"]= max_pay
        
    if compound == True:
            
        prob_dict_2 =prob_dict.copy()
        for i in range (number-1):
            prob_dict_2.remove(prob_dict_2[1])
        prob_dict.remove(prob_dict[0])
        prob_dict_2.append({'prob':(1-(1/number)),'out':prob_dict})
        return prob_dict_2
            
    else:
            
        return prob_dict 
def expected_value(lottery):
#returns expected value of a lottery
    ev = 0.0
    for node in lottery:
        if type(node['out']) == type([]):
            # make recursive call to evaluate sub-lottery
            ev = node['prob'] * expected_value(node['out'])
        else:
            ev = ev + node['prob'] * node['out']
    return ev

def expected_utility(lottery, u):
    #returns the expected utility of a lottery (weighted average of utility for each event and probability)
    sum = 0
    for i in range (len(lottery)):
        a = u(lottery[i]["out"])*(lottery[i]["prob"])
        sum = sum + a
    return sum

def reduce_lottery(lottery):
#takes a compound lottery and reduces it to a simple lottery    
    if len(lottery)==2:
        a = lottery[1]['out']
        lottery.remove(lottery[1])
        
    for i in range(len(a)):
        for j in a:
            a[i]['prob']=1/(len(a)+1)
    lottery.append(a)
    return lottery
def certainty_equivalent(lottery, u):
# Returns the certinty equivalent given a lottery and a utility function         
        if len(lottery)==2:
            lower = lottery[0]['out']
            upper = lottery[1]['out']
            
            lower_u = u(lower)
            upper_u=u(upper)
            slope = (upper_u - lower_u)/(upper - lower)
            y_intercept =upper_u-slope*upper
            
            x = slope*(expected_value(lottery))+ y_intercept
            delta = .0001
            counter =0
            inc = .01
        
            delta = .001
            counter=expected_value(lottery)
            inc = .00001
            while abs(u(counter) - x)>= delta:
                counter = counter - inc
            return counter
def risk_premium(lottery, u):
#returns the risk premium given a lottery and a utility function (defined as the difference between the 
#certian outcome equal to engaging in the lottery and the expected outcome of playing the lottery)
    rp = expected_value(lottery) - certainty_equivalent(lottery, u)
    return rp 
def lottery_choice(lottery_list, u):
#Given lottery (n events) and a utility function, this returns the
#Lottery which has the highest utility     
    list = []
    for i in range(len(lottery_list)):
        list.append(expected_utility(lottery_list[i],u))
    
    return print(f"lottery {list.index(max(list))} has a value of {max(list)}")
def robot_holt_laury(min_pay, max_pay,min_pay_1,max_pay_1,u):
# Given a minimum and maximum value for two different lotteries, this uses the make_lotteries_2() function to
#create two different lotteries and the lottery_choice() for the computer to choice one of the two lotteries 
#The probabilities for each choice "a" and "b" change by .1 while the outputs stay fixed    
    list = []
    x=0 
    while x<1.0:
        
        print()
        print()
        print(f"choice a = {make_random_lotteries_3(x,min_pay, max_pay)} choice b = {make_random_lotteries_3(1-x,min_pay_1, max_pay_1)}")
        list.append(make_random_lotteries_3(x,min_pay, max_pay))
        list.append(make_random_lotteries_3(1-x,min_pay_1, max_pay_1))
        lottery_choice(list,u)
        list.clear()
        x=x+.1
        
def human_holt_laury(min_pay, max_pay,min_pay_1,max_pay_1):
# same function as robot_holt_laury(), except uses human input to choose between two lotteries and returns a list of 
#the choices
    list = []
    x=0 
    while x<1.0:
        
        print(f"choice a = {make_random_lotteries_3(x,min_pay, max_pay)} choice b = {make_random_lotteries_3(1-x,min_pay_1, max_pay_1)}")
        inp = input("Enter a or b: ")
        if inp == "a":
            list.append(make_random_lotteries_3(x,min_pay, max_pay))
        if inp == "b":
            list.append(make_random_lotteries_3(1-x,min_pay_1, max_pay_1))
        
        
        
        x=x+.1
    print()
    print()
    print(list)
def merge(list1, list2): 
# Turns two lists into a list of tuples       
    merged_list = [(list1[i], list2[i]) for i in range(0, len(list1))] 
    return merged_list

def elicitation_algorithm (U_min,U_max,lottery):
#returns a list of tuples which indicate payoffs and utility values based on human unput    
    print(lottery)
    low = lottery[0]['out']
    high = lottery[1]['out']
    ce_1 = float(input("what lowest value would you take if p = 1?: "))
    lottery[1]['out']=ce_1
    print(lottery)
    ce_2 = float(input("what lowest value would you take if p = 1?: "))
    lottery[0]['out']=ce_1
    lottery[1]['out']=high
    print(lottery)
    ce_3 = float(input("what lowest value would you take if p = 1?: "))
    
    Utility= [0,25,50,75,100]
    Payoff = [low,ce_2,ce_1,ce_3,high]
    a = merge(Payoff,Utility)
    return a



def line_function(c):
#input into main function is a list of tuples. This takes the list of tuples and turns them into a linear peacewise
#function. This function returns a second function which can take the input value x and returns a utility based
#on the payoff 
    m_1 = (c[1][1]-c[0][1])/(c[1][0]-c[0][0])
    y_1 = c[1][1] - m_1*c[1][0]
    m_2 = (c[2][1]-c[1][1])/(c[2][0]-c[1][0])
    y_2 = c[2][1]- m_2*c[2][0]
    m_3 = (c[3][1]-c[2][1])/(c[3][0]-c[2][0])
    y_3 = c[3][1]- m_2*c[3][0]
    m_4 = (c[4][1]-c[3][1])/(c[4][0]-c[3][0])
    y_4 = c[4][1]- m_2*c[4][0]
   
    def function(x):
        if c[0][0]<=x <c[1][0]:
            return m_1*x+y_1
        if c[1][0] <=x < c[2][0]:
            return m_2*x+y_2
        if c[2][0] <= x < c[3][0]:
            return m_3*x+y_3
        if c[3][0] <= x <= c[4][0]:
            return m_4*x+y_4
        else: 
            print("error")
    
    return function
#TESTS
print("creates a function based on  elicitation_algorithm and runs holt_laury as a robot")
#creates a function based on  elicitation_algorithm and runs holt_laury as a robot
test = make_random_lotteries_3(.5,1,20)
q = elicitation_algorithm (0,100,test)
z = line_function(q)
print("Holt Laury Choices based on elicitation function")
robot_holt_laury(5,10,1,20,z)
print("____________________________________________________________________________________________________________________")
print("____________________________________________________________________________________________________________________")
print("____________________________________________________________________________________________________________________")
#Using risk_averse to make choices
print("Using risk_averse function to make choices")
robot_holt_laury(5,10,1,20,risk_averse)
#Human making Holt Laury Choices
print("____________________________________________________________________________________________________________________")
print("____________________________________________________________________________________________________________________")
print("____________________________________________________________________________________________________________________")
print("Holt Laury Choices based on human input")
human_holt_laury(5, 10,1,20)
print("____________________________________________________________________________________________________________________")
print("____________________________________________________________________________________________________________________")
print("____________________________________________________________________________________________________________________")
print("printing lottery compound with n events ")
print(make_random_lotteries(5, 100, compound=True))
print("____________________________________________________________________________________________________________________")
print("____________________________________________________________________________________________________________________")
print("____________________________________________________________________________________________________________________")
print("printing simple with n events ")
print(make_random_lotteries(6, 100, compound=False))
print("____________________________________________________________________________________________________________________")
print("____________________________________________________________________________________________________________________")
print("____________________________________________________________________________________________________________________")
print("creating lottery from user input")
make_random_lotteries_2()
print("____________________________________________________________________________________________________________________")
print("____________________________________________________________________________________________________________________")
print("____________________________________________________________________________________________________________________")
