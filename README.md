# LRM1200 V2.6

- Map menu and POI controls are circular and match the 38 px loading-circle size.
- Menu route and utility buttons use rounded pill styling.
- The old POI copy-name/address action is removed.
- Every POI popup now provides “在百度地圖開啟”.
- The Baidu Maps URI receives the POI's WGS84 latitude/longitude and explicitly sets coord_type=wgs84 to avoid China coordinate offset.
- V2.5 checked-category querying and default POI selections are retained.
