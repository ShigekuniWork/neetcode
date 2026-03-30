SELECT
  s.seller_name
FROM
  seller AS s
WHERE
  NOT EXISTS (
    SELECT
      1
    FROM
      orders AS o
    WHERE
      o.seller_id = s.seller_id
      AND o.sale_date >= '2020-01-01'
      AND o.sale_date <= '2020-12-31'
  )
ORDER BY
  s.seller_name ASC;