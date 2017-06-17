import requests

# coding = utf-8
import requests
import os,sys
nextLine = "\n"
with open("domain.txt") as f:
    print(sys.argv[1])
    for i in f.readlines():
        findDoman = str(i).strip()

        keyWord = "没有被注册，立即抢先注册"
        lastKey = sys.argv[1]
        url = "https://www.quyu.net/domainchecker.php"

        payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data;" \
                  " name=\"token\"\r\n\r\n461279b9dfb1fb04bd46423d9730a590c1c2a35a\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\n" \
                  "Content-Disposition: form-data; name=\"domain\"\r\n\r\n%s\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW" \
                  "\r\nContent-Disposition: form-data; name=\"tlds[]\"\r\n\r\n.%s\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--" \
                  % (findDoman, lastKey)
        headers = {
            'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
            'cache-control': "no-cache",
            'postman-token': "05d6797c-313c-d1e0-d39f-8ae53bc6dbd5"
        }
        response = requests.request("POST", url, data=payload, headers=headers)
        print(findDoman, lastKey, response.text.find(keyWord))
        file = open(lastKey + "_result.txt", "a")
        file.writelines(findDoman + lastKey + str(response.text.find(keyWord)) )
        file.write("\n")

