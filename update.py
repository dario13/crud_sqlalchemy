from models.actor import Actor
from base import Session
from models.contact_details import ContactDetails

session = Session()

session.query(ContactDetails) \
    .filter(ContactDetails.phone_number == '421 444 2323') \
    .update({'phone_number' : '421 445 2424'})

session.commit()
session.close()

