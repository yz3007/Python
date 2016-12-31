from BeautifulSoup import *
from urllib import *


html = urlopen('file:///Users/zhaox694/Desktop/pokemon.html').read()

soup = BeautifulSoup(html)

#print(soup.prettify())  #print neat html format

#print soup.title
# print soup.title.string



#
# for item in soup.findAll('a'):
#     if item.get('title') is not None:
#         print item.get('title')


file = open('/Users/zhaox694/Desktop/pokemon.txt','w')



# method 1
name = list()
for i in soup.findAll('tr', style = 'background:#FFF'):
    value = i.findAll('a')[0]
    name.append(value['title'].encode('utf-8'))

#print 'Number:', len(name), name


# method_2
# name = list()
#
# for i in soup.findAll('tr', style = 'background:#FFF'):
#     name.append(i.findAll('a')[1].string)


for i in name:
    i += ' '
    file.write(i)

# we can also use string method to process the info
#a =  str(i[0].findAll('a')[1])


file.close()