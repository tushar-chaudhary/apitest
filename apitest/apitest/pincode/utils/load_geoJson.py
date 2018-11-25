import psycopg2
import json
from django.contrib.gis.geos import GEOSGeometry


jsonData = json.loads(open('geoJson.json', 'r').read())['features']
conn = psycopg2.connect("host='localhost' port='5432' dbname='apitest' user='root' password='tushar1997'")
cur = conn.cursor()
co_ordinates_array = []
for index, features in enumerate(jsonData):
    id = index
    name = features['properties']['name']
    type = features['properties']['type']
    parent = features['properties']['parent']
    co_ordinates = str(GEOSGeometry(str(features['geometry'])))
    co_ordinates_array.append(co_ordinates)
    cur.execute(
        "INSERT INTO pincode_polygonmapping (id, name, type, parent, co_ordinates)  VALUES (%s, %s, %s, %s, %s)",
        [id, name, type, parent, co_ordinates]
    )

multiple_coordinates = []
for features in jsonData:
    multiple_coordinates.append(features['geometry']['coordinates'])

multiple_coordinate = GEOSGeometry(str({ "type": "MultiPolygon", "coordinates": multiple_coordinates
}))

cur.execute(
        "INSERT INTO pincode_multiplepolygonmapping (id, co_ordinates)  VALUES (%s, %s)",
        ['0', str(multiple_coordinate)]
)
conn.commit()



