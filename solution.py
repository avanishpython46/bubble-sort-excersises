def bubblesort(my_list,key):
    if key=='transaction_amount':
        for i in my_list:
            for x in  range(len(my_list)-1):
                if my_list[x]['transaction_amount'] > my_list[x+1]['transaction_amount']:
                    my_list[x],my_list[x+1] = my_list[x+1],my_list[x]
        for i in elements:
            print(i)
    if key=="name":
        for dic in my_list:
            for i in range(len(my_list)-1):
                if my_list[i]["name"] > my_list[i+1]["name"]:
                    my_list[i],my_list[i+1] = my_list[i+1],my_list[i]
        for a in my_list:
            print(a)
elements = [
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
    ]
bubblesort(elements,key="transaction_amount")
        
