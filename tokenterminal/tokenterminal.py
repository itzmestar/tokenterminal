# -*- coding: utf-8 -*- #
import json

import requests

# --------- Constants --------- #

BASE_URL = "https://api.tokenterminal.com"

# --------- Constants --------- #


class TokenTerminal:
    """
    TokenTerminal class to act as Token Terminal's API client.
    All the requests can be made through this class.
    """

    def __init__(self, key):
        """
        Initialize the object
        :param key: API key
        """
        self.key = key
        self.session = requests.Session()
        self.session.headers.update({'Authorization': 'Token {}'.format(key)})

    def _get(self, endpoint, params=None, stream=False):
        """
        Get API request
        :param endpoint: Endpoint (to be added to base URL)
        :param params: HTTP request parameters
        :return:
        """
        url = BASE_URL + endpoint
        return self.session.get(url, params=params, timeout=30, stream=stream)

    def retrieve_market_caps(self, data_version=None):
        """
        Returns historical, fully-diluted market cap data. Supports only daily granularity for now.

        :param data_version: Use this to specify which version of the data you want. The format is YYYY-MM-DD,
                e.g. 2020-12-07. Defaults to latest if not specified.
        :return:
        """
        path = '/v1/metrics/financial/market_caps'

        params = {
            'redirect': True,
            'data_version': data_version
        }

        response = self._get(path, params=params, stream=True)
        for line in response.iter_lines():
            data = json.loads(line.decode())
            yield data

    def retrieve_prices(self, data_version=None):
        """
        Returns historical price data. Supports only daily granularity for now.

        :param data_version: Use this to specify which version of the data you want. The format is YYYY-MM-DD,
                e.g. 2020-12-07. Defaults to latest if not specified.
        :return:
        """
        path = '/v1/metrics/financial/prices'

        params = {
            'redirect': True,
            'data_version': data_version
        }

        response = self._get(path, params=params, stream=True)
        for line in response.iter_lines():
            data = json.loads(line.decode())
            yield data

    def retrieve_price_to_sales_ratios(self, data_version=None):
        """
        Returns historical price-to-sales data. Supports only daily granularity for now.

        :param data_version: Use this to specify which version of the data you want. The format is YYYY-MM-DD,
                e.g. 2020-12-07. Defaults to latest if not specified.
        :return:
        """
        path = '/v1/metrics/financial/ps'

        params = {
            'redirect': True,
            'data_version': data_version
        }

        response = self._get(path, params=params, stream=True)
        for line in response.iter_lines():
            data = json.loads(line.decode())
            yield data

    def retrieve_tvls(self, data_version=None):
        """
        Returns historical TVL data. Supports only daily granularity for now.

        :param data_version: Use this to specify which version of the data you want. The format is YYYY-MM-DD,
                e.g. 2020-12-07. Defaults to latest if not specified.
        :return:
        """
        path = '/v1/metrics/financial/tvls'

        params = {
            'redirect': True,
            'data_version': data_version
        }

        response = self._get(path, params=params, stream=True)
        for line in response.iter_lines():
            data = json.loads(line.decode())
            yield data

    def retrieve_gmvs(self, project_id=None, granularity=None, data_version=None):
        """
        Returns historical GMV data. Supports only daily granularity for now.

        :param project_id: Use this to get a deep-dive to a particular project. Data is provided on a component-level,
                e.g. GMV of each Balancer pool. Ignored by default.
        :param granularity: Use this to specify the interval at which data is provided.
                Defaults to daily if not specified.
        :param data_version: Use this to specify which version of the data you want. The format is YYYY-MM-DD,
                e.g. 2020-12-07. Defaults to latest if not specified.
        :return:
        """
        path = '/v1/metrics/financial/gmvs'

        params = {
            'redirect': True,
            'project_id': project_id,
            'granularity': granularity,
            'data_version': data_version
        }

        response = self._get(path, params=params, stream=True)
        for line in response.iter_lines():
            data = json.loads(line.decode())
            yield data

    def retrieve_revenues(self, project_id=None, granularity=None, data_version=None):
        """
        Returns historical revenue data. Supports only daily granularity for now.

        :param project_id: Use this to get a deep-dive to a particular project. Data is provided on a component-level,
                e.g. GMV of each Balancer pool. Ignored by default.
        :param granularity: Use this to specify the interval at which data is provided.
                Defaults to daily if not specified.
        :param data_version: Use this to specify which version of the data you want. The format is YYYY-MM-DD,
                e.g. 2020-12-07. Defaults to latest if not specified.
        :return:
        """
        path = '/v1/metrics/financial/revenues'

        params = {
            'redirect': True,
            'project_id': project_id,
            'granularity': granularity,
            'data_version': data_version
        }

        response = self._get(path, params=params, stream=True)
        for line in response.iter_lines():
            data = json.loads(line.decode())
            yield data
