# LRM1200 V2.7

Built from the earlier rounded-button V2.6 design, with the fixed control-point GPX layer added.

- Circular 38 px menu and POI controls matching the loading circle.
- Rounded route and utility buttons.
- 15 fixed CP waypoints loaded separately from dynamic OSM POIs.
- 7 fixed CPs assigned to 去程 and 8 to 回程 based on cumulative route distance and the 604.74 km turnaround.
- 去程 shows forward CPs, 回程 shows rebound CPs, and 全程 shows all fixed CPs.
- Both fixed CPs and dynamic OSM POIs include a Baidu Maps hyperlink.
- Baidu URI links pass WGS84 coordinates with coord_type=wgs84.
- Dynamic POI queries continue to request only checked categories.
