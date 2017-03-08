#space rouge
#Python 2.7
import IOlib
import random
class System:
	max_distance=1000

	def __init__(self):
		self.name = self.randomize_name()
		self.planets = []
		self.coX = self.random_co()
		self.coY = self.random_co()
		self.gas_chance = self.randomize_gas()
		self.generate_planets()

	def generate_planets(self):
		for x in range(0,3):
			p = Planet(self)
			#print p.name
			self.planets.append(p)

	def randomize_name(self):
		return "System-"+str(random.randint(1000,9999))
		
	def random_co(self):
		return random.randint(0,self.max_distance)

	def randomize_gas(self):
		return random.randint(25,75)

	def check_name(self):
		return self.name
	def check_coX(self):
		return self.coX
	def check_coY(self):
		return self.coY
	def check_all_planets(self):
		o = ""
		for x in range(0,len(self.planets)):
			o += "\n"
			o += self.planets[x].check_name()
			o += "\n"
			o += self.planets[x].check_composition()
			o += "\n"
			o += str(self.planets[x].check_hazard())
			o += "\n"
			o += "\n"
		return o
	def check_gas_chance(self):
		return self.gas_chance

class Planet:
	max_hazard = 25
	def __init__(self,system_info):
		#system_info must be an instance of System class
		self.system_info = system_info
		self.name = self.randomize_name()
		self.composition = self.randomize_composition()
		self.hazard = self.randomize_hazard()

	def randomize_name(self):
		return "Planet-"+str(random.randint(1000,9999))

	def randomize_composition(self):
		check = random.randint(0,100)
		if(check >= self.system_info.check_gas_chance()):
			return "Gas"
		else:
			return "Solid"

	def randomize_hazard(self):
		return random.randint(0,self.max_hazard)

	def check_name(self):
		return self.name
	def check_composition(self):
		return self.composition
	def check_hazard(self):
		return self.hazard

class Element_Stack:
	def __init__(self, name, description, size):
		self.name = name
		self.description = description
		self.size = size
		self.amount = 1
	def check_name(self):
		return self.name
	def check_descritption(self):
		return self.description
	def check_size(self):
		return self.size
	def check_amount(self):
		return self.amount

	def add(self,amount):
		self.amount = self.amount + amount

	def remove(self,amount):
		if(self.amount >= amount):
			self.amount = self.amount - amount
			return True
		else:
			return False

class Ship:
	max_ship_size = 10
	min_ship_size = 1
	max_storage = 200
	min_storage = 50
	max_shield_size = 125
	min_shield_size = 25
	max_tank_size = 1000
	min_tank_size = 250
	min_fuel_cost = 1
	max_fuel_cost = 20

	def __init__(self,X,Y,name="rand",ship_size=1234,storage_size=1234,shield_size=1234,fuel_tank_size=1234,fuel_cost=1234):
		self.loc_x = X
		self.loc_y = Y

		self.inventory = []

		if(name=="rand"):
			self.name = self.randomize_name()
		else:
			self.name = name

		if(ship_size==1234):
			self.ship_size = random.randint(self.min_ship_size,self.max_ship_size)
		else:
			self.ship_size = ship_size

		if(storage_size==1234):
			self.storage_size = random.randint(self.min_storage,self.max_storage) * self.ship_size
		else:
			self.storage_size = storage_size

		if(shield_size==1234):
			self.shield_size = random.randint(self.min_shield_size,self.max_shield_size) * self.ship_size
		else:
			self.shield_size = shield_size

		if(fuel_tank_size==1234):
			self.fuel_tank_size = random.randint(self.min_tank_size,self.max_tank_size) * self.ship_size
		else:
			self.fuel_tank_size = fuel_tank_size

		if(fuel_cost==1234):
			self.fuel_cost = random.randint(self.min_fuel_cost,self.max_fuel_cost) * self.ship_size
		else:
			self.fuel_cost = fuel_cost

		self.current_fuel = self.fuel_tank_size
		self.current_shield = self.shield_size
		self.current_storage_size = 0

	def randomize_name(self):
		return "Voyager-"+str(random.randint(1000,9999))

	def add_fuel(self, amount):
		if ((self.current_fuel + amount)<=self.max_tank_size):
			self.current_fuel = self.current_fuel + amount
			return True
		else:
			return False
	def remove_fuel(self, amount):
		if((self.current_fuel - amount)>=0):
			self.current_fuel = self.current_fuel - amount
			return True
		else:
			return False

	def add_inv_item(self,ITEM,amount=1):
		#ITEM should be an instance of Element_Stack
		found = False
		if (current_storage_size+ITEM.size >= self.max_storage):
			for x in range(0,len(self.inventory)):
				if (ITEM.name == self.inventory[x].name):
					#we already have item, add to stack
					self.inventory[x].amount=self.inventory[x].amount+amount
					found = True
					return True
			if (found == False):
				self.inventory[x].append(ITEM)
				self.inventory[x].amount = amount
				return True
		else:
			return False

	def remove_inv_item(self,ITEM,amount=1):
		#ITEM should be an instance of Element_Stack
		found = False
		for x in range(0,len(self.inventory)):
			if (ITEM.name == self.inventory[x].name):
				if(self.inventory[x].amount-amount > 0):
					self.inventory[x].amount=self.inventory[x].amount-amount
				elif (self.inventory[x].amount-amount == 0):
					self.inventory.remove(ITEM)
				else:
					return False
			found = True
			return True
		if (found == False):
			return False

	##CHECKS
	def check_loc_x(self):
		return self.loc_x
	def check_loc_y(self):
		return self.loc_y
	def check_name(self):
		return self.name
	def check_ship_size(self):
		return self.ship_size
	def check_storage_size(self):
		return self.storage_size
	def check_current_storage_size(self):
		return self.current_storage_size
	def check_shield_size(self):
		return self.shield_size
	def check_current_shield(self):
		return self.current_shield
	def check_fuel_tank_size(self):
		return self.fuel_tank_size
	def check_current_fuel(self):
		return self.current_fuel
	def check_fuel_cost(self):
		return self.fuel_cost



def Create_Elements():
	E_iron = Element_Stack("Iron","Used for shield repair.",5) 
	E_hydrogen = Element_Stack("Hydrogen","Fuel.",1)
	E_oxygen = Element_Stack("Oxygen","Keeps you alive.",1)  

def Start():
	io = IOlib.IO()
	io.say("starting")
	system = System()
	print system.check_name()
	print system.check_coX()
	print system.check_coY()
	print system.check_all_planets()

	ship1 = Ship(0,0)
	print "name: ",ship1.check_name()
	print "X: ",ship1.check_loc_x()
	print "Y: ",ship1.check_loc_y()
	print "ship size: ",ship1.check_ship_size()
	print "storage size: ",ship1.check_storage_size()
	print "current storage: ",ship1.check_current_storage_size()
	print "shield size: ",ship1.check_shield_size()
	print "current shield: ",ship1.check_current_shield()
	print "fuel tank size: ",ship1.check_fuel_tank_size()
	print "current fuel: ",ship1.check_current_fuel()
	print "fuel cost: ",ship1.check_fuel_cost()



Start()