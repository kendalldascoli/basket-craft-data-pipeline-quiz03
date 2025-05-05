
  create view "postgres"."raw"."fct_website_sessions_utm_source_daily__dbt_tmp"
    
    
  as (
    WITH sessions AS (
    SELECT * FROM "postgres"."raw"."stg_website_sessions"
)

SELECT
    date_trunc('day', website_session_created_at) AS session_date,
    utm_source,
    count(*) AS session_count
FROM sessions
GROUP BY 1, 2
  );