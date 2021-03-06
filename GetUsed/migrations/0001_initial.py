# Generated by Django 3.2 on 2021-12-11 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_type', models.CharField(choices=[('Y', 'ヤフオク'), ('M', 'メルカリ'), ('P', 'PayPayフリマ'), ('R', 'ラクマ'), ('H', 'ハードオフ'), ('m', 'モバオク'), ('E', 'ebay'), ('S', 'セカイモン')], max_length=1, null=True, verbose_name='shop')),
                ('item_category', models.CharField(choices=[('none', '指定なし'), ('computer', 'コンピュータ'), ('books', '本・雑誌'), ('game', 'ゲーム'), ('music', '音楽・CD'), ('movie', '映画・ビデオ'), ('HomeAppliances', '家電・AV・カメラ'), ('fashion', 'ファッション'), ('beauty', '美容・コスメ・香水'), ('interior', 'インテリア'), ('outdoor', 'スポーツ・レジャー'), ('goods', 'おもちゃ・グッズ'), ('food', '食料'), ('car', '自動車・オートバイ')], default='指定なし', max_length=20, null=True, verbose_name='category')),
                ('keyword', models.CharField(max_length=40, null=True, verbose_name='keyword')),
                ('item_link', models.CharField(blank=True, max_length=200, null=True, verbose_name='link')),
                ('item_price', models.PositiveIntegerField(blank=True, null=True, verbose_name='price')),
                ('item_date', models.CharField(blank=True, max_length=10, null=True, verbose_name='date')),
                ('item_name', models.CharField(blank=True, max_length=200, null=True, verbose_name='name')),
                ('item_buy_price', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='buy_price')),
                ('item_limit', models.CharField(blank=True, default='なし', max_length=10, null=True, verbose_name='time_limit')),
                ('item_status', models.CharField(choices=[('指定なし', '指定なし'), ('売り切れ', '売り切れ'), ('販売中', '販売中')], default='指定なし\u3000', max_length=10, null=True, verbose_name='status')),
                ('item_image', models.CharField(blank=True, max_length=500, null=True, verbose_name='image')),
            ],
        ),
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.CharField(max_length=40, null=True, verbose_name='keyword')),
                ('max_price', models.PositiveIntegerField(blank=True, null=True, verbose_name='max_price')),
                ('min_price', models.PositiveIntegerField(blank=True, null=True, verbose_name='min_price')),
                ('sold_out', models.CharField(blank=True, max_length=20, null=True, verbose_name='sold_out')),
                ('category', models.CharField(blank=True, max_length=20, null=True, verbose_name='category')),
            ],
        ),
    ]
