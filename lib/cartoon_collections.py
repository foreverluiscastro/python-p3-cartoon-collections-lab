def roll_call_dwarves(dwarves):
    pass
    for idx, dwarf in enumerate(dwarves):
        pass
        print(f"{idx + 1}. {dwarf}")

def summon_captain_planet(planeteer_calls):
    pass
    return [f"{call.capitalize()}!" for call in planeteer_calls]

def long_planeteer_calls(planeteer_calls):
    pass
    for call in planeteer_calls:
        pass
        if len(call) > 4:
            return True
        
    return False

def find_the_cheese(snacks):
    pass
    cheeses = ["cheddar", "gouda", "camembert"]
    for snack in snacks:
        pass
        if snack in cheeses:
            return snack
    
    return None