import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-add', help='add person by name')
    parser.add_argument('-add_to', help='add field to this person')
    parser.add_argument('-property', help='property to change for ')
    parser.add_argument('-view', help='list all people')
    parser.add_argument('-add_relation', help='link to another person')
    parser.add_argument('-other_person', help='person to add relation to')
    parser.add_argument('-relation', help='the way the person is related to the other person')


if __name__ == '__main__':
    main()
