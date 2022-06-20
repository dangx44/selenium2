from leumi.leumi2 import Luemi2

with Luemi2() as bot:
    bot.land_first_page()
    bot.fill_dates()
    bot.click_continue_btn()
    bot.drop_down_percent()
