from datetime import datetime


class PersonReference:
    tree_id = 0

    def __init__(self, uid, parents, children):
        self.id = uid
        self.parents = parents
        self.children = children


class Person:
    uid = datetime.now().microsecond
    name_first = ""
    name_last = ""
    name_middle = ""
    name_alts = []
    name_nickname = ""  # default nickname for display, eg. Dwayne "The Rock" Johnson (overrides middle initial?)
    name_nicknames = []

    # relations are indicated by uid
    parents = [0, 0]
    relationships = []  # array of PartnerRelationship

    birth_date = 0
    birth_loc = ""

    still_living = False
    death_date = 0
    death_loc = ""

    photos = []  # file addresses of relevant photos; all photos should be in the photos directory


class PartnerRelationShip:
    partnerUid = 0
    married = False
    divorced = False  # must be married to be divorced
    date_start = 0  # use for start of dating relationship (opt)
    date_end = 0  # (opt_
    marriage_start = 0  # use for date of marriage
    marriage_end = 0  # only applicable if divorced
    children = []  # array of Child
    notes = []


class Child:
    uid = 0
    adopted = False
