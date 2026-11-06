from decimal import Decimal


from demo_shop.checkout.cart import Cart, CartItem


import allure


pytestmark = [allure.feature('Orders'), allure.label('component', 'checkout-cart')]


@allure.title('Canvas tote order of 1 subtotal includes accessories')
def test_canvas_tote_order_of_1_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('0.01'), quantity=1))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('2.51')


@allure.title('Canvas tote order of 2 subtotal includes accessories')
def test_canvas_tote_order_of_2_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('0.80'), quantity=2))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('4.10')


@allure.title('Canvas tote order of 3 subtotal includes accessories')
def test_canvas_tote_order_of_3_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('1.59'), quantity=3))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('7.27')


@allure.title('Canvas tote order of 4 subtotal includes accessories')
def test_canvas_tote_order_of_4_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('2.38'), quantity=4))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('12.02')


@allure.title('Travel mug order of 5 subtotal includes accessories')
def test_travel_mug_order_of_5_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('3.17'), quantity=5))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('18.35')


@allure.title('Travel mug order of 6 subtotal includes accessories')
def test_travel_mug_order_of_6_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('3.96'), quantity=6))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('26.26')


@allure.title('Travel mug order of 7 subtotal includes accessories')
def test_travel_mug_order_of_7_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('4.75'), quantity=7))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('35.75')


@allure.title('Travel mug order of 8 subtotal includes accessories')
def test_travel_mug_order_of_8_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('5.54'), quantity=8))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('46.82')


@allure.title('Pocket notebook order of 9 subtotal includes accessories')
def test_pocket_notebook_order_of_9_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('6.33'), quantity=9))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('59.47')


@allure.title('Pocket notebook order of 10 subtotal includes accessories')
def test_pocket_notebook_order_of_10_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('7.12'), quantity=10))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('73.70')


@allure.title('Pocket notebook order of 1 subtotal includes accessories')
def test_pocket_notebook_order_of_1_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('7.91'), quantity=1))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('10.41')


@allure.title('Pocket notebook order of 2 subtotal includes accessories')
def test_pocket_notebook_order_of_2_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('8.70'), quantity=2))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('19.90')


@allure.title('Cotton scarf order of 3 subtotal includes accessories')
def test_cotton_scarf_order_of_3_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('9.49'), quantity=3))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('30.97')


@allure.title('Cotton scarf order of 4 subtotal includes accessories')
def test_cotton_scarf_order_of_4_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('10.28'), quantity=4))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('43.62')


@allure.title('Cotton scarf order of 5 subtotal includes accessories')
def test_cotton_scarf_order_of_5_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('11.07'), quantity=5))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('57.85')


@allure.title('Cotton scarf order of 6 subtotal includes accessories')
def test_cotton_scarf_order_of_6_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('11.86'), quantity=6))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('73.66')


@allure.title('Desk lamp order of 7 subtotal includes accessories')
def test_desk_lamp_order_of_7_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('12.65'), quantity=7))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('91.05')


@allure.title('Desk lamp order of 8 subtotal includes accessories')
def test_desk_lamp_order_of_8_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('13.44'), quantity=8))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('110.02')


@allure.title('Desk lamp order of 9 subtotal includes accessories')
def test_desk_lamp_order_of_9_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('14.23'), quantity=9))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('130.57')


@allure.title('Desk lamp order of 10 subtotal includes accessories')
def test_desk_lamp_order_of_10_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('15.02'), quantity=10))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('152.70')


@allure.title('Water bottle order of 1 subtotal includes accessories')
def test_water_bottle_order_of_1_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('15.81'), quantity=1))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('18.31')


@allure.title('Water bottle order of 2 subtotal includes accessories')
def test_water_bottle_order_of_2_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('16.60'), quantity=2))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('35.70')


@allure.title('Water bottle order of 3 subtotal includes accessories')
def test_water_bottle_order_of_3_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('17.39'), quantity=3))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('54.67')


@allure.title('Water bottle order of 4 subtotal includes accessories')
def test_water_bottle_order_of_4_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('18.18'), quantity=4))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('75.22')


@allure.title('Laptop sleeve order of 5 subtotal includes accessories')
def test_laptop_sleeve_order_of_5_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('18.97'), quantity=5))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('97.35')


@allure.title('Laptop sleeve order of 6 subtotal includes accessories')
def test_laptop_sleeve_order_of_6_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('19.76'), quantity=6))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('121.06')


@allure.title('Laptop sleeve order of 7 subtotal includes accessories')
def test_laptop_sleeve_order_of_7_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('20.55'), quantity=7))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('146.35')


@allure.title('Laptop sleeve order of 8 subtotal includes accessories')
def test_laptop_sleeve_order_of_8_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('21.34'), quantity=8))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('173.22')


@allure.title('Weekend bag order of 9 subtotal includes accessories')
def test_weekend_bag_order_of_9_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('22.13'), quantity=9))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('201.67')


@allure.title('Weekend bag order of 10 subtotal includes accessories')
def test_weekend_bag_order_of_10_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('22.92'), quantity=10))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('231.70')


@allure.title('Weekend bag order of 1 subtotal includes accessories')
def test_weekend_bag_order_of_1_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('23.71'), quantity=1))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('26.21')


@allure.title('Weekend bag order of 2 subtotal includes accessories')
def test_weekend_bag_order_of_2_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('24.50'), quantity=2))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('51.50')


@allure.title('Wool beanie order of 3 subtotal includes accessories')
def test_wool_beanie_order_of_3_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('25.29'), quantity=3))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('78.37')


@allure.title('Wool beanie order of 4 subtotal includes accessories')
def test_wool_beanie_order_of_4_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('26.08'), quantity=4))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('106.82')


@allure.title('Wool beanie order of 5 subtotal includes accessories')
def test_wool_beanie_order_of_5_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('26.87'), quantity=5))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('136.85')


@allure.title('Wool beanie order of 6 subtotal includes accessories')
def test_wool_beanie_order_of_6_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('27.66'), quantity=6))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('168.46')


@allure.title('Leather wallet order of 7 subtotal includes accessories')
def test_leather_wallet_order_of_7_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('28.45'), quantity=7))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('201.65')


@allure.title('Leather wallet order of 8 subtotal includes accessories')
def test_leather_wallet_order_of_8_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('29.24'), quantity=8))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('236.42')


@allure.title('Leather wallet order of 9 subtotal includes accessories')
def test_leather_wallet_order_of_9_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('30.03'), quantity=9))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('272.77')


@allure.title('Leather wallet order of 10 subtotal includes accessories')
def test_leather_wallet_order_of_10_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('30.82'), quantity=10))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('310.70')


@allure.title('Ceramic bowl order of 1 subtotal includes accessories')
def test_ceramic_bowl_order_of_1_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('31.61'), quantity=1))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('34.11')


@allure.title('Ceramic bowl order of 2 subtotal includes accessories')
def test_ceramic_bowl_order_of_2_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('32.40'), quantity=2))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('67.30')


@allure.title('Ceramic bowl order of 3 subtotal includes accessories')
def test_ceramic_bowl_order_of_3_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('33.19'), quantity=3))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('102.07')


@allure.title('Ceramic bowl order of 4 subtotal includes accessories')
def test_ceramic_bowl_order_of_4_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('33.98'), quantity=4))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('138.42')


@allure.title('Linen apron order of 5 subtotal includes accessories')
def test_linen_apron_order_of_5_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('34.77'), quantity=5))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('176.35')


@allure.title('Linen apron order of 6 subtotal includes accessories')
def test_linen_apron_order_of_6_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('35.56'), quantity=6))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('215.86')


@allure.title('Linen apron order of 7 subtotal includes accessories')
def test_linen_apron_order_of_7_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('36.35'), quantity=7))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('256.95')


@allure.title('Linen apron order of 8 subtotal includes accessories')
def test_linen_apron_order_of_8_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('37.14'), quantity=8))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('299.62')


@allure.title('Phone stand order of 9 subtotal includes accessories')
def test_phone_stand_order_of_9_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('37.93'), quantity=9))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('343.87')


@allure.title('Phone stand order of 10 subtotal includes accessories')
def test_phone_stand_order_of_10_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('38.72'), quantity=10))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('389.70')


@allure.title('Phone stand order of 1 subtotal includes accessories')
def test_phone_stand_order_of_1_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('39.51'), quantity=1))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('42.01')


@allure.title('Phone stand order of 2 subtotal includes accessories')
def test_phone_stand_order_of_2_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('40.30'), quantity=2))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('83.10')


@allure.title('Reading light order of 3 subtotal includes accessories')
def test_reading_light_order_of_3_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('41.09'), quantity=3))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('125.77')


@allure.title('Reading light order of 4 subtotal includes accessories')
def test_reading_light_order_of_4_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('41.88'), quantity=4))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('170.02')


@allure.title('Reading light order of 5 subtotal includes accessories')
def test_reading_light_order_of_5_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('42.67'), quantity=5))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('215.85')


@allure.title('Reading light order of 6 subtotal includes accessories')
def test_reading_light_order_of_6_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('43.46'), quantity=6))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('263.26')


@allure.title('Picnic blanket order of 7 subtotal includes accessories')
def test_picnic_blanket_order_of_7_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('44.25'), quantity=7))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('312.25')


@allure.title('Picnic blanket order of 8 subtotal includes accessories')
def test_picnic_blanket_order_of_8_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('45.04'), quantity=8))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('362.82')


@allure.title('Picnic blanket order of 9 subtotal includes accessories')
def test_picnic_blanket_order_of_9_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('45.83'), quantity=9))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('414.97')


@allure.title('Picnic blanket order of 10 subtotal includes accessories')
def test_picnic_blanket_order_of_10_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('46.62'), quantity=10))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('468.70')


@allure.title('Coffee grinder order of 1 subtotal includes accessories')
def test_coffee_grinder_order_of_1_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('47.41'), quantity=1))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('49.91')


@allure.title('Coffee grinder order of 2 subtotal includes accessories')
def test_coffee_grinder_order_of_2_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('48.20'), quantity=2))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('98.90')


@allure.title('Coffee grinder order of 3 subtotal includes accessories')
def test_coffee_grinder_order_of_3_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('48.99'), quantity=3))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('149.47')


@allure.title('Coffee grinder order of 4 subtotal includes accessories')
def test_coffee_grinder_order_of_4_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('49.78'), quantity=4))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('201.62')


@allure.title('Running belt order of 5 subtotal includes accessories')
def test_running_belt_order_of_5_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('50.57'), quantity=5))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('255.35')


@allure.title('Running belt order of 6 subtotal includes accessories')
def test_running_belt_order_of_6_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('51.36'), quantity=6))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('310.66')


@allure.title('Running belt order of 7 subtotal includes accessories')
def test_running_belt_order_of_7_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('52.15'), quantity=7))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('367.55')


@allure.title('Running belt order of 8 subtotal includes accessories')
def test_running_belt_order_of_8_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('52.94'), quantity=8))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('426.02')


@allure.title('Yoga mat order of 9 subtotal includes accessories')
def test_yoga_mat_order_of_9_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('53.73'), quantity=9))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('486.07')


@allure.title('Yoga mat order of 10 subtotal includes accessories')
def test_yoga_mat_order_of_10_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('54.52'), quantity=10))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('547.70')


@allure.title('Yoga mat order of 1 subtotal includes accessories')
def test_yoga_mat_order_of_1_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('55.31'), quantity=1))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('57.81')


@allure.title('Yoga mat order of 2 subtotal includes accessories')
def test_yoga_mat_order_of_2_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('56.10'), quantity=2))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('114.70')


@allure.title('Wireless mouse order of 3 subtotal includes accessories')
def test_wireless_mouse_order_of_3_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('56.89'), quantity=3))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('173.17')


@allure.title('Wireless mouse order of 4 subtotal includes accessories')
def test_wireless_mouse_order_of_4_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('57.68'), quantity=4))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('233.22')


@allure.title('Wireless mouse order of 5 subtotal includes accessories')
def test_wireless_mouse_order_of_5_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('58.47'), quantity=5))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('294.85')


@allure.title('Wireless mouse order of 6 subtotal includes accessories')
def test_wireless_mouse_order_of_6_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('59.26'), quantity=6))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('358.06')


@allure.title('Usb charger order of 7 subtotal includes accessories')
def test_usb_charger_order_of_7_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('60.05'), quantity=7))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('422.85')


@allure.title('Usb charger order of 8 subtotal includes accessories')
def test_usb_charger_order_of_8_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('60.84'), quantity=8))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('489.22')


@allure.title('Usb charger order of 9 subtotal includes accessories')
def test_usb_charger_order_of_9_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('61.63'), quantity=9))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('557.17')


@allure.title('Usb charger order of 10 subtotal includes accessories')
def test_usb_charger_order_of_10_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('62.42'), quantity=10))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('626.70')


@allure.title('Travel pillow order of 1 subtotal includes accessories')
def test_travel_pillow_order_of_1_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('63.21'), quantity=1))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('65.71')


@allure.title('Travel pillow order of 2 subtotal includes accessories')
def test_travel_pillow_order_of_2_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('64.00'), quantity=2))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('130.50')


@allure.title('Travel pillow order of 3 subtotal includes accessories')
def test_travel_pillow_order_of_3_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('64.79'), quantity=3))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('196.87')


@allure.title('Travel pillow order of 4 subtotal includes accessories')
def test_travel_pillow_order_of_4_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('65.58'), quantity=4))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('264.82')


@allure.title('Packing cubes order of 5 subtotal includes accessories')
def test_packing_cubes_order_of_5_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('66.37'), quantity=5))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('334.35')


@allure.title('Packing cubes order of 6 subtotal includes accessories')
def test_packing_cubes_order_of_6_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('67.16'), quantity=6))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('405.46')


@allure.title('Packing cubes order of 7 subtotal includes accessories')
def test_packing_cubes_order_of_7_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('67.95'), quantity=7))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('478.15')


@allure.title('Packing cubes order of 8 subtotal includes accessories')
def test_packing_cubes_order_of_8_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('68.74'), quantity=8))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('552.42')


@allure.title('Rain jacket order of 9 subtotal includes accessories')
def test_rain_jacket_order_of_9_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('69.53'), quantity=9))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('628.27')


@allure.title('Rain jacket order of 10 subtotal includes accessories')
def test_rain_jacket_order_of_10_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('70.32'), quantity=10))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('705.70')


@allure.title('Rain jacket order of 1 subtotal includes accessories')
def test_rain_jacket_order_of_1_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('71.11'), quantity=1))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('73.61')


@allure.title('Rain jacket order of 2 subtotal includes accessories')
def test_rain_jacket_order_of_2_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('71.90'), quantity=2))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('146.30')


@allure.title('Hiking socks order of 3 subtotal includes accessories')
def test_hiking_socks_order_of_3_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('72.69'), quantity=3))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('220.57')


@allure.title('Hiking socks order of 4 subtotal includes accessories')
def test_hiking_socks_order_of_4_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('73.48'), quantity=4))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('296.42')


@allure.title('Hiking socks order of 5 subtotal includes accessories')
def test_hiking_socks_order_of_5_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('74.27'), quantity=5))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('373.85')


@allure.title('Hiking socks order of 6 subtotal includes accessories')
def test_hiking_socks_order_of_6_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('75.06'), quantity=6))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('452.86')


@allure.title('Bike lock order of 7 subtotal includes accessories')
def test_bike_lock_order_of_7_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('75.85'), quantity=7))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('533.45')


@allure.title('Bike lock order of 8 subtotal includes accessories')
def test_bike_lock_order_of_8_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('76.64'), quantity=8))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('615.62')


@allure.title('Bike lock order of 9 subtotal includes accessories')
def test_bike_lock_order_of_9_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('77.43'), quantity=9))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('699.37')


@allure.title('Bike lock order of 10 subtotal includes accessories')
def test_bike_lock_order_of_10_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('78.22'), quantity=10))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('784.70')


@allure.title('Camping lantern order of 1 subtotal includes accessories')
def test_camping_lantern_order_of_1_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('79.01'), quantity=1))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('81.51')


@allure.title('Camping lantern order of 2 subtotal includes accessories')
def test_camping_lantern_order_of_2_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('79.80'), quantity=2))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('162.10')


@allure.title('Camping lantern order of 3 subtotal includes accessories')
def test_camping_lantern_order_of_3_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('80.59'), quantity=3))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('244.27')


@allure.title('Camping lantern order of 4 subtotal includes accessories')
def test_camping_lantern_order_of_4_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('81.38'), quantity=4))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('328.02')


@allure.title('Lunch box order of 5 subtotal includes accessories')
def test_lunch_box_order_of_5_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('82.17'), quantity=5))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('413.35')


@allure.title('Lunch box order of 6 subtotal includes accessories')
def test_lunch_box_order_of_6_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('82.96'), quantity=6))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('500.26')


@allure.title('Lunch box order of 7 subtotal includes accessories')
def test_lunch_box_order_of_7_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('83.75'), quantity=7))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('588.75')


@allure.title('Lunch box order of 8 subtotal includes accessories')
def test_lunch_box_order_of_8_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('84.54'), quantity=8))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('678.82')


@allure.title('Tea infuser order of 9 subtotal includes accessories')
def test_tea_infuser_order_of_9_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('85.33'), quantity=9))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('770.47')


@allure.title('Tea infuser order of 10 subtotal includes accessories')
def test_tea_infuser_order_of_10_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('86.12'), quantity=10))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('863.70')


@allure.title('Tea infuser order of 1 subtotal includes accessories')
def test_tea_infuser_order_of_1_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('86.91'), quantity=1))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('89.41')


@allure.title('Tea infuser order of 2 subtotal includes accessories')
def test_tea_infuser_order_of_2_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('87.70'), quantity=2))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('177.90')


@allure.title('Plant pot order of 3 subtotal includes accessories')
def test_plant_pot_order_of_3_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('88.49'), quantity=3))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('267.97')


@allure.title('Plant pot order of 4 subtotal includes accessories')
def test_plant_pot_order_of_4_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('89.28'), quantity=4))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('359.62')


@allure.title('Plant pot order of 5 subtotal includes accessories')
def test_plant_pot_order_of_5_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('90.07'), quantity=5))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('452.85')


@allure.title('Plant pot order of 6 subtotal includes accessories')
def test_plant_pot_order_of_6_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('90.86'), quantity=6))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('547.66')


@allure.title('Photo frame order of 7 subtotal includes accessories')
def test_photo_frame_order_of_7_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('91.65'), quantity=7))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('644.05')


@allure.title('Photo frame order of 8 subtotal includes accessories')
def test_photo_frame_order_of_8_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('92.44'), quantity=8))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('742.02')


@allure.title('Photo frame order of 9 subtotal includes accessories')
def test_photo_frame_order_of_9_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('93.23'), quantity=9))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('841.57')


@allure.title('Photo frame order of 10 subtotal includes accessories')
def test_photo_frame_order_of_10_subtotal_with_accessories():
    cart = Cart()
    cart.add_item(CartItem(sku='PRODUCT', unit_price=Decimal('94.02'), quantity=10))
    cart.add_item(CartItem(sku='ACCESSORY', unit_price=Decimal('1.25'), quantity=2))
    with allure.step('Verify subtotal includes product quantities and accessories'):
        assert cart.subtotal() == Decimal('942.70')
