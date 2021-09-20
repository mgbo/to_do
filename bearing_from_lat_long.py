
"""
Calculating the bearing between two geospatial coordinates

Let ‘R’ be the radius of Earth,
‘L’ be the longitude,
‘θ’ be latitude,
‘β‘ be Bearing.

Formula to find Bearing, when two different points latitude, longitude is given:
Bearing from point A to B, can be calculated as,

β = atan2(X,Y),

where, X and Y are two quantities and can be calculated as:

X = cos θb * sin ∆L

Y = cos θa * sin θb – sin θa * cos θb * cos ∆L

"""

import math

city_1_lat, city_1_lon = 39.099912, -94.581213
city_2_lat, city_2_lon = 38.627089, -90.2002203

x = math.cos(l)

