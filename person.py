def add_person(people_dict: dict, **kwargs):
    pid = max((int(i) for i in people_dict.keys()), default=0) + 1

    people_dict[pid] = kwargs


def add_attribute(person, people_dict, **kwargs):
    possible_ids = find_id(person, people_dict)

    if len(possible_ids) == 1:
        people_dict[possible_ids[0]].update(kwargs)


def find_id(person, people_dict):
    results = []
    for k, v in people_dict.items():
        if 'name' in v and v['name'] == person:
            results += k

    return results
