-- Example: Query total value for a specific event name.
--
-- Queries the total event value for all 'purchase' events.

SELECT
  SUM(
    (
      SELECT COALESCE(value.int_value, value.float_value, value.double_value)
      FROM UNNEST(event_params)
      WHERE key = 'value'
    ))
    AS event_value
FROM
  -- Replace table name.
  `bigquery-public-data.ga4_obfuscated_sample_ecommerce.events_*`
WHERE
  event_name = 'purchase'
  -- Replace date range.
  AND _TABLE_SUFFIX BETWEEN '20201201' AND '20201202';