# ceneoscrapper

## analiza struktury opinii w serwisie [ceneo.pl](https://www.ceneo.pl/)

|Składowa|Selektor|Zmienna|
|========|========|=======|
|opinia|div.js_product-review|review|
|identyikator opinii|\[data-entry-id\]|review_id|
|autor|span.user-post__author-name|author|
|rekomendacja|span.user-post__author-recomendation > em|recommendation|
|liczba gwiazdek|span.user-post__score-count|stars|
|treść|div.user-post__text|content|
|data wystawienia|span.user-post__published > time:nth-child(1) \[datetime\]|publish_date|
|data zakupu|span.user-post__published > time:nth-child(2) \[datetime\]|purchase_date|
|dla ilu przydatna|button.vote-yes\[data-total-vote\]<br>button.vote-yes > span<br>span\[id^=votes-yes\]|useful|
|dla ilu nieprzydatna|button.vote-no\[data-total-vote\]<br>button.vote-yes > span<br>span\[id^=votes-no\]|useless|
|lista zalet|div.review-feature__col:has( > div.review-feature__title--positives)>div.review-feature__item|pros|
|lista wad|div.review-feature__col:has( > div.review-feature__title--negatives)>div.review-feature__item|cons|