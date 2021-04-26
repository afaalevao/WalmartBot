from selenium import webdriver
from selenium.webdriver.support.ui import Select  # ADDED
import time


class WalmartBot:

    def __init__(self, first_name, last_name, email, address1, address2, city, postal_code, phone, credit_number,
                 credit_month, credit_year, credit_ccv, chrome_path):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.address1 = address1  # ADDED
        self.address2 = address2  # ADDED
        self.city = city  # ADDED
        self.postal_code = postal_code  # ADDED
        self.phone = phone
        self.credit_number = credit_number
        self.credit_month = credit_month
        self.credit_year = credit_year
        self.credit_ccv = credit_ccv
        self.driver = webdriver.Chrome(chrome_path)
        #self.driver.get('https://www.walmart.com/ip/PlayStation-5-Console/363472942')  # Walmart PS5
        self.driver.get('https://www.walmart.com/ip/Call-of-Duty-Black-Ops-Cold-War-Activision-PlayStation-5/176630812')

    def add_to_cart_and_checkout(self):
        addToCart = '//*[@id="add-on-atc-container"]/div[1]/section/div[1]/div[3]/button/span/span'
        checkOut = ('//*[@id="cart-root-container-content-skip"]/div[1]/div/div[2]/div/div/div/div/'
                    'div[3]/div/div/div[2]/div/div[2]/div/button[1]')
        continueWithoutAccount = ('/html/body/div[1]/div/div[1]/div/div[1]/div[3]/div/div/div/div[1]'
                                  '/div/div/div/div/div[3]/div/div[1]/div/section/section/div/button/span')
        self.click_button(addToCart)
        self.click_button(checkOut)
        self.click_button(continueWithoutAccount)

    def filling_shipping_info(self):
        firstContinue = ('/html/body/div[1]/div/div[1]/div/div[1]/div[3]/div/div/div/div[2]/div/div[2]/'
                         'div/div/div/div[3]/div/div/div[2]/button/span')
        firstName = '//*[@id="firstName"]'
        lastName = '//*[@id="lastName"]'
        email = '//*[@id="email"]'
        address1 = '//*[@id="addressLineOne"]'
        address2 = '//*[@id="addressLineTwo"]'
        city = '//*[@id="city"]'
        postal_code = '//*[@id="postalCode"]'
        phone = '//*[@id="phone"]'
        confirmInfo = ('/html/body/div[1]/div/div[1]/div/div[1]/div[3]/div/div/div/div[3]/div[1]/div[2]/'
                       'div/div/div/div[3]/div/div/div/div/div/form/div[2]/div[2]/button/span')

        # Auto-populate input fields
        self.click_button(firstContinue)
        self.enter_data(firstName, self.first_name)
        self.enter_data(lastName, self.last_name)
        self.enter_data(phone, self.phone)
        self.enter_data(email, self.email)
        self.enter_data(address1, self.address1)
        self.enter_data(address2, self.address2)
        self.enter_data(city, self.city)
        self.enter_data(postal_code, self.postal_code)

        # Code to auto-populate state select option
        select = Select(self.driver.find_element_by_id('state'))
        select.select_by_visible_text('California')  # ADDED

        # Submit information
        self.click_button(confirmInfo)

    def fill_out_payment_and_order(self):  # FILLS OUT PAYMENT
        creditCardNum = '//*[@id="creditCard"]'
        creditExpireMonth = '//*[@id="month-chooser"]'
        creditExpireYear = '//*[@id="year-chooser"]'
        creditCVV = '//*[@id="cvv"]'
        reviewOrder = ('/html/body/div[1]/div/div[1]/div/div[1]/div[3]/div/div/div/div[4]/div[1]/div[2]/div/div'
                       '/div/div[3]/div[2]/div/div/div/div[2]/div/div/div/form/div[3]/div/button/span/span/span')
        self.enter_data(creditCardNum, self.credit_number)
        self.enter_data(creditExpireMonth, self.credit_month)
        self.enter_data(creditExpireYear, self.credit_year)
        self.enter_data(creditCVV, self.credit_ccv)
        self.click_button(reviewOrder)

    def click_button(self, xpath):
        try:
            self.driver.find_element_by_xpath(xpath).click()
        except Exception:
            time.sleep(1)
            self.click_button(xpath)

    def enter_data(self, field, data):
        try:
            if field == '//*[@id="city"]' or field == '//*[@id="postalCode"]':
                self.driver.find_element_by_xpath(field).clear()
            self.driver.find_element_by_xpath(field).send_keys(data)
            pass

        except Exception:
            time.sleep(1)
            self.enter_data(field, data)


if __name__ == "__main__":
    personal_info = dict(
        first_name="Andrew",
        last_name="Faalevao",
        email="",
        address1="",
        address2="",
        city="",
        postal_code="",
        phone="",
        credit_number="",
        credit_month="",
        credit_year="",
        credit_ccv="",
        chrome_path="C:/Users/andre/Downloads/chromedriver_win32/chromedriver.exe"
    )

    bot = WalmartBot(**personal_info)
    bot.add_to_cart_and_checkout()
    bot.filling_shipping_info()
    bot.fill_out_payment_and_order()
    # You can add those methods in the __init__ as well