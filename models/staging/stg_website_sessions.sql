{{ config(materialized='view') }}

SELECT
  created_at AS website_session_created_at,
  utm_source,
  CURRENT_TIMESTAMP AS loaded_at
FROM {{ source("raw", "website_sessions") }}
