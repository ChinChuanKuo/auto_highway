def solution_website(json):
    from selenium import webdriver
    from selenium.webdriver.support.ui import Select
    from time import sleep
    json_data = json["info"]
    url = "https://irs.thsrc.com.tw/IMINT/?locale=tw"
    driver = webdriver.Chrome()
    driver.get(url)
    driver.maximize_window()
    driver.find_element_by_xpath("//input[@id='btn-confirm']").click()
    startStation = driver.find_element_by_xpath("//select[@name='selectStartStation']")
    for option in startStation.find_elements_by_tag_name('option'):
        if option.text == json_data["start_station"]:
            option.click()
            break
    endStation = driver.find_element_by_xpath("//select[@name='selectDestinationStation']")
    for option in endStation.find_elements_by_tag_name('option'):
        if option.text == json_data["end_station"]:
            option.click()
            break
    if json_data["train_type"] == "商務車廂":
        driver.find_element_by_xpath("//input[@id='trainCon:trainRadioGroup_1']").click()
    if json_data["seat_like"] == "靠窗優先":
        driver.find_element_by_xpath("//input[@id='seatRadio1']").click()
    elif json_data["seat_like"] == "走道優先":
        driver.find_element_by_xpath("//input[@id='seatRadio2']").click()
    if json_data["order_way"] == "直接輸入":
        driver.find_element_by_xpath("//input[@id='bookingMethod_1']").click()
    driver.find_element_by_xpath("//input[@id='toTimeInputField']").send_keys(json_data["start_date"])
    startTime = driver.find_element_by_xpath("//select[@name='toTimeTable']")
    for option in startTime.find_elements_by_tag_name('option'):
        if option.text == json_data["start_time"]:
            option.click()
            break
    if json_data["go_back"] == "Yes":
        driver.find_element_by_xpath("//input[@id='returnCheckBox']").click()
        driver.find_element_by_xpath("//input[@id='backTimeInputField']").send_keys(json_data["end_date"])
        endTime = driver.find_element_by_xpath("//select[@name='backTimeTable']")
        for option in endTime.find_elements_by_tag_name('option'):
            if option.text == json_data["end_time"]:
                option.click()
                break
    adultCount = driver.find_element_by_xpath("//select[@name='ticketPanel:rows:0:ticketAmount']")
    for option in adultCount.find_elements_by_tag_name('option'):
        if option.text == json_data["adult_count"]:
            option.click()
            break
    childCount = driver.find_element_by_xpath("//select[@name='ticketPanel:rows:1:ticketAmount']")
    for option in childCount.find_elements_by_tag_name('option'):
        if option.text == json_data["child_count"]:
            option.click()
            break
    loverCount = driver.find_element_by_xpath("//select[@name='ticketPanel:rows:2:ticketAmount']")
    for option in loverCount.find_elements_by_tag_name('option'):
        if option.text == json_data["lover_count"]:
            option.click()
            break
    oldCount = driver.find_element_by_xpath("//select[@name='ticketPanel:rows:3:ticketAmount']")
    for option in oldCount.find_elements_by_tag_name('option'):
        if option.text == json_data["old_count"]:
            option.click()
            break
    studentCount = driver.find_element_by_xpath("//select[@name='ticketPanel:rows:4:ticketAmount']")
    for option in studentCount.find_elements_by_tag_name('option'):
        if option.text == json_data["student_count"]:
            option.click()
            break
    download_file(driver.find_element_by_xpath("//img[@id='BookingS1Form_homeCaptcha_passCode']").get_attribute("src"))
    #driver.find_element_by_xpath("//img[@id='BookingS1Form_homeCaptcha_passCode']").get_attribute("src")

def get_json():
    import json
    with open("main.json", "r") as f:
        data = json.load(f)
        return data


if __name__ == "__main__":
    solution_website(get_json())