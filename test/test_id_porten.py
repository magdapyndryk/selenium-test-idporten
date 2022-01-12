from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def test_logging_in_idporten():
    # Uruchomienie przeglądarki Chrome. Ścieżka do chromedrivera
    # Ustawiana automatycznie przez bibliotekę webdriver-manager
    browser = Chrome(executable_path=ChromeDriverManager().install())

    browser.get("https://login-test.dfo.no/?idp=idporten")
    browser.find_element(By.CSS_SELECTOR, '#MinIDEksternChain').click()
    browser.find_element(By.CSS_SELECTOR, '#personalIdNumber').send_keys('08089406901')
    browser.find_element(By.CSS_SELECTOR, '#passord').send_keys('passord01')
    browser.find_element(By.CSS_SELECTOR, '#next').click()
    browser.find_element(By.CSS_SELECTOR, '#otpCode').send_keys('12345')
    browser.find_element(By.CSS_SELECTOR, '#next').click()
    assert browser.find_element(By.CSS_SELECTOR, '.brandingLogo').is_displayed()
    browser.quit()