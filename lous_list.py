# Olivia Bicks ohb3fs
import urllib.request


def instructors(department):
    professors = []
    link = "http://stardock.cs.virginia.edu/louslist/Courses/view/" + department
    stream = urllib.request.urlopen(link)
    for line in stream:
        data = line.strip().decode("UTF-8")
        course = data.split(";")
        teacher = course[4]
        if teacher not in professors:
            professors.append(teacher)
    professors = sorted(professors)
    return professors


def class_search(dept_name, has_seats_available=True, level=None, not_before=None, not_after=None):
    link = "http://stardock.cs.virginia.edu/louslist/Courses/view/" + dept_name
    stream = urllib.request.urlopen(link)
    classes = []
    for line in stream:
        data = line.strip().decode("UTF-8")
        course = data.split(";")
        total = 4
        if has_seats_available is True and int(course[15]) >= int(course[16]):
            total -= 1
        if level is not None:
            level = str(level)
            if course[1][0] != level[0]:
                total -= 1
        if not_before is not None:
            if int(course[12]) < not_before:
                total -= 1
            if int(course[12]) == -1:
                total -= 1
        if not_after is not None and (int(course[12]) > not_after or int(course[12]) == -1):
            total -= 1
        if total == 4:
            classes.append(course)
    return classes








