from selenium import webdriver
from selenium.webdriver.edge.options import Options
from const_promotions import collect_constant_promotions
from day_promotions import collect_day_promotions
from const_promotions import days_of_week
import time

options = Options()
options.add_argument('--headless')
driver = webdriver.Edge(options=options)

while True:
    location = input("Podaj miejsce promocji: Radość/Józefów:").lower()
    if location in ['radość', 'radosc']:
        driver.get("https://www.pizzazradosci.pl/promocje#/r=pizza-z-radosci-" + 'radosc')
        break
    elif location in ['jozefow','józefów']:
        driver.get("https://www.pizzazradosci.pl/promocje#/r=pizza-z-radosci-" + 'jozefow')
        break
    else:
        print("Podaj poprawne miejsce promocji.")

driver.execute_script("document.body.style.zoom='10%'")

while(True):
    promotion_day = input("Podaj dzień promocji, który Cię interesuje: ").capitalize()
    promotion_day = promotion_day.capitalize()
    for day in days_of_week: day.capitalize()
    if promotion_day in days_of_week:
        break
    else:
        print("Podaj poprawny dzień tygodnia")
full_info = collect_day_promotions(driver, promotion_day)

if full_info:
    print(f"\n🎉 Promocja na {promotion_day}:\n")
    print(full_info)
else:
    print(f"\nBrak promocji na {promotion_day}.\n")
print("\n📌 Inne promocje stałe:\n")
additional_info = collect_constant_promotions(driver)
print(additional_info)
time.sleep(1.5)
driver.quit()
