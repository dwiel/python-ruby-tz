#!/usr/bin/env python
# -*- coding: utf-8 -*-

tzs =    [[-43200, "International Date Line West" ],
          [-39600, "Midway Island", "Samoa" ],
          [-36000, "Hawaii" ],
          [-32400, "Alaska" ],
          [-28800, "Pacific Time (US & Canada)", "Tijuana" ],
          [-25200, "Mountain Time (US & Canada)", "Chihuahua", "Mazatlan", 
                   "Arizona" ],
          [-21600, "Central Time (US & Canada)", "Saskatchewan", "Guadalajara",
                   "Mexico City", "Monterrey", "Central America" ],
          [-18000, "Eastern Time (US & Canada)", "Indiana (East)", "Bogota",
                   "Lima", "Quito" ],
          [-14400, "Atlantic Time (Canada)", "Caracas", "La Paz", "Santiago" ],
          [-12600, "Newfoundland" ],
          [-10800, "Brasilia", "Buenos Aires", "Georgetown", "Greenland" ],
          [ -7200, "Mid-Atlantic" ],
          [ -3600, "Azores", "Cape Verde Is." ],
          [     0, "Dublin", "Edinburgh", "Lisbon", "London", "Casablanca",
                   "Monrovia", "UTC"],
          [  3600, "Belgrade", "Bratislava", "Budapest", "Ljubljana", "Prague",
                   "Sarajevo", "Skopje", "Warsaw", "Zagreb", "Brussels",
                   "Copenhagen", "Madrid", "Paris", "Amsterdam", "Berlin",
                   "Bern", "Rome", "Stockholm", "Vienna",
                   "West Central Africa" ],
          [  7200, "Bucharest", "Cairo", "Helsinki", "Kyev", "Riga", "Sofia",
                   "Tallinn", "Vilnius", "Athens", "Istanbul", "Minsk",
                   "Jerusalem", "Harare", "Pretoria" ],
          [ 10800, "Moscow", "St. Petersburg", "Volgograd", "Kuwait", "Riyadh",
                   "Nairobi", "Baghdad" ],
          [ 12600, "Tehran" ],
          [ 14400, "Abu Dhabi", "Muscat", "Baku", "Tbilisi", "Yerevan" ],
          [ 16200, "Kabul" ],
          [ 18000, "Ekaterinburg", "Islamabad", "Karachi", "Tashkent" ],
          [ 19800, "Chennai", "Kolkata", "Mumbai", "New Delhi" ],
          [ 20700, "Kathmandu" ],
          [ 21600, "Astana", "Dhaka", "Sri Jayawardenepura", "Almaty",
                   "Novosibirsk" ],
          [ 23400, "Rangoon" ],
          [ 25200, "Bangkok", "Hanoi", "Jakarta", "Krasnoyarsk" ],
          [ 28800, "Beijing", "Chongqing", "Hong Kong", "Urumqi",
                   "Kuala Lumpur", "Singapore", "Taipei", "Perth", "Irkutsk",
                   "Ulaan Bataar" ],
          [ 32400, "Seoul", "Osaka", "Sapporo", "Tokyo", "Yakutsk" ],
          [ 34200, "Darwin", "Adelaide" ],
          [ 36000, "Canberra", "Melbourne", "Sydney", "Brisbane", "Hobart",
                   "Vladivostok", "Guam", "Port Moresby" ],
          [ 39600, "Magadan", "Solomon Is.", "New Caledonia" ],
          [ 43200, "Fiji", "Kamchatka", "Marshall Is.", "Auckland",
                   "Wellington" ],
          [ 46800, "Nuku'alofa" ]]

tz_names = {}
for row in tzs :
	for name in row[1:] :
		tz_names[name] = row[0]

if __name__ == '__main__' :
  print tz_names
