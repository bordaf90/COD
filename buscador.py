import selenium

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait  # faltaba importar esto
from selenium.webdriver.support import expected_conditions as EC  # faltaba importar esto
from selenium.webdriver.common.by import By  # faltaba importar esto

import unittest
import time
import pandas as pd
import datetime

import re
import math

import os
import sys
os.path.dirname(sys.executable)

website = 'https://www.google.com.ar'
path = '/Users/macbookpro/Downloads/chromedriver'

print("Ingrese nueva búsqueda")
buscar = input()


class Items(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(path)
        self.driver.get(website)

    def test_buscador(self):
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(buscar)
        self.driver.implicitly_wait(5)
        # time.sleep(4)

        self.driver.find_element_by_class_name(
            'gNO89b').click()
        # self.driver.implicitly_wait(5)
        time.sleep(5)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
