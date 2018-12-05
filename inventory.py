# Your code goes here:





#########################################
# Do not touch the code below.
#########################################

if __name__ == '__main__':
    iPhone = Product('iPhone', 699, 'SKU123')
    sofa = Product('Sofa', 1200, 'SKU456')
    dishwasher = Product('Dishwasher', 750, 'SKU789')
    sofa.discount_pct = 10

    warehouse = ProductWarehouse()
    warehouse.receive(iPhone, 100)    # Put 100 iPhones in the warehouse
    warehouse.receive(sofa, 10)       # Put 10 sofas in the warehouse
    warehouse.receive(dishwasher, 1)  # Put 1 dishwasher in the warehouse

    assert (100*699 + 10*1200 + 750*1) == warehouse.total_value
    assert (100*699 + 10*1200*0.9 + 750*1) == warehouse.potential_revenue

    warehouse.ship(iPhone, 1)
    warehouse.ship(sofa, 1)

    assert (99*699 + 9*1200 + 750*1) == warehouse.total_value
    assert (99*699 + 9*1200*0.9 + 750*1) == warehouse.potential_revenue

    print("All tests passed.")
