from pymongo import *
from mongoengine import *
from datetime import *
from time import *
import os

# Connection to the DB
connect(
    db="UmuziProspects",
    username=os.environ.get("USERNAME"),
    password=os.environ.get("PASSWORD"),
    authentication_source=os.environ.get("AUTHENTICATION"),
    host=os.environ.get("HOST"),
    port=int(os.environ.get("PORT"))
)

# Visitor Collection Schema
class Visiter(Document):
    name = StringField()
    age = IntField()
    date_of_visit = DateTimeField()
    time_of_visit = StringField()
    assisted_by = StringField()
    comments = StringField()


# Create a visiter
def create_visiter(name, age, assisted_by, comments):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    try:
        visiter = Visiter(
            name=name,
            age=age,
            date_of_visit=date.today(),
            time_of_visit=current_time,
            assisted_by=assisted_by,
            comments=comments,
        )
        visiter.save()
        return f"Visiter Created"
    except:
        return f"Error creating a visiter."


# Return all Visiters
def list_visiters():
    try:
        visiters = Visiter.objects()
        visiters_list = []
        for visiter in visiters:
            visiters_list.append(
                {
                    "id": visiter.id,
                    "name": visiter.name,
                    "age": visiter.age,
                    "date_of_visit": visiter.date_of_visit,
                    "time_of_visit": visiter.time_of_visit,
                    "assisted_by": visiter.assisted_by,
                    "comments": visiter.comments,
                }
            )
        return visiters_list
    except DoesNotExist:
        return f"Something went wrong when retreving the data"


# Return a single visiter
def single_visiter(id):
    try:
        visiter = Visiter.objects(id=id).get()
        visiter = {
            "id": visiter.id,
            "name": visiter.name,
            "age": visiter.age,
            "date_of_visit": visiter.date_of_visit,
            "time_of_visit": visiter.time_of_visit,
            "assisted_by": visiter.assisted_by,
            "comments": visiter.comments,
        }
        return visiter
    except DoesNotExist:
        return f"Visiter does not exit"


# Update Vister
def update_visiter(id, name, assisted_by, comments):
    try:
        visiter = Visiter.objects(id=id).get()
        visiter.update(name=name, assisted_by=assisted_by, comments=comments)
        visiter.reload()
        return f"Vister details updated"
    except DoesNotExist:
        return f"Visiter not found"


# Delete a single visiter
def delete_visiter(id):
    try:
        visiter = Visiter.objects(id=id).get()
        visiter.delete()
        return f"Visiter details deleted"
    except DoesNotExist:
        return f"Visiter not found"


# delete all visiters
def delete_all_visiters():
    try:
        visiter = Visiter.objects()
        visiter.delete()
        return f"All Visiters deleted"
    except DoesNotExist:
        return f"Error deleting visiters"


if __name__ == "__main__":
    # Create Visiter
    # visiter_create = create_visiter(
    #     "Adrian", 22, "Admin", "Added by Admin")
    # print(visiter_create)

    # list visiters
    visiters_list = list_visiters()
    print(" == === All Visiters == ===")
    print(visiters_list)

    # list single visiter
    # single_visiter = single_visiter("5eaf6e42281f06e890656ee6")
    # print(" == === Single Visiter Search == ===")
    # print(single_visiter)

    # update Visiter
    # visiter_update = update_visiter(
    #     "5eaf6e42281f06e890656ee6", "Bongo", "Adrian", "Changed name to Bongo")
    # print(" == === Update Visiter Details == ===")
    # print(visiter_update)

    # Delete Single Visiter
    # delete_visiter = delete_visiter("5eaf6e42281f06e890656ee6")
    # print(" == === Delete Visiter Details == ===")
    # print(delete_visiter)

    # Delete all visiters
    # delete_all_visiters = delete_all_visiters()
    # print(" == === Deleting all visiters == ===")
    # print(delete_all_visiters)
