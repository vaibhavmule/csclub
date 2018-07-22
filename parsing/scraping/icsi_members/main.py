import os
import re
import csv
import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup


class MemberFinderScraper(object):
    def __init__(self):
        self.url = "https://www.icsi.in/student/Members/MemberSearch.aspx?SkinSrc=%5BG%5DSkins/IcsiTheme/IcsiIn-Bare&ContainerSrc=%5BG%5DContainers/IcsiTheme/NoContainer"
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=1920x1080")
        chrome_driver = os.path.abspath("chromedriver")
        self.driver = webdriver.Chrome(
            chrome_options=chrome_options,
            executable_path=chrome_driver)
        self.driver.set_window_size(1120, 550)

    def scrape(self):
        self.driver.get(self.url)

        wait = WebDriverWait(self.driver, 20)
        element = wait.until(EC.element_to_be_clickable((
            By.XPATH, '//*[@id="dnn_ctr410_MemberSearch_btnSearch"]')))
        self.driver.find_element_by_xpath(
            '//*[@id="dnn_ctr410_MemberSearch_btnSearch"]').click()

        wait = WebDriverWait(self.driver, 20)
        handle = wait.until(EC.presence_of_element_located((
            By.XPATH, '//*[@id="dnn_ctr410_MemberSearch_pnlHolder"]')))

        # select = self.driver.find_element_by_id('dnn_ctr410_MemberSearch_grdMembers_ctl00_ctl02_ctl01_PageSizeComboBox_Input').click()
        # wait = WebDriverWait(self.driver, 20)
        # select_element = wait.until(EC.visibility_of_element_located((
        #     By.XPATH, '//*[@id="dnn_ctr410_MemberSearch_grdMembers_ctl00_ctl02_ctl01_PageSizeComboBox_DropDown"]/div/ul/li[3]')))
        # select_element.click()

        # self.driver.implicitly_wait(10)

        pageno = 2

        emailscsv = open('emails.csv', 'w', newline='')
        writer = csv.writer(emailscsv)

        while True:
            if pageno == 4573:
                break

            if pageno in range(10, 5000, 10):
                time.sleep(1)

            if pageno in range(100, 5000, 100):
                time.sleep(5)

            s = BeautifulSoup(self.driver.page_source, "lxml")
            id_r = re.compile(
                r'dnn_ctr410_MemberSearch_grdMembers_ctl00_ctl([A-Z0-9-]+)_lblEmail')
            attrs = {
                'id': id_r}

            for name in s.findAll('span', attrs=attrs):
                email = name.text
                if email:
                    writer.writerow([email])
                    print(email)

            try:
                next_page_elem = self.driver.find_element_by_xpath(
                    '//*[@id="dnn_ctr410_MemberSearch_grdMembers_ctl00"]/thead/tr[2]/td/table/tbody/tr/td/div[3]/input[1]')
            except NoSuchElementException:
                print('no such element')
                # break # no more pages

            print('page ', pageno, '\n')
            next_page_elem.click()

            def next_page(driver):
                '''
                Wait until the next page comes.
                '''
                element = driver.find_element_by_css_selector(
                    '#dnn_ctr410_MemberSearch_grdMembers_ctl00 > thead > tr.rgPager > td > table > tbody > tr > td > div.rgWrap.rgNumPart > a.rgCurrentPage > span')
                print(element.text, 'stopped')
                return int(element.text) == pageno
            wait = WebDriverWait(self.driver, 120)
            wait.until(next_page)
            pageno += 1

        emailscsv.close()
        self.driver.quit()


if __name__ == '__main__':
    scraper = MemberFinderScraper()
    scraper.scrape()
