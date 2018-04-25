import urllib.request
import urllib.parse

# 1st tutorial
# x = urllib.request.urlopen('https://www.google.com/')# url for request
# print(x.read()) #this will read all data in url page
    #2nd tutorial
# url = 'https://www.utopia.pk/search' #url to access
# values = {'q' : 'python programming tutorials'}
# data = urllib.parse.urlencode(values) # encoding values which is in dict key-value pair
# data = data.encode('utf-8') # data should be bytes // encoding in utf-8
# req = urllib.request.Request(url, data) # combining  encoded query(data) with url i.e. https://www.google.com/search?q=python+programming+tutorials
# resp = urllib.request.urlopen(req)
# respData = resp.read()
#print(respData)
        #3rd tutorial
# try:
#     x = urllib.request.urlopen('https://www.google.com/search?q=test')
#     #print(x.read())

#     saveFile = open('noheaders.txt','w')
#     saveFile.write(str(x.read()))
#     saveFile.close()
# except Exception as e:
#     print(str(e))

#       4th tutorial Accessing data as a web brower
try:
    url = 'https://www.google.com/search?q=python'

    # now, with the below headers, we defined ourselves as a simpleton who is
    # still using internet explorer.
    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
    req = urllib.request.Request(url, headers = headers)
    resp = urllib.request.urlopen(req)
    respData = resp.read()
    print(respData)

    saveFile = open('withHeaders.txt','w')
    saveFile.write(str(respData))
    saveFile.close()
except Exception as e:
    print(str(e))