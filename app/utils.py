def normalize_recipe_params(quantities, units, ingredients):
    '''
    Will make a tuple that groups the params. It is assumed that quantities,
    units, and ingredients are arranged respectively. Returns False if their
    lengths are uneven.

    Arguments:
    quantities -- list of quantities
    units -- list of units
    ingredients -- list of ingredients
    '''
    if quantities or units or ingredients:

        quantities = quantities.split(',')
        units = units.split(',')
        ingredients = ingredients.split(',')

        q_len = len(quantities)
        u_len = len(units)
        i_len = len(ingredients)

        if q_len is u_len and u_len is i_len:
            result = []

            for i in range(0, q_len):
                result.append({
                    'quantity': float(quantities[i]),
                    'unit': int(units[i]),
                    'ingredient': int(ingredients[i]),
                })

            return result
