# RandomDataGenertor:
> This is a small project which generates random data using https://api.namefake.com/ api,just to ease of assigning values to a variable when you want to test something.
Currently it only generates random person names, address data.
The data can be retrieved in form of list,set and dict.
Since the data is fetched through api, the number of calls are limited to 10 records for now.

## Usages:
> import the file in python using the following statment.<br/>
```python
from DataGenerator import RandomDataGenerator.
```

> Then you can access the methods as shown below.
> To get list of names/addresses:

 ```python
 names_list = RandomDataGenerator.get_names_data()
 ```
  
 ```python
 address_list = RandomDataGenerator.get_address_data()
 ```

> To get set of names/address: <br/>
  ```python
 names_set = RandomDataGenerator.get_names_data(collection_type="set")
 ```
 ```python
 address_set = RandomDataGenerator.get_address_data(collection_type="set")
 ```

> By default the results are of size 5, you can also pass the length as shown in the example below. <br/>
  ```python
  names_set = RandomDataGenerator.get_names_data(collection_type="set",length=8)
  ```

> To get dict of items: <br/>
  ```python
  data = RandomDataGenerator.get_dict_of_data()
  ```

> To get list of dict: <br/>
  ```python
  data = RandomDataGenerator.get_list_of_dict()
  ```
  ```python
  data = RandomDataGenerator.get_list_of_dict(length=8)
  ```
