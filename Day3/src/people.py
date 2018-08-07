# based of the swagger.yml file operationId
# we must have a method in people.py called read.

from datetime import datetime

from flask import (
    make_response,
    abort
)

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

# Data to serve with our API
# Real world app would use a db to store this data
# to make the data persist

PEOPLE = {
    "Farrell": {
        "fname": "Doug",
        "lname": "Farrell",
        "timestamp": get_timestamp()
    },
    "Brockman": {
        "fname": "Kent",
        "lname": "Brockman",
        "timestamp": get_timestamp()
    },
    "Easter": {
        "fname": "Bunny",
        "lname": "Easter",
        "timestamp": get_timestamp()
    }
}

# We create the handler for our read (GET method) people
def read_all():
    """
    This function responds to a request for /api/people
    with the complete lists of people
    :return:        json string of list of people
    """
    # Create the list of people from our data
    return [PEOPLE[key] for key in sorted(PEOPLE.keys())]

def read_one(lname):
    """
    This function responds to a request for api/people/{lname}
    with one matching person from people

    :param lname:    last name of the person to find
    :return:         Person matching the last name
    """
    if lname in PEOPLE:
        person = PEOPLE.get(lname)

    # other wise, not found
    else:
        abort(404, f'Person with the last name "{lname}" not found')

    return person

def create(person):
    """
    This function creates a new person in the people structure
    based on the passed in person data

    :param person:    Person to create in people structure
    :return:          201 on success, 406 on person exists
    """
    lname = person.get('lname', None)
    fname = person.get('fname', None)

    # Does this person exist already?
    if lname not in PEOPLE and lname is not None:
        PEOPLE[lname] = {
            'lname': lname,
            'fname': fname,
            "timestamp": get_timestamp()
        }
        return make_response(f'{lname} successfully created', 201)
    else:
        # they exist, meaning an error response
        abort(406, f'Person with last name "{lname}" already exists')
        
def update(lname, person):
    """
    This function updates a existing person in the people structure

    :param lname:    Last name of a person to update in the people structure
    :param person:   Person to update
    :return:         Updated person structure
    """
    # first check to see if they exist:
    if lname in PEOPLE:
        # then update them
        PEOPLE[lname]['fname'] = person.get('fname')
        PEOPLE[lname]['timestamp'] = get_timestamp()

        # returns the structure
        return PEOPLE[lname]
    # else, abort throwing an error
    else:
        abort(404, f'Person with the last name "{lname}" was not found')

def delete(lname):
    """
    This function deletes a person from the people structure

    :param lname:    last name of person to delete
    :return:         200 on successful delete, 404 if not found
    """
    # First check if the person is there
    if lname in PEOPLE:
        # if so, delete them
        del PEOPLE[lname]
        return make_response(f'"{lname}" was successfully deleted from the collection')
    # if not, throw a 404
    else:
        abort(404, f'The person with the last name of "{lname}" was not found')      