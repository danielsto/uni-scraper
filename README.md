# uni-scraper 🎓 

## Overview
``uni-scraper`` allows data from [El Mundo's ranking]() to be scraped and translated into a JSON file, making it easier to work with it. For example for your own data visualizations such as [D3]() or [Chartjs]().

## Instructions
Run it from the command line typing ``python scraper.py`` or use your IDE of choice. A file named ``university_rankings.json`` should be created in your working directory.

## How it works
[El Mundo's ranking]() is a yearly publication about spanish universities. Each degree is evaluated among these institutions and the best five are listed in order. ``ùni-scraper`` assigns points to each university according to the position in that ranking:
- 1st gets 5 points
- 2nd gets 4 points
- 3rd gets 3 points
- 4th gets 2 points
- 5th gets 1 point  

This conversion is made using ``rank_to_points`` function, which is probably not the best solution:
```python
def rank_to_points(rank):
    if rank == '1º':
        points = 5
    elif rank == '2º':
        points = 4
    elif rank == '3º':
        points = 3
    elif rank == '4º':
        points = 2
    elif rank == '5º':
        points = 1
    return points
```
Points are summed for each university and that represents its score. Each university is stored in a dictionary ``uni_data`` with its name as key and score as value. 
