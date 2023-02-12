
import pytest
from .pages.men_page import MenPage

def test_go_to_tops_men_page(driver):
    url = "https://magento.softwaretestingboard.com/men.html"
    page = MenPage(driver, url)
    page.open()
    page.go_to_tops_men_page()
    assert "tops-men" in driver.current_url , "Tops men page is not presented"
def test_go_to_bottoms_men_page(driver):
    url = "https://magento.softwaretestingboard.com/men.html"
    page = MenPage(driver, url)
    page.open()
    page.go_to_bottoms_men_page()
    assert "bottoms-men" in driver.current_url, "Tops men page is not presented"
def test_go_to_hoodies_men_page(driver):
    url = "https://magento.softwaretestingboard.com/men.html"
    page = MenPage(driver, url)
    page.open()
    page.go_to_hoodies_men_page()
    assert "hoodies-and-sweatshirts-men" in driver.current_url, "Hoodies men page is not presented"
def test_go_to_jackets_men_page(driver):
    url = "https://magento.softwaretestingboard.com/men.html"
    page = MenPage(driver, url)
    page.open()
    page.go_to_jackets_men_page()
    assert "jackets-men" in driver.current_url, "Jackets men page is not presented"
def test_go_to_tees_men_page(driver):
    url = "https://magento.softwaretestingboard.com/men.html"
    page = MenPage(driver, url)
    page.open()
    page.go_to_tees_men_page()
    assert "tees-men" in driver.current_url, "Tees men page is not presented"
def test_go_to_tanks_men_page(driver):
    url = "https://magento.softwaretestingboard.com/men.html"
    page = MenPage(driver, url)
    page.open()
    page.go_to_tanks_men_page()
    assert "tanks-men" in driver.current_url, "Tanks men page is not presented"
def test_go_to_pants_men_page(driver):
    url = "https://magento.softwaretestingboard.com/men.html"
    page = MenPage(driver, url)
    page.open()
    page.go_to_pants_men_page()
    assert "pants-men" in driver.current_url, "Pants men page is not presented"
def test_go_to_shorts_men_page(driver):
    url = "https://magento.softwaretestingboard.com/men.html"
    page = MenPage(driver, url)
    page.open()
    page.go_to_shorts_men_page()
    assert "shorts-men" in driver.current_url, "Shorts men page is not presented"