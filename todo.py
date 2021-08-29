import sqlite3
from bottle import route, run, debug, template
import pandas as pd
import requests
import bs4

#STUFF
#region
query1 = "SELECT id, task FROM todo WHERE status LIKE '0' OR '1'"
list1 = [['one', 'two', 'three'],[1,2,3],[4,5,6],[1,12312,98080],[324,1231,123]]
print('reading data, please wait...')
excel_file_path = r'C:\storage\data\data.xlsx'
df = pd.read_excel(excel_file_path)
df = df.sort_values(by=['Change'], ascending=False)
print('done reading data')
list2 = df.values.tolist()
x = df.columns
y = x.tolist()
list3 = [y] + list2
#endregion

# SOUP
#region
wikiurl="https://en.wikipedia.org/wiki/List_of_cities_in_India_by_population"
table_class="wikitable sortable jquery-tablesorter"
response=requests.get(wikiurl)
soup = bs4.BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find('table',{'class':"wikitable"})
df1=pd.read_html(str(indiatable))
# convert list to dataframe
df1=pd.DataFrame(df[0])
listw = df1.values.tolist()
x = df1.columns
y = x.tolist()
listwiki = [y] + listw

#endregion


@route('/todo')
def todo_list():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute(query1)
    result = c.fetchall()
    c.close()
    output = template(r'C:\Users\jason\OneDrive\Documents\GitHub\test-bottle\make_table.tpl', rows=result)
    return output

@route('/testing')
def tezt():
    output = template(r'C:\Users\jason\OneDrive\Documents\GitHub\test-bottle\make_table.tpl', rows=list1)
    return output

@route('/pandas')
def tezt():
    output = template(r'C:\Users\jason\OneDrive\Documents\GitHub\test-bottle\make_table.tpl', rows=list3)
    return output

@route('/soup')
def tezt():
    output = template(r'C:\Users\jason\OneDrive\Documents\GitHub\test-bottle\make_table.tpl', rows=listwiki)
    return output

debug(True)
run(reloader=True)

run()