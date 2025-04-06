from selenium.webdriver.common.by import By

days_of_week = ["Poniedziałek", "Wtorek", "Środa", "Czwartek", "Piątek","Sobota","Niedziela"]

def collect_constant_promotions(driver):
    elements = driver.find_elements(By.XPATH, "//h3[@class='m-heading m-featured__title']")
    additional_info = ""

    for element in elements:
        if not any(day.upper() in element.text for day in days_of_week) and element.text:
            additional_info += element.text + "\n"
            paragraph_info = element.find_element(By.XPATH, "following-sibling::p[contains(text(),'romocja')]")
            additional_info += paragraph_info.text + "\n"

    return additional_info
