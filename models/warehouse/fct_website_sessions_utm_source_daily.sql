WITH sessions AS (
    SELECT * FROM {{ ref('stg_website_sessions') }}
)

SELECT
    date_trunc('day', created_at) AS session_date,
    utm_source,
    count(*) AS session_count
FROM sessions
GROUP BY 1, 2
