import json


def read_input_data(test_file):
    json_file = open(test_file)
    return json.load(json_file)


def generate_raport(test_raport):
    with open("TestData/test_raport.json", "w") as out_file:
        json.dump(test_raport, out_file, indent=4)


if __name__ == '__main__':
    test_data = read_input_data("C:/Users/serbd/Desktop/GitHub/ITFProjects/DataDriven/TestData/Adressess.json")
    print(test_data)
