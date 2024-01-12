import pytz
import icalendar
from datetime import datetime
from pathlib import Path
import os
from icalendar import Calendar, Event,  vText, vCalAddress



def new_ical(series_name):
    from icalendar import Calendar 
   
    series_name = Calendar()
    series_name.add('prodid', '-//My calendar product//example.com//')
    series_name.add('version', '2.0')
    
    return series_name



def make_events(cal):
    uid = 110
    circuit = 'Nürburgring Gesamtrecke' '\n' 'Nürburg, Rhineland-Palatinate, Germany'

    for title, description, year, month, day in zip(titles, descriptions, cln_yrs, cln_mons, cln_days):
        ievent = Event()
        ievent.add('summary', title) #Title of the event
        ievent.add('description', description)     #Description of event
        ievent.add('dtstart', datetime(int(year), int(month), int(day), 10, 0, 0, tzinfo=pytz.timezone('utc')))
        ievent.add('dtend', datetime(int(year), int(month), int(day), 14, 0, 0, tzinfo=pytz.timezone('utc')))
        ievent.add('dtstamp', datetime(2023, 3, 17, 0, 10, 0, tzinfo=pytz.timezone('utc')))
        ievent.add('location', vText(circuit))
        ievent.add('uid', uid)
        uid += 1
        cal.add_component(ievent)
        
    return cal
    



def make_ics():
    directory = str(Path(r'C:\Users\chris\Documents\Calendars')) + "/"
    print("ics file will be generated at ", directory)
    f = open(os.path.join(directory, 'NLS 2023.ics'), 'wb')
    f.write(NLS.to_ical())
    f.close()
