from selenium.webdriver.common.by import By


def test_availability_button_add_to_basket(browser):
    """ Функция проверки наличия кнопки Добавить в корзину, для испанского языка """

    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(link)
    submit_button = browser.find_element(by=By.CSS_SELECTOR, value='.add-to-basket > [type="submit"]')
    assert submit_button.text == "Añadir al carrito", 'Текст не соответствует'
