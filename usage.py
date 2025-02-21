import json_to_df as j2df

# With json file path
sample_dict_path = "./test_json/test.json"

output = j2df.convert(sample_dict_path, save_excel=False)

print(output)

# With a dictionary (API output, JSON converted to dictionary)

sample_dict = {
    "user": {
        "name": "Alice",
        "address": {"city": "London", "zip": "SW1A"},
        "orders": [
            {"id": 1, "items": [{"name": "ItemA", "price": 30}, {"name": "ItemB", "price": 40}]},
            {"id": 2, "items": [{"name": "ItemC", "price": 50}]}
        ]
    },
    "admin": {"role": "supervisor"}
}

output_2 = j2df.convert(sample_dict, save_excel=False)

for tab_name, table in output_2.items():
    print("\nDataFrame : ", tab_name)
    print(table)
