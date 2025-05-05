WITH source AS (
    SELECT * FROM {{ source('public', 'website_sessions') }}
)

SELECT
    id,
    utm_source,
    created_at,
    current_timestamp as loaded_at
FROM source
