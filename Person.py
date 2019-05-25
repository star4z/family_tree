from datetime import datetime
from enum import Enum

from PyQt5.QtCore import QDate


class PersonReference:
    tree_id = 0

    def __init__(self, uid, parents, partners):
        self.id = uid
        self.parents = parents
        self.partners = partners


class Person:
    def __init__(self):
        self.uid = datetime.now().microsecond
        self.name_title = ""
        self.name_first = ""
        self.name_middle = ""
        self.name_last = ""
        self.name_alts = []  # legal name changes, e.g. maiden names
        self.name_suffix = ""
        self.name_nickname = ""  # default nickname, e.g. Dwayne "The Rock" Johnson (overrides middle initial?)
        self.name_nicknames = []

        self.gender = None

        # relations are indicated by uid
        self.parents = [0, 0]
        self.relationships = []  # array of PartnerRelationship

        self.birth_date = QDate()
        self.birth_loc = ""

        self.still_living = False
        self.death_date = 0
        self.death_loc = ""

        self.photos = []  # file addresses of relevant photos; all photos should be in the photos directory

    def partners(self):
        return map(lambda relationship: relationship.partnerUid, self.relationships)

    def middle_initial(self):
        if len(self.name_middle) > 0:
            return self.name_middle[0]
        else:
            return ""


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


class Gender(Enum):
    MALE = 0
    FEMALE = 1
    OTHER = 2
