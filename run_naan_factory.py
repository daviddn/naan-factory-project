# Functions
def make_dough(ingredient1, ingredient2):
    if (ingredient1 == 'wheat' and ingredient2 == 'water') or (ingredient1 == 'water' and ingredient2 == 'wheat'):
        return 'dough'
    else:
        return 'not dough'

def wood_oven(ingredient):
    if ingredient == 'dough':
        return 'Naan bread'
    else:
        return 'not Naan bread'

def run_naan_factory(ingredient1, ingredient2):
    # Needs to make dough
    dough_r = make_dough(ingredient1, ingredient2)
    # It need to send the dough to the oven
    result_bread = wood_oven(dough_r)
    # I want it to make naan bread
    return result_bread

# Calling of functions

print(run_naan_factory('wheat', 'water'))


# Tests TDD
# As a user I can pass 'wheat' and 'water' to the function make_dough, so that I can make 'dough'.
# evaluates --> True or False (Boolean)
print("Testing make_dough, with 'wheat' and 'water' --> 'dough' to come out")
print(make_dough('wheat', 'water') == 'dough')

print("Testing make_dough, with 'sand' and 'cement' --> 'not dough' to come out")
print(make_dough('sand', 'cement') == 'not dough')

# As a user I can pass 'dough' to the function oven_wood, so that I can make 'bread'.
print("Testing wood_oven with 'dough' --> 'Naan bread'")
print(wood_oven('dough') == 'Naan bread')

print("Testing wood_oven with 'rats' --> 'not Naan bread'")
print(wood_oven('rats') == 'not Naan bread')