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

    def get_all_metrics(self):
        """
        Use this method to retrieve a list of all metrics available on the API.
        :return:
        """
        path = f'/v2/metrics'

        response = self._get(path)
        return response

    def get_projects_metric_data(self, metric_id: str, project_ids: list = None, start: str = None, end: str = None):
        """
        Use this method to retrieve metric data for multiple projects.
        You can get specific metric for all projects by omiting project_ids or using project_ids=all.
        :param metric_id: Allows you to select one of the metrics available. The full list is available on the metrics endpoint
        :param project_ids: Allows you to select one or more of the projects available for a specific metric.
                            When including multiple projects, separate each one with a comma. Example: aave,uniswap
        :param start: Allows you to select the start date for the query. If no start is selected,
                        the query defaults to launch date or the first date for which there is data available for the chosen metric(s).
        :param end: Allows you to select the end date for the query. If no end is selected,
                    the query defaults to the latest date for which there is data available for the chosen metric(s).
        :return:
        """
        path = f'/v2/metrics/{metric_id}'

        params = {
            'project_ids': project_ids,
            'start': start,
            'end': end,
        }

        response = self._get(path, params=params)
        return response

    def get_projects_metric_aggregations(self, project_ids: list[str], metric_ids: list = None):
        """
        Use this method to retrieve metric aggregations for multiple projects.

        You can get all aggregations for all projects by omiting project_ids and metric_ids parameters.
        Fetching all projects or metrics you can omit the parameter or using parameter value all.
        :param project_ids:
        :param metric_ids:
        :return:
        """
        path = f'/v2/metrics/metric-aggregations'

        params = {
            'project_ids': project_ids,
            'metric_ids': metric_ids
        }

        response = self._get(path, params=params)
        return response

    def get_blockchain_comparison_dataset(
            self,
            chain_ids: list = None,
            order_by: str = None,
            order_direction: str = None,
            limit: int = None
    ):
        """
        Use this method to retrieve the Blockchain comparison dataset.

        You can get the whole dataset by omiting all parameters.
        :param chain_ids:
        :param order_by:
        :param order_direction:
        :param limit:
        :return:
        """
        path = f'/v2/datasets/blockchain_comparison'

        params = {
            'chain_ids': chain_ids,
            'order_by': order_by,
            'order_direction': order_direction,
            'limit': limit
        }

        response = self._get(path, params=params)
        return response

    def get_cohort_analysis_dataset(
            self,
            project_ids: list = None,
            market_sector_ids: list = None,
            order_by: str = None,
            order_direction: str = None,
            limit: int = None
    ):
        """
        Use this method to retrieve the Cohort analysis dataset.

        You can get the whole dataset by omiting all parameters.
        :param project_ids:
        :param market_sector_ids:
        :param order_by:
        :param order_direction:
        :param limit:
        :return:
        """
        path = f'/v2/datasets/cohort_analysis'

        params = {
            'project_ids': project_ids,
            'market_sector_ids': market_sector_ids,
            'order_by': order_by,
            'order_direction': order_direction,
            'limit': limit
        }

        response = self._get(path, params=params)
        return response

    def get_crypto_screener_dataset(
            self,
            project_ids: list = None,
            market_sector_ids: list = None,
            order_by: str = None,
            order_direction: str = None,
            limit: int = None
    ):
        """
        Use this method to retrieve the Crypto screener dataset. You can get the whole dataset by omiting all parameters.

        Metrics use the following pattern in the response body: <metric_id>_<interval>_<aggregation>.

        Metric IDs are the same as the ones used in the /v2/metrics endpoint.
        Intervals are 24h, 7d, 30d, 90d, 180d, 365d, max.
        Aggregations are trend, change, avg, ath, atl.
        :param project_ids:
        :param market_sector_ids:
        :param order_by:
        :param order_direction:
        :param limit:
        :return:
        """
        path = f'/v2/datasets/crypto_screener'

        params = {
            'project_ids': project_ids,
            'market_sector_ids': market_sector_ids,
            'order_by': order_by,
            'order_direction': order_direction,
            'limit': limit
        }

        response = self._get(path, params=params)
        return response

    def get_insider_transactions_dataset(
            self,
            project_ids: list = None,
            chain_ids: list = None,
            order_by: str = None,
            order_direction: str = None,
            limit: int = None
    ):
        """
        Use this method to retrieve the Insider transactions dataset.

        You can get the whole dataset by omiting all parameters.
        :param project_ids:
        :param chain_ids:
        :param order_by:
        :param order_direction:
        :param limit:
        :return:
        """
        path = f'/v2/datasets/insider_transactions'

        params = {
            'project_ids': project_ids,
            'chain_ids': chain_ids,
            'order_by': order_by,
            'order_direction': order_direction,
            'limit': limit
        }

        response = self._get(path, params=params)
        return response

    def get_top_tokenholders_dataset(
            self,
            project_ids: list = None,
            chain_ids: list = None,
            market_sector_ids: list = None,
            order_by: str = None,
            order_direction: str = None,
            limit: int = None
    ):
        """
        Use this method to retrieve the Top tokenholders dataset.

        You can get the whole dataset by omiting all parameters.
        :param project_ids:
        :param chain_ids:
        :param market_sector_ids:
        :param order_by:
        :param order_direction:
        :param limit:
        :return:
        """
        path = f'/v2/datasets/top_tokenholders'

        params = {
            'project_ids': project_ids,
            'chain_ids': chain_ids,
            'market_sector_ids': market_sector_ids,
            'order_by': order_by,
            'order_direction': order_direction,
            'limit': limit
        }

        response = self._get(path, params=params)
        return response

    def get_project_contracts_dataset(
            self,
            project_ids: list = None,
            chain_ids: list = None,
            market_sector_ids: list = None,
            order_by: str = None,
            order_direction: str = None,
            limit: int = None
    ):
        """
        Use this method to retrieve the Project contracts dataset.

        You can get the whole dataset by omiting all parameters.
        :param project_ids:
        :param chain_ids:
        :param market_sector_ids:
        :param order_by:
        :param order_direction:
        :param limit:
        :return:
        """
        path = f'/v2/datasets/project_contracts'

        params = {
            'project_ids': project_ids,
            'chain_ids': chain_ids,
            'market_sector_ids': market_sector_ids,
            'order_by': order_by,
            'order_direction': order_direction,
            'limit': limit
        }

        response = self._get(path, params=params)
        return response

    def get_stablecoins_dataset(
            self,
            project_ids: list = None,
            chain_ids: list = None,
            market_sector_ids: list = None,
            order_by: str = None,
            order_direction: str = None,
            limit: int = None
    ):
        """
        Use this method to retrieve the Stablecoins dataset.

        You can get the whole dataset by omiting all parameters.
        :param project_ids:
        :param chain_ids:
        :param market_sector_ids:
        :param order_by:
        :param order_direction:
        :param limit:
        :return:
        """
        path = f'/v2/datasets/stablecoins'

        params = {
            'project_ids': project_ids,
            'chain_ids': chain_ids,
            'market_sector_ids': market_sector_ids,
            'order_by': order_by,
            'order_direction': order_direction,
            'limit': limit
        }

        response = self._get(path, params=params)
        return response

    def get_trending_contracts_dataset(
            self,
            project_ids: list = None,
            chain_ids: list = None,
            market_sector_ids: list = None,
            order_by: str = None,
            order_direction: str = None,
            limit: int = None
    ):
        """
        Use this endpoint to retrieve the Trending contracts dataset.

        You can get the whole dataset by omiting all parameters.
        :param project_ids:
        :param chain_ids:
        :param market_sector_ids:
        :param order_by:
        :param order_direction:
        :param limit:
        :return:
        """
        path = f'/v2/datasets/trending_contracts'

        params = {
            'project_ids': project_ids,
            'chain_ids': chain_ids,
            'market_sector_ids': market_sector_ids,
            'order_by': order_by,
            'order_direction': order_direction,
            'limit': limit
        }

        response = self._get(path, params=params)
        return response
