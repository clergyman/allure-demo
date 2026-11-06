from decimal import Decimal


from demo_shop.catalog.pricing import apply_discount, price_with_tax


import allure


pytestmark = [allure.feature('Catalog'), allure.label('component', 'catalog-pricing')]


@allure.title('Canvas tote price includes zero percent tax')
def test_canvas_tote_price_with_zero_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('0.05'), Decimal('0')) == Decimal('0.05')


@allure.title('Canvas tote price includes five percent tax')
def test_canvas_tote_price_with_five_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('1.18'), Decimal('0.05')) == Decimal('1.24')


@allure.title('Canvas tote price includes ten percent tax')
def test_canvas_tote_price_with_ten_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('2.31'), Decimal('0.10')) == Decimal('2.54')


@allure.title('Canvas tote price includes twenty percent tax')
def test_canvas_tote_price_with_twenty_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('3.44'), Decimal('0.20')) == Decimal('4.13')


@allure.title('Canvas tote price includes twenty three percent tax')
def test_canvas_tote_price_with_twenty_three_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('4.57'), Decimal('0.23')) == Decimal('5.62')


@allure.title('Canvas tote price includes twenty five percent tax')
def test_canvas_tote_price_with_twenty_five_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('5.70'), Decimal('0.25')) == Decimal('7.13')


@allure.title('Travel mug price includes zero percent tax')
def test_travel_mug_price_with_zero_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('6.83'), Decimal('0')) == Decimal('6.83')


@allure.title('Travel mug price includes five percent tax')
def test_travel_mug_price_with_five_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('7.96'), Decimal('0.05')) == Decimal('8.36')


@allure.title('Travel mug price includes ten percent tax')
def test_travel_mug_price_with_ten_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('9.09'), Decimal('0.10')) == Decimal('10.00')


@allure.title('Travel mug price includes twenty percent tax')
def test_travel_mug_price_with_twenty_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('10.22'), Decimal('0.20')) == Decimal('12.26')


@allure.title('Travel mug price includes twenty three percent tax')
def test_travel_mug_price_with_twenty_three_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('11.35'), Decimal('0.23')) == Decimal('13.96')


@allure.title('Travel mug price includes twenty five percent tax')
def test_travel_mug_price_with_twenty_five_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('12.48'), Decimal('0.25')) == Decimal('15.60')


@allure.title('Pocket notebook price includes zero percent tax')
def test_pocket_notebook_price_with_zero_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('13.61'), Decimal('0')) == Decimal('13.61')


@allure.title('Pocket notebook price includes five percent tax')
def test_pocket_notebook_price_with_five_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('14.74'), Decimal('0.05')) == Decimal('15.48')


@allure.title('Pocket notebook price includes ten percent tax')
def test_pocket_notebook_price_with_ten_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('15.87'), Decimal('0.10')) == Decimal('17.46')


@allure.title('Pocket notebook price includes twenty percent tax')
def test_pocket_notebook_price_with_twenty_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('17.00'), Decimal('0.20')) == Decimal('20.40')


@allure.title('Pocket notebook price includes twenty three percent tax')
def test_pocket_notebook_price_with_twenty_three_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('18.13'), Decimal('0.23')) == Decimal('22.30')


@allure.title('Pocket notebook price includes twenty five percent tax')
def test_pocket_notebook_price_with_twenty_five_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('19.26'), Decimal('0.25')) == Decimal('24.08')


@allure.title('Cotton scarf price includes zero percent tax')
def test_cotton_scarf_price_with_zero_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('20.39'), Decimal('0')) == Decimal('20.39')


@allure.title('Cotton scarf price includes five percent tax')
def test_cotton_scarf_price_with_five_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('21.52'), Decimal('0.05')) == Decimal('22.60')


@allure.title('Cotton scarf price includes ten percent tax')
def test_cotton_scarf_price_with_ten_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('22.65'), Decimal('0.10')) == Decimal('24.92')


@allure.title('Cotton scarf price includes twenty percent tax')
def test_cotton_scarf_price_with_twenty_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('23.78'), Decimal('0.20')) == Decimal('28.54')


@allure.title('Cotton scarf price includes twenty three percent tax')
def test_cotton_scarf_price_with_twenty_three_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('24.91'), Decimal('0.23')) == Decimal('30.64')


@allure.title('Cotton scarf price includes twenty five percent tax')
def test_cotton_scarf_price_with_twenty_five_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('26.04'), Decimal('0.25')) == Decimal('32.55')


@allure.title('Desk lamp price includes zero percent tax')
def test_desk_lamp_price_with_zero_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('27.17'), Decimal('0')) == Decimal('27.17')


@allure.title('Desk lamp price includes five percent tax')
def test_desk_lamp_price_with_five_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('28.30'), Decimal('0.05')) == Decimal('29.72')


@allure.title('Desk lamp price includes ten percent tax')
def test_desk_lamp_price_with_ten_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('29.43'), Decimal('0.10')) == Decimal('32.37')


@allure.title('Desk lamp price includes twenty percent tax')
def test_desk_lamp_price_with_twenty_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('30.56'), Decimal('0.20')) == Decimal('36.67')


@allure.title('Desk lamp price includes twenty three percent tax')
def test_desk_lamp_price_with_twenty_three_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('31.69'), Decimal('0.23')) == Decimal('38.98')


@allure.title('Desk lamp price includes twenty five percent tax')
def test_desk_lamp_price_with_twenty_five_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('32.82'), Decimal('0.25')) == Decimal('41.03')


@allure.title('Water bottle price includes zero percent tax')
def test_water_bottle_price_with_zero_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('33.95'), Decimal('0')) == Decimal('33.95')


@allure.title('Water bottle price includes five percent tax')
def test_water_bottle_price_with_five_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('35.08'), Decimal('0.05')) == Decimal('36.83')


@allure.title('Water bottle price includes ten percent tax')
def test_water_bottle_price_with_ten_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('36.21'), Decimal('0.10')) == Decimal('39.83')


@allure.title('Water bottle price includes twenty percent tax')
def test_water_bottle_price_with_twenty_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('37.34'), Decimal('0.20')) == Decimal('44.81')


@allure.title('Water bottle price includes twenty three percent tax')
def test_water_bottle_price_with_twenty_three_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('38.47'), Decimal('0.23')) == Decimal('47.32')


@allure.title('Water bottle price includes twenty five percent tax')
def test_water_bottle_price_with_twenty_five_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('39.60'), Decimal('0.25')) == Decimal('49.50')


@allure.title('Laptop sleeve price includes zero percent tax')
def test_laptop_sleeve_price_with_zero_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('40.73'), Decimal('0')) == Decimal('40.73')


@allure.title('Laptop sleeve price includes five percent tax')
def test_laptop_sleeve_price_with_five_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('41.86'), Decimal('0.05')) == Decimal('43.95')


@allure.title('Laptop sleeve price includes ten percent tax')
def test_laptop_sleeve_price_with_ten_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('42.99'), Decimal('0.10')) == Decimal('47.29')


@allure.title('Laptop sleeve price includes twenty percent tax')
def test_laptop_sleeve_price_with_twenty_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('44.12'), Decimal('0.20')) == Decimal('52.94')


@allure.title('Laptop sleeve price includes twenty three percent tax')
def test_laptop_sleeve_price_with_twenty_three_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('45.25'), Decimal('0.23')) == Decimal('55.66')


@allure.title('Laptop sleeve price includes twenty five percent tax')
def test_laptop_sleeve_price_with_twenty_five_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('46.38'), Decimal('0.25')) == Decimal('57.98')


@allure.title('Weekend bag price includes zero percent tax')
def test_weekend_bag_price_with_zero_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('47.51'), Decimal('0')) == Decimal('47.51')


@allure.title('Weekend bag price includes five percent tax')
def test_weekend_bag_price_with_five_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('48.64'), Decimal('0.05')) == Decimal('51.07')


@allure.title('Weekend bag price includes ten percent tax')
def test_weekend_bag_price_with_ten_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('49.77'), Decimal('0.10')) == Decimal('54.75')


@allure.title('Weekend bag price includes twenty percent tax')
def test_weekend_bag_price_with_twenty_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('50.90'), Decimal('0.20')) == Decimal('61.08')


@allure.title('Weekend bag price includes twenty three percent tax')
def test_weekend_bag_price_with_twenty_three_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('52.03'), Decimal('0.23')) == Decimal('64.00')


@allure.title('Weekend bag price includes twenty five percent tax')
def test_weekend_bag_price_with_twenty_five_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('53.16'), Decimal('0.25')) == Decimal('66.45')


@allure.title('Wool beanie price includes zero percent tax')
def test_wool_beanie_price_with_zero_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('54.29'), Decimal('0')) == Decimal('54.29')


@allure.title('Wool beanie price includes five percent tax')
def test_wool_beanie_price_with_five_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('55.42'), Decimal('0.05')) == Decimal('58.19')


@allure.title('Wool beanie price includes ten percent tax')
def test_wool_beanie_price_with_ten_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('56.55'), Decimal('0.10')) == Decimal('62.21')


@allure.title('Wool beanie price includes twenty percent tax')
def test_wool_beanie_price_with_twenty_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('57.68'), Decimal('0.20')) == Decimal('69.22')


@allure.title('Wool beanie price includes twenty three percent tax')
def test_wool_beanie_price_with_twenty_three_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('58.81'), Decimal('0.23')) == Decimal('72.34')


@allure.title('Wool beanie price includes twenty five percent tax')
def test_wool_beanie_price_with_twenty_five_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('59.94'), Decimal('0.25')) == Decimal('74.93')


@allure.title('Leather wallet price includes zero percent tax')
def test_leather_wallet_price_with_zero_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('61.07'), Decimal('0')) == Decimal('61.07')


@allure.title('Leather wallet price includes five percent tax')
def test_leather_wallet_price_with_five_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('62.20'), Decimal('0.05')) == Decimal('65.31')


@allure.title('Leather wallet price includes ten percent tax')
def test_leather_wallet_price_with_ten_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('63.33'), Decimal('0.10')) == Decimal('69.66')


@allure.title('Leather wallet price includes twenty percent tax')
def test_leather_wallet_price_with_twenty_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('64.46'), Decimal('0.20')) == Decimal('77.35')


@allure.title('Leather wallet price includes twenty three percent tax')
def test_leather_wallet_price_with_twenty_three_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('65.59'), Decimal('0.23')) == Decimal('80.68')


@allure.title('Leather wallet price includes twenty five percent tax')
def test_leather_wallet_price_with_twenty_five_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('66.72'), Decimal('0.25')) == Decimal('83.40')


@allure.title('Ceramic bowl price includes zero percent tax')
def test_ceramic_bowl_price_with_zero_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('67.85'), Decimal('0')) == Decimal('67.85')


@allure.title('Ceramic bowl price includes five percent tax')
def test_ceramic_bowl_price_with_five_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('68.98'), Decimal('0.05')) == Decimal('72.43')


@allure.title('Ceramic bowl price includes ten percent tax')
def test_ceramic_bowl_price_with_ten_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('70.11'), Decimal('0.10')) == Decimal('77.12')


@allure.title('Ceramic bowl price includes twenty percent tax')
def test_ceramic_bowl_price_with_twenty_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('71.24'), Decimal('0.20')) == Decimal('85.49')


@allure.title('Ceramic bowl price includes twenty three percent tax')
def test_ceramic_bowl_price_with_twenty_three_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('72.37'), Decimal('0.23')) == Decimal('89.02')


@allure.title('Ceramic bowl price includes twenty five percent tax')
def test_ceramic_bowl_price_with_twenty_five_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('73.50'), Decimal('0.25')) == Decimal('91.88')


@allure.title('Linen apron price includes zero percent tax')
def test_linen_apron_price_with_zero_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('74.63'), Decimal('0')) == Decimal('74.63')


@allure.title('Linen apron price includes five percent tax')
def test_linen_apron_price_with_five_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('75.76'), Decimal('0.05')) == Decimal('79.55')


@allure.title('Linen apron price includes ten percent tax')
def test_linen_apron_price_with_ten_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('76.89'), Decimal('0.10')) == Decimal('84.58')


@allure.title('Linen apron price includes twenty percent tax')
def test_linen_apron_price_with_twenty_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('78.02'), Decimal('0.20')) == Decimal('93.62')


@allure.title('Linen apron price includes twenty three percent tax')
def test_linen_apron_price_with_twenty_three_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('79.15'), Decimal('0.23')) == Decimal('97.35')


@allure.title('Linen apron price includes twenty five percent tax')
def test_linen_apron_price_with_twenty_five_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('80.28'), Decimal('0.25')) == Decimal('100.35')


@allure.title('Phone stand price includes zero percent tax')
def test_phone_stand_price_with_zero_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('81.41'), Decimal('0')) == Decimal('81.41')


@allure.title('Phone stand price includes five percent tax')
def test_phone_stand_price_with_five_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('82.54'), Decimal('0.05')) == Decimal('86.67')


@allure.title('Phone stand price includes ten percent tax')
def test_phone_stand_price_with_ten_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('83.67'), Decimal('0.10')) == Decimal('92.04')


@allure.title('Phone stand price includes twenty percent tax')
def test_phone_stand_price_with_twenty_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('84.80'), Decimal('0.20')) == Decimal('101.76')


@allure.title('Phone stand price includes twenty three percent tax')
def test_phone_stand_price_with_twenty_three_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('85.93'), Decimal('0.23')) == Decimal('105.69')


@allure.title('Phone stand price includes twenty five percent tax')
def test_phone_stand_price_with_twenty_five_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('87.06'), Decimal('0.25')) == Decimal('108.83')


@allure.title('Reading light price includes zero percent tax')
def test_reading_light_price_with_zero_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('88.19'), Decimal('0')) == Decimal('88.19')


@allure.title('Reading light price includes five percent tax')
def test_reading_light_price_with_five_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('89.32'), Decimal('0.05')) == Decimal('93.79')


@allure.title('Reading light price includes ten percent tax')
def test_reading_light_price_with_ten_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('90.45'), Decimal('0.10')) == Decimal('99.50')


@allure.title('Reading light price includes twenty percent tax')
def test_reading_light_price_with_twenty_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('91.58'), Decimal('0.20')) == Decimal('109.90')


@allure.title('Reading light price includes twenty three percent tax')
def test_reading_light_price_with_twenty_three_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('92.71'), Decimal('0.23')) == Decimal('114.03')


@allure.title('Reading light price includes twenty five percent tax')
def test_reading_light_price_with_twenty_five_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('93.84'), Decimal('0.25')) == Decimal('117.30')


@allure.title('Picnic blanket price includes zero percent tax')
def test_picnic_blanket_price_with_zero_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('94.97'), Decimal('0')) == Decimal('94.97')


@allure.title('Picnic blanket price includes five percent tax')
def test_picnic_blanket_price_with_five_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('96.10'), Decimal('0.05')) == Decimal('100.91')


@allure.title('Picnic blanket price includes ten percent tax')
def test_picnic_blanket_price_with_ten_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('97.23'), Decimal('0.10')) == Decimal('106.95')


@allure.title('Picnic blanket price includes twenty percent tax')
def test_picnic_blanket_price_with_twenty_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('98.36'), Decimal('0.20')) == Decimal('118.03')


@allure.title('Picnic blanket price includes twenty three percent tax')
def test_picnic_blanket_price_with_twenty_three_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('99.49'), Decimal('0.23')) == Decimal('122.37')


@allure.title('Picnic blanket price includes twenty five percent tax')
def test_picnic_blanket_price_with_twenty_five_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('100.62'), Decimal('0.25')) == Decimal('125.78')


@allure.title('Coffee grinder price includes zero percent tax')
def test_coffee_grinder_price_with_zero_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('101.75'), Decimal('0')) == Decimal('101.75')


@allure.title('Coffee grinder price includes five percent tax')
def test_coffee_grinder_price_with_five_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('102.88'), Decimal('0.05')) == Decimal('108.02')


@allure.title('Coffee grinder price includes ten percent tax')
def test_coffee_grinder_price_with_ten_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('104.01'), Decimal('0.10')) == Decimal('114.41')


@allure.title('Coffee grinder price includes twenty percent tax')
def test_coffee_grinder_price_with_twenty_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('105.14'), Decimal('0.20')) == Decimal('126.17')


@allure.title('Coffee grinder price includes twenty three percent tax')
def test_coffee_grinder_price_with_twenty_three_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('106.27'), Decimal('0.23')) == Decimal('130.71')


@allure.title('Coffee grinder price includes twenty five percent tax')
def test_coffee_grinder_price_with_twenty_five_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('107.40'), Decimal('0.25')) == Decimal('134.25')


@allure.title('Running belt price includes zero percent tax')
def test_running_belt_price_with_zero_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('108.53'), Decimal('0')) == Decimal('108.53')


@allure.title('Running belt price includes five percent tax')
def test_running_belt_price_with_five_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('109.66'), Decimal('0.05')) == Decimal('115.14')


@allure.title('Running belt price includes ten percent tax')
def test_running_belt_price_with_ten_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('110.79'), Decimal('0.10')) == Decimal('121.87')


@allure.title('Running belt price includes twenty percent tax')
def test_running_belt_price_with_twenty_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('111.92'), Decimal('0.20')) == Decimal('134.30')


@allure.title('Running belt price includes twenty three percent tax')
def test_running_belt_price_with_twenty_three_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('113.05'), Decimal('0.23')) == Decimal('139.05')


@allure.title('Running belt price includes twenty five percent tax')
def test_running_belt_price_with_twenty_five_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('114.18'), Decimal('0.25')) == Decimal('142.73')


@allure.title('Yoga mat price includes zero percent tax')
def test_yoga_mat_price_with_zero_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('115.31'), Decimal('0')) == Decimal('115.31')


@allure.title('Yoga mat price includes five percent tax')
def test_yoga_mat_price_with_five_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('116.44'), Decimal('0.05')) == Decimal('122.26')


@allure.title('Yoga mat price includes ten percent tax')
def test_yoga_mat_price_with_ten_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('117.57'), Decimal('0.10')) == Decimal('129.33')


@allure.title('Yoga mat price includes twenty percent tax')
def test_yoga_mat_price_with_twenty_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('118.70'), Decimal('0.20')) == Decimal('142.44')


@allure.title('Yoga mat price includes twenty three percent tax')
def test_yoga_mat_price_with_twenty_three_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('119.83'), Decimal('0.23')) == Decimal('147.39')


@allure.title('Yoga mat price includes twenty five percent tax')
def test_yoga_mat_price_with_twenty_five_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('120.96'), Decimal('0.25')) == Decimal('151.20')


@allure.title('Wireless mouse price includes zero percent tax')
def test_wireless_mouse_price_with_zero_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('122.09'), Decimal('0')) == Decimal('122.09')


@allure.title('Wireless mouse price includes five percent tax')
def test_wireless_mouse_price_with_five_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('123.22'), Decimal('0.05')) == Decimal('129.38')


@allure.title('Wireless mouse price includes ten percent tax')
def test_wireless_mouse_price_with_ten_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('124.35'), Decimal('0.10')) == Decimal('136.79')


@allure.title('Wireless mouse price includes twenty percent tax')
def test_wireless_mouse_price_with_twenty_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('125.48'), Decimal('0.20')) == Decimal('150.58')


@allure.title('Wireless mouse price includes twenty three percent tax')
def test_wireless_mouse_price_with_twenty_three_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('126.61'), Decimal('0.23')) == Decimal('155.73')


@allure.title('Wireless mouse price includes twenty five percent tax')
def test_wireless_mouse_price_with_twenty_five_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('127.74'), Decimal('0.25')) == Decimal('159.68')


@allure.title('Usb charger price includes zero percent tax')
def test_usb_charger_price_with_zero_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('128.87'), Decimal('0')) == Decimal('128.87')


@allure.title('Usb charger price includes five percent tax')
def test_usb_charger_price_with_five_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('130.00'), Decimal('0.05')) == Decimal('136.50')


@allure.title('Usb charger price includes ten percent tax')
def test_usb_charger_price_with_ten_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('131.13'), Decimal('0.10')) == Decimal('144.24')


@allure.title('Usb charger price includes twenty percent tax')
def test_usb_charger_price_with_twenty_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('132.26'), Decimal('0.20')) == Decimal('158.71')


@allure.title('Usb charger price includes twenty three percent tax')
def test_usb_charger_price_with_twenty_three_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('133.39'), Decimal('0.23')) == Decimal('164.07')


@allure.title('Usb charger price includes twenty five percent tax')
def test_usb_charger_price_with_twenty_five_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('134.52'), Decimal('0.25')) == Decimal('168.15')


@allure.title('Travel pillow price includes zero percent tax')
def test_travel_pillow_price_with_zero_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('135.65'), Decimal('0')) == Decimal('135.65')


@allure.title('Travel pillow price includes five percent tax')
def test_travel_pillow_price_with_five_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('136.78'), Decimal('0.05')) == Decimal('143.62')


@allure.title('Travel pillow price includes ten percent tax')
def test_travel_pillow_price_with_ten_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('137.91'), Decimal('0.10')) == Decimal('151.70')


@allure.title('Travel pillow price includes twenty percent tax')
def test_travel_pillow_price_with_twenty_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('139.04'), Decimal('0.20')) == Decimal('166.85')


@allure.title('Travel pillow price includes twenty three percent tax')
def test_travel_pillow_price_with_twenty_three_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('140.17'), Decimal('0.23')) == Decimal('172.41')


@allure.title('Travel pillow price includes twenty five percent tax')
def test_travel_pillow_price_with_twenty_five_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('141.30'), Decimal('0.25')) == Decimal('176.63')


@allure.title('Packing cubes price includes zero percent tax')
def test_packing_cubes_price_with_zero_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('142.43'), Decimal('0')) == Decimal('142.43')


@allure.title('Packing cubes price includes five percent tax')
def test_packing_cubes_price_with_five_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('143.56'), Decimal('0.05')) == Decimal('150.74')


@allure.title('Packing cubes price includes ten percent tax')
def test_packing_cubes_price_with_ten_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('144.69'), Decimal('0.10')) == Decimal('159.16')


@allure.title('Packing cubes price includes twenty percent tax')
def test_packing_cubes_price_with_twenty_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('145.82'), Decimal('0.20')) == Decimal('174.98')


@allure.title('Packing cubes price includes twenty three percent tax')
def test_packing_cubes_price_with_twenty_three_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('146.95'), Decimal('0.23')) == Decimal('180.75')


@allure.title('Packing cubes price includes twenty five percent tax')
def test_packing_cubes_price_with_twenty_five_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('148.08'), Decimal('0.25')) == Decimal('185.10')


@allure.title('Rain jacket price includes zero percent tax')
def test_rain_jacket_price_with_zero_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('149.21'), Decimal('0')) == Decimal('149.21')


@allure.title('Rain jacket price includes five percent tax')
def test_rain_jacket_price_with_five_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('150.34'), Decimal('0.05')) == Decimal('157.86')


@allure.title('Rain jacket price includes ten percent tax')
def test_rain_jacket_price_with_ten_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('151.47'), Decimal('0.10')) == Decimal('166.62')


@allure.title('Rain jacket price includes twenty percent tax')
def test_rain_jacket_price_with_twenty_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('152.60'), Decimal('0.20')) == Decimal('183.12')


@allure.title('Rain jacket price includes twenty three percent tax')
def test_rain_jacket_price_with_twenty_three_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('153.73'), Decimal('0.23')) == Decimal('189.09')


@allure.title('Rain jacket price includes twenty five percent tax')
def test_rain_jacket_price_with_twenty_five_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('154.86'), Decimal('0.25')) == Decimal('193.58')


@allure.title('Hiking socks price includes zero percent tax')
def test_hiking_socks_price_with_zero_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('155.99'), Decimal('0')) == Decimal('155.99')


@allure.title('Hiking socks price includes five percent tax')
def test_hiking_socks_price_with_five_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('157.12'), Decimal('0.05')) == Decimal('164.98')


@allure.title('Hiking socks price includes ten percent tax')
def test_hiking_socks_price_with_ten_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('158.25'), Decimal('0.10')) == Decimal('174.08')


@allure.title('Hiking socks price includes twenty percent tax')
def test_hiking_socks_price_with_twenty_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('159.38'), Decimal('0.20')) == Decimal('191.26')


@allure.title('Hiking socks price includes twenty three percent tax')
def test_hiking_socks_price_with_twenty_three_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('160.51'), Decimal('0.23')) == Decimal('197.43')


@allure.title('Hiking socks price includes twenty five percent tax')
def test_hiking_socks_price_with_twenty_five_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('161.64'), Decimal('0.25')) == Decimal('202.05')


@allure.title('Bike lock price includes zero percent tax')
def test_bike_lock_price_with_zero_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('162.77'), Decimal('0')) == Decimal('162.77')


@allure.title('Bike lock price includes five percent tax')
def test_bike_lock_price_with_five_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('163.90'), Decimal('0.05')) == Decimal('172.10')


@allure.title('Bike lock price includes ten percent tax')
def test_bike_lock_price_with_ten_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('165.03'), Decimal('0.10')) == Decimal('181.53')


@allure.title('Bike lock price includes twenty percent tax')
def test_bike_lock_price_with_twenty_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('166.16'), Decimal('0.20')) == Decimal('199.39')


@allure.title('Bike lock price includes twenty three percent tax')
def test_bike_lock_price_with_twenty_three_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('167.29'), Decimal('0.23')) == Decimal('205.77')


@allure.title('Bike lock price includes twenty five percent tax')
def test_bike_lock_price_with_twenty_five_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('168.42'), Decimal('0.25')) == Decimal('210.53')


@allure.title('Camping lantern price includes zero percent tax')
def test_camping_lantern_price_with_zero_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('169.55'), Decimal('0')) == Decimal('169.55')


@allure.title('Camping lantern price includes five percent tax')
def test_camping_lantern_price_with_five_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('170.68'), Decimal('0.05')) == Decimal('179.21')


@allure.title('Camping lantern price includes ten percent tax')
def test_camping_lantern_price_with_ten_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('171.81'), Decimal('0.10')) == Decimal('188.99')


@allure.title('Camping lantern price includes twenty percent tax')
def test_camping_lantern_price_with_twenty_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('172.94'), Decimal('0.20')) == Decimal('207.53')


@allure.title('Camping lantern price includes twenty three percent tax')
def test_camping_lantern_price_with_twenty_three_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('174.07'), Decimal('0.23')) == Decimal('214.11')


@allure.title('Camping lantern price includes twenty five percent tax')
def test_camping_lantern_price_with_twenty_five_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('175.20'), Decimal('0.25')) == Decimal('219.00')


@allure.title('Lunch box price includes zero percent tax')
def test_lunch_box_price_with_zero_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('176.33'), Decimal('0')) == Decimal('176.33')


@allure.title('Lunch box price includes five percent tax')
def test_lunch_box_price_with_five_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('177.46'), Decimal('0.05')) == Decimal('186.33')


@allure.title('Lunch box price includes ten percent tax')
def test_lunch_box_price_with_ten_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('178.59'), Decimal('0.10')) == Decimal('196.45')


@allure.title('Lunch box price includes twenty percent tax')
def test_lunch_box_price_with_twenty_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('179.72'), Decimal('0.20')) == Decimal('215.66')


@allure.title('Lunch box price includes twenty three percent tax')
def test_lunch_box_price_with_twenty_three_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('180.85'), Decimal('0.23')) == Decimal('222.45')


@allure.title('Lunch box price includes twenty five percent tax')
def test_lunch_box_price_with_twenty_five_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('181.98'), Decimal('0.25')) == Decimal('227.48')


@allure.title('Tea infuser price includes zero percent tax')
def test_tea_infuser_price_with_zero_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('183.11'), Decimal('0')) == Decimal('183.11')


@allure.title('Tea infuser price includes five percent tax')
def test_tea_infuser_price_with_five_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('184.24'), Decimal('0.05')) == Decimal('193.45')


@allure.title('Tea infuser price includes ten percent tax')
def test_tea_infuser_price_with_ten_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('185.37'), Decimal('0.10')) == Decimal('203.91')


@allure.title('Tea infuser price includes twenty percent tax')
def test_tea_infuser_price_with_twenty_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('186.50'), Decimal('0.20')) == Decimal('223.80')


@allure.title('Tea infuser price includes twenty three percent tax')
def test_tea_infuser_price_with_twenty_three_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('187.63'), Decimal('0.23')) == Decimal('230.78')


@allure.title('Tea infuser price includes twenty five percent tax')
def test_tea_infuser_price_with_twenty_five_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('188.76'), Decimal('0.25')) == Decimal('235.95')


@allure.title('Plant pot price includes zero percent tax')
def test_plant_pot_price_with_zero_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('189.89'), Decimal('0')) == Decimal('189.89')


@allure.title('Plant pot price includes five percent tax')
def test_plant_pot_price_with_five_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('191.02'), Decimal('0.05')) == Decimal('200.57')


@allure.title('Plant pot price includes ten percent tax')
def test_plant_pot_price_with_ten_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('192.15'), Decimal('0.10')) == Decimal('211.37')


@allure.title('Plant pot price includes twenty percent tax')
def test_plant_pot_price_with_twenty_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('193.28'), Decimal('0.20')) == Decimal('231.94')


@allure.title('Plant pot price includes twenty three percent tax')
def test_plant_pot_price_with_twenty_three_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('194.41'), Decimal('0.23')) == Decimal('239.12')


@allure.title('Plant pot price includes twenty five percent tax')
def test_plant_pot_price_with_twenty_five_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('195.54'), Decimal('0.25')) == Decimal('244.43')


@allure.title('Photo frame price includes zero percent tax')
def test_photo_frame_price_with_zero_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('196.67'), Decimal('0')) == Decimal('196.67')


@allure.title('Photo frame price includes five percent tax')
def test_photo_frame_price_with_five_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('197.80'), Decimal('0.05')) == Decimal('207.69')


@allure.title('Photo frame price includes ten percent tax')
def test_photo_frame_price_with_ten_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('198.93'), Decimal('0.10')) == Decimal('218.82')


@allure.title('Photo frame price includes twenty percent tax')
def test_photo_frame_price_with_twenty_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('200.06'), Decimal('0.20')) == Decimal('240.07')


@allure.title('Photo frame price includes twenty three percent tax')
def test_photo_frame_price_with_twenty_three_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('201.19'), Decimal('0.23')) == Decimal('247.46')


@allure.title('Photo frame price includes twenty five percent tax')
def test_photo_frame_price_with_twenty_five_percent_tax():
    with allure.step('Verify tax-inclusive price rounds to the expected amount'):
        assert price_with_tax(Decimal('202.32'), Decimal('0.25')) == Decimal('252.90')


@allure.title('Canvas tote price after a 0% discount')
def test_canvas_tote_price_after_0_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('0.10'), Decimal('0')) == Decimal('0.10')


@allure.title('Canvas tote price after a 1% discount')
def test_canvas_tote_price_after_1_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('1.67'), Decimal('1')) == Decimal('1.65')


@allure.title('Canvas tote price after a 5% discount')
def test_canvas_tote_price_after_5_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('3.24'), Decimal('5')) == Decimal('3.08')


@allure.title('Canvas tote price after a 10% discount')
def test_canvas_tote_price_after_10_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('4.81'), Decimal('10')) == Decimal('4.33')


@allure.title('Canvas tote price after a 15% discount')
def test_canvas_tote_price_after_15_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('6.38'), Decimal('15')) == Decimal('5.42')


@allure.title('Canvas tote price after a 25% discount')
def test_canvas_tote_price_after_25_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('7.95'), Decimal('25')) == Decimal('5.96')


@allure.title('Canvas tote price after a 50% discount')
def test_canvas_tote_price_after_50_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('9.52'), Decimal('50')) == Decimal('4.76')


@allure.title('Canvas tote price after a 100% discount')
def test_canvas_tote_price_after_100_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('11.09'), Decimal('100')) == Decimal('0.00')


@allure.title('Travel mug price after a 0% discount')
def test_travel_mug_price_after_0_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('12.66'), Decimal('0')) == Decimal('12.66')


@allure.title('Travel mug price after a 1% discount')
def test_travel_mug_price_after_1_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('14.23'), Decimal('1')) == Decimal('14.09')


@allure.title('Travel mug price after a 5% discount')
def test_travel_mug_price_after_5_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('15.80'), Decimal('5')) == Decimal('15.01')


@allure.title('Travel mug price after a 10% discount')
def test_travel_mug_price_after_10_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('17.37'), Decimal('10')) == Decimal('15.63')


@allure.title('Travel mug price after a 15% discount')
def test_travel_mug_price_after_15_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('18.94'), Decimal('15')) == Decimal('16.10')


@allure.title('Travel mug price after a 25% discount')
def test_travel_mug_price_after_25_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('20.51'), Decimal('25')) == Decimal('15.38')


@allure.title('Travel mug price after a 50% discount')
def test_travel_mug_price_after_50_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('22.08'), Decimal('50')) == Decimal('11.04')


@allure.title('Travel mug price after a 100% discount')
def test_travel_mug_price_after_100_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('23.65'), Decimal('100')) == Decimal('0.00')


@allure.title('Pocket notebook price after a 0% discount')
def test_pocket_notebook_price_after_0_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('25.22'), Decimal('0')) == Decimal('25.22')


@allure.title('Pocket notebook price after a 1% discount')
def test_pocket_notebook_price_after_1_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('26.79'), Decimal('1')) == Decimal('26.52')


@allure.title('Pocket notebook price after a 5% discount')
def test_pocket_notebook_price_after_5_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('28.36'), Decimal('5')) == Decimal('26.94')


@allure.title('Pocket notebook price after a 10% discount')
def test_pocket_notebook_price_after_10_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('29.93'), Decimal('10')) == Decimal('26.94')


@allure.title('Pocket notebook price after a 15% discount')
def test_pocket_notebook_price_after_15_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('31.50'), Decimal('15')) == Decimal('26.78')


@allure.title('Pocket notebook price after a 25% discount')
def test_pocket_notebook_price_after_25_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('33.07'), Decimal('25')) == Decimal('24.80')


@allure.title('Pocket notebook price after a 50% discount')
def test_pocket_notebook_price_after_50_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('34.64'), Decimal('50')) == Decimal('17.32')


@allure.title('Pocket notebook price after a 100% discount')
def test_pocket_notebook_price_after_100_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('36.21'), Decimal('100')) == Decimal('0.00')


@allure.title('Cotton scarf price after a 0% discount')
def test_cotton_scarf_price_after_0_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('37.78'), Decimal('0')) == Decimal('37.78')


@allure.title('Cotton scarf price after a 1% discount')
def test_cotton_scarf_price_after_1_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('39.35'), Decimal('1')) == Decimal('38.96')


@allure.title('Cotton scarf price after a 5% discount')
def test_cotton_scarf_price_after_5_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('40.92'), Decimal('5')) == Decimal('38.87')


@allure.title('Cotton scarf price after a 10% discount')
def test_cotton_scarf_price_after_10_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('42.49'), Decimal('10')) == Decimal('38.24')


@allure.title('Cotton scarf price after a 15% discount')
def test_cotton_scarf_price_after_15_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('44.06'), Decimal('15')) == Decimal('37.45')


@allure.title('Cotton scarf price after a 25% discount')
def test_cotton_scarf_price_after_25_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('45.63'), Decimal('25')) == Decimal('34.22')


@allure.title('Cotton scarf price after a 50% discount')
def test_cotton_scarf_price_after_50_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('47.20'), Decimal('50')) == Decimal('23.60')


@allure.title('Cotton scarf price after a 100% discount')
def test_cotton_scarf_price_after_100_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('48.77'), Decimal('100')) == Decimal('0.00')


@allure.title('Desk lamp price after a 0% discount')
def test_desk_lamp_price_after_0_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('50.34'), Decimal('0')) == Decimal('50.34')


@allure.title('Desk lamp price after a 1% discount')
def test_desk_lamp_price_after_1_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('51.91'), Decimal('1')) == Decimal('51.39')


@allure.title('Desk lamp price after a 5% discount')
def test_desk_lamp_price_after_5_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('53.48'), Decimal('5')) == Decimal('50.81')


@allure.title('Desk lamp price after a 10% discount')
def test_desk_lamp_price_after_10_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('55.05'), Decimal('10')) == Decimal('49.55')


@allure.title('Desk lamp price after a 15% discount')
def test_desk_lamp_price_after_15_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('56.62'), Decimal('15')) == Decimal('48.13')


@allure.title('Desk lamp price after a 25% discount')
def test_desk_lamp_price_after_25_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('58.19'), Decimal('25')) == Decimal('43.64')


@allure.title('Desk lamp price after a 50% discount')
def test_desk_lamp_price_after_50_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('59.76'), Decimal('50')) == Decimal('29.88')


@allure.title('Desk lamp price after a 100% discount')
def test_desk_lamp_price_after_100_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('61.33'), Decimal('100')) == Decimal('0.00')


@allure.title('Water bottle price after a 0% discount')
def test_water_bottle_price_after_0_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('62.90'), Decimal('0')) == Decimal('62.90')


@allure.title('Water bottle price after a 1% discount')
def test_water_bottle_price_after_1_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('64.47'), Decimal('1')) == Decimal('63.83')


@allure.title('Water bottle price after a 5% discount')
def test_water_bottle_price_after_5_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('66.04'), Decimal('5')) == Decimal('62.74')


@allure.title('Water bottle price after a 10% discount')
def test_water_bottle_price_after_10_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('67.61'), Decimal('10')) == Decimal('60.85')


@allure.title('Water bottle price after a 15% discount')
def test_water_bottle_price_after_15_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('69.18'), Decimal('15')) == Decimal('58.80')


@allure.title('Water bottle price after a 25% discount')
def test_water_bottle_price_after_25_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('70.75'), Decimal('25')) == Decimal('53.06')


@allure.title('Water bottle price after a 50% discount')
def test_water_bottle_price_after_50_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('72.32'), Decimal('50')) == Decimal('36.16')


@allure.title('Water bottle price after a 100% discount')
def test_water_bottle_price_after_100_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('73.89'), Decimal('100')) == Decimal('0.00')


@allure.title('Laptop sleeve price after a 0% discount')
def test_laptop_sleeve_price_after_0_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('75.46'), Decimal('0')) == Decimal('75.46')


@allure.title('Laptop sleeve price after a 1% discount')
def test_laptop_sleeve_price_after_1_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('77.03'), Decimal('1')) == Decimal('76.26')


@allure.title('Laptop sleeve price after a 5% discount')
def test_laptop_sleeve_price_after_5_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('78.60'), Decimal('5')) == Decimal('74.67')


@allure.title('Laptop sleeve price after a 10% discount')
def test_laptop_sleeve_price_after_10_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('80.17'), Decimal('10')) == Decimal('72.15')


@allure.title('Laptop sleeve price after a 15% discount')
def test_laptop_sleeve_price_after_15_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('81.74'), Decimal('15')) == Decimal('69.48')


@allure.title('Laptop sleeve price after a 25% discount')
def test_laptop_sleeve_price_after_25_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('83.31'), Decimal('25')) == Decimal('62.48')


@allure.title('Laptop sleeve price after a 50% discount')
def test_laptop_sleeve_price_after_50_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('84.88'), Decimal('50')) == Decimal('42.44')


@allure.title('Laptop sleeve price after a 100% discount')
def test_laptop_sleeve_price_after_100_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('86.45'), Decimal('100')) == Decimal('0.00')


@allure.title('Weekend bag price after a 0% discount')
def test_weekend_bag_price_after_0_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('88.02'), Decimal('0')) == Decimal('88.02')


@allure.title('Weekend bag price after a 1% discount')
def test_weekend_bag_price_after_1_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('89.59'), Decimal('1')) == Decimal('88.69')


@allure.title('Weekend bag price after a 5% discount')
def test_weekend_bag_price_after_5_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('91.16'), Decimal('5')) == Decimal('86.60')


@allure.title('Weekend bag price after a 10% discount')
def test_weekend_bag_price_after_10_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('92.73'), Decimal('10')) == Decimal('83.46')


@allure.title('Weekend bag price after a 15% discount')
def test_weekend_bag_price_after_15_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('94.30'), Decimal('15')) == Decimal('80.16')


@allure.title('Weekend bag price after a 25% discount')
def test_weekend_bag_price_after_25_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('95.87'), Decimal('25')) == Decimal('71.90')


@allure.title('Weekend bag price after a 50% discount')
def test_weekend_bag_price_after_50_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('97.44'), Decimal('50')) == Decimal('48.72')


@allure.title('Weekend bag price after a 100% discount')
def test_weekend_bag_price_after_100_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('99.01'), Decimal('100')) == Decimal('0.00')


@allure.title('Wool beanie price after a 0% discount')
def test_wool_beanie_price_after_0_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('100.58'), Decimal('0')) == Decimal('100.58')


@allure.title('Wool beanie price after a 1% discount')
def test_wool_beanie_price_after_1_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('102.15'), Decimal('1')) == Decimal('101.13')


@allure.title('Wool beanie price after a 5% discount')
def test_wool_beanie_price_after_5_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('103.72'), Decimal('5')) == Decimal('98.53')


@allure.title('Wool beanie price after a 10% discount')
def test_wool_beanie_price_after_10_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('105.29'), Decimal('10')) == Decimal('94.76')


@allure.title('Wool beanie price after a 15% discount')
def test_wool_beanie_price_after_15_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('106.86'), Decimal('15')) == Decimal('90.83')


@allure.title('Wool beanie price after a 25% discount')
def test_wool_beanie_price_after_25_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('108.43'), Decimal('25')) == Decimal('81.32')


@allure.title('Wool beanie price after a 50% discount')
def test_wool_beanie_price_after_50_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('110.00'), Decimal('50')) == Decimal('55.00')


@allure.title('Wool beanie price after a 100% discount')
def test_wool_beanie_price_after_100_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('111.57'), Decimal('100')) == Decimal('0.00')


@allure.title('Leather wallet price after a 0% discount')
def test_leather_wallet_price_after_0_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('113.14'), Decimal('0')) == Decimal('113.14')


@allure.title('Leather wallet price after a 1% discount')
def test_leather_wallet_price_after_1_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('114.71'), Decimal('1')) == Decimal('113.56')


@allure.title('Leather wallet price after a 5% discount')
def test_leather_wallet_price_after_5_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('116.28'), Decimal('5')) == Decimal('110.47')


@allure.title('Leather wallet price after a 10% discount')
def test_leather_wallet_price_after_10_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('117.85'), Decimal('10')) == Decimal('106.07')


@allure.title('Leather wallet price after a 15% discount')
def test_leather_wallet_price_after_15_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('119.42'), Decimal('15')) == Decimal('101.51')


@allure.title('Leather wallet price after a 25% discount')
def test_leather_wallet_price_after_25_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('120.99'), Decimal('25')) == Decimal('90.74')


@allure.title('Leather wallet price after a 50% discount')
def test_leather_wallet_price_after_50_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('122.56'), Decimal('50')) == Decimal('61.28')


@allure.title('Leather wallet price after a 100% discount')
def test_leather_wallet_price_after_100_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('124.13'), Decimal('100')) == Decimal('0.00')


@allure.title('Ceramic bowl price after a 0% discount')
def test_ceramic_bowl_price_after_0_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('125.70'), Decimal('0')) == Decimal('125.70')


@allure.title('Ceramic bowl price after a 1% discount')
def test_ceramic_bowl_price_after_1_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('127.27'), Decimal('1')) == Decimal('126.00')


@allure.title('Ceramic bowl price after a 5% discount')
def test_ceramic_bowl_price_after_5_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('128.84'), Decimal('5')) == Decimal('122.40')


@allure.title('Ceramic bowl price after a 10% discount')
def test_ceramic_bowl_price_after_10_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('130.41'), Decimal('10')) == Decimal('117.37')


@allure.title('Ceramic bowl price after a 15% discount')
def test_ceramic_bowl_price_after_15_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('131.98'), Decimal('15')) == Decimal('112.18')


@allure.title('Ceramic bowl price after a 25% discount')
def test_ceramic_bowl_price_after_25_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('133.55'), Decimal('25')) == Decimal('100.16')


@allure.title('Ceramic bowl price after a 50% discount')
def test_ceramic_bowl_price_after_50_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('135.12'), Decimal('50')) == Decimal('67.56')


@allure.title('Ceramic bowl price after a 100% discount')
def test_ceramic_bowl_price_after_100_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('136.69'), Decimal('100')) == Decimal('0.00')


@allure.title('Linen apron price after a 0% discount')
def test_linen_apron_price_after_0_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('138.26'), Decimal('0')) == Decimal('138.26')


@allure.title('Linen apron price after a 1% discount')
def test_linen_apron_price_after_1_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('139.83'), Decimal('1')) == Decimal('138.43')


@allure.title('Linen apron price after a 5% discount')
def test_linen_apron_price_after_5_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('141.40'), Decimal('5')) == Decimal('134.33')


@allure.title('Linen apron price after a 10% discount')
def test_linen_apron_price_after_10_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('142.97'), Decimal('10')) == Decimal('128.67')


@allure.title('Linen apron price after a 15% discount')
def test_linen_apron_price_after_15_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('144.54'), Decimal('15')) == Decimal('122.86')


@allure.title('Linen apron price after a 25% discount')
def test_linen_apron_price_after_25_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('146.11'), Decimal('25')) == Decimal('109.58')


@allure.title('Linen apron price after a 50% discount')
def test_linen_apron_price_after_50_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('147.68'), Decimal('50')) == Decimal('73.84')


@allure.title('Linen apron price after a 100% discount')
def test_linen_apron_price_after_100_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('149.25'), Decimal('100')) == Decimal('0.00')


@allure.title('Phone stand price after a 0% discount')
def test_phone_stand_price_after_0_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('150.82'), Decimal('0')) == Decimal('150.82')


@allure.title('Phone stand price after a 1% discount')
def test_phone_stand_price_after_1_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('152.39'), Decimal('1')) == Decimal('150.87')


@allure.title('Phone stand price after a 5% discount')
def test_phone_stand_price_after_5_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('153.96'), Decimal('5')) == Decimal('146.26')


@allure.title('Phone stand price after a 10% discount')
def test_phone_stand_price_after_10_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('155.53'), Decimal('10')) == Decimal('139.98')


@allure.title('Phone stand price after a 15% discount')
def test_phone_stand_price_after_15_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('157.10'), Decimal('15')) == Decimal('133.54')


@allure.title('Phone stand price after a 25% discount')
def test_phone_stand_price_after_25_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('158.67'), Decimal('25')) == Decimal('119.00')


@allure.title('Phone stand price after a 50% discount')
def test_phone_stand_price_after_50_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('160.24'), Decimal('50')) == Decimal('80.12')


@allure.title('Phone stand price after a 100% discount')
def test_phone_stand_price_after_100_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('161.81'), Decimal('100')) == Decimal('0.00')


@allure.title('Reading light price after a 0% discount')
def test_reading_light_price_after_0_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('163.38'), Decimal('0')) == Decimal('163.38')


@allure.title('Reading light price after a 1% discount')
def test_reading_light_price_after_1_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('164.95'), Decimal('1')) == Decimal('163.30')


@allure.title('Reading light price after a 5% discount')
def test_reading_light_price_after_5_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('166.52'), Decimal('5')) == Decimal('158.19')


@allure.title('Reading light price after a 10% discount')
def test_reading_light_price_after_10_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('168.09'), Decimal('10')) == Decimal('151.28')


@allure.title('Reading light price after a 15% discount')
def test_reading_light_price_after_15_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('169.66'), Decimal('15')) == Decimal('144.21')


@allure.title('Reading light price after a 25% discount')
def test_reading_light_price_after_25_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('171.23'), Decimal('25')) == Decimal('128.42')


@allure.title('Reading light price after a 50% discount')
def test_reading_light_price_after_50_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('172.80'), Decimal('50')) == Decimal('86.40')


@allure.title('Reading light price after a 100% discount')
def test_reading_light_price_after_100_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('174.37'), Decimal('100')) == Decimal('0.00')


@allure.title('Picnic blanket price after a 0% discount')
def test_picnic_blanket_price_after_0_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('175.94'), Decimal('0')) == Decimal('175.94')


@allure.title('Picnic blanket price after a 1% discount')
def test_picnic_blanket_price_after_1_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('177.51'), Decimal('1')) == Decimal('175.73')


@allure.title('Picnic blanket price after a 5% discount')
def test_picnic_blanket_price_after_5_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('179.08'), Decimal('5')) == Decimal('170.13')


@allure.title('Picnic blanket price after a 10% discount')
def test_picnic_blanket_price_after_10_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('180.65'), Decimal('10')) == Decimal('162.59')


@allure.title('Picnic blanket price after a 15% discount')
def test_picnic_blanket_price_after_15_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('182.22'), Decimal('15')) == Decimal('154.89')


@allure.title('Picnic blanket price after a 25% discount')
def test_picnic_blanket_price_after_25_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('183.79'), Decimal('25')) == Decimal('137.84')


@allure.title('Picnic blanket price after a 50% discount')
def test_picnic_blanket_price_after_50_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('185.36'), Decimal('50')) == Decimal('92.68')


@allure.title('Picnic blanket price after a 100% discount')
def test_picnic_blanket_price_after_100_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('186.93'), Decimal('100')) == Decimal('0.00')


@allure.title('Coffee grinder price after a 0% discount')
def test_coffee_grinder_price_after_0_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('188.50'), Decimal('0')) == Decimal('188.50')


@allure.title('Coffee grinder price after a 1% discount')
def test_coffee_grinder_price_after_1_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('190.07'), Decimal('1')) == Decimal('188.17')


@allure.title('Coffee grinder price after a 5% discount')
def test_coffee_grinder_price_after_5_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('191.64'), Decimal('5')) == Decimal('182.06')


@allure.title('Coffee grinder price after a 10% discount')
def test_coffee_grinder_price_after_10_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('193.21'), Decimal('10')) == Decimal('173.89')


@allure.title('Coffee grinder price after a 15% discount')
def test_coffee_grinder_price_after_15_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('194.78'), Decimal('15')) == Decimal('165.56')


@allure.title('Coffee grinder price after a 25% discount')
def test_coffee_grinder_price_after_25_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('196.35'), Decimal('25')) == Decimal('147.26')


@allure.title('Coffee grinder price after a 50% discount')
def test_coffee_grinder_price_after_50_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('197.92'), Decimal('50')) == Decimal('98.96')


@allure.title('Coffee grinder price after a 100% discount')
def test_coffee_grinder_price_after_100_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('199.49'), Decimal('100')) == Decimal('0.00')


@allure.title('Running belt price after a 0% discount')
def test_running_belt_price_after_0_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('201.06'), Decimal('0')) == Decimal('201.06')


@allure.title('Running belt price after a 1% discount')
def test_running_belt_price_after_1_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('202.63'), Decimal('1')) == Decimal('200.60')


@allure.title('Running belt price after a 5% discount')
def test_running_belt_price_after_5_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('204.20'), Decimal('5')) == Decimal('193.99')


@allure.title('Running belt price after a 10% discount')
def test_running_belt_price_after_10_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('205.77'), Decimal('10')) == Decimal('185.19')


@allure.title('Running belt price after a 15% discount')
def test_running_belt_price_after_15_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('207.34'), Decimal('15')) == Decimal('176.24')


@allure.title('Running belt price after a 25% discount')
def test_running_belt_price_after_25_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('208.91'), Decimal('25')) == Decimal('156.68')


@allure.title('Running belt price after a 50% discount')
def test_running_belt_price_after_50_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('210.48'), Decimal('50')) == Decimal('105.24')


@allure.title('Running belt price after a 100% discount')
def test_running_belt_price_after_100_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('212.05'), Decimal('100')) == Decimal('0.00')


@allure.title('Yoga mat price after a 0% discount')
def test_yoga_mat_price_after_0_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('213.62'), Decimal('0')) == Decimal('213.62')


@allure.title('Yoga mat price after a 1% discount')
def test_yoga_mat_price_after_1_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('215.19'), Decimal('1')) == Decimal('213.04')


@allure.title('Yoga mat price after a 5% discount')
def test_yoga_mat_price_after_5_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('216.76'), Decimal('5')) == Decimal('205.92')


@allure.title('Yoga mat price after a 10% discount')
def test_yoga_mat_price_after_10_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('218.33'), Decimal('10')) == Decimal('196.50')


@allure.title('Yoga mat price after a 15% discount')
def test_yoga_mat_price_after_15_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('219.90'), Decimal('15')) == Decimal('186.92')


@allure.title('Yoga mat price after a 25% discount')
def test_yoga_mat_price_after_25_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('221.47'), Decimal('25')) == Decimal('166.10')


@allure.title('Yoga mat price after a 50% discount')
def test_yoga_mat_price_after_50_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('223.04'), Decimal('50')) == Decimal('111.52')


@allure.title('Yoga mat price after a 100% discount')
def test_yoga_mat_price_after_100_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('224.61'), Decimal('100')) == Decimal('0.00')


@allure.title('Wireless mouse price after a 0% discount')
def test_wireless_mouse_price_after_0_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('226.18'), Decimal('0')) == Decimal('226.18')


@allure.title('Wireless mouse price after a 1% discount')
def test_wireless_mouse_price_after_1_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('227.75'), Decimal('1')) == Decimal('225.47')


@allure.title('Wireless mouse price after a 5% discount')
def test_wireless_mouse_price_after_5_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('229.32'), Decimal('5')) == Decimal('217.85')


@allure.title('Wireless mouse price after a 10% discount')
def test_wireless_mouse_price_after_10_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('230.89'), Decimal('10')) == Decimal('207.80')


@allure.title('Wireless mouse price after a 15% discount')
def test_wireless_mouse_price_after_15_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('232.46'), Decimal('15')) == Decimal('197.59')


@allure.title('Wireless mouse price after a 25% discount')
def test_wireless_mouse_price_after_25_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('234.03'), Decimal('25')) == Decimal('175.52')


@allure.title('Wireless mouse price after a 50% discount')
def test_wireless_mouse_price_after_50_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('235.60'), Decimal('50')) == Decimal('117.80')


@allure.title('Wireless mouse price after a 100% discount')
def test_wireless_mouse_price_after_100_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('237.17'), Decimal('100')) == Decimal('0.00')


@allure.title('Usb charger price after a 0% discount')
def test_usb_charger_price_after_0_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('238.74'), Decimal('0')) == Decimal('238.74')


@allure.title('Usb charger price after a 1% discount')
def test_usb_charger_price_after_1_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('240.31'), Decimal('1')) == Decimal('237.91')


@allure.title('Usb charger price after a 5% discount')
def test_usb_charger_price_after_5_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('241.88'), Decimal('5')) == Decimal('229.79')


@allure.title('Usb charger price after a 10% discount')
def test_usb_charger_price_after_10_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('243.45'), Decimal('10')) == Decimal('219.11')


@allure.title('Usb charger price after a 15% discount')
def test_usb_charger_price_after_15_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('245.02'), Decimal('15')) == Decimal('208.27')


@allure.title('Usb charger price after a 25% discount')
def test_usb_charger_price_after_25_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('246.59'), Decimal('25')) == Decimal('184.94')


@allure.title('Usb charger price after a 50% discount')
def test_usb_charger_price_after_50_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('248.16'), Decimal('50')) == Decimal('124.08')


@allure.title('Usb charger price after a 100% discount')
def test_usb_charger_price_after_100_percent_discount():
    with allure.step('Verify promotion produces the expected discounted price'):
        assert apply_discount(Decimal('249.73'), Decimal('100')) == Decimal('0.00')


@allure.title("Half cent tax rounds up")
def test_half_cent_tax_rounds_up():
    with allure.step("Verify tax rounding boundary"):
        assert price_with_tax(Decimal("0.05"), Decimal("0.10")) == Decimal("0.06")


@allure.title("Tax below half cent rounds down")
def test_tax_below_half_cent_rounds_down():
    with allure.step("Verify tax rounding boundary"):
        assert price_with_tax(Decimal("0.04"), Decimal("0.10")) == Decimal("0.04")


@allure.title("Free product remains free with tax")
def test_free_product_remains_free_with_tax():
    with allure.step("Verify tax rounding boundary"):
        assert price_with_tax(Decimal("0"), Decimal("0.23")) == Decimal("0.00")


@allure.title("Whole price keeps two decimal places")
def test_whole_price_keeps_two_decimal_places():
    with allure.step("Verify tax rounding boundary"):
        assert price_with_tax(Decimal("20"), Decimal("0")) == Decimal("20.00")


@allure.title("High value order includes tax")
def test_high_value_order_includes_tax():
    with allure.step("Verify tax rounding boundary"):
        assert price_with_tax(Decimal("9999.99"), Decimal("0.23")) == Decimal("12299.99")


@allure.title("Fractional tax rate is preserved")
def test_fractional_tax_rate_is_preserved():
    with allure.step("Verify tax rounding boundary"):
        assert price_with_tax(Decimal("100"), Decimal("0.075")) == Decimal("107.50")


@allure.title("Half cent discount rounds up")
def test_half_cent_discount_rounds_up():
    with allure.step("Verify discount rounding boundary"):
        assert apply_discount(Decimal("0.05"), Decimal("50")) == Decimal("0.03")


@allure.title("Discount below half cent rounds down")
def test_discount_below_half_cent_rounds_down():
    with allure.step("Verify discount rounding boundary"):
        assert apply_discount(Decimal("0.04"), Decimal("90")) == Decimal("0.00")


@allure.title("Free product stays free after discount")
def test_free_product_stays_free_after_discount():
    with allure.step("Verify discount rounding boundary"):
        assert apply_discount(Decimal("0"), Decimal("25")) == Decimal("0.00")


@allure.title("Full discount removes entire price")
def test_full_discount_removes_entire_price():
    with allure.step("Verify discount rounding boundary"):
        assert apply_discount(Decimal("999.99"), Decimal("100")) == Decimal("0.00")


@allure.title("Fractional discount is preserved")
def test_fractional_discount_is_preserved():
    with allure.step("Verify discount rounding boundary"):
        assert apply_discount(Decimal("100"), Decimal("12.5")) == Decimal("87.50")


@allure.title("Small discount on high value product")
def test_small_discount_on_high_value_product():
    with allure.step("Verify discount rounding boundary"):
        assert apply_discount(Decimal("10000"), Decimal("0.01")) == Decimal("9999.00")
