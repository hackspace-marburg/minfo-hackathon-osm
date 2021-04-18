from .check import Check, register_check
from .osm import OsmEntry

from typing import Set, Optional, Callable

from selenium import webdriver
import textdistance

import logging
import os


log_format = "%(asctime)s - %(levelname)s - %(message)s"
log_level = logging.getLevelName(os.environ.get("LOG_LEVEL", "INFO"))
logging.basicConfig(format=log_format, level=log_level)
logger = logging.getLogger("lieferando")
logger.setLevel('DEBUG')


def _lieferando_init() -> Set[str]:
    logger.info(f"lieferando init...")
    rs = set()
    urls = (
        "https://www.lieferando.de/lieferservice/essen/marburg-35037",
        "https://www.lieferando.de/lieferservice/essen/marburg-35039",
        "https://www.lieferando.de/lieferservice/essen/marburg-35041",
        "https://www.lieferando.de/lieferservice/essen/35043",
    )

    options = webdriver.ChromeOptions()
    options.headless = False
    driver = webdriver.Chrome(options=options)

    for url in urls:
        driver.get(url)
        candidates = driver.find_elements_by_class_name("restaurantname")
        candidates = set(
            c.text.lower().strip().replace('®','')
            for c in candidates if len(c.text) > 0
        )
        rs = rs.union(candidates)

    driver.close()

    return rs


restaurants = _lieferando_init()
logger.debug(f"known restaurants:\n{restaurants}")


def _check_lieferando(entry_name: str, city: str) -> Optional[float]:
    propabilities = list()
    for e in restaurants:
        levenshtein_distance = textdistance.levenshtein(entry_name.lower(), e.lower())
        distance = max(1 - (levenshtein_distance / len(e)), 0)

        propabilities.append(distance)

    highest_propability = sorted(propabilities)[-1:]
    return highest_propability[0]


@register_check
class CheckLieferando(Check):
    """
    checks if an entry is of "food" type and queries the lieferando website for it.
    returns 1.0 if a matching entry is found, because it is very likely that an
    food place that delivcers still exists.
    """

    @staticmethod
    def eval(entry: OsmEntry) -> Optional[float]:
        tags = entry.tags
        logger.debug(tags)

        candidate = False

        if 'amenity' in tags:
            amenity_value = tags['amenity']
            check_tags = (
                'bar',
                'biergarten',
                'cafe',
                'fast_food',
                'food_court',
                'ice_cream',
                'pub',
                'restaurant',
            )
            if amenity_value in check_tags:
                candidate = True

        if 'shop' in tags:
            shop_value = tags['shop']
            check_tags = (
                'alcohol',
                'bakery',
                'beverages',
                'brewing_supplies',
                'butcher',
                'cheese',
                'chocolate',
                'coffee',
                'confectionery',
                'convenience',
                'deli',
                'dairy',
                'farm',
                'frozen_food',
                'greengrocer',
                'health_food',
                'ice_cream',
                'organic',
                'pasta',
                'pastry',
                'seafood',
                'spices',
                'tea',
                'wine',
                'water',
            )
            if shop_value in check_tags:
                candidate = True


        if "name" not in tags:
            # TODO can we do better than this...?
            return None

        entry_name = tags['name']

        if candidate:
            return _check_lieferando(entry_name, "Marburg")

        return None
