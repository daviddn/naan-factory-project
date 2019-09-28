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