import pytest
from .pages.women_page import WomenPage

def test_go_to_tops_women_page(driver):
    url = "https://magento.softwaretestingboard.com/women.html"
    page = WomenPage(driver, url)
    page.open()
    page.go_to_tops_women_page()
    assert "tops-women" in driver.current_url , "Tops women page is not presented"
def test_go_to_bottoms_women_page(driver):
    url = "https://magento.softwaretestingboard.com/women.html"
    page = WomenPage(driver, url)
    page.open()
    page.go_to_bottoms_women_page()
    assert "bottoms-women" in driver.current_url , "Bottoms women page is not presented"
def test_go_to_hoodies_women_page(driver):
    url = "https://magento.softwaretestingboard.com/women.html"
    page = WomenPage(driver, url)
    page.open()
    page.go_to_hoodies_women_page()
    assert "hoodies-and-sweatshirts-women" in driver.current_url , "Hoodies women page is not presented"
def test_go_to_jackets_women_page(driver):
    url = "https://magento.softwaretestingboard.com/women.html"
    page = WomenPage(driver, url)
    page.open()
    page.go_to_jackets_women_page()
    assert "jackets-women" in driver.current_url , "Jackets women page is not presented"
def test_go_to_tees_women_page(driver):
    url = "https://magento.softwaretestingboard.com/women.html"
    page = WomenPage(driver, url)
    page.open()
    page.go_to_tees_women_page()
    assert "tees-women" in driver.current_url , "Tees women page is not presented"
def test_go_to_brass_women_page(driver):
    url = "https://magento.softwaretestingboard.com/women.html"
    page = WomenPage(driver, url)
    page.open()
    page.go_to_brass_women_page()
    assert "tanks-women" in driver.current_url , "Brass women page is not presented"
def test_go_to_pants_women_page(driver):
    url = "https://magento.softwaretestingboard.com/women.html"
    page = WomenPage(driver, url)
    page.open()
    page.go_to_pants_women_page()
    assert "pants-women" in driver.current_url , "Pants women page is not presented"
def test_go_to_shorts_women_page(driver):
    url = "https://magento.softwaretestingboard.com/women.html"
    page = WomenPage(driver, url)
    page.open()
    page.go_to_shorts_women_page()
    assert "shorts-women" in driver.current_url , "Shorts women page is not presented"