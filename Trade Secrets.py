
#=========================================================================
#-------------------------------NOTES--------------------------------    
#=========================================================================

#Often confused Variables
#piratefleet is the enemy fleet

#Credits:

#http://nine.frenchboys.net/
#For awesome names

#Tradewinds by Bigfishgames
#Taipan
#For general game build

#Spice and Wolf
#For ideas about economy

#http://en.wikipedia.org/wiki/Zheng_He
#http://en.wikipedia.org/wiki/Sailing_ships

#=========================================================================
#-------------------------------BALANCE--------------------------------    
#=========================================================================

#-------------------------------GENERAL--------------------------------   
            
initailcash = 10000

bankinterest = 0.01 #per month
deptinterest = 0.05
credit = 2 # credit * playercash.getbalance() = maximum_money_that_can_be_borrowed
repay = 2 #if you have x dept, you are forced to repay it when you have (repay) times your dept

maximumstormdamage = 0.25 #what fraction of a ship's max hp can be damaged

shipname = ["Raft","Schooner","Barge","Brig","Caravel","Galley","Junk","Frigate","Battleship"] #9 items

shipstorage = [0,200,1000,1000,5000,250,500,1200,2000] #note the Treasure ship has 24 cannons
shiphp = [50,100,200,700,2000,175,300,1300,5000]
shipfluctuation = [0.01,0.01,0.01,0.01,0.02,0.06,0.07,0.09,0.11]
shipmaxcannons = [0,10,0,20,24,20,30,70,100]
startingshipmarket = [500,2000,10000,10000,50000,3000,5000,10000,50000]
startingcannonprice = 1500

lootpercent = 0.9 #how much of an enemy's fleet can be salvaged
piratestrength = 0.3 #the budget of a pirate in comparison to you
standard_pirate_cannon_concentration = 0.9 #how much of a space's maxcannons is loaded up

contraband = 30 #chance out of 100 that contraband will be seized
warehousecontraband = 10 #chance out of 100 that contraband from the warehouse will be seized

shippricereduction = 0.9 # price = ship_price_reduction ^ months_in_service
cannontax = 0.5
maxhpreductionpercent = 0.1 #how much damage goes towards maxhp damage

cannonweight = 10
cannondamage = 10
cannonfluctuation = 0.01
spacefluctuation = 0.01

goods = ["food     ","metal    ","oil      ","spices   ","weapons  ","gunpowder","opium    "] #the list of items in the market, unit price, 7 items
fluctuation = [0.2,0.6,0.3,1.7,0.8,1.3,6.2] #how much the value will change based on luck
combination = 0.1 #to keep all the prices similar

stormchance = 30 #of out 100
piratechance = 100
stormdamagechance = 30 #of out 100
stormreturnchance = 30
stormthrowoffchance = 30
stormdelaychance = 30
muggedchance = 10 #chance of getting mugged when doing an action, out of 1000
muggeddelaychance = 30 #change of getting hospitalized for a month when getting mugged, out of 100

repaircost = 10 # cost/hp
warehousetax = 0.9 #how much money you get back from selling a warehouse

cannonsizestorage = 20 #how much space a cannon slot takes up
shipsizestorage = 2 #how much space a storage slot takes up
cannonstorage = 5 #how much space a cannon takes up
lakefrontproperty = 2 #how much more expensive shipyard space is than warehouse space

initaildisplacement = -20.0 #starting economy.  IS THE STANDARD FOR BAD
warboost = 5.0 #a number, in the scale of initaildisplacement, to boost the probability of war.  Search it up in the find function in Wing Ide to get the details
maxwarmagnitude = 100.0 #the largest magnitude that a civil war can start at
minwarmagnitude = 10 #the smallest magnitude a war can be at before it automatically "loses momentum" and ends
warmagnitudefluctuation = 0.2 #fluctuation of war magnitudes
warmagnitudefluctuation2 = 5.0 #another fluctuation, but addition instead of multiplication
warreduction = 0.95 #to increase the chance of the war ending, because it must eventually end
roaringtwenties = 30.0 #the boost at the end of a war

westernexpedition1 = 2.0 #the first boost in price.  Note this is distinguised from the variable "westernexpedition"
westernexpedition2 = 5.0 #the second boost in price

earlyarrival = 10 #chance of the western expedition arriving in febuary
latearrival = 10 #chance of the western expedition arrive in april.  Note that late arrival cannot happen if early arrival, making late arrival less likely to happen than early arrival (check the code to see what this means)

avgharvest = 3 #avg amount the price is divided by during the harvest season
winterboostsfood = 2
winterboostsoil = 2.5
warboostsfood = 0.05 #note that the war boosts coefficients is in the scale of 0.01
warboostsoil = 0.08
warboostsweapons = 0.53
warboostsgunpowder = 0.43
warboostsopium = 0.035

#supply = demand/warehouse, but with a tendency to be on the extreme (when demand is low, demand for supply is lower, when demand is high, demand for supply is higher
#demand = fluctuates with employment but less
#basedemand = 5
#warehouse += supply - demand

#goods = fluctuate + demand

#THEREFORE
#note to self: in storyline, say that a great war has just ended

#given demand is high, supply is higher, warehouse is low, but rocketing up
##supply goes high
##demand goes high but not so high
##warehouse goes low, but eventually starts to curve up, (parabolically?)
#eventually warehouse becomes too high
#rinse, repeat
#given demand is high, supply  is higher, but warehouse is even higher
##supply slows down and drops (parabolically?)
##demand drops, but not as much
##warehouse begins to curve down(parabolically?)
#rinse,repeat
#given demand is low, supply is lower, warehouse is low
##warehouse is going down
##supply begins to curve up
##demand moves up with supply but not as much
#rinse, repeat
#given demand is high, supply is higher, warehouse is low
#back to beginning

#political stability fluctuates around supply, aka employment
#war = fluctuates randomly
##occurs based on political stability
##creates a random, fluctuating magnitude

#Option 1
##creates another variable for magnitude
##basedemand = 5 + magnitude

#ask:
#did black tuesday have a warning?
#what made WW1 and WW2 bigger than other wars?

import os
import random

def fluctuate(initail,amount):
    if random.randint(0,1) == 1:
        return int(round(initail * random.uniform(1 , 1 + amount)))
    else:
        return int(round(initail * random.uniform(1/(1 + amount) , 1)))

#=========================================================================
#-------------------------------QUESTS--------------------------------    
#=========================================================================    

class quest(object):
    #auto means automatically accept, but not automatically complete
    def __init__(self,name,prerequisites,description,acceptancelocation,intro,segments):
        self.name = name
        self.segments = segments #list
        self.description = description
        self.acceptancelocation = acceptancelocation
        self.progress = 0
        self.satisfied = False
        self.current = False
        self.prerequisites = prerequisites #prerequisites is a list of classes
        self.current = False
        self.intro = intro
    def playintro(self):
        count2 = 0 #the 2 has not much reason other than saying that count, for once, does not act as an index.
        for item in self.intro:
            count2 += 1
            printgeneraldata()
            if count2 != len(self.intro):
                raw_input(item)
            else:
                print item
    def getaid(self):
        self.segments[self.progress].getaid()
    def check(self): #check if its finished
        if self.segments[self.progress].check():
            return True
        else:
            return False
    def complete(self):
        if self.segments[self.progress].check():
            self.segments[self.progress].complete()
            self.progress += 1
            if self.progress > len(self.segments) - 1:
                self.satisfied = True
                self.current = False
                raw_input("Completed " + self.name + "!")
    def getacceptancelocation(self):
        return self.acceptancelocation
    def getdescription(self):
        return self.description
    def getsatisfied(self):
        return self.satisfied
    def getname(self):
        return self.name
    def getvalid(self):
        for item in self.prerequisites:
            if item.check() == False:
                return False
        return True
    def getcurrent(self):
        return self.current
    def accept(self):
        self.current = True
    def getauto(self):
        if self.progress == len(self.segments):
            return False
        else:
            if self.segments[self.progress].getauto():
                return True
            else:
                return False

class prerequisite(object):
    def __init__(self,method,details):
        self.method = method
        self.detail = details
        if self.method == "kills":
            self.detail += playerkills
        if self.method == "timed" or self.method == "wait":
            self.detail += timeconvert()
    def check(self):
        if self.method == "quest":
            for item in quests:
                if item.getname() == self.detail:
                    if item.getsatisfied() == False:
                        return False
            return True
        if self.method == "playerworth":
            if getplayerworth() > self.detail:
                return True
            else:
                return False
        if self.method == "kills":
            if playerkills >= self.detail:
                return True
            else:
                return False
            
class segment(object):
    def __init__(self,conditions,results,aid):
        self.conditions = conditions
        self.results = results
        self.aid = aid
    def check(self): #check if its finished
        for item in self.conditions:
            if item.check() == False:
                return False
        return True
    def complete(self):
        for item in self.results:
            item.activate()
    def seekaid(self):
        raw_input(self.aid)
    def getauto(self):
        if len(self.conditions) == 0:
            return True
        else:
            return False
        
class condition(object):
    def __init__(self,method,details): #method is a string, details vary
        self.method = method
        self.detail = details
    def check(self):
        if self.method == "location":
            if playerlocation == self.detail:
                return True
            else:
                return False
        if self.method == "cash":
            if playercash.getbalance() >= self.detail:
                return True
            else:
                return False
        if self.method == "ship":
            for item in playerfleet.getfleet():
                if item.getshipindex() == self.detail:
                    return True
            return False
        if self.method == "kills":
            if playerkills >= details:
                return True
            else:
                return False
class result(object): #method is a string, details vary
    def __init__(self,method,details):
        self.method = method
        self.detail = details
    def activate(self):
        if self.method == "text":
            for item in self.detail:
                printgeneraldata()
                print item
                raw_input("next...")
        if self.method == "cash":
            playercash.deposit(self.detail)
        if self.method == "normalship":
            playerfleet.giveship(self.detail)
        if self.method == "specialship":
            playerfleet.givespecailship(self.detail)   
        if self.method == "town":
            newtown(self.detail)
        if self.method == "startwar":
            towns[self.detail[0]].startwar(self.detail[1])
            
quests = [quest("Learning to travel",[],"The guild master at Agorea needs you.",0,["I need someone to deliver this message to Sarantion.  Are you free?"],
    [segment([],[result("text",["Have this old raft of mine.  You need a ship to travel.","Tutorial: Do you remember how to sail?  You choose the option 'sail' on the main menu and then choose the location you want to sail to.  You can come across storms, and pirates.  Right now you can't do anything against pirates so flee when you run into them.  Oh, you have your pistol?  I guess you'll still be able to finish off defenseless pirates..."]),result("normalship",0)],"The guild master at Agorea has something for you."),
     segment([condition("location",1)],[result("text",["What's this say?","""Tutorial:
     A few of the obstacles you come across while sailing can hinder your travels.
     Storms can delay you, blow you off course, and even damage your ships
     Pirates often come to try to kill you.  But if you kill them, you get a reward.
     
     To repair your ships, simply select the option 'manage ships.'  You can repair your entire fleet, or one ship at a time.  But be aware that repairing ships is costly.
     
     Ships also go down in value over time.  They lose 10% of their value every month they spend sailing.  Also, cannons go down in value when you buy them.  Why?  Because when people buy cannons from anyone other than authorities, they assume they're buying from a pirate so you have to offer low prices to get their attention.
     
     But at the shipyard, you can store your ships and cannons.  Though you need to buy space first.
     ""","Having a fleet sounds expensive.  Have $" + str(initailcash) + " as your starting funds.  You might need it to repair your ships.  No, you don't need to pay it back"]),result("cash",initailcash)],"Go to Sarantion.")]),

quest("Learning to buy ships",[prerequisite("quest","Learning to travel")],"The guild master at Agorea wants you again.",0,["I'm really busy.  So busy I can't find the time to go to the ship market next door and buy me a ship.  A schooner sounds nice."],
      [segment([],[result("text",["Tutorial:\nDo you remember how to buy a ship?  Go to the ship market, select buy, and select the ship you want to buy.  Keep in mind that the prices of ships will fluctuate, just like the market.  Not as much though.","The guild master at Agorea wishes for you."]),result("cash",startingshipmarket[1])],"The guild master wishes for you"),
       segment([condition("location",0),condition("ship",1)],[result("text",["Oh I've been asking the same thing of multiple lads.  So I have a couple new schooners now.  You can keep that one."])],"Go buy a schooner")]),

quest("Learning to trade",[prerequisite("quest","Learning to buy ships")],"The guild master at Agorea wants you...again.",0,["The market at Sarantion is high at the moment.  Probably because its one of the cities most damaged from the war and is using up resources.  I don't think this will last long though.  You should load up on goods and transport them to Sarantion to sell.  I think it will be easy for you to rack up, say, $" + str(1.2*initailcash) + " in one round trip.  Oh speaking of money, I'm not going to give you any so use that $" + str(initailcash) + " you got the other day."],
      [segment([],[result("text",["Tutorial:\nDo you remember how to buy and sell goods?  On the main menu, just select the option to buy goods and type in how much you want to buy.  To sell, just enter a negative value."])],"The guild master wishes for you."),
       segment([condition("cash",1200),condition("location",0)],[result("text",["I see you know how to trade.  Well, don't think you can call yourself a trader without that knowledge...","You have learned all that I can teach you.  I have friends in Cirania and Cromon.  They shall teach you the true world of merchanting."]),result("town",3),result("town",4)],"Gather $" + str(initailcash * 1.2) + " and return to Agorea")]),

quest("Learning about the Western Expedition",[prerequisite("quest","Learning to trade")],"The guild master at Cirania wants you",2,["My brother taught you to trade?  No he didn't.  He just taught you how to buy and sell.  Rack up $50000.  Then you can call yourself a trader."],
      [segment([],[result("text",["Hah! did you think you can rack up $50000 immediately?  Buy some warehouse space and then come back.  Take note though, the warehouse space in Cirania is better for reasons I will soon explain, but it's also more expensive than in other places."])],"The guild master doesn't think you can do it without a few tips."),
       segment([condition("warehouse",1),condition("location",0)],[result("text",["You only bought that much warehouse space?  Guess its cause warehouse space is so expensive here.  You need some more.  And you might need some extra funds too."]),result("warehouse",[2,1000]),result("cash",10000),result("text",["""Tutorial:
      Well lets get started.  You've probably heard of the phrase 'buy high, sell low.'  Bullshit.  That's obvious.  You buy low, wait for the price to go up, then sell high.  But how do you know whether the market's gonna go up or down?  Well there are several tricks.
      The first trick is the most obvious.  When one town has a higher price than another, instead of waiting, just transport goods from one town to another.  That's what my brother taught you.  But the problem is this only works for a short while because so many merchants do this, the price eventually balances out in both towns.  So let me teach you another trick.
      Have you wondered why there's so many merchants here?  There's something called the Western Expedition.  Each March, a whole fleet of ships pass by Cirania to head to some far-off place.  When they pass, they need to restock on food, and the food price jumps.  They can return in either September, October, or November.  When they return, the price of spices drops.  And another tip.  The month before the Western Expedition, the changes in price starts to take place.  So if you want to take as much profit as you can, buy early two months early or just come stocked up on food from another town.  But be careful.  Sometimes the Western Expedition gets cancelled.
      There's also the harvest and the anticipation of winter.  Every August and September, the harvest comes, and drops the price of food, depending on how good the crops are.  But then it quickly rises again, along with oil, because people are anticipating winter and stocking up on food.  After winter, it drops to its normal price."""])],"Buy 1 warehouse space"),
       segment([condition("cash",50000),condition("location",0)],[result("text",["There.  Now you can call yourself a trader.  Have my old barge.  It holds a lot but doesn't have much attack power."]),result("normalship",2)],"Stock up $50000")]),
quest("Learning to fight",[prerequisite("quest","Learning to trade")],"The mafia head at Cromon can teach you how to defend yourself.",3,["You think you can defend yourself?  Take down 3 pirates.  Then I'll give you a real ship."],
    [segment([],[result("text",["Tutorial:\nI think I should tell you how to fight first.  Go to the shipmarket and buy cannons.  The more the better.  But keep in mind that each ship can only hold a limited number of cannons.  Then when in battle just select the fire option.  Remember to keep the health of your ships in mind, and retreat if you really have to."])],"Do you know how to take down pirates?"),
    segment([condition("kills",3),condition("location",3)],[result("text",["Great job.  Here's a warship.","""Tutorial:
    What's a warship?  Well, ships can be put into 3 catagories.
    1: Rafts are cheap but useless.  Use them as meat bait.
    2: Merchant ships carry a lot of cargo, but don't hold very many cannons.
    3: Warships can hold a lot of cannons.  They have a bit of storage too, but when you load them up with cannons, well, there won't be that much space.  And they are significantly more expensive, so just use them for battle.
    
    Ship prices fluctuate, check your databook on ships for details.

    Furthermore, some merchant ships are capable of battle.  They are not as well equipped as warships, but its enough to fend pirates off.
    
    """])],"Sink 3 pirate fleets")]),
quest("Learning about the world",[prerequisite("quest","Learning to fight"),prerequisite("quest","Learning about the Western Expedition")],"The guild master at Cirania has one final thing he wants to teach you.",2,["I need you to deliver this message to the mafia boss in Cromon.  Why would a merchant and a pirate work together?  Well lets put it this way.  We want to start a war.  If we do, the prices of his opium stock will rise, and so will a lot of my stocks.  War does a lot of things.  Check your database on goods for details.  The pay is $50000"],
      [segment([],[result("text",["This message says that he should send rebels to set fire to the Justice Building in Thoramin.","Wait!  Do you think I wouldn't award you for such a dangerous mission?","Tutorial:\n Look in your databook.  Some goods will rise in price based on a war.  Stock up in those goods, then sell them during the war.  War can be very profitable."])],"Did you think you wouldn't get anything out of this?"),
      segment([condition("location",3)],[result("text",["Reading...","Can I get you to do me a favor?  Bring my troops to Thoramin.  We should travel in a merchant ship to avoid rousing suspision.","Just let us in!"]),result("newtown",4)],"To Chromon"),
      segment([condition("location",4)],[result("text",["BURN!  BURN!  BURN IT ALL!",'I should return to Cirania to tell the Guild master to sell his stocks']),result("startwar",[4,100])],"TO THORAMIN!  I don't like the look of this..."),
      segment([condition("location",2)],[result("text",["Don't tell me you feel guilty for starting a war?  Don't worry, its a small war, I doubt it will get as big as the one that just ended.  I hope.  Anyways, I should tell you about the last trend in this game.","""Tutorial: 
      The economy in this game as an up and down trend.  The fluctuating economy determines whether the price is 'low' or 'high.' but its kind of difficult to tell.  Check your databooks, one of them should make it easier for you.
      But anyways, when the economy is low, people complain.  Rebellions and wars often start in times of bad economy and boost the market.  And when the war ends, the economy starts off good.
      ""","But anyways, have your pay."]),result("cash",50000)],"Send notice to Cirania")])]

def autoaccept():
    for item in quests:
        if item.getauto() and item.getcurrent():
            item.complete()

def checkquests():#check for new quests in the quest section, rolldown from the main menu
    
    option = "trollolol"
    while option != "0":
        autoaccept()
        printgeneraldata()
        print "QUESTS"
        print line2
        count = -1
        for item in quests:
            count += 1
            if item.getvalid() and item.getsatisfied() == False:
                if item.getcurrent() == True and item.check():
                    print str(count) + " : " + item.getname() + "\t" + "Complete"
                if item.getcurrent() == True and item.check() == False:
                    print str(count) + " : " + item.getname() + "\t" + "Current"
                if item.getcurrent() == False and item.getacceptancelocation() == playerlocation:
                    print str(count) + " : " + item.getname() + "\t" + "Accept"
        print line1
        print "0: Back"
        print "1: Complete or accept"
        print "2: Check"
        print line2
        option = raw_input("What would you like to do?: ")
        if option != "0":
            index = int(raw_input("Which quest?: "))
            if option == "1" and quests[index].getsatisfied() == False:
                if quests[index].getcurrent() == True and quests[index].check():
                    quests[index].complete()
                if quests[index].getcurrent() == False and item.getacceptancelocation() == playerlocation and quests[index].getvalid() == True:
                    quests[index].playintro()
                    print "1: Accept"
                    print "2: Decline"
                    if raw_input("Do you accept?: ") == "1":
                        quests[index].accept()
            if option == "2":
                if quests[index].getcurrent():
                    quests[index].getaid()
                if quests[index].getcurrent() == False and item.getvalid() == True:
                    quests[index].getaid()
    
#=========================================================================
#-------------------------------DATABOOKS--------------------------------    
#=========================================================================

class databook(object):
    def __init__(self,name,data):
        self.name = name
        self.data = data
    def getname(self):
        return self.name
    def printdata(self):
        print line1
        print self.name
        print line1
        for item in self.data:
            print item
            print line2
        print line1
    def addtext(self,text):
        self.data.append(text)
        
book_goods1 = databook("Goods 1",["""
Food:
The most basic commodity. Fluctuates in price little.
Metal:
Another basic commodity. Fluctuates in price moderately.
Oil:
Another basic commodity. Fluctuates in price little.
Spices:
Another basic commodity. Fluctuates in price heavily.
Weapons:
Another basic commodity. Fluctuates in price moderately.
Gunpowder:
A contraband. Fluctuates in price heavily.
Opium:
A contraband. Fluctuates in price. A lot.
"""])
book_goods2 = databook("Goods 2",["""
Food:
-The price goes down during the harvest season, around August and September, but how much depends on how good the harvest was. It goes back down a set amount in October.
-The price goes up during the winter season; around November and December, then goes down in January and Febuary when the winter ends.
-In Cirania, the price goes up around March because of the leaving Western Expedition.  It begins to go up in Febuary from merchants stocking up on goods.
-In Cirania, the price goes up around August, September, or November because of the returning Western Expedition.  Whether the western expedition returns early, late, or on time, the price begins to go up around August
Metal:
-Can be converted into weapons and vice versa.  However, this consumes oil, and the price of oil determines how much metal is converted into weaponry or vice versa
Oil:
-Price goes up during winter
Spices:
Another basic commodity. Fluctuates in price heavily.
Weapons:
Another basic commodity. Fluctuates in price moderately.
Gunpowder:
-See Metal
-A contraband during times of peace, but legal during times of war.
-Jumps in price during war
Opium:
-A contraband always.  
-Rises in price during war.
"""])
book_towns = databook("Towns",[])

book_ships = ["Raft:\nThe weakest ship.  Used mostly as meat bait in battles.  Cannot hold any cannons.","Schooner:\nUsed mainly as a merchant ship, but contains a bit of bang as well.","Barge:\nUsed as a merchant ship.  Cannot hold any cannons.","Brig:\nA bigger version of the schooner.  Holds significant cargo, and has some firepower to it as well.","Caravel:\nA bigger version of the brig.  Holds a lot of cargo, and can hold out in a battle.","Galley:\nThe basic warship.","Junk:\nA warship that can hold some cargo on the side.","Frigate:\nA tough warship.","Battleship:\nBig and powerful.","Notes: \nWarships fluctuate in price more than merchant ships.\nThe bigger the ship, the more its price fluctuates.\nA ship loses 10% of its price every month it has sent at sea"]
count = -1
for item in shipname:
    count += 1
    book_ships[count] += "\nHp             : " + str(shiphp[count])
    book_ships[count] += "\nStorage        : " + str(shipstorage[count])
    book_ships[count] += "\nMaximum cannons: " + str(shipmaxcannons[count])
    
book_ships = databook("Ships",book_ships)

initailjournaltext = ["Note: Numbers correspond to the index of the commodity","Y/D\tLocation\t0\t1\t2\t3\t4\t5\t6"]

def updatejournal():
    output = ""
    output += str(time[0]) + "/" + str(time[1]) + "\t"
    output += towns[playerlocation].getname() + "\t"
    for item in localmarket:
        output += str(item) + "\t"
    databooks[1].addtext(output)

databooks = [book_towns,databook("Journal",initailjournaltext),book_goods1,book_goods2,book_ships]

#=========================================================================
#-------------------------------MONEY--------------------------------    
#=========================================================================

class moneystorage(object): #player, bank, moneylender
    def __init__(self, initial):
        self.balance = initial
    def deposit(self, amt):
        self.balance += amt
    def getbalance(self):
        return self.balance
    
#=========================================================================
#-------------------------------SHIPS--------------------------------    
#=========================================================================

class ship(object): #ships
    def __init__(self,index,storage,hp,maxhp,cannons,maxcannons):
        self.storage = storage
        self.cannons = cannons
        self.maxcannons = maxcannons
        self.hp = hp
        self.shipindex = index
        self.maxhp = maxhp
        ship.use = 0 #how many months the ship has been in service
        ship.recordeddamage = 0
    def getname(self):
        return shipname[self.shipindex]
    def getshipindex(self):
        return self.shipindex
    def getstorage(self):
        return self.storage - cannonweight*self.cannons
    def getmaxstorage(self): 
        return self.storage
    def getcannons(self):
        return self.cannons
    def getmaxcannons(self):
        return self.maxcannons
    def givecannon(self,quantity):
        self.cannons += quantity
    def gethp(self):
        return self.hp
    def getmaxhp(self):
        return self.maxhp
    def atk(self,target): #target is a target fleet
        targetindex = random.randint(0,len(target.getfleet())-1)
        for item in range(0,self.getcannons()):
            target.damage(targetindex, random.randint(0,cannondamage))
        target.checkfleet() #sink the ships whose hp drops to or below 0
    def damage(self,amount):
        self.hp -= amount
    def stormdamage(self):
        damage = random.randint(0, int(maximumstormdamage * self.maxhp))
        self.hp -= damage
        self.recordeddamage = damage
    def getprice(self):
        usedcoefficient = 1
        for item in range(0,self.use):
            usedcoefficient = usedcoefficient * shippricereduction #for some reason the exponent thing won't work
        price = int( localshipmarket[self.getshipindex()] * self.maxhp/shiphp[self.shipindex] * usedcoefficient ) #price of a ship goes down relative to its maxhp.
        for item in range(0,self.getcannons()):
            price += int(localcannonmarket * cannontax)
        return price
    def passtime(self):
        self.use += 1
    def inflictrecordeddamage(self):
        self.maxhp -= int( self.recordeddamage * maxhpreductionpercent )
        self.recordeddamage = 0
    def getrepaircost(self):
        return (self.maxhp - self.hp) * repaircost
    def repair(self):
        self.hp = self.maxhp
    def getsize(self):
        return self.hp + self.cannons * cannonstorage
        #return self.storage * shipsizestorage + self.maxcannons * cannonsizestorage + self.cannons * cannonstorage
            
class fleet(object): #fleet, a list of ships
    def __init__(self,ships):
        self.ships = ships
    def replacefleet(self,ships):
        self.ships = ships
    def getfleet(self):
        return self.ships
    def getstorage(self):
        totalstorage = 0
        for item in self.ships:
            totalstorage += item.getstorage()
        return totalstorage
    def getmaxstorage(self):
        totalstorage = 0
        for item in self.ships:
            totalstorage += item.getmaxstorage()
        return totalstorage
    def giveship(self,shipindex):
        self.ships.append(ship(shipindex,shipstorage[shipindex],shiphp[shipindex],shiphp[shipindex],0,shipmaxcannons[shipindex]))
    def givespecailship(self,shipstats):
        self.ships.append(shipstats)
    def takeship(self,fleetindex):
        self.ships.pop(fleetindex)
    def checkfleet(self):
        count = -1
        for item in self.ships:
            count += 1
            if item.gethp() <= 0:
                if self == playerfleet: #cause we don't care about the enemy fleet...too many of them die anyways
                    if playerfleet.getstorage() - item.storage() > spaceused(playerstock):
                        lostcargo = spaceused(playerstock) - (playerfleet.getstorage() - item.storage())
                        raw_input("We lost a ship and " + str(lostcargo) + " units of our cargo!")
                        lostgoods = [0,0,0,0,0,0,0]
                        count = -1
                        for item in playerstock:
                            count += 1
                            playerstock[count] -= int(item/float(spaceused(playerstock)) * lostcargo) #turns it into a float for accuracy, then back into an integer.  Will result in less cargo lost than actually should be.
                        # get rid of the remainder                 
                        count = -1
                        for item in playerstock:
                            count += 1
                            lostcargo = spaceused(playerstock) - (playerfleet.getstorage() - item.storage())
                            if item > 0 and lostcargo > 0:
                                playerstock[count] -= 1 #will take items from the player's stock from the cheapest
                    else:
                        raw_input("One of our ships has sunk!: ")
                self.ships.pop(count)
    def givecannon(self,shipindex,number):
        self.ships[shipindex].givecannon(number)
    def damage(self,shipindex,amount):
        self.ships[shipindex].damage(amount)
    def stormdamage(self):
        for item in self.ships:
            item.stormdamage()
    def attack(self,target): #target is a fleet
        for item in self.ships: #Each ship fires all of their cannons round at a random enemy ship.
            item.atk(target)
    def passtime(self):
        for item in self.ships:
            item.passtime()
    def getrepaircost(self):
        repairprice = 0 #to differentiate it from the global variable repaircost
        for item in self.ships:
            repairprice += item.getrepaircost()
        return repairprice
    def repair(self):
        for item in self.ships:
            item.repair()
    def repairship(self,shipindex):
        self.ships[shipindex].repair()
    def getmaxcannons(self):
        maxcannons = 0
        for item in self.ships:
            maxcannons += item.getmaxcannons()
        return maxcannons
    def getcannons(self):
        cannons = 0
        for item in self.ships:
            cannons += item.getcannons()
        return cannons
 
#=========================================================================
#-------------------------------TOWNDATA--------------------------------    
#=========================================================================             
            
class town(object):
    def __init__(self,name,market,shipmarket,cannonmarket,spacecost,profile):
        self.name = name
        self.market = market
        self.shipmarket = shipmarket
        self.cannonmarket = cannonmarket
        self.warehouse = [0,0,0,0,0,0,0]
        self.warehousestorage = 0
        self.spacecost = spacecost
        self.shipyard = fleet([])
        self.shipyardcannons = 0
        self.shipyardstorage = 0
        self.warmagnitude = 0 #a country starts...not being in war
        self.warmagnitudechange = 0 #record change
        self.profile = profile
    def getprofile(self):
        return self.profile
    def getname(self):
        return self.name
    def getmarket(self):
        return self.market
    def getshipmarket(self):
        return self.shipmarket
    def getcannonmarket(self):
        return self.cannonmarket
    
    # Warehouse functions
    def getwarehouse(self):
        return self.warehouse
    def getwarehousestorage(self):
        return self.warehousestorage
    def givewarehouse(self,amount):
        self.warehousestorage += amount
    def getspacecost(self):
        return self.spacecost
    def storegoods(self,index,amount):
        self.warehouse[index] += amount

    # Shipyard functions
    def getshipyard(self):
        return self.shipyard #returns a fleet
    def giveship(self,index):
        self.shipyard.givespecailship(playerfleet.getfleet()[index])
        playerfleet.takeship(index)
    def takeship(self,index):
        playerfleet.givespecailship(self.shipyard.getfleet()[index])
        self.shipyard.takeship(index)
    def getextracannons(self):
        return self.shipyardcannons
    def getshipyardstorage(self):
        return self.shipyardstorage
    def getcannons(self,shipyard):
        output = self.shipyardcannons
        for item in self.shipyard.getfleet():
            output += item.getcannons()
        return output
    def getshipyardstorageused(self):
        output = self.shipyardcannons * cannonstorage
        for item in self.shipyard.getfleet():
            output += item.getsize()
        return output
    def givecannons(self,amount):
        self.shipyardcannons += amount
    def giveshipyardstorage(self,amount):
        self.shipyardstorage += amount        
        
    #war functions        
    def getwar(self):
        return self.warmagnitude
    def startwar(self,magnitude):
        self.warmagnitude = magnitude
    def progresswar(self):
        if self.warmagnitude == 0 and displacement < initaildisplacement:
            if random.randint(int(displacement),0) < initaildisplacement + warboost:
                raw_input("Sir, " + self.name + "has fallen into civil war!")
                initailwarmagnitude = random.uniform(1,maxwarmagnitude)
                towns[count].startwar(initailwarmagnitude)
                self.warmagnitudechange = initailwarmagnitude
        elif self.warmagnitude != 0 and self.warmagnitude < minwarmagnitude:
            self.warmagnitudechange = -self.warmagnitude + random.uniform(roaringtwenties)
            self.warmagnitude = 0
            raw_input( "War over!" ) #There is supposed to be a "roaring 20s" after a war, but the economy gets boosts cause of a war anyways, the economy can start of bad because of destroyed infrastructure...lalala...*tries to think of more excuses to slack off on programming
        elif self.warmagnitude != 0:
            memory = self.warmagnitude
            memory = fluctuate(memory,warmagnitudefluctuation)
            memory += random.uniform(-warmagnitduefluctuation2,warmagnitduefluctuation2)
            memory *= warreduction #to increase the chance of the war ending, because it must eventually end
            self.warmagnitudechange = memory - self.warmagnitude
            self.warmagnitude = memory
        else:
            self.warmagnitudechange = 0
            
    def markettrends(self): #WHOOO  THE GLORY OF MY GAME LIES IN THIS ONE FUNCTION XD...hey you can't backspace while pressing shift.
        ##WAR
        self.market[0] *= int(self.warmagnitudechange * warboostsfood)
        #war does not boost metal, only indirectly through weapons
        self.market[2] *= int(self.warmagnitudechange * warboostsoil)
        #war does not boost spices
        self.market[4] *= int(self.warmagnitudechange * warboostsweapons) #no duh...
        self.market[5] *= int(self.warmagnitudechange * warboostsgunpowder)
        self.market[6] *= int(self.warmagnitudechange * warboostsopium) #somehow...
        ##PREPARING FOR THE EXPEDITION TO THE NEW WORLD
        #let the expedition to the new world arrive in march 3 and return in september 9, and cross by town 3
        
        if self.name == "Cirania":
            if time[0] == 2: #Febuary
                if westernexpedition:
                    self.market[0] *= westernexpedition1
                else:
                    if playerlocation == 3:
                        raw_input("It appears that there will be no western expedition")
            if time[0] == 3:
                if westernexpedition:
                    self.market[0] *= westernexpedition2
                else:
                    if playerlocation == 3:
                        raw_input("It appears that there will be no western expedition")
            if time[0] == 4:
                if westernexpedition:
                    self.market[0] /= westernexpedition1*westernexpedition2
                    
            if westernexpedition:
                if time[0] == 8:
                    if earlyarrival == False: #if it does not arrive early
                        self.market[0] *= westernexpedition1
                        self.market[3] /= westernexpedition1
                    if earlyarrival == True: #if it does arrive early
                        self.market[0] *= westernexpedition2*westernexpedition1
                        self.market[3] /= westernexpedition2*westernexpedition1
                        if playerlocation == 3:
                            raw_input("The western expedition has returned early.")
                if time[0] == 9:
                    if earlyarrival == False and latearrival == False and westernexpedition: #if it arrives on time
                        self.market[0] *= westernexpedition2
                        self.market[3] /= westernexpedition2
                    if earlyarrival == True: #if it arrived early
                        self.market[0] /= westernexpedition1*westernexpedition2
                        self.market[3] *= westernexpedition1*westernexpedition2
                        if playerlocation == 3:
                            raw_input("The western expedition returned early.")
                    if latearrival == True:
                        if playerlocation == 3:
                            raw_input("The western expedition will be returning late")
                if time[0] == 10:
                    if earlyarrival == False and latearrival == False and westernexpedition: #if it arrives on time
                        self.market[0] /= westernexpedition1*westernexpedition2
                        Self.market[3] *= westernexpedition1*westernexpedition2
                    if latearrival == True:
                        self.market[0] *= westernexpedition2
                        self.market[3] /= westernexpedition2
                        if playerlocation == 3:
                            raw_input("The western expedition has returned late")
                if time[0] == 11:
                    if latearrival == True:
                        self.market[0] /= westernexpedition1 * westernexpedition2
                        self.market[3] *= westernexpedition1 * westernexpedition2
                        
        ##HARVEST
        harvestluck = random.randint(self.market[0],self,market[0]*avgharvest*2)
        if time[0] == 8:
            self.market[0] /= harvestluck
        if time[0] == 10:
            self.market[0] *= avgharvest
        ##WINTER
        if time[0] == 11:
            self.market[0] *= winterboostsfood
            self.market[2] *= winterboostsoil
        if time[0] == 12:
            self.market[0] *= winterboostsfood
            self.market[2] *= winterboostsoil
        if time[0] == 1:
            self.market[0] /= winterboostsfood
            self.market[2] /= winterboostsoil
        if time[0] == 2:
            self.market[0] /= winterboostsfood
            self.market[2] /= winterboostsoil
            
        ## Metals can be converted into weapons and vice-versa, using oil
        # Let one metal (1) can be converted into one weapons (4) by one oil (2)
        
        metalcombination =  float(self.market[2]) / abs(self.market[1] - self.market[4]) #the variable metalcombination undergoes some rather complicated changes.  But if you think hard enough you can understand it.
        
        if metalcombination < 1: #in other words if difference in metal and iron is greater than oil cost
            metalcombination = 1-metalcombination
            self.market[2] *= 1/metalcombination #oil gets used up from conversion and increases in price
            avgvalue = ( self.market[1] + selfmarket[4] ) / 2
            self.market[1] = self.market[1] * (1-metalcombination) + avgvalue * metalcombination #bring metal closer to the average cost
            self.market[4] = self.market[4] * (1-metalcombination) + avgvalue * metalcombination #bring weapons closer to the average cost
        
    def balancemarkets(self):
        count = -1
        for item in self.market: #balance the markets
            count += 1
            avgvalue = 0
            for item2 in towns:
                avgvalue += item2.getmarket()[count] / len(towns)
            self.market[count] = int(round((1-combination)*self.getmarket()[count] + combination*avgvalue))
        count = -1
        for item in self.shipmarket: #balance the ship markets
            count += 1
            avgvalue = 0
            for item2 in towns:
                avgvalue += item2.getshipmarket()[count]/ len(towns)
            self.shipmarket[count] = int(round((1-combination)*item + combination*avgvalue))
        avgvalue = 0 #balance the cannon markets
        for item in towns:
            avgvalue += item.getcannonmarket() / len(towns)
        self.cannonmarket = int(round((1-combination)*self.cannonmarket + combination*avgvalue))
        avgvalue = 0 #balance the space markets
        for item in towns:
            avgvalue += item.getspacecost() / len(towns)
        self.spacecost = int(round((1-combination)*self.spacecost + combination*avgvalue))
    def fluctuatemarkets(self):
        #fluctuate the cannon markets
        self.cannonmarket = fluctuate(self.cannonmarket,cannonfluctuation)    
        #fluctuate the space markets
        self.spacecost = fluctuate(self.spacecost,spacefluctuation)
        #fluctuate normal market
        count = -1
        for item in self.market: 
            count += 1
            self.market[count] = fluctuate(self.market[count],fluctuation[count])
        #fluctuate shipmarket
        count = -1
        for item in self.shipmarket: 
            count += 1
            self.shipmarket[count] = fluctuate(self.shipmarket[count],shipfluctuation[count])
    def fluctuatemarket(self): #main function
        self.fluctuatemarkets()
        self.balancemarkets()

#=========================================================================
#-------------------------------GENERAL GAME FUNCTIONS--------------------------------    
#========================================================================= 

#=========================================================================
#-------------------------------AT SEA--------------------------------    
#========================================================================= 

#-------------------------------MAIN FUNCTION-------------------------------- 

def getdestination(): #sailing
    count = -1
    for item in towns:
        count += 1
        print str(count) + " : " + item.getname()
        
    destination = int(raw_input("Where would you like to go?: "))
    
    if destination != playerlocation: #basically by going to the town you are already at, you are clicking the back button
        sailing = True
        passtime()
        sailing = False
        
        noevent = True #events that can take place
        if random.randint(0,100) < stormchance:
            destination = storm(destination)
            noevent = False
        if random.randint(0,100) < piratechance:
            pirate(0)
            noevent = False
        if noevent:
            raw_input("Nothing worth noting.")
            
        if playerbank.getbalance() > 0 and playercash.getbalance() > -playerbank.getbalance() * repay: #forced repayment to the moneylender
            playercash.deposit(playerbank.getbalance())
            playerbank.deposit(-playerbank.getbalance())
        
    return destination

#-------------------------------STORM-------------------------------- 

def storm(destination):
    harmlessstorm = True
    if random.randint(0,100) < stormdamagechance:
        raw_input("A storm did quite a bit of damage...I'm going to have to repair my ships")
        harmlessstorm = False
        playerfleet.stormdamage()
        checkgameover()
    if random.randint(0,100) < stormreturnchance:
        harmlessstorm = False
        destination = playerlocation
        raw_input("A storm made us retreat to " + towns[playerlocation].getname())
    elif random.randint(0,100) < stormthrowoffchance:
        newdestination = random.randint(0,len(towns)-1)
        if destination != newdestination: #because if you get blown off course to the same town it doesn't really do much
            destination = newdestination
            raw_input("A storm threw us off course to " + towns[destination].getname())
            harmlessstorm = False
    if random.randint(0,100) < stormdelaychance:
        harmlessstorm = False
        raw_input("A storm left us lost at sea for a month")
        passtime()
    if harmlessstorm:
        raw_input("There was a storm but we made it through.")
    return destination

#-------------------------------BATTLE-------------------------------- 

piratefleet = fleet([]) #this is a global variable, even though it is only used inside a function.  For the sake of allowing a functions to activate within functions.
def displaybattlefleet(fleet):
    count = -1
    for item in fleet.getfleet():
        count += 1
        print "I : Type \tHp \tCannons"
        print str(count) + " : " + item.getname(),
        print "\t" + str(item.gethp()) + "/" + str(item.getmaxhp()),
        print "\t" + str(item.getcannons())
def printbattledata():
    print line2
    print "BATTLE!"
    print line1
    print "PLAYER FLEET:"
    print line2
    displaybattlefleet(playerfleet)
    print line1
    print "ENEMY FLEET:"
    displaybattlefleet(piratefleet)
    print line1
def getbattleorder():
    print "1: Fight"
    print "2: Flee"
    print line2
    return raw_input("What should we do, Captain?: ")
def generatepiratefleet(): # to contrast with the net yet existing generatemerchantfleet
    #max_enemy_strength = playerfleet.getmaxstorage()^2 / playerfleet.getmaxcannons() * strength * strengthcoefficient
    
    global piratefleet
    enemyships = []
    max_enemy_strength = getcurrentplayerworth() * random.uniform(0,piratestrength)
    enemystrength = 0
    battleships = [0,5,6,7,8]
    drawpool =    [3,5,4,3,1]
    
    count = -1
    for item in drawpool:
        count += 1
        if count != 0:
            drawpool[count] += drawpool[count - 1] #gives each ship a number, if the random is less than or equal to that number, but greater than the number given to the one before it, that ship is selected.
        
    while True:
        shipnumber = random.randint(1,drawpool[-1])
        count = -1
        for item in drawpool:
            count += 1
            if shipnumber <= item:
                shipindex = battleships[count]
                break
        enemystrength += localshipmarket[shipindex]
        enemystrength += random.randint(0,shipmaxcannons[shipindex]*standard_pirate_cannon_concentration) * towns[playerlocation].getcannonmarket() #No, the added number is not the number of cannons that were actually added.  But this adds to the randomness.
        
        if enemystrength >= max_enemy_strength:
            break
        
        enemyships.append (ship(shipindex,shipstorage[shipindex],shiphp[shipindex],shiphp[shipindex],random.randint(0,shipmaxcannons*standard_pirate_cannon_concentration),shipmaxcannons[shipindex]))
    piratefleet.replacefleet(enemyships)
    
    return int(random.uniform(0, piratestrength * lootpercent * getplayerworth()))
        
def pirate(strengthindex):
    global piratefleet
    global playerkills
    
    if strengthindex == 0:
        loot = generatepiratefleet()
    if piratefleet.getcannons() != 0:        
        
        printbattledata()    
        nonretreat = True
        while len(playerfleet.getfleet()) > 0 and len(piratefleet.getfleet()) > 0 and nonretreat: #while player and pirate still have ships and player does not want to retreat
            order = getbattleorder()
            if order == "1":
                playerfleet.attack(piratefleet)
                piratefleet.attack(playerfleet)
            if order == "2":
                piratefleet.attack(playerfleet)
                nonretreat = False
                raw_input("Fled like the coward you were to a random location.")
                destination = random.randint(0,len(towns)-1)
            printbattledata() #placed here so you see the statistics when you die or flee
            
        checkgameover()       
                
        if nonretreat:
            raw_input("We got $" + str(loot) + "!")
            playercash.deposit(loot)
            playerkills += 1

#=========================================================================
#-------------------------------AT TOWN--------------------------------    
#=========================================================================    

def displaytime():
    months = ["troll","January","Febuary","March","April","May","June","July","August","September","October","November","December"]
    return months[time[0]] + ", Year " + str(time[1]) #eg January 1
    
line2 = ""
line1 = "\n================================================================================\n"

def printgeneraldata():
    os.system('clear')
    print line2
    print "DATE: ", displaytime()
    print "TOWN: ",towns[playerlocation].getname()
    print line2
    print "CASH: $" + str(playercash.getbalance())
    print "BANK: $" + str(playerbank.getbalance())
    print "FLEET: " + str(spaceused(playerstock) + playerfleet.getmaxstorage() - playerfleet.getstorage()) + "/" + str(playerfleet.getmaxstorage()) #maxstorage - storage = space taken up by cannons
    print line1

def printinterface():
    printgeneraldata()
    print "MARKET: "
    print line2
    print "I : \tname         \tcost \tOwned \tWarehouse" 
    count = -1
    for item in goods:
        count += 1
        print str(count) + " : \t" + item + "\t" + str(localmarket[count]) + "\t" + str(playerstock[count]) + "\t" + str(towns[playerlocation].getwarehouse()[count])
    print line1

def getorder():
    print "0: Set sail"
    print "1: Buy goods for fleet"
    print "2: Buy goods for warehouse"
    print "3: Waste time"
    print "4: Manage Ships"
    print "5: Visit warehouse"
    print "6: Check databooks"
    print "7: Visit bank"
    print "8: Visit shipyard"
    return raw_input("What would you like to do?: ")

def getpurchase(store_location): #where store location is either playerstock or towns[playerlocation].getwarehouse()
    purchase = [int(raw_input("What would you like to buy?: ")),int(raw_input("How much would you like to buy?: "))]
    totalprice = localmarket[purchase[0]] * purchase[1]
    if totalprice > playercash.getbalance(): #prevent a user from buying more than he can afford
        purchase[1] = playercash.getbalance() / localmarket[purchase[0]]
        raw_input("I can't afford that much, but I'll buy what I can afford...")
    if purchase[1] > playerfleet.getstorage()-spaceused(store_location): #prevent a user from buying more than he can store
        purchase[1] = playerfleet.getstorage()-spaceused(store_location)
        raw_input("I can't store that much, but I'll buy what I can store")
    if purchase[1] + store_location[purchase[0]] < 0: #prevent a user from selling more than he has
        purchase[1] = -store_location[purchase[0]]
        raw_input("I'll sell everything I have of that item")
    return purchase

#-------------------------------MANAGE FLEET--------------------------------    

def displayfleet(fleet): #only for use at the ship market
    count = -1
    for item in fleet.getfleet():
        count += 1
        print "I : Type \tPrice \tStorage \tHp \tCannons \tMax cannons"
        print str(count) + " : " + item.getname(),
        print "\t" + str(item.getprice()),
        print "\t" + str(item.getmaxstorage()),
        print "\t\t" + str(item.gethp()) + "/" + str(item.getmaxhp()),
        print "\t" + str(item.getcannons()),
        print "\t\t" + str(item.getmaxcannons())
def getfleetorder():
    printgeneraldata()
    print "PLAYER FLEET:"
    print line2
    displayfleet(playerfleet)
    print line1

    print "FLEET MARKET:"
    print line2
    
    print "I : Type \tPrice"    
    count = -1
    for item in shipname:
        count += 1
        print str(count) + " : " + item + "\t$" + str(localshipmarket[count])
        
    print line2
    print "CANNONS     : $" + str(localcannonmarket)
    print "USED CANNONS: $" + str(int(localcannonmarket * cannontax))
    print line1
    
    print "0: Stop managing fleet"
    print "1: Sell ship"
    print "2: Buy ship"
    print "3: Buy cannons"
    print "4: Buy cannons for shipyard"
    print "5: Repair fleet: $" + str(playerfleet.getrepaircost())
    print "6: Repair ship"
    
    return raw_input("What would you like to do? :")
def buycannons():
    purchase = [int(raw_input("Which ship would you like to buy cannons for?: ")),int(raw_input("How many cannons would you like to buy?: "))]
                
    if playerfleet.getfleet()[purchase[0]].getcannons() + purchase[1] > playerfleet.getfleet()[purchase[0]].getmaxcannons(): #prevent a player from buying more cannons than can be loaded onto the ship
        raw_input("I can't fit that many onto my ship, but I'll load on what I can...")
        purchase[1] = playerfleet.getfleet()[purchase[0]].getmaxcannons() - playerfleet.getfleet()[purchase[0]].getcannons()
    if purchase[1] * localcannonmarket > playercash.getbalance(): #prevent a player from buying more cannons than can be afforded
        raw_input("I can't buy that many, but I'll buy what I can afford...")
        purchase[1] = int( playercash.getbalance() / localcannonmarket )
    if purchase[1] + playerfleet.getfleet()[purchase[0]].getcannons() < 0: #prevent a player from selling more cannons than he has
        raw_input("I'll sell all the cannons I have on this ship.")
        purchase[1] = -playerfleet.getfleet()[purchase[0]].getcannons()
        
    if purchase[1] < 0:
        playercash.deposit(-int(purchase[1] * localcannonmarket * cannontax))
    else:
        playercash.deposit(-purchase[1] * localcannonmarket)
        
    playerfleet.givecannon(purchase[0],purchase[1])   
def buycannonsforshipyard():
    purchase = int(raw_input("How many cannons would you like to buy?: "))
                
    if towns[playerlocation].shipyard() - towns[playerlocation].shipyardspaceused() < purchase * cannonstorage: #prevent a player from buying more cannons than can be loaded into the warehouse
        raw_input("I can't fit that many, but I'll load what I can...")
        purchase = ( towns[playerlocation].shipyard() - towns[playerlocation].shipyardspaceused() ) / cannonstorage
    if purchase[1] * localcannonmarket > playercash.getbalance(): #prevent a player from buying more cannons than can be afforded
        raw_input("I can't buy that many, but I'll buy what I can afford...")
        purchase = int( playercash.getbalance() / localcannonmarket )
    if purchase + towns[playerlocation].getcannons() < 0: #prevent a player from selling more cannons than he has
        raw_input("I'll sell all the cannons I have.")
        purchase = -towns[playerlocation].getcannons()
        
    if purchase[1] < 0:
        playercash.deposit(-int(purchase[1] * localcannonmarket * cannontax))
    else:
        playercash.deposit(-purchase[1] * localcannonmarket)
        
    towns[playerlocation].givecannons(purchase)
    
#-------------------------------WAREHOUSE--------------------------------    
    
def printwarehousedata():
    
    item = towns[playerlocation]
    
    print line2
    print "Available space: " + str(item.getwarehousestorage())
    print "I : Good \tStock"
    count = -1
    for item2 in goods:
        count += 1
        print str(count) + " : " + item2 + "\t" + str(item.getwarehouse()[count])
def printallwarehousedata():
    printgeneraldata()
    print "FLEET"
    print "I : Good \tStock"
    count =-1
    for item in goods:
        count += 1
        print str(count) + " : " + item + "\t" + str(playerstock[count])
    
    print line1
    print "WAREHOUSES"
    
    for item in towns:
        print line2
        print item.getname() + "(Available space: " + str(item.getwarehousestorage()) + ")"
        print "I : Good \tStock"
        count = -1
        for item2 in goods:
            count += 1
            print str(count) + " : " + item2 + "\t" + str(item.getwarehouse()[count])
    raw_input("Back: ")
def getwarehouseorder():
    printgeneraldata()
    print "FLEET"
    print "I : Good \tStock"
    count =-1
    for item in goods:
        count += 1
        print str(count) + " : " + item + "\t" + str(playerstock[count])
    
    print line1
    print "WAREHOUSE"
    print line2
    print "Cost per unit: $" + str(towns[playerlocation].getspacecost())
    printwarehousedata()
    print "0: Back"
    print "1: Transfer goods to warehouse"
    print "2: Buy more space"
    print "3: See all warehouses"
    print line2
    return raw_input("What would you like to do?: ")
def buyspace(location): #used for both warehouse and storage
    morespace = int(raw_input("How much space do you want to buy?: "))
    if location == "warehouse":
        if morespace * towns[playerlocation].getspacecost() > playercash.getbalance():
            raw_input("Bought as much space as I could.")
            morespace = playercash.getbalance()/towns[playerlocation].getspacecost()
        if morespace + towns[playerlocation].getwarehousestorage() < 0:
            raw_input("Got rid of my warehouse")
            morespace = towns[playerlocation].getwarehousestorage()
        towns[playerlocation].givewarehouse(morespace)
        if morespace < 0:
            playercash.deposit(-int(morespace * towns[playerlocation].getspacecost() * warehousetax))
        else:
            playercash.deposit(-morespace * towns[playerlocation].getspacecost())
    if location == "shipyard":
        if morespace * towns[playerlocation].getspacecost() * lakefrontproperty > playercash.getbalance():
            raw_input("Bought as much space as I could.")
            morespace = playercash.getbalance()/ ( towns[playerlocation].getspacecost() * lakefrontproperty )
        if morespace + towns[playerlocation].getshipyardstorage() < 0:
            raw_input("Got rid of my shipyard")
            morespace = towns[playerlocation].getshipyardstorage()
        towns[playerlocation].giveshipyardstorage(morespace)
        if morespace < 0:
            playercash.deposit(-int(morespace * towns[playerlocation].getspacecost() * lakefrontproperty * warehousetax))
        else:
            playercash.deposit(-morespace * towns[playerlocation].getspacecost() * lakefrontproperty)
            
def getshipyardorder():
    printgeneraldata()
    print "FLEET"
    displayfleet(playerfleet)
    print line1
    print "SHIPYARD"
    print line2
    print "Storagespace: " + str(towns[playerlocation].getshipyardstorage())
    print "Extra cannons: " + str(towns[playerlocation].getextracannons())
    print "Cost per unit: $" + str(towns[playerlocation].getspacecost() * lakefrontproperty)
    displayfleet(towns[playerlocation].getshipyard())
    print line1
    print "0: Back"
    print "1: Store ship"
    print "2: Take ship"
    print "3: Store cannons"
    print "4: Buy storage"
    return raw_input("What would you like to do?: ")
        
#-------------------------------INITIALIZE--------------------------------               

displacement = initaildisplacement #initail economy strengh.  The economy was the only thing that required somewhat complicated background calculations, so there should not be any conflict even if I use seemingly irrevelant physics terms
velocity = 0.0 #initail economy motion

def seizecontraband():
    if towns[playerlocation].getwar() == 0 and random.randint(0,100) > contraband and (playerstock[5] > 0 or playerstock[6] > 0): #where stocks 6 and 7 are gunpowder and opium, both contraband
        raw_input(str(playerstock[5]) + " units of gunpowder and " + str(playerstock[6]) + "units of opium have been seized from the fleet.")
        playerstock[5] = 0
        playerstock[6] = 0
    if towns[playerlocation].getwar() > 0 and random.randint(0,100) > contraband and playerstock[6] > 0: #where stock 6 are opium, contraband
        raw_input(str(playerstock[6]) + "units of opium have been seized from the fleet.")
        playerstock[6] = 0
    
    count = -1
    for item in towns:
        count += 1
        if item.getwar() == 0 and random.randint(0,100) > warehousecontraband and (item.getwarehouse()[6] > 0 or item.getwarehouse()[5] > 0): #where stocks 5 and 6 are gunpowder and opium, both contraband
            raw_input(str(item.getwarehouse()[5]) + " units of gunpowder and " + str(item.getwarehouse()[6]) + "units of opium have been seized from the warehouse in " + item.getname() + ".")
            towns[count].storegoods(5,-item.getwarehouse()[5])
            towns[count].storegoods(6,-item.getwarehouse()[6])
        if item.getwar() > 0 and random.randint(0,100) > warehousecontraband and item.getwarehouse()[6] > 0: #where stocks 6 are opium, both contraband
            raw_input(str(item.getwarehouse()[6]) + "units of opium have been seized from the warehouse in " + item.getname() + ".")
            towns[count].storegoods(6,-item.getwarehouse()[6])

def getplayerworth():
    worth = getcurrentplayerworth()
    for item in towns: #shipyardfleet
        for item2 in item.getshipyard().getfleet():
            worth += item2.getprice()
    for item in towns:
        worth += item.getextracannons() * item.getcannonmarket()
    for item in towns: #warehouse
        count = -1
        for item2 in item.getwarehouse():
            count += 1
            worth += item2 * localmarket[count]
    return worth

def getcurrentplayerworth():
    worth = playercash.getbalance() + playerbank.getbalance() #cash and bank
    for item in playerfleet.getfleet(): #fleet
        worth += item.getprice()
    count = -1
    for item in playerstock(): #stock
        count += 1
        worth += localmarket[count] * item
    return worth
            
def checkgameover():
    if len(playerfleet.getfleet()) == 0:
        os.system('clear')
        raw_input("\n\n\nGame over...")
        "string" + 0 #aka generate a syntax error 

time = [1,1] #month, year
def passtime():
    
    updatejournal() #update journal comes before, since we don't really need to know what's going on at the moment

    global time
    time[0] += 1
    if time[0] > 12:
        time[0] = 1
        time[1] += 1
        
    global towns
    for item in towns:
        item.fluctuatemarket()
        
    if sailing: #only make the player's ships go down in value if sailing
        playerfleet.passtime()
    
    if playerbank.getbalance() > 0:
        playerbank.deposit(int(playerbank.getbalance() * bankinterest))
    else:
        playerbank.deposit(int(playerbank.getbalance() * deptinterest))
    
    seizecontraband()
    
    global velocity
    global displacement
    
    velocity -= displacement * random.uniform(0,0.05)
    displacement += velocity * random.uniform(0,2)
    #war
    count = -1
    for item in towns:
        count += 1
        towns[count].progresswar()
    
    if time[0] == 1: #for the explorer union makes its decision in january
        earlyarrival = False
        latearrival = False
        if displacement < initaildisplacement:
            westernexpedition = False
        else:
            westernexpedition = True
            if random.randint(0,100) < earlyarrival:
                earlyarrival = True
            elif random.randint(0,100) < latearrival:
                latearrival = True

playerkills = 0 #just a statistic used in the quests                
                
playercash = moneystorage(0)
playerbank = moneystorage(0)
playerfleet = fleet([])
playerfleet.giveship(0)
playerlocation = 0 #the index of the town
playerstock = [0,0,0,0,0,0,0] #what and how many items the player has

def spaceused(store_location):
    spaceused = 0
    for item in store_location:
        spaceused += item
    return spaceused

alltowns = []
towns = []
alltowns.append(town("Agorea",[12,97,152,290,530,1102,2450],startingshipmarket,startingcannonprice,100,"The starting town.  Prices here tend to be low when the game starts."))
alltowns.append(town("Sarantion",[60,233,234,556,1055,2335,2502],startingshipmarket,startingcannonprice,100,"A great town that was bombed during the great war.  It is not so great now, but many people are trying to use up resources to rebuild it."))
alltowns.append(town("Cirania",[29,123,134,356,755,1735,3002],startingshipmarket,startingcannonprice,200,"A town by the ocean.  The western expedition passes Cirania and has its impacts on the economy there.  A gathering-place for merchants."))
alltowns.append(town("Cromon",[29,123,134,356,755,1735,3002],startingshipmarket,startingcannonprice,100,"The underground capitol, gathering place of pirates and mafia."))
alltowns.append(town("Thoramin",[29,123,134,356,755,1735,3002],startingshipmarket,startingcannonprice,100,"A great empire, that still stands proud after the war."))

def newtown(index):
    towns.append(alltowns[index])
    databooks[0].addtext(alltowns[index].getname() + ": \n" + alltowns[index].getprofile())
    
newtown(0)
newtown(1)
newtown(2)
newtown(3)
newtown(4)

#========================================================================
#-------------------------------GAME--------------------------------    
#========================================================================= 

sailing = False

while True:
    try:
        localmarket = towns[playerlocation].getmarket()
        localshipmarket = towns[playerlocation].getshipmarket()
        localcannonmarket = towns[playerlocation].getcannonmarket()
        
        printinterface()
        order = getorder()
        
        #-------------------------------GET MUGGED--------------------------------      
        
        if random.randint(0,1000) < muggedchance:
            if random.randint(0,100) < muggeddelaychance:
                raw_input("You were mugged of all your money and sent to the hospital for a month")
                playercash.deposit(-playercash.getbalance())
                passtime()
            else:
                raw_input("You were mugged of all your money")
                playercash.deposit(-playercash.getbalance())
                
        #-------------------------------ORDERS--------------------------------      
         
        if order == "0":
            playerlocation = getdestination()
        if order == "1": #buy goods for fleet
            purchase = getpurchase(playerstock)
            playercash.deposit(purchase[1] * localmarket[purchase[0]] * -1)
            playerstock[purchase[0]] += purchase[1]
        if order == "2": #buy goods for warehouse
            purchase = getpurchase(towns[playerlocation].getwarehouse())
            playercash.deposit(purchase[1] * localmarket[purchase[0]] * -1)
            towns[playerlocation].storegoods(purchase[0],purchase[1])
        if order == "3": #passtime
            passtime()
        if order == "4": #manage fleet
            fleetorder = "not zero"
            while fleetorder != "0":
                fleetorder = getfleetorder()
                if fleetorder == "1": #sellship
                    shipindex = int(raw_input("Which ship would you like to sell? "))
                    if playerfleet.getstorage() - playerfleet.getfleet()[shipindex].getstorage() < spaceused(playerstock): #prevent users from selling ships and having more goods than they can store
                        raw_input("Where will you leave your goods?")
                    elif playerfleet.getfleet()[shipindex].gethp() != playerfleet.getfleet()[shipindex].getmaxhp():
                        raw_input("I can't sell a damaged ship...")
                    else:
                        playercash.deposit(playerfleet.getfleet()[shipindex].getprice())
                        playerfleet.takeship(shipindex)
                if fleetorder == "2": #buy ship
                    shipindex = int(raw_input("Which ship would you like to buy? "))
                    if playercash.getbalance() < localshipmarket[shipindex]:
                        print raw_input("You do not have enough cash")
                    else:
                        playerfleet.giveship(shipindex)
                        playercash.deposit(-localshipmarket[shipindex])
                if fleetorder == "3": #buy cannons
                    buycannons()
                if fleetorder == "4":
                    buycannonsforshipyard()
                if fleetorder == "5": #repair fleet
                    if playercash.getbalance() < playerfleet.getrepaircost():
                        raw_input("I do not have enough cash.")
                    else:
                        playercash.deposit(-playerfleet.getrepaircost())
                        playerfleet.repair()
                if fleetorder == "6": #repair ship
                    shipforrepair = raw_input("Which ship would you like to repair?: ")
                    if playercash.getbalance() < playerfleet.getfleet()[shipforrepair].getrepaircost():
                        raw_input("I do not have enough cash.")
                    else:
                        playercash.deposit(-playerfleet.getfleet()[shipforrepair].getrepaircost())
                        playerfleet.repairship(shipforrepair)
        if order == "5": #visit warehouse
            warehouseorder = ""
            while warehouseorder != "0":
                warehouseorder = getwarehouseorder()
                if warehouseorder == "1":
                    transfer = [int(raw_input("Which good do you want to transfer?: ")),int(raw_input("How much do you want to store?: "))]
                    if transfer[1] > playerstock[0]:
                        raw_input("I'll store everything I got of that good.")
                        transfer[1] = playerstock[0]
                    if transfer[1] > towns[playerlocation].getwarehousestorage() - spaceused(towns[playerlocation].getwarehouse()):
                        raw_input("I'll store everthing I can fit.")
                        transfer[1] = towns[playerlocation].getwarehousestorage() - spaceused(towns[playerlocation].getwarehouse())
                    if transfer[1] + towns[playerlocation].getwarehouse()[transfer[0]] < 0:
                        raw_input("I'll take out everything I have of that good.")
                        transfer[1] = -towns[playerlocation].getwarehouse()[transfer[0]]
                    if spaceused(playerstock) - transfer[1] > playerfleet.getstorage():
                        raw_input("I'll move everything I can.")
                        transfer[1] = playerfleet.getstorage() - spaceused(playerstock)
                        
                    playerstock[0] -= transfer[1]
                    towns[playerlocation].storegoods(transfer[0],transfer[1])
                if warehouseorder == "2":
                    buyspace("warehouse")
                if warehouseorder == "3":
                    printallwarehousedata()
        if order == "6": #check databooks 
            count = -1
            for item in databooks:
                count += 1
                print str(count) + " : " + item.getname()
            databaseorder = int(raw_input("Which book would you like to read?: "))
            printgeneraldata()
            databooks[databaseorder].printdata()
            raw_input("Done.")
        if order == "7": #bank
            print "Bank Interest : " + str(bankinterest)
            print "Dept Interest : " + str(deptinterest)
            print line2
            deposit = int(raw_input("How much money do you want to deposit to the bank?: $"))
            if deposit > playercash.getbalance():
                raw_input("I'll deposit everything I have")
                deposit = playercash.getbalance()
            if deposit + playerbank.getbalance() < 0 and playerbank.getbalance() > 0:
                deposit = -playerbank.getbalance()
                raw_input("I'll withdraw everything")
            if deposit < 0 and playerbank.getbalance() <= 0 and deposit < -getplayerworth() * credit:
                deposit = -getplayerworth() * credit
                raw_input("I'll borrow everything he lets me.")
            playerbank.deposit(deposit)
            playercash.deposit(-deposit)
        if order == "8": #visit shipyard
            shipyardorder = ""
            while shipyardorder != "0":
                shipyardorder = getshipyardorder()
                if shipyardorder == "1": #store ship
                    shipindex = int(raw_input("Which ship you do want to store?: "))
                    if towns[playerlocation].getshipyardstorage() - towns[playerlocation].getshipyardstorageused() < playerfleet.getfleet()[shipindex].getsize():
                        raw_input("My ship takes too much room. ")
                    elif spaceused(playerstock) > playerfleet.getstorage() - playerfleet.getfleet()[shipindex].getstorage():
                        raw_input("I won't be able to hold all my goods.")
                    else:
                        towns[playerlocation].giveship(shipindex)
                if shipyardorder == "2": #get ship
                    shipindex = int(raw_input("Which ship do you want to take out?"))
                    towns[playerlocation].takeship(shipindex)
                if shipyardorder == "3": #store cannons
                    storecannons = [int(raw_input("Which ship do you want to move cannons from?: ")),int(raw_input("How many cannons do you want to move?: "))]
                    if storecannons[1] > playerfleet.getfleet()[storecannons[0]].getcannons():
                        raw_input("I'll store all the cannons I have on that ship")
                        storecannons[1] = playerfleet.getfleet()[storecannons[0]].getcannons()
                    if -storecannons[1] + playerfleet.getfleet()[storecannons[0]].getcannons() > playerfleet.getfleet()[storecannons[0]].getmaxcannons():
                        storecannons[1] = -playerfleet.getfleet()[storecannons[0]].getmaxcannons() - playerfleet.getfleet()[storecannons[0]].getcannons()
                        raw_input("Loaded as many cannons as I could fit on the ship")
                    if -storecannons[1] > towns[playerlocation].getshipyardextracannons():
                        raw_input("Moved all my extra cannons onto the ship: ")
                        storecannons[1] = towns[playerlocation].getshipyardextracannons()
                    if storecannons[1] * cannonsizestorage > towns[playerlocation].getshipyardstorage()-towns[playerlocation].getshipyardstorageused:
                        raw_input("Loaded as many cannons as I could fit in the warehouse")
                    playerfleet.givecannon(storecannons[1],storecannons[0])
                if shipyardorder == "4": #buy more space
                    buyspace("shipyard")
    except:
        raw_input("Generated unknown error")
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            