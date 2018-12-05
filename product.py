# Your code goes here:



#########################################
# Do not touch the code below.
#########################################

if __name__ == '__main__':
    iPhone = Product('iPhone', 699, 'SKU123')
    sofa = Product('Sofa', 1200, 'SKU456')
    sofa.discount_pct = 10

    assert 'iPhone' == iPhone.name
    assert 'SKU123' == iPhone.sku
    assert 699 == iPhone.price
    assert 699 == iPhone.cost()

    assert 'Sofa' == sofa.name
    assert 'SKU456' == sofa.sku
    assert 1200 == sofa.price
    assert 1080 == sofa.cost()

    print("All tests passed.")
