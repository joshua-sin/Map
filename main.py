class Map(object):
    global id
    def __init__(self,name):
        self.zones = []
        self.name = name

    def get_name(self):
        return self.name
    
    def set_name(self,new):
        self.name = new
        return self.get_name()

    def get_id(self):
        return self.id
    
    def set_id(self,new):
        self.id = new
        return self.get_id()

    def get_zones(self):
        return self.zones
    
    def set_zones(self,new):
        self.zones = new
        return self.get_zones()

    def add_zone(self,zone):
        curr = self.get_zones()
        curr.append(zone)
        self.set_zones(curr)
        return self.get_zones()
    
    def __repr__(self):
        return str('Map of ' + self.get_name())

    def __str__(self):
        return str(self.get_name())
        

class Zone(object):
    def __init__(self,name,id):
        self.levels = []
        self.name = name
        self.id = id

    def get_name(self):
        return self.name
    
    def set_name(self,new):
        self.name = new
        return self.get_name()

    def get_id(self):
        return self.id
    
    def set_id(self,new):
        self.id = new
        return self.get_id()
    
    def get_levels(self):
        return self.levels
    
    def set_levels(self,new):
        self.levels = new
        return self.get_levels()

    def add_level(self,level):
        curr = self.get_levels()
        curr.append(level)
        self.set_levels(curr)
        return self.get_levels()
    
    def __repr__(self):
        return str(self.get_name())

    def __str__(self):
        return str(self.get_name())

class Level(object):
    def __init__(self,name,number):
        self.connectors = []
        self.nodes = []
        self.name = name
        self.number = number

    def get_name(self):
        return self.name
    
    def set_name(self,new):
        self.name = new
        return self.get_name()

    def get_number(self):
        return self.number
    
    def set_number(self,new):
        self.number = new
        return self.get_number()

    def get_nodes(self):
        return self.nodes
    
    def set_nodes(self,new):
        self.nodes = new
        return self.get_nodes()

    def add_node(self,node):
        curr = self.get_nodes()
        curr.append(node)
        self.set_nodes(curr)
        return self.get_nodes()

    def __repr__(self):
        return str(self.get_name())

    def __str__(self):
        return str(self.get_name())

class Node(object):
    def __init__(self,name,area,level,x,y):
        self.name = name
        self.area = area
        self.level = level
        self.x = x
        self.y = y
        level.add_node(self)

    def get_type(self):
        return self.type

    def set_type(self, new):
        self.type = new
        return get_type(self)

    def get_x(self):
        return self.x

    def set_x(self,new):
        self.x = new
        return self.get_x()

    def get_y(self):
        return self.y

    def set_y(self,new):
        self.y = new
        return self.get_y()
    
    def get_name(self):
        return self.name
    
    def set_name(self,new):
        self.name = new
        return self.get_name()
    
    def __repr__(self):
        return str(self.get_name())

    def __str__(self):
        return str(self.get_name())
    
class Classroom(Node):
    def __init__(self,name,area,level,x,y,civics_class):
        super().__init__(name,area,level,x,y)
        self.civics_class = civics_class

    def get_civics(self):
        return self.civics_class
    
    def set_civics(self,new):
        self.civics_class = new
        return self.get_civics()
    
    def __repr__(self):
        return str(self.get_name())
    
    def __str__(self):
        return str(self.get_name())

class Stairs(Node):
    def __init__(self, a, b):
        self.a = a
        self.b = b
        #a and b are levels that the stairs connect

    def get_a(self):
        return self.a

    def set_a(self,new):
        self.x = new
        return self.get_a()

    def get_b(self):
        return self.x

    def set_b(self,new):
        self.x = new
        return self.get_x()

class Lift(Node):
    def __init__(self, levels):
        self.levels = levels
        

m = Map('RI')
a = Zone('Raja',1)
b = Zone('Sheares',2)

rl1 = Level('rl1',1)
rl2 = Level('rl2',2)
rl3 = Level('rl3',3)
rl4 = Level('rl4',4)
rl5 = Level('rl5',5)
rl6 = Level('rl6',6)
rl7 = Level('rl7',7)
raja_levels = [rl1,rl2,rl3,rl4,rl5,rl6,rl7]
for r in raja_levels:
    a.add_level(r)

g0201 = Node('g0201',a,rl2,0,0)
g0202 = Classroom('g0202',a,rl2,1,0,'s06g')

m.add_zone(a)
m.add_zone(b)



