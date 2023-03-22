import pandas as pd

df1= pd.read_json(r'C:\Users\HP\Dropbox\PC\Desktop\football\players\players\williams_data.json')

df2=pd.read_json(r'C:\Users\HP\Dropbox\PC\Desktop\football\football\football\player_links.json')
target_links=[]
list_=df1['id'].values.tolist()
list_2 = df2['link'].values.tolist()



for counter,i in enumerate(list_):
    for j in list_2[0:300]:
        if str(i)  not in j:
            print(counter)
            target_links.append(j)
      

pd.DataFrame(target_links).to_csv('links.csv')

#scrapy crawl somespider -s JOBDIR=crawls/somespider-1