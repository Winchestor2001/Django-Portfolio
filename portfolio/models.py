from django.db import models



class Portfolio(models.Model):
    CHOICES = (
        ('Web Site', 'Web'),
        ('Telegram Bot', 'TgBot')
    )
    CHOICES_2 = (
        ('Web', 'Web'),
        ('TgBot', 'TgBot')
    )

    category = models.CharField(max_length=100, choices=CHOICES)
    category_2 = models.CharField(max_length=100, choices=CHOICES_2, null=True)
    client = models.CharField(max_length=50)
    image_1 = models.ImageField(upload_to='articles/', null=True)
    image_2 = models.ImageField(upload_to='articles/', null=True)
    image_3 = models.ImageField(upload_to='articles/', null=True)
    project_date = models.DateTimeField(auto_now_add=True)
    project_url = models.CharField(max_length=100)
    about_project = models.TextField()


class MyInfoConfig(models.Model):
    image = models.ImageField(upload_to='articles/')
    myName = models.CharField(max_length=50)
    mySurname = models.CharField(max_length=50)
    my_location_link = models.CharField(max_length=500)



class AboutInfoConfig(models.Model):
    birthday = models.CharField(max_length=100)
    own_website = models.CharField(max_length=100)
    myPhone_number = models.CharField(max_length=50)
    now_city = models.CharField(max_length=100)
    my_age = models.CharField(max_length=20)
    my_level = models.CharField(max_length=100)
    my_email = models.CharField(max_length=100)
    freelance_status = models.CharField(max_length=50)
    about_text = models.TextField()



class FactsInfoConfig(models.Model):
    happy_clients = models.CharField(max_length=30)
    projects = models.CharField(max_length=30)
    support_hours = models.CharField(max_length=30)
    hard_workers = models.CharField(max_length=30)
    facts_text = models.TextField()



class SkillsInfoConfig(models.Model):
    html_status = models.CharField(max_length=10)
    css_status = models.CharField(max_length=10)
    js_status = models.CharField(max_length=10)
    python_status = models.CharField(max_length=10)
    django_status = models.CharField(max_length=10)
    react_status = models.CharField(max_length=10)
    skill_text = models.TextField()


