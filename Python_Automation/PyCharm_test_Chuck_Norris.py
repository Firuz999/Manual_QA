import requests
class Test_new_joke():
    """Create new joke"""

    def __init__(self):
        pass

    def test_create_new_random_joke(self):
        """Create random joke"""
        url = "https://api.chucknorris.io/jokes/random"
        print(url)

        result = requests.get(url)
        print("status code : " + str(result.status_code))
        assert 200 == result.status_code
        if result.status_code == 200:
            print("YES")
        else:
            print("NO")
        print("method : " + str(result.request))
        result.encoding = 'utf-8'
        print(result.text)
        check = result.json()
        check_info_value = check.get("value")
        print(check_info_value)
        name = "Chuck Norris"
        if name in check_info_value:
            print("Chuck here!")
        else:
            print("Chuck absent...")


random_joke = Test_new_joke()
random_joke.test_create_new_random_joke()