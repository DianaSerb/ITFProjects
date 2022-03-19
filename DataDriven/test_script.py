from fuzzywuzzy import fuzz

from DataDriven.Parsers import read_input_data, generate_raport


def test_script(input_data, expected_data):
    similarity = fuzz.partial_ratio(input_data, expected_data)
    if similarity > 90:
        print("Passed")
    elif 90 > similarity > 80:
        print("Warning")
    else:
        print("Failed")
    return similarity


if __name__ == '__main__':
    test_data = read_input_data("C:/Users/serbd/Desktop/GitHub/ITFProjects/DataDriven/TestData/Adressess.json")
    a = []
    for k, v in test_data.items():
        test_status = test_script(test_data[k]["input"], test_data[k]["expected"])
        a.append(dict(input=test_data[k]["input"],
                      expected=test_data[k]["expected"],
                      status=test_status))
        print(test_status)
    print(a)
    generate_raport(a)