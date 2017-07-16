# coding = utf-8
import requests
import os, sys

nextLine = "\n"
try:
    whichFile = sys.argv[2]
except:
    print("except")
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
        keyWord = "没有被注册，立即抢先注册"
        url = "https://www.quyu.net/domainchecker.php"
        payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data;" \
                  " name=\"token\"\r\n\r\nf1c27e743b116b1fe26081ea11d1d2a1bf80c6fe\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\n" \
                  "Content-Disposition: form-data; name=\"domain\"\r\n\r\n%s\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW" \
                  "\r\nContent-Disposition: form-data; name=\"tlds[]\"\r\n\r\n.%s\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--" \
                  % (findDoman, lastKey)
        headers = {
            'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
            'cache-control': "no-cache",
            'postman-token': "05d6797c-313c-d1e0-d39f-8ae53bc6dbd5"
        }
        response = requests.request("POST", url, data=payload, headers=headers)
        print(findDoman + lastKey + str(response.text.find(keyWord)))
        file.writelines(findDoman + lastKey + str(response.text.find(keyWord)))
        file.write("\n")
