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
        curr = list(self.get_zones())
        curr.append(zone)
        self.set_zones(curr)
        return self.get_zones()
    
    def __repr__(self):
        return str('Map of ' + self.get_name())

    def __str__(self):
        return str(self.get_name())
        

class Zone(object):
    def __init__(self,name,id,lifts=[],levels=[]):
        self.levels = []
        self.name = name
        self.lifts = []
        self.id = id

    def get_name(self):
        return self.name
    
    def set_name(self,new):
        self.name = new
        return self.get_name()

    def get_lifts(self):
        return self.lifts

    def set_lifts(self,new):
        self.lifts = new
        return self.get_lifts()

    def add_lift(self,new):
        curr = list(self.get_lifts())
        curr.append(new)
        self.lifts = curr
        return self.get_lifts()
    
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
        curr = list(self.get_levels())
        curr.append(level)
        self.set_levels(curr)
        return self.get_levels()
    
    def __repr__(self):
        return str(self.get_name())

    def __str__(self):
        return str(self.get_name())

class Level(object):
    def __init__(self,zone,name,number,nodes=[],edges=[]):
        self.edges = edges
        self.nodes = nodes
        self.name = name
        self.number = number
        self.zone = zone
        zone.add_level(self)

    def get_zone(self):
        return self.zone

    def set_zone(self,new):
        prev = self.get_zone()
        prev.set_levels(prev.get_levels().remove(self))
        self.zone = new
        return self.get_zone()

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
        curr = list(self.get_nodes())
        curr.append(node)
        self.set_nodes(curr)
        return self.get_nodes()

    def get_edges(self):
        return self.edges

    def set_edges(self,new):
        self.edges = new
        return self.get_edges()

    def add_edge(self,new):
        curr = list(self.get_edges())
        if new not in curr:
            curr.append(new)
        self.edges = curr
        return self.get_edges()

    def __repr__(self):
        return str(self.get_name())

    def __str__(self):
        return str(self.get_name())

class Node(object):
    def __init__(self,name,area,level,edges=[]):
        self.name = name
        self.area = area
        self.level = level
        level.add_node(self)
        self.edges = edges

    def get_edges(self):
        return self.edges

    def set_edges(self,new):
        self.edges = new
        return self.get_edges()

    def add_edge(self,new):
        self.level.add_edge(new)
        new_list = list(self.get_edges())
        new_list.append(new)
        self.edges = new_list
        return self.get_edges()
    
    def get_level(self):
        return self.level

    def set_level(self,new):
        prev = self.level
        prev.set_nodes(prev.get_nodes().remove(self))
        self.level = new
        return self.get_level()

    def get_type(self):
        return self.type

    def set_type(self, new):
        self.type = new
        return self.get_type()

##    def get_x(self):
##        return self.x
##
##    def set_x(self,new):
##        self.x = new
##        return self.get_x()
##
##    def get_y(self):
##        return self.y
##
##    def set_y(self,new):
##        self.y = new
##        return self.get_y()
    
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
    def __init__(self,name,area,level,civics_class):
        super().__init__(name,area,level)
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

class Edge(object):
    def __init__(self, a, b,name):
        if a == b:
            print('unaccepted')
        else:
            self.a = a
            self.b = b
            self.name = name
            a.add_edge(self)
            b.add_edge(self)
        #a and b are nodes that the edge connects

    def get_name(self):
        return self.name

    def set_name(self,new):
        self.name = new
        return self.get_name()
    
    def get_a(self):
        return self.a

    def set_a(self,new):
        self.a = new
        return self.get_a()

    def get_b(self):
        return self.b

    def set_b(self,new):
        self.b = new
        return self.get_b()

    def __repr__(self):
        return (str('Edge '+ str(self.get_name()) + ' ' + str(self.get_a()) + ',' + str(self.get_b())))

    def __eq__(self,x):
        if ((self.get_a() == x.get_a() and self.get_b() == x.get_b()) or (self.get_b() == x.get_a() and self.get_a() == x.get_b())) and (self.get_name() == x.get_name()):
            return True
        return False

class Stairs(Edge):
    def __init__(self, a, b, name, steps=10):
        super().__init__(a,b,name)
        self.steps = steps


class Lift():
    def __init__(self, name, levels=[]):
        self.levels = levels
        self.name = name

    def get_name(self):
        return self.name

    def set_name(self,new):
        self.name = new
        return self.get_name()

    def get_levels(self):
        return self.levels

    def set_levels(self,new):
        self.levels = new
        return self.get_levels()

    def add_level(self,new):
        curr = list(self.get_levels())
        curr.append(new)
        self.set_levels(curr)
        return self.get_levels()

    def __repr__(self):
        return str(self.get_name())

def dfs(node,prev,path=[]):
    print('Move from ' + str(prev) + ' to ' + str(node))
    for i in list(node.get_edges()):
        if (i.get_a() == node and i.get_b() == prev) or (i.get_a() == prev and i.get_b() == node):
            print('end')
            path.append(i)
            return path
    for d in list(prev.get_edges()):
        path.append(d)
        if d.get_a() == prev:
            print('Move from ' + str(prev) + ' to '+ str(d.get_b()))
            return dfs(node,d.get_b(),path=path)
        else:
            print('Move from ' + str(prev) + ' to '+ str(d.get_a()))
            return dfs(node,d.get_a(),path=path)

##if running dfs multiple times, must reset path = [] for some reason!

def search_level(start,end):
    if start.get_level() == end.get_level():
        return True
        #commence depth first search
        
##def search_area(start,end):
##    #assume the start and end are in the same area
##    
m = Map('RI')
raja = Zone('Raja',1)
sheares = Zone('Sheares',2)
rl2 = Level(raja,'rl2',2)
##rs12 = Stairs(rl1,rl2,20)
##rajalift = Lift('Raja Block Lift')
##raja_levels = [rl1,rl2,rl3,rl4,rl5,rl6,rl7]
##for r in raja_levels:
##    rajalift.add_level(r)
##raja.add_lift(rajalift)
##
##rlift2 = Node('Raja L2 Lift Landing',raja, rl2)
g0201 = Classroom('g0201',raja,rl2,'s06f')
g0202 = Classroom('g0202',raja,rl2,'s06g')
g0203 = Classroom('g0203',raja,rl2,'4f')

x = Edge(g0201,g0202,'xxx')
y = Edge(g0201,g0202,'yyy')
z = Edge(g0202,g0203,'zzz')

dfs(g0201,g0203)

m.add_zone(raja)
m.add_zone(sheares)


