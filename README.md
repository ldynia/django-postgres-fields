# Description

Plain django init project.

# Instructions

```bash
$ docker-compose up
```

- [Indexing JsonField in Django and PostgreSQL](https://medium.com/analytics-vidhya/indexing-jsonfield-in-django-and-postgresql-89b7571df830)
- [django_jsonfield_index](https://github.com/abtinmo/django_jsonfield_index)
- [Using JSONB in PostgreSQL](https://dev.to/scalegrid/using-jsonb-in-postgresql-how-to-effectively-store-index-json-data-in-postgresql-5d7e)
- [jsonschema](https://python-jsonschema.readthedocs.io/en/stable/)

# SQL

```
-- select * from demo_product where name = '1';
select * from demo_product where attributes_idx->>'name' = '1';
select * from demo_product where attributes_idx@>'{"name": "1"}';



TRUNCATE demo_product;
ALTER SEQUENCE demo_product_id_seq RESTART WITH 1;
SELECT * FROM  demo_product ORDER BY id DESC;

-- Create on column
CREATE INDEX attrs_idx_hash ON demo_product USING HASH((attributes_idx) jsonb_ops);
CREATE INDEX attrs_idx_gin ON demo_product USING GIN((attributes_idx) jsonb_ops);
CREATE INDEX attrs_idx_gin ON demo_product USING GIN((attributes_idx) jsonb_path_ops);

-- Create on key
CREATE INDEX attrs_idx_hash ON demo_product USING HASH((attributes_idx->name) jsonb_ops);
CREATE INDEX attrs_idx_hash ON demo_product USING HASH((attributes_idx->>name) text_ops);

CREATE INDEX attrs_idx_btree ON demo_product USING BTREE((attributes_idx->name) jsonb_ops);
CREATE INDEX attrs_idx_btree ON demo_product USING BTREE((attributes_idx->>name) text_ops);

CREATE INDEX attrs_idx_gin ON demo_product USING GIN((attributes_idx->name) jsonb_ops);
CREATE INDEX attrs_idx_gin ON demo_product USING GIN((attributes_idx->name) jsonb_path_ops);

-- Drop indexs
DROP INDEX IF EXISTS exist attrs_idx_hash;
DROP INDEX IF EXISTS attrs_idx_btree;
DROP INDEX IF EXISTS attrs_idx_gin;
```
