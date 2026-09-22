# 毅行1200 騎行離線地圖

Static, GitHub Pages-ready cycling route viewer generated from `lushu-5630109.gpx`.

## Included
- Offline route display with forward / return toggle
- Offline custom map renderer, no online JavaScript dependency
- GPX route, start and finish markers
- POI category toggles and click-to-copy Chinese name
- Device GPS positioning, including positions far away from the route
- Local raster tile loading from `tiles/{z}/{x}/{y}.png`

## Run locally
Browsers restrict GPS and some file features on `file://`. Start a local server:

```bash
python -m http.server 8000
```

Then open `http://localhost:8000`.

## Publish to GitHub Pages
1. Create a repository.
2. Upload all files in this folder.
3. In Settings > Pages, deploy from the main branch root.
4. Open the generated HTTPS Pages URL. HTTPS is required for browser geolocation.

## Baidu offline tiles and POIs
This package does not scrape or redistribute Baidu tiles. Use your own authorized Baidu Maps account, AK, quota and caching/distribution permission. Put licensed/pre-generated tiles in `tiles/{z}/{x}/{y}.png` and add POIs to `data/pois.js`.

The GPX contains no waypoint elements, so only Start and Finish are generated automatically. Restaurants, fuel stations, convenience stores and hotels require an authorized POI data source. Keep only POIs whose shortest distance to the route is <= 50 m before writing `pois.js`.

## China coordinate note
The GPX is WGS-84. Baidu map data normally uses BD-09. If your authorized tile package is BD-09 aligned, convert route and POI coordinates consistently during the asset build step. Do not mix WGS-84 route coordinates directly with BD-09 tiles.

## Size note
The route spans roughly 3.37 degrees north-south, so a complete high-zoom offline corridor can be very large. For GitHub Pages, package corridor tiles only and consider Git LFS or a release artifact for large tile sets.
