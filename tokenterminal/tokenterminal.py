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
        self.session.headers.update({'Authorization': 'Bearer {}'.format(key)})

    def _get(self, endpoint, params=None, stream=False):
        """
        Get API request
        :param endpoint: Endpoint (to be added to base URL)
        :param params: HTTP request parameters
        :return:
        """
        url = BASE_URL + endpoint
        response = self.session.get(url, params=params, timeout=30, stream=stream)
        return response.json()

    def get_all_projects(self):
        """
        Returns an overview of latest data for all projects, ranging from metadata such as
        launch dates, logos brand colors and Twitter followers to more fundamental metrics
        such as Revenue, GMV, TVL and P/S ratios.
        The project_id can be used as a Path parameter in subsequent endpoints.

        The data is updated every 10 minutes.
        :return:
        """
        path = '/v1/projects'

        response = self._get(path)
        return response

    def get_historical_metrics(self, project_id, granularity='project', interval='daily'):
        """
        Returns project's historical metrics. The project_id can be fetched from the v1/projects endpoint.
        The datetime granularity can be controlled with interval, omitting it will default to daily.

        The metric data of a given project can be split into components. In Uniswap's case a component is
        the trading pair (e.g. USDC-WETH or DAI-WETH), in Compound's case it's the lending market (e.g. ETH,
        USDC or WBTC).
        By choosing top10 or component for data_granularity, the composition of a given metric can be examined
        more thoroughly. Project's that have top10 or component data can be seen from /v1/projects's
        metric_availability field.

        By default project-level data is shown, ignoring component-level data altogether.

        The data is updated once a day.

        :param project_id: Project's id, can be fetched from v1/projects endpoint.
        :param granularity: The granularity of data, options are project, top10 or component.
                Defaults to project.
        :param interval: The interval historical data is given, options are daily or monthly.
                Defaults to daily.
        :return:
        """
        path = f'/v1/projects/{project_id}/metrics'

        params = {
            'data_granularity': granularity,
            'interval': interval
        }

        response = self._get(path, params=params)
        return response
