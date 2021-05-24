from selenium import webdriver
from requests import get
import clipboard
import time

password = 'lollollolQ1_'
mail_url = 'https://temp-mail.org/pl/'
zappka_url = 'https://www.zabka.pl/zarejestruj-sie'


class bot():
    def __init__(self):
        self.driver = webdriver.Chrome('/Users/jasiek/PycharmProjects/zappka/chromedriver')
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)

    def get_mail(self):
        self.driver.get(mail_url)
        time.sleep(6)
        mail_button = self.driver.find_element_by_xpath('//*[@id="click-to-copy"]')
        mail_button.click()
        mail = clipboard.paste()
        f = open("mails.txt", "a")
        f.write(mail + '\n')
        f.close()
        return mail

    def fill_zappka(self, mail, password):
        self.driver.get(zappka_url)
        time.sleep(2)
        name_input = self.driver.find_element_by_xpath('//*[@id="register_form_firstName"]')
        name_input.send_keys('Janek')
        mail_input = self.driver.find_element_by_xpath('//*[@id="register_form_email"]')
        mail_input.send_keys(mail)
        age_input = self.driver.find_element_by_xpath('//*[@id="register_form_birthDate"]')
        age_input.send_keys('11/11/1999')
        password_input = self.driver.find_element_by_xpath('//*[@id="register_form_password_first"]')
        password_input.send_keys(password)
        repassword_input = self.driver.find_element_by_xpath('//*[@id="register_form_password_second"]')
        repassword_input.send_keys(password)
        agree_button = self.driver.find_element_by_xpath('//*[@id="CybotCookiebotDialog"]/div/div/div/div[2]/button[1]')
        agree_button.click()
        agree_button_1 = self.driver.find_element_by_xpath(
            '//*[@id="main"]/section/div/div/div[1]/div/div[2]/div/form/div[7]/div/label/span')
        agree_button_1.click()
        agree_button_2 = self.driver.find_element_by_xpath(
            '//*[@id="register_form_rulesAgreement"]')  # problem
        agree_button_2.click()
        agree_button_3 = self.driver.find_element_by_xpath(
            '//*[@id="main"]/section/div/div/div[1]/div/div[2]/div/form/div[8]/div/label/span')
        agree_button_3.click()
        submit = self.driver.find_element_by_xpath('//*[@id="register_form_submit"]')
        submit.click()
        time.sleep(5)

    def agree(self):
        self.driver.get(mail_url)
        time.sleep(5)
        mail = self.driver.find_element_by_xpath(
            '//*[@id="tm-body"]/main/div[1]/div/div[2]/div[2]/div/div[1]/div/div[4]/ul/li[2]/div[1]/a/span[2]')
        mail.click()
        time.sleep(5)
        agree = self.driver.find_element_by_xpath(
            '//*[@id="tm-body"]/main/div[1]/div/div[2]/div[2]/div/div[1]/div/div[2]/div[3]/table/tbody/tr[4]/td/a[3]')
        print(agree.text)
        agree.click()


def main():
    botek = bot()
    mail = botek.get_mail()
    botek.fill_zappka(mail, password)
    botek.agree()
    time.sleep(5)


main()
