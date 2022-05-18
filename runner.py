from WebUI import Scenario
from keys import *

if __name__ == "__main__":
    c = Scenario()
    c.login_site(login, password)
    c.choose_laptops()
    c.choose_dell()
    c.click_add_to_cart_button()
    c.go_to_cart_and_click_place_order()
    c.fill_in_the_fields_and_click_button_purchase(name, country, city, card, month, year)
    c.check_for_pop_up_window()
