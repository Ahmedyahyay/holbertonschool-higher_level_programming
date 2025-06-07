# Python Serialization Exercises

This project focuses on learning and implementing different serialization techniques in Python. Serialization is the process of converting data structures or objects into a format that can be stored and reconstructed later.

---

## Task 0: Basic Serialization

**File:** `task_00_basic_serialization.py`

### Description:

Create a module that allows serializing a Python dictionary to a JSON file and deserializing it back to a Python dictionary.

### Functions:

* `serialize_and_save_to_file(data, filename)`: Serializes a dictionary and writes it to a JSON file. If the file exists, it will be overwritten.
* `load_and_deserialize(filename)`: Reads a JSON file and returns the content as a Python dictionary.

### Example Usage:

```python
from task_00_basic_serialization import load_and_deserialize, serialize_and_save_to_file

# Sample data
data_to_serialize = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}

serialize_and_save_to_file(data_to_serialize, 'data.json')
print("Data serialized and saved to 'data.json'.")

deserialized_data = load_and_deserialize('data.json')
print("Deserialized Data:")
print(deserialized_data)
```

---

## Task 1: Pickling Custom Classes

**File:** `task_01_pickle.py`

### Description:

Create a class `CustomObject` with attributes and methods to serialize and deserialize itself using the `pickle` module.

### Class: `CustomObject`

* Attributes: `name`, `age`, `is_student`
* Methods:

  * `display()`: Prints the object's information.
  * `serialize(self, filename)`: Saves the object using pickle.
  * `@classmethod deserialize(cls, filename)`: Loads the object from a pickle file. Returns `None` on error.

### Example:

```python
obj = CustomObject(name="John", age=25, is_student=True)
obj.display()
obj.serialize("object.pkl")

new_obj = CustomObject.deserialize("object.pkl")
new_obj.display()
```

---

## Task 2: Converting CSV Data to JSON Format

**File:** `task_02_csv.py`

### Description:

Read a CSV file and convert it to JSON format. Write the JSON to `data.json`.

### Function:

* `convert_csv_to_json(filename)`: Reads a CSV file and writes its content as JSON. Returns `True` if successful, `False` on error.

### Example:

```python
csv_file = "data.csv"
convert_csv_to_json(csv_file)
print(f"Data from {csv_file} has been converted to data.json")
```

### Example Input (CSV):

```
name,age,city
John,28,New York
Alice,24,Los Angeles
```

### Example Output (JSON):

```json
[
  {"name": "John", "age": "28", "city": "New York"},
  {"name": "Alice", "age": "24", "city": "Los Angeles"}
]
```

---

## Task 3: Serializing and Deserializing with XML

**File:** `task_03_xml.py`

### Description:

Serialize a Python dictionary to XML and deserialize it back.

### Functions:

* `serialize_to_xml(dictionary, filename)`: Saves a dictionary to an XML file.
* `deserialize_from_xml(filename)`: Loads XML and returns it as a dictionary.

### Example:

```python
sample_dict = { 'name': 'John', 'age': '28', 'city': 'New York' }
serialize_to_xml(sample_dict, 'data.xml')
print("Dictionary serialized to data.xml")

data = deserialize_from_xml('data.xml')
print("Deserialized Data:")
print(data)
```

### Output Example:

```xml
<data>
    <name>John</name>
    <age>28</age>
    <city>New York</city>
</data>
```

