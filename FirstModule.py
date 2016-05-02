'''
Created on 2015-11-08

@author: Nitasha
'''
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys



testSite = "http://mobiletest.me/user/login"
testURLS = ["https://www.doctella.com/", 
            "https://www.doctella.com/activity-feed",
            "https://www.doctella.com/patients.html"
            "https://www.doctella.com/about-us.html",
            "https://www.doctella.com/contact.html",
            "https://www.doctella.com/careers.html",
            "https://groups.google.com/forum/?hl=en#!forum/doctella-support"
            ]
testSiteLoginName = "nitasha@doctella.com"
testSiteLoginPassword = "n1229syed"
deviceTotal = 200

class Test(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()    
   

    def TestWebsiteSetup(self):
        driver = self.driver
        driver.get(testSite)
        
        driver.find_element_by_id("google_provider").click()
        time.sleep(2)
        #enter email
        Emailelement = driver.find_element_by_id("Email")
        Emailelement.clear()
        Emailelement.send_keys(testSiteLoginName)
        
        #click next
        driver.find_element_by_id("next").click()
        
        #enter password
        PasswordElement = driver.find_element_by_id("Passwd")
        PasswordElement.clear()
        PasswordElement.send_keys(testSiteLoginPassword)
        
        driver.find_element_by_id("signIn").click()
        time.sleep(2)
        driver.find_element_by_id("submit_approve_access").click()
          
    def testURLS(self):
        driver = self.driver
        
        deviceSelect = driver.find_element_by_id("amazon_kindle_fire_emulator")
        deviceSelect.click()
        
        
        for URL in testURLS:
            for  i in deviceTotal:
                inputURL = driver.find_element_by_name("url")
                inputURL.send_keys(URL)
                inputURL.send_keys(Keys.ENTER)
                driver.save_screenshot("Screenshot %i")%(i)
                nextDevice = driver.find_element_by_class_name("next_device")
                nextDevice.click()
            
    def tearDown(self):
        self.driver.close()
   
