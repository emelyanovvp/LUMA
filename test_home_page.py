from .pages.home_page import HomePage
import pytest
def test_customer_can_go_to_login_page_from_sign_in_link(driver):
    url = "https://magento.softwaretestingboard.com/"
    home_page = HomePage(driver, url)
    home_page.open()
    home_page.click_link_sign_in_and_go_to_login_page()
    assert "login" in driver.current_url , "Login page is not presented"

def test_customer_can_go_to_regform_page_from_create_account_link(driver):
    url = "https://magento.softwaretestingboard.com/"
    page = HomePage(driver, url)
    page.open()
    page.click_link_create_account_and_go_to_regform_page()
    assert "create" in driver.current_url, "Registration form page is not presented"

def test_customer_can_go_to_women_tops_jackets_link_and_click(driver):
    url = "https://magento.softwaretestingboard.com/"
    page = HomePage(driver, url)
    page.open()
    page.move_mouse_to_women_tops_jackets_link_and_click()
    assert "jackets-women" in driver.current_url, "Women jackets page is not presented"

def test_go_to_whats_new_page(driver):
    url = "https://magento.softwaretestingboard.com/"
    page = HomePage(driver, url)
    page.open()
    page.go_to_whats_new_page()
    assert "what-is-new" in driver.current_url, "Whats new page is not presented"

def test_go_to_men_page(driver):
    url = "https://magento.softwaretestingboard.com/"
    page = HomePage(driver, url)
    page.open()
    page.go_to_men_page()
    assert "men" in driver.current_url, "Men page is not presented"

def test_go_to_women_page(driver):
    url = "https://magento.softwaretestingboard.com/"
    page = HomePage(driver, url)
    page.open()
    page.go_to_women_page()
    assert "women" in driver.current_url, "Women page is not presented"

def test_go_to_gear_page(driver):
    url = "https://magento.softwaretestingboard.com/"
    page = HomePage(driver, url)
    page.open()
    page.go_to_gear_page()
    assert "gear" in driver.current_url, "Gear page is not presented"

def test_go_to_training_page(driver):
    url = "https://magento.softwaretestingboard.com/"
    page = HomePage(driver, url)
    page.open()
    page.go_to_training_page()
    assert "training" in driver.current_url, "Training page is not presented"

def test_go_to_sale_page(driver):
    url = "https://magento.softwaretestingboard.com/"
    page = HomePage(driver, url)
    page.open()
    page.go_to_sale_page()
    assert "sale" in driver.current_url, "Sale page is not presented"
@pytest.mark.smoke
def test_go_to_new_yoga_page(driver):
    url = "https://magento.softwaretestingboard.com/"
    page = HomePage(driver, url)
    page.open()
    page.go_to_new_yoga_page()
    assert "yoga" in driver.current_url, "Yoga page is not presented"
@pytest.mark.smoke
def test_go_to_pants_page(driver):
    url = "https://magento.softwaretestingboard.com/"
    page = HomePage(driver, url)
    page.open()
    page.go_to_pants_page()
    assert "pants" in driver.current_url, "Pants page is not presented"
@pytest.mark.smoke
def test_go_to_erin_page(driver):
    url = "https://magento.softwaretestingboard.com/"
    page = HomePage(driver, url)
    page.open()
    page.go_to_erin_page()
    assert "erin" in driver.current_url, "Erin page is not presented"
@pytest.mark.smoke
def test_go_to_tees_page(driver):
    url = "https://magento.softwaretestingboard.com/"
    page = HomePage(driver, url)
    page.open()
    page.go_to_tees_page()
    assert "tees" in driver.current_url, "Tees page is not presented"
@pytest.mark.smoke
def test_go_to_performance_page(driver):
    url = "https://magento.softwaretestingboard.com/"
    page = HomePage(driver, url)
    page.open()
    page.go_to_performance_page()
    assert "performance" in driver.current_url, "Performance page is not presented"
@pytest.mark.smoke
def test_go_to_eco_page(driver):
    url = "https://magento.softwaretestingboard.com/"
    page = HomePage(driver, url)
    page.open()
    page.go_to_eco_page()
    assert "eco" in driver.current_url, "Eco page is not presented"

if __name__ == '__main__':
    pytest.main()