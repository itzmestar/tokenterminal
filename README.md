# Token Terminal

[![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-370/)
[![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-380/)
[![Python 3.9](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/downloads/release/python-390/)

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

-------

### Unofficial [Token Terminal API](https://www.tokenterminal.com/) client in python

For more information, see [Token Terminal API Documentation](https://docs.tokenterminal.com/)

### Installation:

use pip to install:

``` 
pip install tokenterminal
```

-----------

### Authentication:

Pass API key in object initialization.

-----------

### Example usage:

```
from tokenterminal import TokenTerminal

# object initialization
token_terminal = TokenTerminal(key='xxxxx-xxxx-xxxx-xxxx-xxxxxxxx')

# Fetch all data for projects' 
projects_data = token_terminal.get_all_projects()

for project_info in projects_data:
    print(project_info)

# Fetch project's historical metrics

project_metrics = token_terminal.get_historical_metrics('0x')
for metrics in project_metrics:
    print(metrics)

# To retrieve the metric availability for a project.
reponse = token_terminal.get_metric_availability(project_id=project_id)

# To retrieve metric aggregation data for one project.
reponse = token_terminal.get_metric_aggregations(project_id=project_id)

# Get financial statement for a project
reponse = token_terminal.get_financial_statement(
    project_id=project_id, 
    timestamp_granularity='week',
    interval='1m'
    )

# Get list of all available market sectors that are available
reponse = token_terminal.get_market_sectors()

# Get list of all metrics
reponse = token_terminal.get_all_metrics()

# To retrieve metric aggregations for multiple projects.
project_ids = ['aave', 'uniswap']
reponse = token_terminal.get_projects_metric_aggregations(project_ids=project_ids)
```
-------
#### Donate & Help maintain the library

[![Paypal](qrcode.png)](https://www.paypal.com/ncp/payment/KLFNJN7SH39EN)

-------