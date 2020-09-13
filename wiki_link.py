import requests

def wiki_req (page_name):
    res = requests.get('https://he.wikipedia.org/w/api.php?action=query&format=json&titles='+page_name+'&prop=links&pllimit=max').json()
    page_num = list(res['query']['pages'])
    if 'links' in res['query']['pages'][page_num[0]]:
        dic = res['query']['pages'][page_num[0]]['links']
        links_list = [item['title'] for item in dic]
        return (links_list)
    else:
        return ({"!page not found!"})

def link_count_list (start,i):
    uniq_list = set({start})
    if i < 3:
        i = i + 1
        wiki = wiki_req(start)
        count = len(wiki)
        for page in wiki:
            if page not in uniq_list:
                count_link,link_list = link_count_list(page,i)
                uniq_list.update(link_list)
                count = count + count_link
        return (count,uniq_list)
    return (0,uniq_list)


start = 'רקורסיה'
count_link,link_list = link_count_list(start,0)
print(f'יש {count_link} לינקים בסך הכל ')
print(f'יש {len(link_list)} ערכים יחודיים')