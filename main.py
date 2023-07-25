# Do not modify these lines
__winc_id__ = '25596924dffe436da9034d43d0af6791'
__human_name__ = 'conditions'

# Add your code after this line
def farm_action(weather, time_of_day, milking_status, locations_of_cows, season, slurry_tank, grass_status): 

    if locations_of_cows == "pasture":
        if milking_status == True:
            return "take cows to cowshed\nmilk cows\ntake cows back to pasture"
        if slurry_tank == True and weather not in ["sunny", "windy"]:
            return "take cows to cowshed\nfertilize pasture\ntake cows back to pasture"
        if season == "spring" and weather == "sunny" and grass_status == True:
            return "take cows to cowshed\nmow grass\ntake cows back to pasture"
        if time_of_day == "night" or weather == "rainy": 
            return "take cows to the cowshed"
        else:
            return "wait"

    if locations_of_cows == "cowshed":
        if milking_status == True:
            return "milk cows"
        if slurry_tank == True and weather not in ["sunny", "windy"]:
            return "fertilize pasture"
        if season == "spring" and weather == "sunny" and grass_status == True:
            return "mow grass"
        else:
            return "wait"

print(farm_action('rainy', 'night', False, 'cowshed', 'winter', True, True))
# fertilize pasture

print(farm_action('rainy', 'night', False, 'cowshed', 'winter', False, True))
# wait

print(farm_action('windy', 'night', True, 'cowshed', 'winter', True, True))
# milk cows

print(farm_action('sunny', 'day', True, 'pasture', 'spring', False, True))
# take cows to cowshed
# milk cows
# take cows back to pasture