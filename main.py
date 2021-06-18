from selenium import webdriver
from time import sleep

driver = webdriver.Chrome(r"C:\Users\ommm\PycharmProject\selenium\Browsers\chromedriver.exe")
driver.get("https://www.google.co.in/maps/@10.8091781,78.2885026,7z")
sleep(2)


def searchplace():
    Place = driver.find_element_by_class_name("tactile-searchbox-input")
    Place.send_keys("gajuwaka")
    Submit = driver.find_element_by_xpath(
        "/html/body/jsl/div[3]/div[9]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/button")
    Submit.click()


searchplace()


def directions():
    sleep(10)
    directions = driver.find_element_by_xpath(
        "/html/body/jsl/div[3]/div[9]/div[8]/div/div[1]/div/div/div[4]/div[1]/div/button/img")
    directions.click()


directions()


def find():
    sleep(6)
    find = driver.find_element_by_xpath(
        "/html/body/jsl/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/div/div/input")
    find.send_keys("visakhapatnam")
    sleep(2)
    search = driver.find_element_by_xpath(
        "/html/body/jsl/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/button[1]")
    search.click()


find()


def kilometers():
    sleep(5)
    Totalkilometers = driver.find_element_by_xpath(
        "/html/body/jsl/div[3]/div[9]/div[8]/div/div[1]/div/div/div[5]/div[1]/div/div[1]/div[1]/div[2]/div")
    print("Total Kilometers:", Totalkilometers.text)
    sleep(5)
    time = driver.find_element_by_xpath(
        "/html/body/jsl/div[3]/div[9]/div[8]/div/div[1]/div/div/div[5]/div[1]/div/div[1]/div[1]/div[1]/span[1]")
    print("Time Taken:", time.text)
    sleep(7)

kilometers()
