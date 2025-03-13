class Event:
    """
    Calendar event

    Stores event `summary`, `location`, and `dtstart` as strings
    """
    def __init__(self, summary, dtstart, location):
        self.summary = summary
        self.location = location
        self.dtstart = dtstart
            
    def get_year(self):
        return int(self.dtstart[:4])

    def get_month(self):
        return int(self.dtstart[4:6])
    
    

    def __repr__(self):
        """ Set printable representation of object """
        return f"{self.dtstart} {self.summary}"


# Verify constructor
assert Event("a", "2015", "b").location == "b"
assert Event("c", "2016", "d").summary == "c"
assert Event("e", "2017", "f").dtstart == "2017"

# Verify get_year
assert Event("a", "201801", "b").get_year() == 2018
assert Event("a", "201910", "b").get_year() == 2019

# Verify get_month
assert Event("a", "201801", "b").get_month() == 1
assert Event("a", "201910", "b").get_month() == 10


class Calendar:
    """
    Calendar of events

    Maintains and internal list of `Events`

    Events can be added, removed, and searched
    """
    def __init__(self):
        self.events = []

    def add_event(self, event):
        self.events.append(event)

    def remove_event(self, event):
        self.events.remove(event)

    def search(self, query):

        matching_events = []

        for event in self.events:
            eventstring = event.summary.lower()
            if query in eventstring:
                matching_events.append(event)

        return matching_events 
        
    def get_month(self,year,month):
        
        matching_events = []
        for event in self.events:
            if event.get_year() == year and event.get_month() == month:
                    matching_events.append(event)
        return matching_events


# Verify constructor
assert Calendar().events == []

# Verify add_event
c = Calendar()
e1 = Event("a", "202502", "b")
c.add_event(e1)
assert len(c.events) == 1
e2 = Event("c", "202503", "d")
c.add_event(e2)
assert len(c.events) == 2
assert isinstance(c.events[0], Event)

# Verify remove_event
c.remove_event(e1)
assert len(c.events) == 1
c.remove_event(e2)
assert len(c.events) == 0

# Verify search
c.add_event(e1)
c.add_event(e1)
c.add_event(e2)
assert len(c.search("a")) == 2
assert len(c.search("c")) == 1
assert c.search("c")[0] == e2

# Verify get_month
assert len(c.get_month(2025, 2)) == 2
assert len(c.get_month(2025, 3)) == 1
c.add_event(Event("a", "202611", "l"))
assert len(c.get_month(2026, 11)) == 1
assert len(c.get_month(2027, 11)) == 0
assert isinstance(c.get_month(2026, 11)[0], Event)


def load_calendar(filename):
    """
    Return a populated `Calendar` object from an iCal file

    Each event in the file becomes one `Event` on the calendar

    See RFC5545 for more information.
    """
    

    # Open and read the iCal file contents
    with open(filename) as f:
        webcal = f.read()

    # Create empty calendar
    calendar = Calendar()

   

    # Process iCal file line by line building events
    for line in webcal.splitlines():
        # Create a new event and add to calendar
        if line.startswith("BEGIN:VEVENT"):
            event = Event(None, None, None)
            calendar.add_event(event)

        if line.startswith("DTSTART:"):
            event.dtstart = line[8:].strip()

        # Set summary of current event
        if line.startswith("SUMMARY:"):
            event.summary = line[8:].strip()
            

        # Set location of current event
        if line.startswith("LOCATION:"):
            event.location = line[9:].strip()
        

    return calendar


# Populate calendar from iCal file
calendar = load_calendar("cal.ics")

# Verify load_calendar
assert len(calendar.search("fox")) == 1
assert calendar.search("fox")[0].summary[-3:] == "Fox"
assert calendar.search("fox")[0].dtstart[:8] == "20250325"
assert calendar.search("fox")[0].location[:7] == "Reardon"
assert len(calendar.get_month(2025, 2)) == 68
assert len(calendar.search("chapel")) == 45

# Print all events from calendar with "chapel" in summary
for chapel in calendar.search("chapel"):
    print(f"{chapel.dtstart[:8]}: {chapel.summary}")