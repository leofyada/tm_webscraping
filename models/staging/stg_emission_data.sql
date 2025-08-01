SELECT 
    C2 AS "product_category",
    C4 AS "product",
    C7 AS "climatiq_name",
    C8 AS "climatiq_category",
    C9 AS "sector",
    C10 AS "source",
    C11 AS "link",
    C12 AS "source_dataset",
    C14 AS "year",
    C15 AS "year_release",
    C16 AS "region",
    C17 AS "region_name",
    C18 AS "description",
    C19 AS "unit_type",
    C20 AS "unit",
    C21 AS "source_lca_activity",
    C25 AS "factor"
FROM TM_DB.PUBLIC.EMISSION_TB
WHERE C1 IS NOT NULL
