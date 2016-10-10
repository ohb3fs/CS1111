# Olivia Bicks ohb3fs

import urllib.request
import re


def find_emails_in_website(url):
    email_list = []
    stream = urllib.request.urlopen(url)
    for line in stream:
        decoded = line.decode("UTF-8")
        decoded = decoded.replace("NOSPAM", "")
        link_regex = re.compile('<a\s*href=[\'|"](.*?)[\'"].*?>')
        normal_email_regex = re.compile(r"([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+(\.[a-zA-Z]{2,}))")
        mo = normal_email_regex.findall(decoded)
        if mo is not None:
            for item in mo:
                match = item[0]
                email_list.append(match)
        links = link_regex.findall(decoded)
        for link in links:
            mo = normal_email_regex.search(link)
            if mo is not None:
                email_list.append(mo.group())
        no_at_regex = re.compile(r"([a-zA-Z0-9._%+-]+ \bat\b [a-zA-Z0-9.-]+(\.[a-zA-Z]{2,}))")
        mo_1 = no_at_regex.search(decoded)
        if mo_1 is not None:
            at_sign = re.sub(r"( \bat\b )", "@", mo_1.group())
            email_list.append(at_sign)
        no_at_or_dot_regex = re.compile(r"([a-zA-Z0-9._%+-]+ \bat\b [a-zA-Z0-9.-]+ \bdot\b [a-zA-Z]{2,})")
        mo_2 = no_at_or_dot_regex.search(decoded)
        if mo_2 is not None:
            at_sign = re.sub(r"( \bat\b )", "@", mo_2.group())
            dot_sign = re.sub(r"( \bdot\b )", ".", at_sign)
            email_list.append(dot_sign)
        parentheses_regex = re.compile(r"([a-zA-Z0-9._%+-]+ ?\(\bat\b\) ?[a-zA-Z0-9.-]+ ?\(\bdot\b\) ?[a-zA-Z]{2,})")
        mo_3 = parentheses_regex.search(decoded)
        if mo_3 is not None:
            at_parenthesis = re.sub(r"( ?\(?\bat\b\)? ?)", "@", mo_3.group())
            dot_parenthesis = re.sub(r"( ?\(?\bdot\b\)? ?)", ".", at_parenthesis)
            email_list.append(dot_parenthesis)
        multiple_dots_regex = re.compile(r"([a-zA-Z0-9._%+-]+ \bdot\b [a-zA-Z0-9._%+-]+ \bat\b [a-zA-Z0-9.-]+ \bdot\b "
                                         r"[a-zA-Z]{2,})")
        mo_4 = multiple_dots_regex.search(decoded)
        if mo_4 is not None:
            at_parenthesis = re.sub(r"( ?\(?\bat\b\)? ?)", "@", mo_4.group())
            dot_parenthesis = re.sub(r"( ?\(?\bdot\b\)? ?)", ".", at_parenthesis)
            email_list.append(dot_parenthesis)
        for item in email_list:
            if email_list.count(item) > 1:
                index = email_list.index(item)
                email_list.pop(index)
            if item == "initial@virginia.edu":
                index = email_list.index(item)
                email_list.pop(index)
    return email_list


