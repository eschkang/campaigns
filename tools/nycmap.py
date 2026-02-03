import json
from shapely.geometry import shape, Point

# 1. Load your uploaded file
with open('Borough_Boundaries_20260202.geojson') as f:
    data = json.load(f)

# 2. Create a single geometry object for all boroughs
polygons = [shape(feature['geometry']) for feature in data['features']]
nyc_landmass = polygons[0]
for p in polygons[1:]:
    nyc_landmass = nyc_landmass.union(p)

# 3. Grid Dimensions
WIDTH, HEIGHT = 520, 520

# 4. NYC Bounding Box
MIN_LON, MAX_LON = -74.259, -73.700
MIN_LAT, MAX_LAT = 40.477, 40.917

# 5. Generate ASCII
ascii_map = []
for y in range(HEIGHT):
    line = ""
    # Invert Y so North is at the top
    lat = MAX_LAT - (y / HEIGHT) * (MAX_LAT - MIN_LAT)
    for x in range(WIDTH):
        lon = MIN_LON + (x / WIDTH) * (MAX_LON - MIN_LON)
        if nyc_landmass.contains(Point(lon, lat)):
            line += "#"
        else:
            line += " "
    ascii_map.append(line)

# 6. Save to file
with open('nyc_ascii_520.txt', 'w') as f:
    f.write("\n".join(ascii_map))

print("520x520 ASCII map generated: nyc_ascii_520.txt")