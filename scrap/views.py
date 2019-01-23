from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from django.http import JsonResponse
import re


def get_hiver_data_as_api(request):
    p_tag_list=[]
    h1_tag_list=[]
    h2_tag_list=[]
    h3_tag_list=[]
    h4_tag_list=[]
    anchor_tag_list=[]
    li_tag_list = []
    span_tag_list = []
    option_tag_list = []
    address_tag_list = []
    title_tag_list = []
    desc_tag_list = []

    dict={}
    dict2={}
    lst = []
    r=requests.get("https://hiverhq.com/")
    c=r.content
    soup=BeautifulSoup(c,"html.parser")
    p_tags  =soup.find_all("p")
    h1_tags =soup.find_all("h1")
    h2_tags =soup.find_all("h2")
    h3_tags =soup.find_all("h3")
    h4_tags =soup.find_all("h4")
    anchor_tags =soup.find_all("a")
    li_tags =soup.find_all("li")
    span_tags =soup.find_all("span")
    option_tags = soup.find_all("option")
    address_tags = soup.find_all("address")
    title_tags = soup.find_all("title")
    desc_tags = soup.find_all("desc")


    p_tag_list = [i.text for i in p_tags]
    h1_tag_list = [i.text for i in h1_tags]
    h2_tag_list = [i.text for i in h2_tags]
    h4_tag_list = [i.text for i in h4_tags]
    h3_tag_list = [i.text for i in h3_tags]
    anchor_tag_list = [i.text for i in anchor_tags]
    li_tag_list = [i.text for i in li_tags]
    span_tag_list = [i.text for i in span_tags]
    option_tag_list = [i.text for i in option_tags]
    address_tag_list = [i.text for i in address_tags]
    title_tag_list = [i.text for i in title_tags]
    desc_tag_list = [i.text for i in desc_tags]


    dict["p_tags"] = p_tag_list
    dict["h1_tag_list"] = h1_tag_list
    dict["h2_tag_list"] = h2_tag_list
    dict["h3_tag_list"] = h3_tag_list
    dict["h4_tag_list"] = h4_tag_list
    dict["anchor_tag_list"] = anchor_tag_list
    dict["li_tag_list"] = li_tag_list
    dict["span_tag_list"] = span_tag_list
    dict["option_tag_list"] = option_tag_list
    dict["address_tag_list"] = address_tag_list
    dict["title_tag_list"] = title_tag_list
    dict["desc_tag_list"] = desc_tag_list

    lst.append(dict)
    return JsonResponse(lst,safe=False)

def get_hiver_data(request):
    sentence_bundle = []
    p_tag_list=[]
    h1_tag_list=[]
    h2_tag_list=[]
    h3_tag_list=[]
    h4_tag_list=[]
    anchor_tag_list=[]
    li_tag_list = []
    span_tag_list = []
    option_tag_list = []
    address_tag_list = []
    title_tag_list = []
    desc_tag_list = []

    dict={}
    dict2={}
    lst = []
    r=requests.get("https://hiverhq.com/")
    c=r.content
    soup=BeautifulSoup(c,"html.parser")
    p_tags  =soup.find_all("p")
    h1_tags =soup.find_all("h1")
    h2_tags =soup.find_all("h2")
    h3_tags =soup.find_all("h3")
    h4_tags =soup.find_all("h4")
    anchor_tags =soup.find_all("a")
    li_tags =soup.find_all("li")
    span_tags =soup.find_all("span")
    option_tags = soup.find_all("option")
    address_tags = soup.find_all("address")
    title_tags = soup.find_all("title")
    desc_tags = soup.find_all("desc")


    p_tag_list = [i.text for i in p_tags]
    h1_tag_list = [i.text for i in h1_tags]
    h2_tag_list = [i.text for i in h2_tags]
    h4_tag_list = [i.text for i in h4_tags]
    h3_tag_list = [i.text for i in h3_tags]
    anchor_tag_list = [i.text for i in anchor_tags]
    li_tag_list = [i.text for i in li_tags]
    span_tag_list = [i.text for i in span_tags]
    option_tag_list = [i.text for i in option_tags]
    address_tag_list = [i.text for i in address_tags]
    title_tag_list = [i.text for i in title_tags]
    desc_tag_list = [i.text for i in desc_tags]


    def common_tag_validator(tag_list):
        temp_tags = []
        for i in tag_list:
            temp_tags.append(re.sub('[^A-Za-z0-9 ]+', '', i))
        tag_list = []
        tag_list = temp_tags
        tag_list = [i.strip() for i in tag_list]
        tag_list = [i for i in tag_list if i != ""]
        tag_list = [",".join(i.split(" ")) for i in tag_list]
        return tag_list

    p_tag_list = common_tag_validator(p_tag_list)
    h1_tag_list = [",".join(i.split(" ")) for i in h1_tag_list]
    h2_tag_list = [",".join(i.split(" ")) for i in h2_tag_list]
    h3_tag_list = [",".join(i.split(" ")) for i in h3_tag_list]
    h4_tag_list = common_tag_validator(h4_tag_list)
    anchor_tag_list = common_tag_validator(anchor_tag_list)
    li_tag_list = common_tag_validator(li_tag_list)
    address_tag_list = common_tag_validator(address_tag_list)
    title_tag_list = common_tag_validator(title_tag_list)
    option_tag_list = common_tag_validator(option_tag_list)


    dict["p_tags"] = p_tag_list
    dict["h1_tag_list"] = h1_tag_list
    dict["h2_tag_list"] = h2_tag_list
    dict["h3_tag_list"] = h3_tag_list
    dict["h4_tag_list"] = h4_tag_list
    dict["anchor_tag_list"] = anchor_tag_list
    dict["li_tag_list"] = li_tag_list
    dict["span_tag_list"] = span_tag_list
    dict["option_tag_list"] = option_tag_list
    dict["address_tag_list"] = address_tag_list
    dict["title_tag_list"] = title_tag_list
    dict["desc_tag_list"] = list(set(desc_tag_list))

    lst.append(dict)
    sentence_bundle = p_tag_list + h1_tag_list + h2_tag_list + h3_tag_list + h4_tag_list + anchor_tag_list + li_tag_list + span_tag_list + option_tag_list + address_tag_list + title_tag_list + list(set(desc_tag_list))
    res = []
    for i in sentence_bundle:
        res.extend(i.split(","))
    res = [i for i in res if i != ""]
    word_box = []
    for i in res:
        try:
            i = int(i)
        except ValueError:
            pass
        word_box.append(i)
    word_box = [i for i in word_box if not type(i) == int]
    word_box = {x:word_box.count(x) for x in word_box}
    occourances_of_word_desc = []
    for i,j in word_box.items():
        if j > 13:occourances_of_word_desc.append({i:j})
    # import operator
    # word_box = sorted(word_box.items(), key=operator.itemgetter(1))
    # word_box = word_box[-1::-5]
    # word_box = word_box[0:5]
    # word_box = [{i[0]:i[1]} for i in word_box]
    dict2["occourances_of_word_desc"] = occourances_of_word_desc
    return JsonResponse(dict2,safe=False)
