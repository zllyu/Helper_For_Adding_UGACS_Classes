from requests_html import HTMLSession
import csv

# Define output info and formats
f = open('CsClassForUGA.csv', 'w', encoding='utf-8')
csv_writer = csv.writer(f)
csv_writer.writerow(["Course Number", "Course Name", "Requirements"])

url_class_navi = 'https://cs.uga.edu/courses/graduate'
session = HTMLSession()
r_class_navi = session.get(url_class_navi)

class_number_list = []

for i in range(1, 106):  # Only crawl top 104 courses
    sel = '#block-gold-mainpagecontent > div > div > div > div > div:nth-child(' + str(i) + \
          ') > div > div.views-field.views-field-field-course-name > h2 > a'
    articleElement = str(r_class_navi.html.find(sel, first=True).absolute_links).split('/')[-1][:-2]
    url_class_detail = 'https://cs.uga.edu/courses/content/' + articleElement
    r_class_detail = session.get(url_class_detail)
    sel2 = '#block-gold-mainpagecontent > div > article > div > div.cmp-heading-3 > div'
    sel3 = '#block-gold-mainpagecontent > div > article > div > div:nth-child(4) > div.field_multiple'
    articleElement2 = r_class_detail.html.find(sel2, first=True)
    articleElement3 = r_class_detail.html.find(sel3, first=True)
    csv_writer.writerow([articleElement, articleElement2.text, articleElement3.text])



