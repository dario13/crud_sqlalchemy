from models.actor import Actor
from base import Session
from models.contact_details import ContactDetails

session = Session()

session.query(ContactDetails) \
    .filter(ContactDetails.phone_number == '421 333 9428') \
    .delete()

session.commit()
session.close()

