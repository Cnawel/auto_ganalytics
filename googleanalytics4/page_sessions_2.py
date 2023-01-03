# Import Modules
import pandas as pd
from collections import defaultdict

# Authenticate & Build Service
analytics = ga_auth(scopes)

# Set Request Parameters
property_id = 'properties/306503726'
dimensions = ['sessionSourceMedium']
metrics = ['sessions', 'screenPageViews']

# Build Request Body
request = {
  "requests": [
    {
      "dateRanges": [
        {
          "startDate": "2022-03-01",
          "endDate": "2022-03-31"
        }
      ],
      "dimensions": [{'name': name} for name in dimensions],
      "metrics": [{'name': name} for name in metrics],
      "limit": 100000
    }
  ]
}

# Make Request
response = analytics.properties().batchRunReports(property=property_id, body=request).execute()

# Parse Request
report_data = defaultdict(list)

for report in response.get('reports', []):
    rows = report.get('rows', [])
    for row in rows:
        for i, key in enumerate(dimensions):
            report_data[key].append(row.get('dimensionValues', [])[i]['value'])  # Get dimensions
        for i, key in enumerate(metrics):
            report_data[key].append(row.get('metricValues', [])[i]['value'])  # Get metrics

df = pd.DataFrame(report_data)