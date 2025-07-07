-- staging model for customers
select * from {{ source('raw','customers') }}