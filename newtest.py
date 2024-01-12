url = 'https://www.nuerburgring-langstrecken-serie.de/en/calendar-nurburgring-langstrecken-serie-2023/'

import Scraper_Tools
import Calendar_tools

nls_soup = make_soup(url)

scrape_nls(nls_soup)