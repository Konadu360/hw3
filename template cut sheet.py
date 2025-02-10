import pandas as pd, numpy as np
data=pd.read_csv('southAGIBSSB.csv')
# print(type(data))
cut_sheet=pd.DataFrame({})
lista=[]
finish=[]
ports=np.array(data['Port Name'])
# cut_sheet['Client CLEI']=ports
for i in ports:
   lista.append(i.split()[0])
   finish.append(i.split()[1])
print(lista,finish)
cut_sheet['Client CLEI']=lista
cut_sheet['Client Port']=finish
# for index, column in data.iterrows():
#     for i in column['Port Name'].split():


    # for i in new:
    # lista.append(new.split())
    
    # cut_sheet[new[0]]=new[1]
 
    # df=pd.DataFrame(cut_sheet.items(), columns=['Client CLEI','Client Port'])
    
    # cut_sheet['Client CLEI']=new[0]
    # cut_sheet['Client Port']=new[1]
# print(lista)
# final={}
# for i in lista:
#     cut_sheet.setdefault(i,1)
#         # print(i)
# #     new=i.split()
print(cut_sheet)

sheet={'kofi':'1', 'kwame':'2', 'kwadwo':'3', 'kky':'4'}
sheep={'kwame':'2', 'kofi':'1', 'kky':'4', 'kwadwo':'3'}
shee=['kofi', 'kwame', 'kwadwo', 'kky', 'kk']
shee1=['kwame','kofi', 'kwadwo', 'kky', 'kk']
kee='wirimxks'
gee='wirimxkq'
print(sheep==sheet)
print(gee==kee)
print(sheet.values())



    
