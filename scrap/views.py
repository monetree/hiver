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

    for i in p_tags:
        p_tag_list.append({"p":i.text})

    for i in h1_tags:
        h1_tag_list.append({"h1":i.text})

    for i in h2_tags:
        h2_tag_list.append({"h2":i.text})

    for i in h3_tags:
        h3_tag_list.append({"h3":i.text})

    for i in h4_tags:
        h4_tag_list.append({"h4":i.text})

    for i in anchor_tags:
        anchor_tag_list.append({"a":i.text})

    for i in li_tags:
        li_tag_list.append({"li":i.text})

    for i in span_tags:
        span_tag_list.append({"span":i.text})

    for i in option_tags:
        option_tag_list.append({"option":i.text})

    for i in address_tags:
        address_tag_list.append({"address":i.text})

    for i in title_tags:
        title_tag_list.append({"title":i.text})

    for i in desc_tags:
        desc_tag_list.append({"desc":i.text})


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

    for i in p_tags:
        p_tag_list.append(i.text)

    for i in h1_tags:
        h1_tag_list.append(i.text)

    for i in h2_tags:
        h2_tag_list.append(i.text)

    for i in h3_tags:
        h3_tag_list.append(i.text)

    for i in h4_tags:
        h4_tag_list.append(i.text)

    for i in anchor_tags:
        anchor_tag_list.append(i.text)

    for i in li_tags:
        li_tag_list.append(i.text)

    for i in span_tags:
        span_tag_list.append(i.text)

    for i in option_tags:
        option_tag_list.append(i.text)

    for i in address_tags:
        address_tag_list.append(i.text)

    for i in title_tags:
        title_tag_list.append(i.text)

    for i in desc_tags:
        desc_tag_list.append(i.text)

    p_tag_list_temp = []
    for i in p_tag_list:
        p_tag_list_temp.append(re.sub('[^A-Za-z0-9 ]+', '', i))
    p_tag_list = []
    p_tag_list = p_tag_list_temp
    p_tag_list = [i.strip() for i in p_tag_list]
    p_tag_list = [i for i in p_tag_list if i != ""]
    p_tag_list = [",".join(i.split(" ")) for i in p_tag_list]

    h1_tag_list = [",".join(i.split(" ")) for i in h1_tag_list]
    h2_tag_list = [",".join(i.split(" ")) for i in h2_tag_list]
    h3_tag_list = [",".join(i.split(" ")) for i in h3_tag_list]

    h4_tag_list_temp = []
    for i in h4_tag_list:
        h4_tag_list_temp.append(re.sub('[^A-Za-z0-9 ]+', '', i))
    h4_tag_list = []
    h4_tag_list = h4_tag_list_temp
    h4_tag_list = [i.strip() for i in h4_tag_list]
    h4_tag_list = [i for i in h4_tag_list if i != ""]
    h4_tag_list = [",".join(i.split(" ")) for i in h4_tag_list]

    anchor_tag_list_temp = []
    for i in anchor_tag_list:
        anchor_tag_list_temp.append(re.sub('[^A-Za-z0-9 ]+', '', i))
    anchor_tag_list = []
    anchor_tag_list = anchor_tag_list_temp
    anchor_tag_list = [i.strip() for i in anchor_tag_list]
    anchor_tag_list = [i for i in anchor_tag_list if i != ""]
    anchor_tag_list = [",".join(i.split(" ")) for i in anchor_tag_list]

    li_tag_list_temp = []
    for i in li_tag_list:
        li_tag_list_temp.append(re.sub('[^A-Za-z0-9 ]+', '', i))
    li_tag_list = []
    li_tag_list = li_tag_list_temp
    li_tag_list = [i.strip() for i in li_tag_list]
    li_tag_list = [i for i in li_tag_list if i != ""]
    li_tag_list = [",".join(i.split(" ")) for i in li_tag_list]

    address_tag_list_temp = []
    for i in address_tag_list:
        address_tag_list_temp.append(re.sub('[^A-Za-z0-9 ]+', '', i))
    address_tag_list = []
    address_tag_list = address_tag_list_temp
    address_tag_list = [i.strip() for i in address_tag_list]
    address_tag_list = [i for i in address_tag_list if i != ""]
    address_tag_list = [",".join(i.split(" ")) for i in address_tag_list]

    title_tag_list_temp = []
    for i in title_tag_list:
        title_tag_list_temp.append(",".join(i.split("|")))
    title_tag_list = []
    title_tag_list = title_tag_list_temp
    title_tag_list = [i.strip() for i in title_tag_list]
    title_tag_list = [i for i in title_tag_list if i != ""]
    title_tag_list = [",".join(i.split(" ")) for i in title_tag_list]

    option_tag_list_temp = []
    for i in option_tag_list:
        option_tag_list_temp.append(re.sub('[^A-Za-z]+', '', i))
    option_tag_list = []
    option_tag_list = option_tag_list_temp
    option_tag_list = [i.strip() for i in option_tag_list]
    option_tag_list = [i for i in option_tag_list if i != ""]
    option_tag_list = [",".join(i.split(" ")) for i in option_tag_list]


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
    import operator
    word_box = sorted(word_box.items(), key=operator.itemgetter(1))
    word_box = word_box[-1::-5]
    word_box = word_box[0:5]
    word_box = [{i[0]:i[1]} for i in word_box]
    dict2["occourances_of_word_desc"] = word_box
    return JsonResponse(dict2,safe=False)
