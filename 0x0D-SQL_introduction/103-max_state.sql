-- Import in hbtn_0c_0 database this table dump: download (same as Temperatures #0)
SELECT state, MAX(value) as max_tmp FROM temperatures ORDER BY state ASC;
