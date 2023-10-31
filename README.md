# pollution in Daegu

Some people used to say that pollution spikes in Korea are due to China's industrial activities.
Is it really the case? As a scientist, I couldn't trust people who couldn't bring reliable sources.

## DISCLAIMER

**As you can see, the codebase is atrocious to read or maintain.**

This is due to 3 main reasons:
- I was a beginner at that time. I wasn't familiar with 
- I made this project in 3 hours
- I was in a quite heavy hangover

Please do not judge me, and consider it as it is: a funny side project to keep me busy during an afternoon,.

## Sources
I used an open database containing the air quality in Daegu for a little bit less than 3000 days (at aquicn.org).
I retro engineered an archive meteorological API (api.weather.com) to find my datas about wind speed and wind directions.

## Analysis
I don't have enough technical abilities regarding statistics to make anything out of what I found. However, my results are showed in the files 'final_results.txt'.
Feel free to make any analysis with it.

## Files
- meteo.py is used for fetching datas together and putting them in a json file. Since the json is uploaded too, this file is useless
- analysis.py is used for analysing this json. You should focus on this file first
- outputs.json is file generated in meteo.py
- final_results is a synthesis that could lead to a quick analysis
- daegu-air-quality is a downloaded file which indicates the presence of pm25, pm10, o3, no2, so2, co for 2800 days in Daegu


Please make something useful, or at least something fun with my work :)
