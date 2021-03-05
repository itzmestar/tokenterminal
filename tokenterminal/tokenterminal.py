# -*- coding: utf-8 -*- #
import requests

# --------- Constants --------- #

BASE_URL = "https://api.tokenterminal.com"

# --------- Constants --------- #


class TokenTerminal:
    """
    TokenTerminal class to act as Token Terminal's API client.
    All the requests can be made through this class.
    """

    def __init__(self, key=None):
        """
        Initialize the object
        :param key: API key
        """
        self.key = key
