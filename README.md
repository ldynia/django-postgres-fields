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
SELECT * FROM  demo_product ORDER BY id DESC;
CREATE INDEX JsonFieldIndex ON demo_product USING GIN(attributes jsonb_path_ops);
DROP INDEX JsonFieldIndex;

CREATE INDEX JsonFieldIndexList ON demo_product USING GIN((attributes -> 'values') jsonb_path_ops);
CREATE INDEX JsonFieldIndex ON demo_product USING HASH((attributes -> 'name'));

DROP INDEX JsonFieldIndexList;
DROP INDEX JsonFieldIndex;
```
