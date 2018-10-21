import os.path, json, re

def getSize(filename):
    st = os.stat(filename)
    return st.st_size

# constants
filename = 'syberia_land-v1.2-20181013-1614-OFFICIAL.zip'
zip_path = '/home/weritos94/weritos/Syberia/out/target/product/land/'
changelog = "changelog.txt"
developer = 'Weritos'
website_url = r'http://syberiaos.com'
news_url = r'http://github.com/syberia-project'
url= r'https://downloads.sourceforge.net/project/syberiaos/Land/syberia_land-v1.2-20181013-1614-OFFICIAL.zip?r=https%3A%2F%2Fsourceforge.net%2Fprojects%2Fsyberiaos%2Ffiles%2FLand%2Fsyberia_land-v1.2-20181013-1614-OFFICIAL.zip%2Fdownload&ts=1539459328'
error = 'false'
developer_url = r'http://github.com/syberia-project'
donate_url = r'https://syberiaos.com/links'
forum_url = r'https://forum.xda-developers.com/xiaomi-redmi-3s/development/9-0-syberia-os-9-0-t3837103'

ota_data = {}
md5file = zip_path + filename + ".md5sum"

# generate addons nested dict
addons = {'addons':[]}
tmp_addons1 = {}
tmp_addons2 = {}
tmp_addons1['title'] = 'Magisk'
tmp_addons1['summary'] = 'Magisk'
tmp_addons1['url'] = r'"http://tiny.cc/latestmagisk'
tmp_addons2['title'] = 'Magisk'
tmp_addons2['summary'] = 'Magisk Uninstaller'
tmp_addons2['url'] = r'http://tiny.cc/latestuninstaller'
addons.get ('addons').append(tmp_addons1)
addons.get ('addons').append(tmp_addons2)

# read some data from files
raw_changelog = open(changelog,'r', encoding='cp866').read()
raw_md5 = open(md5file,'r', encoding='cp866').readline()
build_date = re.search(r"\b\d{8}\b", filename).group(0)
device = re.search(r"syberia_([^-]*)",filename).group(1)
md5 = raw_md5.rsplit(None, 1)[0]
# fill json struct

ota_data=addons
ota_data['filename'] = filename
ota_data['changelog'] = raw_changelog
ota_data['filesize'] = str(getSize(zip_path+filename))
ota_data['md5'] = md5;
ota_data['build_date'] = build_date
ota_data['device'] = device
ota_data['url'] = url + device + r'/'+ filename
ota_data['donate_url'] = donate_url
ota_data['developer_url'] = developer_url
ota_data['news_url'] = news_url
ota_data['developer'] = developer
ota_data['error'] = error
ota_data['website_url'] = website_url
ota_data['forum_url'] = forum_url
print('Writting json data to ' + device+'.json')
with open(device+'.json', 'w') as f:
  json.dump(ota_data, f, ensure_ascii=False)
