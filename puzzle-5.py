file = open('puzzle-5.txt')

rules = []
pages = []
for line in file:
    if ',' in line:
        pages.append(list(map(int, line.strip().split(','))))
    elif line.strip() != '':
        rules.append(list(map(int, line.strip().split('|'))))

def f(page):
    for rule in rules:
        if (rule[0] in page and rule[1] in page) and page.index(rule[0]) >= page.index(rule[1]):
            #print(rule)
            #print(page)
            return False
    return True

def reorder(unordered_page):
    page = unordered_page.copy()
    while(not f(page)):
        for rule in rules:
            if (rule[0] in page and rule[1] in page) and page.index(rule[0]) >= page.index(rule[1]):
                small_index = page.index(rule[0])
                high_index = page.index(rule[1])
                (page[small_index], page[high_index]) = (page[high_index], page[small_index])
    return page

correct_pages = []
incorrect_pages = []

for page in pages:
    if f(page):
        correct_pages.append(page[int(len(page)/2)])
    else:
        incorrect_pages.append(reorder(page)[int(len(page)/2)])
    
print(sum(correct_pages))
print(sum(incorrect_pages))