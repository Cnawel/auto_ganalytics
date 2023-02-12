from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

# Replace YOUR_PRIVATE_KEY_FILE with the path to your private key file
credentials = Credentials.from_service_account_file(
    "YOUR_PRIVATE_KEY_FILE",
    scopes=["https://www.googleapis.com/auth/analytics.readonly"],
)

# Replace YOUR_GA4_PROPERTY_ID with the ID of your GA4 property
service = build("analytics", "v1alpha", credentials=credentials)
property_id = "YOUR_GA4_PROPERTY_ID"

# Make a request to the GA4 API
response = service.properties().reports().batchGet(
    propertyId=property_id,
    body={
        "reportRequests": [
            {
              "metrics": [
                {
                  "expression": "ga:sessions"
                }
              ],
              "dimensions": [
                {
                  "name": "ga:date"
                }
              ],
              "dateRanges": [
                {
                  "startDate": "2022-01-01",
                  "endDate": "2022-01-31"
                }
              ]
            }
          ]
        }
).execute()

# Print the response from the API
print(response)
