import json
from datetime import datetime

# please update the path of data.json file in main function


def get_data(path):
    with open(path) as f:
        data = json.load(f)

    return data


def search_name(data, inp_name):
    res = []
    time_format = "%H:%M"  # 24 hour format
    for record in data:
        name = record["employeName"]
        if name.lower() == inp_name.lower():
            # expected format: date checkin checkout dept workinghours
            # sample output:   2022-03-01 10:00 11:00 Dev 1:00:00
            value = [
                record["date"]
                + " "
                + record["checkinTime"]
                + " "
                + record["checkouttime"]
                + " "
                + record["dept"]
                + " "
                + str(
                    datetime.strptime(record["checkouttime"], time_format)
                    - datetime.strptime(record["checkinTime"], time_format)
                )
            ]

            res.append(value)
    if not res:
        print("No records found ")
    return res


def show_result(res, user_inp):
    print(f"Total records found for employee {user_inp.upper()}: {len(res)}")
    for i in res:
        print(i)


# Test Cases


def check_input(inp):
    try:
        if not inp:
            raise ValueError("Name cannot be empty")
        return True
    except Exception as e:
        print(e)
        return False


def test_search_name():
    # raise error if the result for employee Test1 is not as expected
    expected_test1 = [
        ["2022-03-01 9:00 10:00 QA 1:00:00"],
        ["2022-03-02 9:00 10:00 QA 1:00:00"],
        ["2022-03-03 9:00 10:00 QA 1:00:00"],
        ["2022-03-04 9:00 10:00 QA 1:00:00"],
        ["2022-03-05 9:00 10:00 QA 1:00:00"],
    ]

    assert (
        search_name(get_data("./data.json"), "Test1") == expected_test1
    ), "Test failed for Employee Test1"


def main():
    path = "./logistics/data.json"
    user_inp = input("Enter employeName: ")
    if check_input(user_inp):
        data = get_data(path)
        res = search_name(data, user_inp)
        if res:
            show_result(res, user_inp)


if __name__ == "__main__":
    test_search_name()
    main()
