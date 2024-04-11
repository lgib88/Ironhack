# define rooms and items

import src.functions as fn

game_room = {
    "name": "game room",
    "type": "room",
}

bedroom_1 = {
    "name": "bedroom 1",
    "type": "room",
}

bedroom_2 = {
    "name": "bedroom 2",
    "type": "room",
}

bedroom_3 = {
    "name": "bedroom 3",
    "type": "room",
}

living_room = {
    "name": "living room",
    "type": "room",
}

outside = {
  "name": "outside"
}

door_a = {
    "name": "door a",
    "type": "door",
}

door_b = {
    "name": "door b",
    "type": "door",
}

door_c = {
    "name": "door c",
    "type": "door",
}

door_d = {
    "name": "door d",
    "type": "door",
}

door_e = {
    "name": "door e",
    "type": "door",
}

key_a = {
    "name": "key for door a",
    "type": "key",
    "target": door_a,
}

key_b = {
    "name": "key for door b",
    "type": "key",
    "target": door_b,
}

key_c = {
    "name": "key for door c",
    "type": "key",
    "target": door_c,
}

key_d = {
    "name": "key for door d",
    "type": "key",
    "target": door_d,
}

key_e = {
    "name": "key for door e",
    "type": "key",
    "target": door_e,
}

couch = {
    "name": "couch",
    "type": "furniture",
}

piano = {
    "name": "piano",
    "type": "furniture",
}

dining_table = {
    "name": "dining table",
    "type": "furniture",
}

queen_bed = {
    "name": "queen bed",
    "type": "furniture",
}

dresser = {
    "name": "dresser",
    "type": "furniture",
}

double_bed = {
    "name": "double bed",
    "type": "furniture",
}

table = {
    "name": "table",
    "type": "furniture",
}

pool_table = {
    "name": "pool table",
    "type": "furniture",
}

desk_1 = {
    "name": "desk 1",
    "type": "furniture",
}

cupboard_1 = {
    "name": "cupboard 1",
    "type": "furniture",
}

cupboard_2 = {
    "name": "cupboard 2",
    "type": "furniture",
}

bed = {
    "name": "bed",
    "type": "furniture",
}

desk_2 = {
    "name": "desk 2",
    "type": "furniture",
}

sofa = {
    "name": "sofa",
    "type": "furniture",
}

all_rooms = [game_room, bedroom_1, outside, bedroom_2, bedroom_3, living_room]

all_doors = [door_a, door_b, door_c, door_d, door_e]

# define which items/rooms are related

object_relations = {
    "game room": [couch, piano, table, pool_table, door_a],
    "piano": [key_a],
    "outside": [door_e],
    "door a": [game_room, bedroom_1],
    "queen bed": [key_b],
    "bedroom 1": [queen_bed, desk_1, cupboard_1, door_a, door_b, door_c],
    "door b": [bedroom_1, bedroom_2],
    "bedroom 2": [double_bed, dresser, door_b],
    "double bed": [key_c],
    "dresser": [key_d],
    "living room": [door_d, door_e, dining_table, sofa],
    "door c": [bedroom_1, bedroom_3],
    "door d": [living_room, outside],
    "bedroom 3": [bed, desk_2, cupboard_2, door_c, door_d],
    "desk 2": [key_e],
    "door e": [living_room, outside]
}

# define game state. Do not directly change this dict. 
# Instead, when a new game starts, make a copy of this
# dict and use the copy to store gameplay state. This 
# way you can replay the game multiple times.

INIT_GAME_STATE = {
    "current_room": game_room,
    "keys_collected": [],
    "target_room": outside
}

game_state = INIT_GAME_STATE.copy()

fn.start_game(game_state,object_relations)