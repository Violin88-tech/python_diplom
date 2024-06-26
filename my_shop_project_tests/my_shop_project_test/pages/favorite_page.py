import allure
from selene import browser, have


class FavoritePage:
    with allure.step("Number book search"):
        def find_item(self):
            browser.element('.header__search input').type(
                "Искусственный интеллект с примерами на Python. Создание приложений искусственного интеллекта"
            ).press_enter()
            return self

    with allure.step("Open product page"):
        def open_page_item(self):
            browser.element('.item .item__title').click()
            return self

    with allure.step("Click add to favorites"):
        def click_add_to_favorites(self):
            browser.element('.form-control .is-heart').click()
            browser.element('.favorite .badge').should(have.exact_text('1'))
            return self

    with allure.step("Open favorites"):
        def open_favorites(self):
            browser.element('.header__icons .favorite').click()
            return self

    with allure.step("Click delete to favorites"):
        def click_delete_to_favorites(self):
            browser.element('.item .is-heart').click()
            return self

    with allure.step("Assert text favorites"):
        def assert_page_favorites(self):
            browser.element('.wrap h3').should(
                have.text("Избранных товаров нет")
            )
            return self


favorite = FavoritePage()
