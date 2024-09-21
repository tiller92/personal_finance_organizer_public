# take an array of transactions with price and locations and return dic with arrays


#make categorys insert locations as they come up
# this needs to take an array need to append huntington data before this poitn
# return an dict with catogorized arrays
expenses_categorys = {
'grocery' : ["Kroger","Gaint Eagle", "Costco"],
'restaurants' : ["Osuwmc Bistroh Uhe","Cpp*grandad's Pizza Ii","Chipotle","The Dk Diner Caterers T","Rc Vending","Osuwmc Bistroh Uh"],
'venmo': ["venmo", "PURCHASE VENMO *CAROLYN CARNEY"],
'coffee': ["Grind","Dunkin","Dunkin #362968","Starbucks"],
'gas' : ["Get Go #3539","BP"],
'car' : [],
'rent' : ["PURCHASE APF*METROPOLITAN HOLDI"],
'trasportation' : [],
'bills':["AT&T","Nationwide Energy Partners"],
'misc': [],
'poker' : [],
'Amazon' : ["Amazon"], 
'subscriptions' : ["PURCHASE GRANDVIEW PRO FITNESS","Brave.com","Amazon Prime","Netflix","Whoop Great Brita", "Gtowizard.com"],
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
'bills':[],
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





