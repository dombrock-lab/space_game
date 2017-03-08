space rogue

3 travel systems
deep space
solar system
planetary

system
-name
-planets list
-2d coords
:check_name
:check_planets_list
:check_location

planet
-name
-gas/solid
-harzard multiplier
-available extracts (must be probed)
-extract level
:check_classification
:check_name
:check_hazard
:check_extracts
:check_extract_level
:remove_extract_level

ship
-name
-class (small/med/large, bigger uses more fuel)
-inv area
-shield
-fuel tank size
-fuel cost per LYear
-current fuel
-current hull state
-current location (2d coords)
:change_location
:check_location
:add_fuel
:spend_fuel
:damage_hull
:repair_hull
:add_inv_item
##if element_stack already exists add to it
:use_inv_item
:organize_inventory
:remove_inv_item
:check_inv
:check_ship_info

element_stack
-name
-description (what do we use it for)
-amount (in this stack)
-size
:check_name
:check_description
:check_size
:check_amount
:add
:remove


Map
-all systems list
-known systems list
-nearby undiscovered systems list
:generate_all_systems
:add_known_system
:list_known_systems
:list_nearby_systems
:list_all_systems
:check_location 
##see if we arrived somewhere

say
-text
##controls printing of text
:say

ask
-question
-anwer
:ask
:return_answer

cmd
-command
:get

