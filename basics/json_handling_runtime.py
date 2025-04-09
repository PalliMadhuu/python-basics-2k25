import requests
import pprint
import json
import os

file_name = input("Enter the JSON file name (e.g., data.json): ")
folder_path = os.path.join("D:\python-file-handling-files", file_name)
try:
    response = requests.get("https://jsonplaceholder.typicode.com/posts/3")
    data = response.json()
    # print(data) just print the data in one line
    pprint.pprint(data)  # but pprint helps us to print the data in a readable format
    if len(data.keys()) > 0:
        try:
            if os.path.exists(folder_path):
                with open(folder_path, "r") as existing_file:
                    existing_data = json.load(
                        existing_file
                    )  # read the data in the json
                    if not isinstance(existing_data, list):
                        existing_data = [existing_data]
                        existing_data.append(data)
                    else:
                        existing_data.append(data)
            else:
                existing_data = []
                existing_data.append(data)
            with open(folder_path, "w") as file:
                json.dump(
                    existing_data, file, indent=4, sort_keys=True, ensure_ascii=True
                )  # dump the entire data into the json format
                print("Json Data Successfully appended in array format")
        except (json.JSONDecodeError, TypeError) as err:
            print(f"An Error Occurred in Json file {err}")

    else:
        print("No data found")
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
