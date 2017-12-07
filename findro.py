# coding = utf-8
import requests
import os, sys

nextLine = "\n"
try:
    whichFile = sys.argv[2]
except:
    whichFile = ""
if len(whichFile) == 0:
    print("没有输入文件名,默认采用domain.txt\n no input filename,use default file domain.txt")
    whichFile = "domain.txt"
lastKey = sys.argv[1]
file = open(lastKey + "_result.txt", "a")
with open(whichFile) as f:
    print(sys.argv[1])
    for i in f.readlines():
        findDoman = str(i).strip()
        keyWord = "is available!"

        url = "https://www.m247.ro/portal/cart.php"

        querystring = {"a": "add", "domain": "register", "currency": "1", "language": "english", "sld": findDoman,
                       "tld": ".ro"}

        headers = {
            'Cache-Control': "no-cache",
            'Postman-Token': "ea4c32cf-048b-bbed-6460-084e33868a73"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)

        print(response.text)
        print(findDoman + "_______________"+lastKey + str(response.text.find(keyWord)))
        file.writelines(findDoman + lastKey + str(response.text.find(keyWord)))
        file.write("\n")
