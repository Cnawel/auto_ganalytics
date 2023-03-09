https://developers.google.com/analytics/bigquery/basic-queries

Basic queries for Google Analytics 4 event data export

bookmark_border
The sample queries in this page apply to the BigQuery event export data for Google Analytics 4. See BigQuery cookbook for Universal Analytics if you are looking for the same resource for Universal Analytics.

All queries listed here use sample datasets and should produce valid results. To use your own Google Analytics property's BigQuery event export data, look for the comment -- Replace table in each query and replace the sample dataset id. You can find your dataset Id by going navigating to your BigQuery export project in the BigQuery UI. For example, if your BigQuery export datasets Id is my- first-gcp-project:analytics_28239234, then replace:


  -- Replace table
  `bigquery-public-data.ga4_obfuscated_sample_ecommerce.events_*`
with:


  -- Replace table
  `my-first-gcp-project.analytics_28239234.events_*`

