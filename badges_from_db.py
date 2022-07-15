#!/usr/bin/env
from sqlalchemy import *
from io import open
from string import Template

with open('db_secret', encoding="utf-8") as f:
    DATABASE_URL = f.read()

db = create_engine(DATABASE_URL)

# Last name of locals
list_of_locals = ['Kirk', 'McCoy']
list_of_locals = [n.lower() for n in list_of_locals]

# Last name of contact persons
list_of_contacts = ['Spock', 'Kirk']
list_of_contacts = [n.lower() for n in list_of_contacts]

# Email of people who have used the wrong slot for their last name
list_of_inverse_behavior = ['toto@toto.org']

sql_query = "select lname, sname, first_name, last_name, affiliation, pronoun, email from participants"
temp = Template('\participant{ $lname }{ $sname }{ $affiliation }{ $pronoun }{ $highlight }\n')

with open('latex/participants.tex', 'w',  encoding="utf-8")as f:
    for lname, sname, first_name, last_name, affiliation, pronoun, email in db.engine.execute(sql_query).fetchall():

        # Defaulting for people who did not provide a preference
        if email in list_of_inverse_behavior:
            if lname == '':
                lname = first_name
            if sname == '':
                sname = last_name
        else:
            if lname == '' and sname == '':
                lname = first_name
                sname = last_name

        # Removing pronoun if blank space provided
        if len(pronoun) < 2:
            print('Warning, setting %s pronoun to empty'%pronoun)
            pronoun = ''

        # if in the list of locals, add flag
        if last_name.lower() in list_of_contacts:
            highlight = '\\contact'
        elif last_name.lower() in list_of_locals:
            highlight = '\\local'
        else:
            highlight = ''

        s = temp.substitute(lname=lname, sname=sname, affiliation=affiliation,
                           pronoun=pronoun, highlight=highlight)

        # Escaping problematic characters
        s = s.replace('&', '\&')
        #s = s.replace('@', '\@')
        s = s.replace('_', '\_')
        f.write(s)
