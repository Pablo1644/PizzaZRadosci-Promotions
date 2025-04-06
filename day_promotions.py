from selenium.webdriver.common.by import By


def collect_day_promotions(driver, promotion_day):
    elements = driver.find_elements(By.XPATH, "//h3[@class='m-heading m-featured__title']")
    full_info = ""

    if promotion_day.upper() == "PIĄTEK":
        xpath = (
            "//h3[contains(@class, 'm-featured__title') and "
            "(contains(text(), 'PIĄTEK') or contains(text(), 'Piątek'))]"
        )
        matching_elements = driver.find_elements(By.XPATH, xpath)
        if matching_elements:
            for element in matching_elements:
                paragraph_info = element.find_element(By.XPATH, "following-sibling::p[contains(text(),'romocja')]")
                full_info += element.text + "\n" + paragraph_info.text + "\n"
    else:
        for element in elements:
            if promotion_day.upper() in element.text.upper() and element.text:
                xpath_paragraph = f"//h3[contains(@class, 'm-featured__title') and contains(text(), '{promotion_day.upper()}')]/following-sibling::p"
                paragraph_info = element.find_element(By.XPATH, "following-sibling::p[contains(text(),'romocja')]")
                full_info = element.text + "\n" + paragraph_info.text
                break

    return full_info
