
  create view "postgres"."raw"."stg_website_sessions__dbt_tmp"
    
    
  as (
    

SELECT
  created_at AS website_session_created_at,
  utm_source,
  CURRENT_TIMESTAMP AS loaded_at
FROM "postgres"."raw"."website_sessions"
  );