# Description

Project for benchmarking indexing on jsonb column as well as a playground for testing JSONField in Django.

# Installation

Clone repo and run below command.

```bash
$ docker-compose up
```

### Links

- [Indexing JsonField in Django and PostgreSQL](https://medium.com/analytics-vidhya/indexing-jsonfield-in-django-and-postgresql-89b7571df830)
- [django_jsonfield_index](https://github.com/abtinmo/django_jsonfield_index)
- [Using JSONB in PostgreSQL](https://dev.to/scalegrid/using-jsonb-in-postgresql-how-to-effectively-store-index-json-data-in-postgresql-5d7e)
- [jsonschema](https://python-jsonschema.readthedocs.io/en/stable/)

# SQL

```SQL
-- Index normal column with defualt index --
CREATE INDEX name_idx on demo_product(name_idx);

--Create index on entire doucument. Use `@> '{"key": "val"}'` for performance gain.
--CREATE INDEX "attributes_idx.btree-idx" ON demo_product USING BTREE(attributes_idx);
--CREATE INDEX "attributes_idx.hash-idx" ON demo_product USING HASH(attributes_idx);
CREATE INDEX "attributes_idx.gin-idx" ON demo_product USING GIN((attributes_idx));

--Create index on doucument's element. Use `"column" -> 'key' = '"val"';` for performance gain.
CREATE INDEX "attributes_idx.name.btree-idx" ON demo_product USING BTREE((attributes_idx -> 'name'));
CREATE INDEX "attributes_idx.name.btree-idx2" ON demo_product USING BTREE((attributes_idx ->> 'name'));
--CREATE INDEX "attributes_idx.name.hash-idx" ON demo_product USING HASH((attributes_idx -> 'name'));
--CREATE INDEX "attributes_idx.name.gin-idx" ON demo_product USING GIN((attributes_idx -> 'name'));

-- Delete created indexes --
--DROP INDEX IF EXISTS "attributes_idx.name.btree-idx";
--DROP INDEX IF EXISTS "attributes_idx.name.btree-idx2";
--DROP INDEX IF EXISTS "attributes_idx.name.hash-idx";
--DROP INDEX IF EXISTS "attributes_idx.name.gin-idx";

-- For detail insights add EXPlAIN ANALYZE in front of SELECT --
SELECT * FROM demo_product order by id desc;
SELECT * FROM demo_product WHERE "attributes_idx" -> 'name' = '"1546321"';
--SELECT * FROM demo_product WHERE "attributes_idx" ->> 'name' = '1546321';
--SELECT * FROM demo_product WHERE "attributes_idx" @> '{"name": "1546321"}';
--SELECT * FROM demo_product WHERE "attributes_idx" -> 'values' @> '[1356788, 1356789]';
--SELECT * FROM "demo_product" WHERE "attributes_idx" -> 'values' @> '[1535440, 1535441]' LIMIT 1;
```
