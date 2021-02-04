import openpyxl
import pprint
import math
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import Select


def init_headless_firefox():
    opt = Options()
    opt.headless = True
    firefox = webdriver.Firefox(options=opt)

    return firefox


driver = init_headless_firefox()


def get_chicken():
    driver.get("https://www.chewy.com/instinct-original-grain-free-pate/dp/34728")
    chicken12 = error_check("Cat Food, 5.5-oz, case of 12", driver.title,
                            driver.find_element_by_css_selector('p.autoship-pricing').text)

    driver.get("https://www.chewy.com/instinct-original-grain-free-pate/dp/33433")
    chicken24 = error_check("Cat Food, 3-oz, case of 24", driver.title,
                            driver.find_element_by_css_selector('p.autoship-pricing').text)

    return chicken12, chicken24


def get_duck():
    driver.get("https://www.chewy.com/instinct-original-grain-free-pate/dp/34742")
    duck12 = error_check("Cat Food, 5.5-oz, case of 12", driver.title,
                         driver.find_element_by_css_selector('p.autoship-pricing').text)

    driver.get("https://www.chewy.com/instinct-original-grain-free-pate/dp/33435")
    duck24 = error_check("Cat Food, 3-oz, case of 24", driver.title,
                         driver.find_element_by_css_selector('p.autoship-pricing').text)

    return duck12, duck24


def get_lamb():
    driver.get("https://www.chewy.com/instinct-original-grain-free-pate/dp/34862")
    lamb12 = error_check("Cat Food, 5.5-oz, case of 12", driver.title,
                         driver.find_element_by_css_selector('p.autoship-pricing').text)

    driver.get("https://www.chewy.com/instinct-original-grain-free-pate/dp/33437")
    lamb24 = error_check("Cat Food, 3-oz, case of 24", driver.title,
                         driver.find_element_by_css_selector('p.autoship-pricing').text)

    return lamb12, lamb24


def get_rabbit():
    driver.get("https://www.chewy.com/instinct-original-grain-free-pate/dp/34870")
    rabbit12 = error_check("Cat Food, 5.5-oz, case of 12", driver.title,
                           driver.find_element_by_css_selector('p.autoship-pricing').text)

    driver.get("https://www.chewy.com/instinct-original-grain-free-pate/dp/33439")
    rabbit24 = error_check("Cat Food, 3-oz, case of 24", driver.title,
                           driver.find_element_by_css_selector('p.autoship-pricing').text)

    return rabbit12, rabbit24


def get_salmon():
    driver.get("https://www.chewy.com/instinct-original-grain-free-pate/dp/44660")
    salmon12 = error_check("Cat Food, 5.5-oz, case of 12", driver.title,
                           driver.find_element_by_css_selector('p.autoship-pricing').text)

    driver.get("https://www.chewy.com/instinct-original-grain-free-pate/dp/44661")
    salmon24 = error_check("Cat Food, 3-oz, case of 24", driver.title,
                           driver.find_element_by_css_selector('p.autoship-pricing').text)

    return salmon12, salmon24


def get_ultimate_chicken():
    driver.get("https://www.chewy.com/instinct-ultimate-protein-grain-free/dp/121824")
    chicken12 = error_check("Cat Food, 5.5-oz, case of 12", driver.title,
                            driver.find_element_by_css_selector('p.autoship-pricing').text)

    driver.get("https://www.chewy.com/instinct-ultimate-protein-grain-free/dp/121823")
    chicken24 = error_check("Cat Food, 3-oz, case of 24", driver.title,
                            driver.find_element_by_css_selector('p.autoship-pricing').text)

    return chicken12, chicken24


def get_ultimate_rabbit():
    driver.get("https://www.chewy.com/instinct-ultimate-protein-grain-free/dp/149497")
    rabbit12 = error_check("Cat Food, 5.5-oz, case of 12", driver.title,
                           driver.find_element_by_css_selector('p.autoship-pricing').text)

    driver.get("https://www.chewy.com/instinct-ultimate-protein-grain-free/dp/149497")
    rabbit24 = error_check("Cat Food, 3-oz, case of 24", driver.title,
                           driver.find_element_by_css_selector('p.autoship-pricing').text)

    return rabbit12, rabbit24


def get_variety():
    driver.get("https://www.chewy.com/instinct-original-grain-free-pate/dp/187498")
    variety3oz = error_check("Variety Pack Wet Canned Cat Food", driver.title,
                             driver.find_element_by_css_selector('p.autoship-pricing').text)
    variety5oz = 999
    # driver.get("https://www.chewy.com/instinct-original-grain-free-pate/dp/187499")
    # variety5oz = error_check("Variety Pack Wet Canned Cat Food", driver.title,
    # driver.find_element_by_css_selector('p.autoship-pricing').text)

    return variety5oz, variety3oz * 2


def get_venison():
    driver.get("https://www.chewy.com/instinct-original-grain-free-pate/dp/34741")
    venison12 = error_check("Cat Food, 5.5-oz, case of 12", driver.title,
                            driver.find_element_by_css_selector('p.autoship-pricing').text)

    driver.get("https://www.chewy.com/instinct-original-grain-free-pate/dp/33441")
    venison24 = error_check("Cat Food, 3-oz, case of 24", driver.title,
                            driver.find_element_by_css_selector('p.autoship-pricing').text)

    return venison12, venison24


def error_check(size, title, price):
    if size in title:
        return float(price.split('(')[0].split('$')[1])
    else:
        return 999


def calc_cheapest(weeks, smallcans, largecans):
    min_small_cans = min(smallcans, key=lambda key: smallcans[key])
    min_large_cans = min(largecans, key=lambda key: largecans[key])

    # Figure out how many days I need
    days = (7 * weeks)

    # Need 3 servings a day
    servings = days * 3

    # Large cans are worth 2 servings
    # Small cans are worth 1 serving

    large_cans = servings / 2
    large_pack = large_cans / 12
    large_pack = math.ceil(large_pack)

    # small_cans = servings / 1, this is small in the loop
    small_pack = servings / 24
    small_pack = math.ceil(small_pack)

    # Init Variables
    min_small = min_large = old_total = 999

    # Loop on the number of packs I need to figure out the math
    # Save the lowest price.  Will probably always be packs * whatever the lowest is.
    for small in range(small_pack + 1):
        total = smallcans[min_small_cans] * small + largecans[min_large_cans] * large_pack

        if old_total > total:
            old_total = total
            min_small = small
            min_large = large_pack
        large_pack -= 1

    return min_small, min_large, old_total


def calc_convenience(weeks, smallcans, largecans):
    min_small_cans = min(smallcans, key=lambda key: smallcans[key])
    min_large_cans = min(largecans, key=lambda key: largecans[key])

    # Figure out how many days I need
    days = (7 * weeks)

    # Use 1 can of each a day.
    packs = math.ceil(days / 24)

    # Need double the amount of Large cans
    total = smallcans[min_small_cans] * packs + largecans[min_large_cans] * (2 * packs)

    return packs, 2 * packs, total


def main():
    # Large Cans, Small Cans = Function()

    chicken12, chicken24 = get_chicken()
    duck12, duck24 = get_duck()
    lamb12, lamb24 = get_lamb()
    rabbit12, rabbit24 = get_rabbit()
    salmon12, salmon24 = get_salmon()
    uchicken12, uchicken24 = get_ultimate_chicken()
    urabbit12, urabbit24 = get_ultimate_rabbit()
    variety5oz, variety3oz = get_variety()
    venison12, venison24 = get_venison()

    # Close Browser
    driver.close()

    largecans = {'Chicken': chicken12,
                 'Duck': duck12,
                 'Lamb': lamb12,
                 'Rabbit': rabbit12,
                 'Salmon': salmon12,
                 'Ultimate Chicken': uchicken12,
                 'Ultimate Rabbit': urabbit12,
                 'Variety': variety5oz,
                 'Venison': venison12}

    smallcans = {'Chicken': chicken24,
                 'Duck': duck24,
                 'Lamb': lamb24,
                 'Rabbit': rabbit24,
                 'Salmon': salmon24,
                 'Ultimate Chicken': uchicken24,
                 'Ultimate Rabbit': urabbit24,
                 'Variety': variety3oz,
                 'Venison': venison24}
    '''
    smallcans = {'Chicken': 31.69,
                 'Duck': 40.81,
                 'Lamb': 40.81,
                 'Rabbit': 45.37,
                 'Salmon': 36.25,
                 'Ultimate Chicken': 33.97,
                 'Ultimate Rabbit': 49.93,
                 'Variety': 34.18,
                 'Venison': 49.93}

    largecans = {'Chicken': 26.11,
                 'Duck': 34.09,
                 'Lamb': 34.09,
                 'Rabbit': 37.51,
                 'Salmon': 28.39,
                 'Ultimate Chicken': 28.39,
                 'Ultimate Rabbit': 999,
                 'Variety': 26.59,
                 'Venison': 39.79}
    '''
    print('3oz cans:', smallcans)
    print('5.5oz cans:', largecans)

    min_small_cans = min(smallcans, key=lambda key: smallcans[key])
    min_large_cans = min(largecans, key=lambda key: largecans[key])

    # 24 weeks is the lowest common multiple where all the math is super nice.
    # 6 weeks is not insane, but the math isn't as nice.
    weeks = 24
    min_small, min_large, cheapest = calc_cheapest(weeks, smallcans, largecans)
    small_packs, large_packs, easiest = calc_convenience(weeks, smallcans, largecans)
    savings = easiest - cheapest

    print(f'Every {weeks} weeks:')
    if min_small > 0:
        print(f'Order {min_small} Cases of', min_small_cans, '3oz cans.')
    if min_large > 0:
        print(f'Order {min_large} Cases of', min_large_cans, '5.5oz cans.')
    print('Total:', '${:,.2f}'.format(cheapest))
    print('or')
    print(f'Every {weeks} weeks:')
    print(f'Order {small_packs} Cases of 24', min_small_cans, '3oz cans.')
    print(f'Order {large_packs} Cases of 12', min_large_cans, '5.5oz cans.')
    print('Total:', '${:,.2f}'.format(easiest))
    print('Convenience Costs:', '${:,.2f}'.format(savings), f'per {weeks} weeks.')

    print('')

    weeks = 6
    min_small, min_large, cheapest = calc_cheapest(weeks, smallcans, largecans)
    small_packs, large_packs, easiest = calc_convenience(weeks, smallcans, largecans)
    savings = easiest - cheapest

    print(f'Every {weeks} weeks:')
    if min_small > 0:
        print(f'Order {min_small} Cases of', min_small_cans, '3oz cans.')
    if min_large > 0:
        print(f'Order {min_large} Cases of', min_large_cans, '5.5oz cans.')
    print('Total:', '${:,.2f}'.format(cheapest))
    print('or')
    print(f'Order {small_packs} Cases of 24', min_small_cans, '3oz cans.')
    print(f'Order {large_packs} Cases of 12', min_large_cans, '5.5oz cans.')
    print('Total:', '${:,.2f}'.format(easiest))
    print('Convenience Costs:', '${:,.2f}'.format(savings), f'per {weeks} weeks.')


if __name__ == "__main__":
    main()
