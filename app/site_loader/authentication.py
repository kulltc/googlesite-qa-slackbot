class Authentication:

    def __init__(self, cookie_string) -> None:
        self.cookie_string = cookie_string

    def get_cookies(self):
        # Replace with your actual Google cookies string

        # Convert the cookies string into a dictionary
        cookies_dict = self._parse_cookies(self.cookie_string)

        return cookies_dict

    def _parse_cookies(self, cookies_str):
        cookies_list = cookies_str.split(';')
        cookies_dict = {}

        for cookie in cookies_list:
            key, value = cookie.strip().split('=', 1)
            cookies_dict[key] = value

        return cookies_dict
