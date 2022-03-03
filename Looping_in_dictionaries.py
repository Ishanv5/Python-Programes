user_info={
    'Name':'Ishan Vaghela',
    'age':18,
    'Fav_movies':['Spiderman','Dr Strange'],
    'fav_tunes':['fariy tales','let me down slowly']
}

if 'Name' in user_info:
    print("Present")
else:
    print("Not Present")
    
if 'Ishan Vaghela' in user_info.values():
    print("Present")
else:
    print("Not Present")
    
for i in user_info:
    print(i)
for i in user_info.values():
    print(i)
    
    
    # **************** Item method ***********
    
    user_items=user_info.items()
    print(user_items)
    print(type(user_items))