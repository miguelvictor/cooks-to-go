def normalize_recipe_params(quantities, units, ingredients):
    ''' Will make a tuple that groups the params '''
    q_len = len(quantities)
    u_len = len(units)
    i_len = len(ingredients)

    if q_len is u_len and u_len is i_len:
        result = []

        for i in range(0, q_len):
            result.append({'quantity': quantities[i],
                          'unit': units[i], 'ingredient': ingredients[i]})

        return result

    return False
