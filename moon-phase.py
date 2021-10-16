import datetime

class Moon_Phase:
    #today = datetime.datetime.now()
    def __init__(self):
        # A Known New Moon Date
        self.new_moon_date = datetime.date(2000,1,6)
        # Current date
        self.today = datetime.datetime.now()
        # Formatted Date
        self.calendar_date = self.today.strftime("%d %B %Y")
        # There is a New moon every 29.53 days
        self.cycle = 29.53
        # Approximate Moon Ages and Phase names (Very Approximate.)
        self.phase_names = [(0, 'New'), (3.69125, 'Waxing Cresent'), (7.3825, 'First Quarter'), (9.07375, 'Waxing Gibbous'), (14.765,'Full'), (18.45625, 'Waning Gibbous'), (22.1475, 'Third Quarter'), (24.83875, 'Waning Cresent')]

    def proleptic_gregorian(self, date):
        """ Convert to Proleptic Gregorian ordinal of the date """
        return date.toordinal()


    def julian_day_number(self, date):
        """ Convert to JDN format """
        date = self.proleptic_gregorian(date)
        return date + 1721424.5

    def days_since_new(self):
        """ Days since the recent known new moon (date defined above). """
        current = self.julian_day_number(self.today)
        last_new = self.julian_day_number(self.new_moon_date)
        return current - last_new

    def previous_cycles(self):
        """ How many full cycles have passed (we will subtract all completed cycles in the moon_age method) """
        days = self.days_since_new()
        return days / self.cycle

    def moon_age(self):
        """ Get the Fraction part of the number of previous cycles and multiple by one cyclic period """
        p_cycles = self.previous_cycles()
        # The fraction part of this number, is an incomplete cycle - the one the moon is currently in.
        days_complete = p_cycles - int(p_cycles)
        # multiply the fraction by the total number of days to find the most recent new moon (when the current cycle began) - this is the moons current age (in days)
        age = days_complete * self.cycle
        # return the moon's current age in days (float)
        return age

    def current_phase(self):
        """ An approximate naming system for the moon's current age """
        age = self.moon_age()
        for phase in self.phase_names:
            if age < phase[0]:
                # Comparing the age of moon phases in the index
                phase_number = self.phase_names.index(phase)
                # Returning only the Name of the Current Phase
                return self.phase_names[phase_number-1][1]



if __name__=='__main__':
    moon = Moon_Phase()
    # If this program is run, it will print out the date and current moon phase name
    print("{} \n{}".format(moon.calendar_date,moon.current_phase()))
