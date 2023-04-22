import json

class HexCell:
    def __init__(self, terrain, has_object):
        self.terrain = terrain
        self.has_object = has_object
        
grid_width = 10
grid_height = 10

hex_grid = [[HexCell('grass', False) for x in range(grid_width)] for y in range(grid_height)]

# Load movable_objects from JSON file
with open('data/original_moveable_objects.json', 'r') as f:
    moveable_objects = json.load(f)

def add_object_to_grid(obj):
    x, y = obj['position']['x'], obj['position']['y']
    hex_grid[y][x].has_object = True
    
for obj in moveable_objects:
    add_object_to_grid(obj)

with open('data/hexgrid.json', 'w') as f:
    json.dump([[cell.__dict__ for cell in row] for row in hex_grid], f)
    
with open('data/moveable_objects.json', 'w') as f:
    json.dump(moveable_objects, f)