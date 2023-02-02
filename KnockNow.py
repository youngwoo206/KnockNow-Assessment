import json
f = open('sample.json')
listingData = json.load(f)


def find_latest_listings(data: dict) -> list:
    '''
    find_latest_listings(dic) -> list

    Takes listing data from imported JSON file, returns listing numbers of
    most recent listings of each property
    '''

    listingsMap = {}

    for i in data["Listings"]:

        if i['address'] not in listingsMap.keys():
            listingsMap[i['address']] = (i['date'], i['listing'])
        else:
            if i['date'] > listingsMap[i['address']][0]:
                listingsMap[i['address']] = (i['date'], i['listing'])

    output = listingsMap.values()

    return [i[1] for i in output]


print(find_latest_listings(listingData))
