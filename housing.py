import csv
from bs4 import BeautifulSoup
import urllib

def get_uni(uni):
    url = "https://directory.columbia.edu/people/uni?code=" + uni
    r = urllib.urlopen(url).read()
    soup = BeautifulSoup(r)
    return str(soup.find_all("th", colspan="4")[0]).split(">")[1].split("<")[0]


with open('data.csv', 'rb') as f:
    reader = csv.reader(f)
    arr = list(reader)

# first lotto number is 25 this year
lotto = 25
weight = 30.0
count = 0
maxcount = 0;
names = []
curr = []

group1 = []
group2 = []
group3 = []
group4 = []
group5 = []
group6 = []
group7 = []
group8 = []

map = {1:group1, 2:group2, 3:group3, 4:group4, 5:group5, 6:group6, 7:group7, 8:group8}
# print data
for elem in arr:
    
    # to know its not broken (doesnt need to be there)
    print elem

    # new group
    if lotto != elem[3]:
        if count > 0:
            group = map[count]
            curr = [names, weight, lotto]
            group.append(curr)
        count = 0
        names = []
        weight = elem[2]
        lotto = elem[3]

    names.append(get_uni(elem[0]))
    count += 1


# do for last one
if count > 0:
    group = map[count]
    curr = [names, weight, lotto]
    group.append(curr)
count = 0
names = []
weight = elem[2]
lotto = elem[3]

print "COMPLETE \n"

print "1: "
print group1
print "2: "
print group2
print "3: "
print group3
print "4: "
print group4
print "5: "
print group5
print "6: "
print group6
print "7: "
print group7
print "8: "
print group8

output1 = []
output2 = []
output3 = []
output4 = []
output5 = []
output6 = []
output7 = []
output8 = []
output_map = {1:output1, 2:output2, 3:output3, 4:output4, 5:output5, 6:output6, 7:output7, 8:output8}

# print formatting
for a in range(0, 8):
    group_num = a + 1;
    group = map[group_num]
    output = output_map[group_num]
    file = "group" + str(group_num) + ".csv"

    for x in range(0, len(group)):
        elem = group[x]
        for i in range(0, len(elem[0])):
            name = elem[0][i]
            if i == 0:
                output.append([x + 1, name, elem[1], elem[2]])
            else:
                output.append([" ", name, " ", " "])
    with open(file, 'w') as fp:
        a = csv.writer(fp, delimiter=',')
        data = output
        a.writerows(data)




