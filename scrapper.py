import json
from typing import Type
import requests
from bs4 import BeautifulSoup

def extract_element(ancestor, selector, attribute=None, return_list = False):
    try:
        if attribute:
            return ancestor.select_one(selector)[attribute]
        elif return_list:
            return [item.text.strip() for item in ancestor.select(selector)]
        else:
            return ancestor.select_one(selector).text.strip()
    except : 
        return None



product_id = input("Podaj kod produktu:\n")
url = f"https://www.ceneo.pl/{product_id}#tab=reviews"
all_reviews = []
while(url):
    response = requests.get(url)
    page_dom = BeautifulSoup(response.text, 'html.parser')
    reviews = page_dom.select("div.js_product-review")

    review_elements = {
        "author": ["span.user-post__author-name"],
        "recommendation": ["span.user-post__author-recomendation > em"],
        "stars": ["span.user-post__score-count"],
        "content": ["div.user-post__text"],
        "publish_date": ["span.user-post__published > time:nth-child(1)", "datetime"],
        "purchase_date": ["span.user-post__published > time:nth-child(2)", "datetime"], 
        "useful": ["span[id^=votes-yes]"], 
        "useless": ["span[id^=votes-no]"],
        "pros": ["div.review-feature__title--positives ~ div.review-feature__item", None,True],
        "cons": ["div.review-feature__title--negatives ~ div.review-feature__item", None,True]
    }

    for review in reviews:
        single_opinion = {key:extract_element(review, *values)
        for key, values in review_elements.items()}

        review_id = review["data-entry-id"]
        single_review['recommendation'] = True if single_review['recommendation'] == "Polecam" else False if single_review['recommendation'] == "Nie polecam" else None
        single_review['stars'] = float(single_review['stars'].split("/").pop(0).replace(",", "."))
        #content = content.replace("\n", " ").replace("  ", " ").strip()
        single_review['useful'] = int(single_review['useful'])
        single_review['useless'] = int(single_review['useless'])
        single_review['publish_date'] = single_review['publish_date'].split(' ').pop(0) if single_review['publish_date'] is not None else None
        single_review['purchase_date'] = single_review['purchase_date'].split(' ').pop(0) if single_review['purchase_date'] is not None else None



    all_reviews.append(single_review)

    try: 
        next_page = page_dom.select_one("a.pagination__next")
        url = "https://www.ceneo.pl"+next_page["href"]
    except TypeError: url = None

with open(f"./reviews/{product_id}.json", "w", encoding="UTF-8") as f:
    json.dump(all_reviews, f, indent=4, ensure_ascii=False)
