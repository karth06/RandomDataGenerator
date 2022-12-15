from random import randint

import json
import time
import requests


class RandomDataGenerator:
    __api_url = "https://api.namefake.com/"
    __connection_timeout = 300

    """
      This class is responsible to generate data, based on your collection preference.
          methods:
              get_names_data returns the list/set of names
              get_get_address_data returns the list/set of addresses.
    """

    @staticmethod
    def get_names_data(collection_type="list", length=5):
        """
        Generates random names in form of list/set, by default it will return in list format
        :param collection_type: [list,set]
        :param length: size of data, default length is 5
        :return: list/set of names
        """
        return RandomDataGenerator._get_data(collection_type, "name", length)

    @staticmethod
    def get_address_data(data_type="list", length=5):
        """
        Generates random addresses in form of list/set, by default it will return in list format
        :param data_type: [list,set]
        :param length: size of data, default length is 5
        :return: list/set of addresses
        """
        return RandomDataGenerator._get_data(data_type, "address", length)

    @staticmethod
    def get_dict_of_data():
        """
        Generates random dict with name as key and address as value
        :return: dict
        """
        data_dict = {}
        data = RandomDataGenerator.__get_data_from_api()
        data_dict["name"] = data["name"]
        data_dict["address"] = data["address"]
        data_dict["age"] = randint(0, 99)
        return data_dict

    @staticmethod
    def get_list_of_dict(length=5):
        """
               Generates list of dictionaries
               :return: dict
               """
        list_of_data = []
        if length < 10:
            for _ in range(0, length):
                data_dict = {}
                data = RandomDataGenerator.__get_data_from_api()
                data_dict["name"] = data["name"]
                data_dict["address"] = data["address"]
                data_dict["age"] = randint(0, 99)
                list_of_data.append(data_dict)
            return list_of_data
        raise ValueError("The length should be greater than 0 and less than 10")

    @staticmethod
    def _get_data(data_type, key, length):
        """
        gets the data from the namegenerator api,
        this method is called from get_names_data() and get_address_data()
        :returns:data
        """
        if data_type.lower() == "set" or data_type.lower() == "list":
            data = eval(data_type + "()")
            if 0 < length <= 10:
                for _ in range(0, length):
                    if data_type != "set":
                        data.append(RandomDataGenerator.__get_data_from_api()[key])
                    else:
                        data.add(RandomDataGenerator.__get_data_from_api()[key])
                return data
            raise ValueError("The length should be greater than 0 and less than 10")
        raise ValueError("Invalid data_type it should be either list or set")


    @staticmethod
    def __get_data_from_api():
        """
        Connects to random name generator api and returns the data.
        :return: response from api
        """
        attempt = 0
        max_attempts = 3
        while attempt < max_attempts:
            try:
                with requests.Session() as session:
                    response_from_api = session.get(url=RandomDataGenerator.__api_url,
                                                    timeout=RandomDataGenerator.__connection_timeout)
                    if response_from_api.status_code == 200 and len(response_from_api.text) > 0:
                        data = json.loads(response_from_api.text)
                        response_from_api.close()
                        return data
                    else:
                        attempt += 1
                        print(f"something went wrong..reconnecting({attempt}/{max_attempts}) times....")
                        time.sleep(5)
            except ConnectionError as conn_error:
                print(conn_error)
        raise ConnectionError(f"Unable to connect to {RandomDataGenerator.__api_url} please try again after sometime")
