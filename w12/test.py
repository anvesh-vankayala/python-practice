import csv
# from collections import namedtuple
import datetime
from typing import NamedTuple


class Tickets(NamedTuple):
    summons_number:str
    plate_id : str
    reg_state : str
    plate_type : str
    issue_date : datetime
    violation_code: int
    body_type: str
    make : str
    violation_type : str


make_wise_violations = {}

def lazy_csv_reader(csv_file):
    maper = lambda x: tuple(int(i) for i in x.split('/')[::-1])
    with open(csv_file) as f:
        r = csv.reader(f)
        for row in r:
            if row[0] == 'Summons Number':
                continue            
            dat = maper(row[4])
            dat = (dat[0],dat[2],dat[1])
            date = datetime.datetime(*dat)
            
            tik = Tickets(row[0],row[1],row[2],row[3],date,
                    row[5],row[6],row[7],row[8])
            if tik.make in make_wise_violations:
                if tik.violation_type!= '':
                    make_wise_violations[tik.make]+= 1
            else:
                make_wise_violations[tik.make]= 1
            yield tik

# ['Summons Number', 'Plate ID', 'Registration State', 'Plate Type', 'Issue Date', 'Violation Code', 'Vehicle Body Type', 'Vehicle Make', 'Violation Description']
csv_pa = '/workspaces/python-practice/w12/nyc_parking_tickets_extract-1.csv'
for row in lazy_csv_reader(csv_pa):
    print(row)

print(make_wise_violations)