import database

#add a record to the database
#database.add_one("femi", "Aguda", "femi@aguda.com")

#delete a record from the database
#database.delete_one("6")

# Add many records

"""stuff = [
    ('Brenda', 'Osulaba', 'brenda@osulaba.com'),
    ('Joshua', 'Ekehila', 'joshua@ekehila.com')
]

database.add_many(stuff)

#show all the records
database.show_all()"""

database.email_lookup("brenda@osulaba.com")