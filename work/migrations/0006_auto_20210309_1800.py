# Generated by Django 3.1.7 on 2021-03-09 18:00

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0005_auto_20210309_1755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workpage',
            name='body',
            field=wagtail.core.fields.StreamField([('heading_and_paragraph', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(default='', help_text='Add your title')), ('paragraph', wagtail.core.blocks.RichTextBlock(default='', help_text='Add your content'))])), ('technology', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(default='', help_text='Add your title')), ('paragraph', wagtail.core.blocks.RichTextBlock(default='', help_text='Add your content'))]))]),
        ),
    ]