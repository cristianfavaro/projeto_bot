# Generated by Django 3.2.18 on 2023-04-10 18:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0002_historycontext'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='HistoryContext',
            new_name='ConversationContext',
        ),
    ]
