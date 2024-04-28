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
        Use this method to retrieve a list of all projects that are available on the API.
        """
        path = '/v2/projects'

        response = self._get(path)
        return response

    def get_historical_metrics(self, project_id: str, **kwargs):
        """
        Use this method to retrieve historical data for a project.
        Fill in the required fields on the modal to the right.
        """
        path = f'/v2/projects/{project_id}/metrics'

        response = self._get(path, params=kwargs)
        return response

    def get_metric_availability(self, project_id: str):
        """
        Use this method to retrieve the metric availability for a project.
        :param project_id: project_id
        :return:
        """
        path = f'/v2/projects/{project_id}'

        response = self._get(path)
        return response

    def get_metric_aggregations(self, project_id: str):
        """
        Use this method to retrieve metric aggregation data for one project.
        :param project_id: project_id
        :return:
        """
        path = f'/v2/projects/{project_id}/metric-aggregations'

        response = self._get(path)
        return response

    def get_financial_statement(
            self,
            project_id: str,
            timestamp_granularity: str = None,
            interval: str = None
    ):
        """
        Use this method to retrieve the financial statement report for a project.
        :param interval: can be '1m', '1y', '2y', '3y', '5y' or 'max'
        :param timestamp_granularity: can be 'year', 'quarter', 'month' or 'week'
        :param project_id: The project ID to retrieve financial statement for.
        :return:
        """
        path = f'/v2/projects/{project_id}/financial-statement'

        params = {
            'timestamp_granularity': timestamp_granularity,
            'interval': interval
        }

        response = self._get(path, params=params)
        return response

    def get_market_sectors(self):
        """
        Use this method to retrieve a list of all available market sectors that are available on the API.
        :return:
        """
        path = f'/v2/market-sectors'

        response = self._get(path)
        return response

    def get_market_sector(self, market_sector_id: str):
        """
        Use this method to retrieve a market sector metadata and the list of all projects belonging to market sector.
        """
        path = f'/v2/market-sectors/{market_sector_id}'

        response = self._get(path)
        return response
