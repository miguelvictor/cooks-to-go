def normalize_recipe_params(ingredients):
    if ingredients is None or ingredients == '':
        return []

    return [int(x) for x in ingredients.split(',')]

''' TEST '''

a = normalize_recipe_params('1,2,3')
if a == [1, 2, 3]:
    print "Test 1 : PASSED"
else:
    print "Test 1 : FAILED"

a = normalize_recipe_params('1')
if a == [1]:
    print "Test 2 : PASSED"
else:
    print "Test 2 : FAILED"

a = normalize_recipe_params('')
if a == []:
    print "Test 3 : PASSED"
else:
    print "Test 3 : FAILED"
