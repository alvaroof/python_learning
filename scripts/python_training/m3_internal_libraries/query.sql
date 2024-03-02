WITH all_data AS (
    SELECT DISTINCT drug_id AS drug_id,
        ims_id AS ims_id,
        country AS country,
        molecule AS molecule
    FROM SNOWFLAKE_TABLE_WITH_INFO
)
SELECT drug_id,
    ims_id,
    country,
    molecule
FROM all_data
