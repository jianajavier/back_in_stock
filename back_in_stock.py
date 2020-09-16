from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException, InvalidArgumentException
from helpers.web_helper_methods import *
from datetime import datetime
import argparse
import os
import pdb

TODAYS_DATE = datetime.today().strftime('%Y-%m-%d')
SCREENSHOT_NAME = "back_in_stock_screenshot_%s.png" % TODAYS_DATE

def everlane(driver):
    f = open("everlane.txt", "r")
    for link in f:
        link = link.strip("\n")
        driver.get(link)

        # if '404' in driver.page_source:
        #     print('Item not found %s' % link)
        #     pass

        try:
            # Dismiss the modal
            ActionChains(driver).send_keys(Keys.ESCAPE).perform()

            # Choose the size
            size_button = driver.find_element(By.XPATH, '//*[@id="content"]/div/div[3]/div[2]/div/div/div/div[2]/div/div[1]/div/div[2]/div[2]/div[3]/div[2]/div[4]')
            size_button.click()

            # Click add button
            add_button = driver.find_element_by_class_name('product-page__purchase-button')

            if add_button.is_enabled():
                save_screenshot(driver, SCREENSHOT_NAME)
                send_email(prepare_email(link))

        except NoSuchElementException as e:
            print(e)
            pass

def prepare_email(link):
    email_params = {}

    subject = "Back in Stock!"

    email_params['subject'] = subject
    email_params['body'] = """\
                            <p>%s</p>
                            <p>Screenshot<br/>
                                <img src="cid:image1">
                            </p>
                            """ % link
    email_params['screenshot_name'] = SCREENSHOT_NAME
    return email_params

def parseArguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-b", "--debug", help="Debug mode", type=int, default=0)
    args = parser.parse_args()

    return args

def main(debug):
    driver = initialize_driver(debug)
    everlane(driver)

if __name__ == '__main__':
    args = parseArguments()
    main(args.debug)

