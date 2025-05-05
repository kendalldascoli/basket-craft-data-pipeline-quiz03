

SELECT
  created_at AS website_session_created_at,
  utm_source,
  CURRENT_TIMESTAMP AS loaded_at
FROM "postgres"."raw"."website_sessions"