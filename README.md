# JSON to DataFrame Converter

**JSON to DataFrame Converter** is a Python package designed to transform deeply nested and irregular JSON structures (including lists of dictionaries, nested lists, and complex hierarchies) into meaningful, minimal, and effective DataFrames. It is ideal for use cases where nested JSON needs to be converted into tabular data with preserved parent-child relationships.

## Features

- Converts deeply nested and irregular JSONs into DataFrames.
- Minimizes the number of DataFrames generated while maintaining data integrity.
- Preserves parent-child relationships with clear references.
- Handles list elements within any level of the JSON hierarchy.
- Automatically merges certain tables to reduce complexity.
- Removes empty or redundant DataFrames.

## Installation

You can install the package directly from PyPI:

```bash
pip install json-to-df
```

## Usage

### Basic Example [Refer usage.py]

```python
import json_to_df as j2df

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
    print("DataFrame : ", tab_name)
    print(table)

```

## Output Example

```
DataFrame :  Refer:Table:1
      table_ref  id                                  items
0  user__orders   1  [## Refer:Table:2 Index(es): 0, 1 ##]
1  user__orders   2     [## Refer:Table:2 Index(es): 2 ##]

DataFrame :  Refer:Table:2
                         table_ref   name  price
0  user__orders__listElem:0__items  ItemA     30
1  user__orders__listElem:0__items  ItemB     40
2  user__orders__listElem:1__items  ItemC     50

DataFrame :  Refer:Table:0
  user__name user__address__city user__address__zip admin__role
1      Alice              London               SW1A  supervisor
```

## Requirements

- Python 3.7+
- pandas >= 1.0.0

## Development & Contributions

Contributions are welcome! Feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License.

## Author

Maintained by Sourin Karmakar.
