from selenium import webdriver
import pytest
import csv

def read_csv_data(file_path):
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        return [row['keyword'] for row in reader]

test_data = read_csv_data('./data/data_test.csv')
# test script -> search for keyworks in google website

@pytest.mark.parametrize('keywork', test_data)
def test_google_search(keywork):
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")
    search_box = driver.find_element("name", "q")
    search_box.send_keys(keywork)
    search_box.submit()

    driver.quit()