__author__ = 'ThanhNam'
def item_order( order ):
    iterate = len(order);
    saladNumber = 0;
    hamburgerNumber = 0;
    waterNumber = 0;

    for i in range(1, len(order) - 1):
        if order[i-1 : i+4] == 'salad':
            saladNumber += 1
        if order[i-1 : i+8] == 'hamburger':
            hamburgerNumber += 1
        if order[i-1 : i+4] == 'water':
            waterNumber += 1

    result = 'salad:' + str(saladNumber) + ' hamburger:' + str(hamburgerNumber) + ' water:' + str(waterNumber);
    return result;

print(item_order('salad hamburger water salad water'));