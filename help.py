    def common_tag_validator(tag_list):
        temp_tags = []
        for i in tag_list:
            temp_tags.append(re.sub('[^A-Za-z0-9 ]+', '', i))
        tag_list = []
        tag_list = temp_tags
        tag_list = [i.strip() for i in tag_list]
        tag_list = [i for i in tag_list if i != ""]
        tag_list = [",".join(i.split(" ")) for i in tag_list]


    p_tag_list= common_tag_validator(p_tag_list)
    h1_tag_list = [",".join(i.split(" ")) for i in h1_tag_list]
    h2_tag_list = [",".join(i.split(" ")) for i in h2_tag_list]
    h3_tag_list = [",".join(i.split(" ")) for i in h3_tag_list]
    h4_tag_list = common_tag_validator(h4_tag_list)
    anchor_tag_list = common_tag_validator(anchor_tag_list)
    li_tag_list = common_tag_validator(li_tag_list)
    address_tag_list = common_tag_validator(address_tag_list)
    title_tag_list = common_tag_validator(title_tag_list)
    option_tag_list = common_tag_validator(option_tag_list)
