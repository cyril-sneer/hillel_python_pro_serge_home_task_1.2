from urllib.parse import urlparse, parse_qsl

def parse(query: str) -> dict:
    """
    Parsing URL for purpose to extract the query-parameters
    Works via standard python lib urllib

    :param query as str:
    :return: dict {query_param: value}
    """
    all_instances = urlparse(query)
    query_instances = all_instances.query
    list_from_query = parse_qsl(query_instances)
    dict_from_query = {k: v for k, v in list_from_query}

    return dict_from_query


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}

    assert parse('http://docs.python.org:80/3/library/urllib.parse.html?highlight=params#url-parsing') == \
           {'highlight': 'params'}
    assert parse('http://user:pwd@NetLoc:80/path;param?query=arg#frag') == {'query': 'arg'}
    assert \
        parse('https://example.com/page?utm_source=google&utm_medium=cpc&utm_campaign=summer_sale&referral=partner') == \
        {'utm_source': 'google', 'utm_medium': 'cpc', 'utm_campaign': 'summer_sale', 'referral': 'partner'}
    assert parse('https://example.com/path/page?param1=value1&param2=value2#section1') == \
           {'param1': 'value1', 'param2': 'value2'}
    assert parse('https://username:password@example.com/search?q=query&category=books&page=2&sort=rating') == \
           {'q': 'query', 'category': 'books', 'page': '2', 'sort': 'rating'}
    assert parse('https://example.com/news;section2?source=bbc&category=sports&date=2023-05-18') == \
           {'source': 'bbc', 'category': 'sports', 'date': '2023-05-18'}
    assert parse('https://user:password@example.com/product?id=9876&size=medium&color=red&discount=true') == \
           {'id': '9876', 'size': 'medium', 'color': 'red', 'discount': 'true'}
    assert parse('https://example.com/search?query=apple&sort=price&order=asc&filter=available') == \
           {'query': 'apple', 'sort': 'price', 'order': 'asc', 'filter': 'available'}
    assert parse('https://example.com/gallery?album=summer2023&sort=date&fullscreen=true#section4') == \
           {'album': 'summer2023', 'sort': 'date', 'fullscreen': 'true'}
    assert parse('https://subdomain.example.com/page?lang=en&country=us&theme=dark') == \
           {'lang': 'en', 'country': 'us', 'theme': 'dark'}


# def parse_cookie(query: str) -> dict:
#     return {}
#
#
# if __name__ == '__main__':
#     assert parse_cookie('name=Dima;') == {'name': 'Dima'}
#     assert parse_cookie('') == {}
#     assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
#     assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}