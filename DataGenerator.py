import requests, json, time


class RandomDataGenerator:
    __api_url = "https://random-data-api.com/api/v2/users"
    __connection_timeout = 300

    @staticmethod
    def get_users(data_type="list", length=5):
        """
        This method returns the data in form of list, set or dict.
        by default the data will return in form of list
        :param data_type: list/set/dict
        :param length: 5
        :return: data of type list, set, dict, list_of_dict
        """
        RandomDataGenerator.__api_url = RandomDataGenerator.__api_url + "?size=" + str(length)
        data = RandomDataGenerator.__connect_to_api()

        if 1 <= length <= 10:
            if data_type == "list" and data is not None:
                return [user_data["first_name"] + " " + user_data["last_name"] for user_data in data]
            elif data_type == "set" and data is not None:
                return {user_data["first_name"] + " " + user_data["last_name"] for user_data in data}
            elif data_type == "dict" and data is not None and length == 1:
                return data
            elif data_type == "dict" and data is not None:
                return [{"name": data[data_range]["username"], "email": data[data_range]["email"], "address":data[data_range]["address"]} for data_range in range(0,length)]
            else:
                raise ValueError("Invalid data_type, the data type must be a List or a Set")
        raise ValueError("The size of the collection must be greater than 0 and less than 10")

    @staticmethod
    def __connect_to_api():
        """
        This method connects to https://random-data-api.com/api/v2/users api
        :param __api_url: https://random-data-api.com/api/v2/users
        :return: response
        """
        try:
            with requests.Session() as session:
                conn = session.get(url=RandomDataGenerator.__api_url, timeout=RandomDataGenerator.__connection_timeout)
                if conn.status_code == 200 and len(conn.text) > 0:
                    return json.loads(conn.text)
                return None
        except ConnectionError as conn_error:
            print(conn_error)
        return None
