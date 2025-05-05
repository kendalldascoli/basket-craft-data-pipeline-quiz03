{{ config(materialized='view') }}

SELECT
    created_at AS website_session_created_at,
    CURRENT_TIMESTAMP AS loaded_at
FROM {{ source("public", "website_sessions") }}