"""
steps:
1. get data regarding to tubes from tfl
2. get data regarding schedule from (google) calendar
3. for each day of the week, find the most likely journey based on schedule
4. display necessary info regarding this journey

"""

##get schedule for piccadilly line from caledonian road to kings cross stations
#using tfl api
#ned to automate the naptan code retrival though
https://api.tfl.gov.uk/Line/piccadilly/Timetable/940GZZLUCAR/to/940GZZLUKSX