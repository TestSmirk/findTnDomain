import requests


# coding = utf-8
import requests

# with open("domain.txt") as f:
# print()
with open("domain.txt") as f:
    # print(f.readlines()," 1111")
    for i in f.readlines():
        # print(str(i).strip(),"11")
        findDoman = str(i).strip()

        url = "http://whois.ati.tn/index.php"

        payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"domain\"\r\n\r\n%s \r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"ext\"\r\n\r\n1\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"" \
                  "b_existe\"\r\n\r\nExiste3F\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW-- " %findDoman
        headers = {
            'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
            'cache-control': "no-cache",
            'postman-token': "0443e07f-be35-2c1f-c744-7036def84f87"
        }

        response = requests.request("POST", url, data=payload, headers=headers)


        print(findDoman, response.text.find("Nom Complet"))

        # open("result.txt", "a").writelines(findDoman + str(response.text.find("est libre pour l'instant."))+"\n")
