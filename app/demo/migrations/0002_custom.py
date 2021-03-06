from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0001_initial'),
    ]

    operations = [
      migrations.RunSQL('CREATE INDEX "name_idx.btree-idx" ON demo_product using BTREE(name_idx text_ops);'),
      migrations.RunSQL('CREATE INDEX "attributes_idx.gin-idx" ON demo_product USING GIN(attributes_idx jsonb_ops);'),
      migrations.RunSQL('CREATE INDEX "attributes_idx.name.btree-idx" ON demo_product USING BTREE((attributes_idx -> \'name\') jsonb_ops);'),
    ]
