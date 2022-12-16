# RandomDataGenertor:
> This is a small project which generates random data using https://random-data-api.com/api/v2/users api,just to ease of assigning values to a variable when you want to test something.
The data can be retrieved in form of list,set and dict.
Since the data is fetched through api, the number of calls are limited to 10 records for now.

## Usages:
> import the file in python using the following statment.<br/>
```python
from DataGenerator import RandomDataGenerator
```

> Then you can access the methods as shown below.
> To get list of names/addresses:

 ```python
 data = RandomDataGenerator.get_users()
 ```
  

> To get set of names: <br/>
  ```python
 data = RandomDataGenerator.get_users(data_type="set")
 ```


> By default the results are of size 5, you can also pass the length as shown in the example below. <br/>
  ```python
  data = RandomDataGenerator.get_users(data_type="set",length=8)
  ```

> To get dict of items: <br/>
  ```python
  data = RandomDataGenerator.get_users(data_type="dict",length=1)
  ```

> To get list of dict: <br/>
  ```python
  data = RandomDataGenerator.get_users(data_type="dict",length=6)
  ```
  ```python
  data = RandomDataGenerator.get_users(data_type="dict")
  ```
> you can also refer to the test_DataGenerator.py file for the usecases.
