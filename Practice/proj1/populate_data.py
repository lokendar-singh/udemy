import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','proj1.settings')

import django
django.setup()

import random
from core.models import Topic,Webpage,AccessRecord
from faker import Faker

fdata = Faker()
cus_topics =['Search','Social','Marketplace','News','Games']

def add_top():
    t = Topic.objects.get_or_create(topic_name=random.choice(cus_topics))[0]
    t.save()
    return t

def pop_data(n=5):
    for i in range(n):
        fk_name = fdata.company()
        fk_url =fdata.url()
        fk_date = fdata.date()
        wb = Webpage.objects.get_or_create(topic=add_top(),web_name=fk_name,web_url=fk_url)[0]
        ar = AccessRecord.objects.get_or_create(name=wb,date=fk_date)[0]

if __name__ == '__main__':
    print('Populating data via faker file')
    pop_data(20)
    print('done')
