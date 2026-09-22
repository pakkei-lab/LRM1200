
#!/usr/bin/env python3
"""Prepare Baidu map tiles/POIs for this static site.
Requires your own authorized Baidu Maps AK and permission to cache/distribute map data.
Set BAIDU_AK, then adapt TILE_URL to the URL supplied under your Baidu license.
The script intentionally does not scrape public tile endpoints.
"""
import os, sys, json
AK=os.getenv('BAIDU_AK','')
if not AK:
    sys.exit('Set BAIDU_AK first. Example: BAIDU_AK=your_key python scripts/build_baidu_assets.py')
print('AK detected. Configure your licensed Baidu tile/POI endpoint in this script before running.')
print('Output tile layout required by the app: tiles/{z}/{x}/{y}.png')
print('POI output format: data/pois.js containing window.POIS=[{name,type,lat,lon}, ...]')
