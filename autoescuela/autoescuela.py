from bs4 import BeautifulSoup

file_name = "autoescuela/aeol_data.html"
test_record = {}


with open(file_name, "r") as f:
    doc = BeautifulSoup(f, "html.parser")
    tests = doc.find("div", {"class": "tests_grid"}).find_all("div")

for test in tests:
    try:
        test_record.update({tests.index(test) + 1: int(test.get("title").split()[5])})
    except:
        pass

print(test_record)