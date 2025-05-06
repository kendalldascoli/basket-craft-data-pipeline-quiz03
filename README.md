# basket-craft-data-pipeline-quiz03

This repository contains a complete data pipeline project learned during lesson exercises and built during Quiz 03. The pipeline extracts website session data from the bakset_craft MySQL database using Python, Pandas, and SQLAlchemy, and then loads it into a raw schema in our Postgres database hosted on AWS RDS. dbt is then used to transform the raw data into cleaned staging models and fct_website_sessions_utm_source_daily for analysis. I then automated the pipeline execution using GitHub Actions, securely managing all credentials using GitHub Secrets. The data is visualized in Looker Studio through an interactive dashboard featuring session trends, repeat session heatmaps, and UTM source comparisons. This project demonstrates best practices in ELT, automation, and data modeling. Below is a link to the visualizations as well as a Data Pipeline Diagram.

Dashboard: [https://lookerstudio.google.com/s/iHTTfdB-XqA]
![Data_Pipeline_Diagram drawio](https://github.com/user-attachments/assets/382b7196-b2b3-4588-978f-17560dd2bb31)
