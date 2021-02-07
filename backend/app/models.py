import random
from datetime import date, timedelta

from passlib.hash import sha256_crypt

from app import db


class User(db.Document):
    username = db.StringField(max_length=255)
    password = db.StringField(max_length=255)


class Table(db.Document):
    number = db.IntField()
    title = db.StringField(max_length=255)
    date = db.StringField(max_length=255)
    status = db.StringField(max_length=255)


def generate_date(start_date, end_date=date.today()):
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + timedelta(days=random_number_of_days)
    return random_date


def generate_table(amount):
    table = []
    first_words = ["Open", "Closed", "Noisy", "Loud", "Quiet", "Light", "Dark", "Easy", "Difficult", "New", "Old",
                   "Fast", "Slow", "Full", "Empty", "Long", "Short", "High", "Low", "Loose", "Tight", "Straight",
                   "Crooked", "Wide", "Narrow", "Good", "Bad", "Hot", "Cold", "Soft", "Neat", "Messy", "Beautiful",
                   "Pretty", "Ugly", "Wet", "Dry", "Big", "Little", "Clean", "Dirty", "Expensive", "Cheap",
                   "Inexpensive", "Large", "Small", "Sharp", "Dull", "Shiny", "Dim"]
    second_words = ["tree", "boat", "brick", "family", "word", "wife", "mother", "father", "son", "bread", 'pie',
                    "hour", "wealth", "man", "woman", "boy", "block", "car", "street", "hand", "foot", "apple", "eye",
                    "head", "arm", "hair", "face", "people", "love", "anger", "ceiling", "wall", "window", "heart",
                    "branch", "break", "kitten", "smile", "building", "wood", "saw", "glue", "table", "animal",
                    "advice", "age", "air", "sun", "king", "circle"]
    statuses = ["In progress", "Done", "Completed", "Finished", "Rejected", "Deferred", "Canceled", "New"]
    for i in range(amount):
        number = random.randint(70000000000, 79999999999)
        title = first_words[random.randrange(len(first_words))] + " " + second_words[random.randrange(len(second_words))]
        status = statuses[random.randrange(len(statuses))]
        random_date = generate_date(date(1970, 1, 1), date(2020, 12, 31))
        table.append({"number": number, "title": title, "date": random_date.isoformat(), "status": status})
    return table


def init_data():
    User.objects.delete()
    Table.objects.delete()
    table = generate_table(20)
    password = sha256_crypt.hash("admin")
    admin = User(username="admin", password=password).save()
    for row in table:
        number = row["number"]
        title = row["title"]
        date = row["date"]
        status = row["status"]
        Table(number=number, title=title, date=date, status=status).save()


init_data()













