# coding = utf-8
import requests

# with open("domain.txt") as f:
# print()
with open("domain.txt") as f:
    # print(f.readlines()," 1111")
    for i in f.readlines():
        # print(str(i).strip(),"11")
        url = "https://www.localhost.tn/clients/cart.php"
        querystring = {"a": "add", "domain": "register"}
        findDoman = str(i).strip()
        payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\n" \
                  "Content-Disposition: form-data; name=\"token" \
                  "\"\r\n\r\ndcaddbf94cc52f1612d93e0628ea43ce603426b0\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW" \
                  "\r\nContent-Disposition: form-data; name" \
                  "=\"sld\"\r\n\r\n%s\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"tld\"\r\n\r\n.tn\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--" % findDoman
        headers = {
            'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
            'cache-control': "no-cache",
            'postman-token': "950d5982-8822-71a2-0aa9-9a9d4658a4fa"
        }
        response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

        print(findDoman, response.text.find("Disponible! Commander maintenant"))

        open("result.txt", "a").writelines(findDoman + str(response.text.find("Disponible! Commander maintenant"))+"\n")
