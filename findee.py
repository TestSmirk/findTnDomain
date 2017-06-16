import requests

# coding = utf-8
import requests
import os,sys
# with open("domain.txt") as f:
nextLine = "\n"
# print()
with open("domain.txt") as f:
    # print(f.readlines()," 1111")
    print(sys.argv[1])
    for i in f.readlines():
        # print(str(i).strip(),"11")
        findDoman = str(i).strip()

        keyWord = "没有被注册，立即抢先注册"
        lastKey = sys.argv[1]
        # url = "http://whois.ati.tn/index.php"
        #
        # payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"domain\"\r\n\r\n%s \r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"ext\"\r\n\r\n1\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"" \
        #           "b_existe\"\r\n\r\nExiste3F\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW-- " %findDoman
        # headers = {
        #     'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
        #     'cache-control': "no-cache",
        #     'postman-token': "0443e07f-be35-2c1f-c744-7036def84f87"
        # }
        #
        # response = requests.request("POST", url, data=payload, headers=headers)
        #
        #
        # print(findDoman, response.text.find("Nom Complet"))

        # open("result.txt", "a").writelines(findDoman + str(response.text.find("est libre pour l'instant."))+"\n")






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

