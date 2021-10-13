import requests
import json
import webbrowser
import csv
import datetime
import pyautogui

previousLink = ""
#webbrowser.open_new('https://marketplace.axieinfinity.com/axie/')
enableBuyLink = True

def fetchPrice():
    responseData = []
    url = "https://graphql-gateway.axieinfinity.com/graphql"

    payload = "{\r\n  \"operationName\": \"GetAxieLatest\",\r\n  \"variables\": {\r\n    \"from\": 0,\r\n    \"size\": 1,\r\n    \"sort\": \"PriceAsc\",\r\n    \"auctionType\": \"Sale\",\r\n    \"criteria\": {}\r\n  },\r\n  \"query\": \"query GetAxieLatest($auctionType: AuctionType, $criteria: AxieSearchCriteria, $from: Int, $sort: SortBy, $size: Int, $owner: String) {  axies(auctionType: $auctionType, criteria: $criteria, from: $from, sort: $sort, size: $size, owner: $owner) {    total    results {      ...AxieRowData      __typename    }    __typename  }}fragment AxieRowData on Axie {  id name  breedCount auction {    ...AxieAuction    __typename  }  __typename}fragment AxieAuction on Auction {  currentPriceUSD  }\"\r\n  \r\n}"
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        }

    response = requests.request("POST", url, data=payload, headers=headers)
    json_obj = json.loads(response.text)
    price = float(json_obj['data']['axies']['results'][0]['auction']['currentPriceUSD'])
    print(price)
    if price<50:
        id = json_obj['data']['axies']['results'][0]['id']
        #responseData.append(id)
        link = 'https://marketplace.axieinfinity.com/axie/'+id
        global previousLink
        print(previousLink)
        print(link)
        if link == previousLink:
            print("same link")
            
        else:
            webbrowser.open_new(link)
            previousLink = link
            global enableBuyLink
            for number in range(30):
                pyautogui.moveTo(1495, 279)
                pyautogui.click()
                #pyautogui.moveTo(1095, 279)
                
while(True):
    try:
        fetchPrice()
        # with open('log.csv', 'w', encoding='UTF8', newline='') as f:
        #     writer = csv.writer(f)
        #     writer.writerows(responseData)
    except Exception as e:
        print(e)
        continue    # otherwise, try again
    