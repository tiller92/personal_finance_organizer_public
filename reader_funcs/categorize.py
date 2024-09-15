# take an array of transactions with price and locations and return dic with arrays


#make categorys insert locations as they come up
# this needs to take an array need to append huntington data before this poitn
# return an dict with catogorized arrays
expenses_categorys = {
'grocery' : ["Kroger","Gaint Eagle", "Costco"],
'restaurants' : ["Osuwmc Bistroh Uhe"],
'venmo': ["venmo"],
'coffee': ["Grind","Dunkin"],
'gas' : [],
'car' : [],
'rent' : [],
'trasportation' : [],
'misc': [],
'poker' : [],
'Amazon' : [], 'subscriptions' : [],
}

categorized_trans = {
'grocery' : [],
'restaurants' : [],
'venmo': [],
'coffee': [],
'gas' : [],
'car' : [],
'rent' : [],
'trasportation' : [],
'misc': [],
'poker' : [],
'Amazon' : [],
'subscriptions' : [],
}


def cate_transactions(trans_arr):
#    trans_len = len(trans_arr)
#    test_count = 0
    for i in range(0, len(trans_arr)):
        found = False 
        for category, locations in expenses_categorys.items():
            for j in range(0,len(locations)):
                if locations[j] == trans_arr[i][1]:
                    categorized_trans[category].append(trans_arr[i][0])
#                    test_count = test_count +1
                    found = True
        if found == False:
            categorized_trans['misc'].append(trans_arr[i][0])
#            test_count = test_count +1
#    print(trans_len, test_count)
    return categorized_trans 





