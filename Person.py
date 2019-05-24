from datetime import datetime


class PersonReference:
    tree_id = 0

    def __init__(self, uid, parents, partners):
        self.id = uid
        self.parents = parents
        self.partners = partners


class Person:
    def __init__(self):
        self.uid = datetime.now().microsecond
        self.name_first = ""
        self.name_last = ""
        self.name_middle = ""
        self.name_alts = []
        self.name_nickname = ""  # default nickname, eg. Dwayne "The Rock" Johnson (overrides middle initial?)
        self.name_nicknames = []

        # relations are indicated by uid
        self.parents = [0, 0]
        self.relationships = []  # array of PartnerRelationship

        self.birth_date = 0
        self.birth_loc = ""

        self.still_living = False
        self.death_date = 0
        self.death_loc = ""

        self.photos = []  # file addresses of relevant photos; all photos should be in the photos directory

    def partners(self):
        return map(lambda relationship: relationship.partnerUid, self.relationships)


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
