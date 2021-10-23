import datetime 
import geocoder

class Sun_Angle:

    def __init__(self, latitude=''):
        # Latitude of User (Optional) - Will use IP address of device for latitude if nothing is entered. 
        self.latitude = latitude
        # Classification of how intense the Sunlight is vs. the angle of the Sun at noon. The article only gave two categories: Low, or High. 
        self.ray_intensity= [('LOW', 45.0), ('HIGH', 90.0)]
        self.today = datetime.datetime.now()

        # Approximate Equinox and Solstice Dates - and their corresponding subsolar point(s) in the list below.     
        # format: (DD, MM, Angle)
        self.seasons = ((22, 3), (21, 6), (22, 9), (21, 12))
    
        self.subsolar_point = (0, 23.5, 0, -23.5)
        
        
    def current_location(self):
        """ Get Current Latitude from IP or enter Latitude desired """
        if self.latitude == '':
            self.latitude = geocoder.ip('me').latlng[0]
        else: 
            self.latitude = float(self.latitude)
        return self.latitude
        
        
    def day_of_year_number(self, dates):
        """ Convert the Equinox and Solstice dates to their day of the year number and compare with the current date """ 
        # get the datetime objects for each date in the self.seasons list
        # Reformt to (Day of Year Number, Datetime Object) for each item in list
        return [(int(date.strftime("%j")), date) for date in dates]


    def current_season(self):
        """ Reformat all seasons dates into datetime objects with the current year, so that they can later be convert into their 'day of the year' numbers """
        # Use Current year
        #year = int(self.today.strftime("%Y"))
        # List of Datetime objects for each date
        datetime_objects = [datetime.datetime(int(self.today.strftime("%Y")), season[1], season[0]) for season in self.seasons]
        return self.day_of_year_number(datetime_objects)
    
    def last_subsolar_point(self):
        """ Compare the Current day of the year number, to the day of the year numbers for the solstice and equinox dates to find the current subsolar point (the 'last' subsolar point as in, what it changed to most recently) """
        current = self.day_of_year_number([self.today])
        seasonal =self.current_season()
        # Return the latitude to guage where the sun will form a 90° angle at noon (based on season). 
        # It will be (+/-)23.5° or 0° depending on the date.
        return [(seasonal[seasonal.index(tilt)-1][0], tilt[0], self.subsolar_point[seasonal.index(tilt)-1])  for tilt in seasonal if current[0][0] <= tilt[0]][0][2]
        
        
    def zenith_angle(self):
        """ Calculate the Zenith Angle """
        # The angle at noon based on the difference of the User's current latitude and subsolar point. It will be the same as the current location if the current date is on or right after an equinox date. 
        return self.current_location() - self.last_subsolar_point() 
        
    
    def noon_sun_angle(self):
        """ Calculate for the Noon sun's angle """
        return 90 - self.zenith_angle()
    
    def sunlight_intensity(self):
        """ The intensity of the sun's rays """ 
        noon_sun = self.noon_sun_angle()
        if noon_sun > 90:
            noon_sun = noon_sun - 90
        return [(angle[0], noon_sun) for angle in self.ray_intensity if noon_sun <= angle[1]][0]

    def __str__(self):
        sun_info = self.sunlight_intensity()
        return "{}\n \nNoon Sun Angle: {} \nSunlight Intensity: {}  \nZenith Angle: {}".format(self.today.strftime('%d %B %Y'), sun_info[1], sun_info[0], 90-sun_info[1])
        


if __name__ == '__main__':
    latitude = input("Enter your latitude or press 'continue' to use your device's IP address: ")
    sun = Sun_Angle(latitude)
    print(sun.__str__())
