from data_store import *

f = open('dbase.pkl','rb')
data = pickle.load(f)

class Tree(object):
	def __init__(self,data):
		self.data = data
		self.children = []
		self.parent = None
	def add_children(self,child):
		child.parent = self
		self.children.append(child)
	def get_level(self):
		level = 0
		p= self.parent
		while p:
			level += 1
			p =p.parent
		return level
	def print_tree(self):
		spaces = ' ' * self.get_level() * 2
		prefix = '\-'
		print(spaces + prefix + self.data )
		print(spaces,"|-" ,"[Door]", self.door())
		print(spaces,"|-")
		print(spaces,"|-" ,"[Access rules]","", self.access_rule())

		if self.children:
			for child in self.children:
				child.print_tree()
		
	def door(self):
		dr = []
		for doors in data['system_data']['doors']:
			area_parent = doors['parent_area']
			door_status = doors['status']
			door_name = doors['name']
			for area in data['system_data']['areas']:
				area_name = area['name']
				if(area_parent == area['id']):
					if( self.data == area_name):
						door = door_name+"("+door_status+")"
						dr.append(door)
		return dr
	
	def access_rule(self):
		ar =[]
		for access in data['system_data']['access_rules']:
			access_doors = access['doors']
			access_name = access['name']
			i=0
			j=0
			while(i<len(access_doors)):
				for doors in data['system_data']['doors']:
					door_id = doors['id']
					parent_area = doors['parent_area']
					if(access_doors[i]==door_id):
						for area in data['system_data']['areas']:
							area_name = area['name']
							if( self.data == area_name):
								if(parent_area == area['id']):
									ar.append(access_name)
									if(ar.count(access_name)==2 ):
										ar.remove(access_name)
									
				i+=1
		return ar
		
def build_tree():
	i=0;
	j=0;
	k=0;
	m=0;
	for area in data['system_data']['areas']:
		area_parent = area['parent_area']
		area_child = area['child_area_ids']
		area_name = area['name']
		area_id = area['id']
		if( area_parent is None):
			root = Tree(area_name)
			root_id = area['id']
		elif( area_parent == root_id):
			stem = Tree(area_name)
			stem_id = area['id']
			root.add_children(stem)
			
		elif( area_parent == stem_id):
			branch = Tree(area_name)
			branch_id = area['id']
			stem.add_children(branch)
		elif( area_parent == branch_id):
			leaf= Tree(area_name)
			leaf_id = area['id']
			branch.add_children(leaf)
		elif( area_parent ==leaf_id):
			a = Tree(area_name)
			a_id = area['id']
			leaf.add_children(a)
			
		
	return root
	
if __name__ == "__main__":
	root = build_tree()
	root.print_tree()
	pass
	