# manhattan-walked-streets-tracker
This codebase hopes to convert raw Google Timeline data and determine which streets/avenues in Manhattan you have walked on.

Getting the Google Timeline data [is trivial](https://takeout.google.com/settings/takeout). Then unselect all, and select only "Location History". You'll want the big `.json` file from this path. Seems as though Google doesn't make this easy to automate, so a constantly updating map may not be easy. Headless browser scraper would probably do the trick, though. 

New York City has been really good about making data open and easy to use. They have [this site](https://streets.planning.nyc.gov/data?lat=-73.9971&lng=40.7304&zoom=15.49) which allows downloading all of the "City Street Features" for the entire city. Just click on the download button on the map, then at the top "All". This provides a set of files that I'm unfamiliar with, but can be converted to JSON with [online tools](https://mygeodata.cloud/converter/) (which results in long/lats for streets) or via [Python it seems as well](https://gis.stackexchange.com/questions/113799/reading-shapefile-in-python). 
