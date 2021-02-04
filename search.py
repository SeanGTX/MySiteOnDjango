import vk_api.tools
import sqlite3
import os
from tqdm import tqdm
import sys
import time

vk_session = vk_api.VkApi('79996002174', '128256512102420484096QWEasdfZXCmegboyZZ')
vk_session.auth()
vk = vk_session.get_api()

VkPublicName = str(input('Ссылка на паблик: '))
VkPublic_temp = []
VkPublic = []

try:
    VkPublic_temp = vk.groups.getMembers(group_id=VkPublicName, count=1000)
except vk_api.exceptions.ApiError:
    print('Паблик не найден')
    exit(0)

VkPublicMembers = VkPublic_temp['count']
VkPublicMembers_Thousands = VkPublicMembers // 1000 + 1

conn = sqlite3.connect("db.sqlite3")
cursor = conn.cursor()


def modelExists(model):
    model_check = open('VkLinkBrowser/apps/Browser/models.py', 'r').readlines()
    if 'class ' + model + '(Public):\n' in model_check:
        return True
    else:
        return False


if not modelExists(VkPublicName):
    models = open('VkLinkBrowser/apps/Browser/models.py', 'a')
    models.write('class ' + VkPublicName + '(Public):\n')
    models.write('  pass\n')
    models.write('\n')
    models.close()
    os.system("python manage.py makemigrations")
    os.system("python manage.py migrate")
    cursor.execute("CREATE TABLE Browser_" + VkPublicName)
    cursor.execute("SELECT * FROM Browser_" + VkPublicName)
else:
    cursor.execute("SELECT * FROM Browser_" + VkPublicName)

year = 0


def recordExists(VKLink=str()):
    global VkPublicName
    VKLink = "'https://vk.com/" + VKLink + "'"
    SQLite_request = "SELECT * FROM Browser_" + VkPublicName + " WHERE VKLink=" + VKLink
    records = cursor.execute(SQLite_request)
    recordsValues = records.fetchall()
    if len(recordsValues) >= 1:
        return True
    else:
        return False


def fitGirl(Girl=dict):
    global year
    if 'bdate' in Girl:
        if len(Girl['bdate'].split('.')[-1]) == 4:
            year = int(Girl['bdate'].split('.')[-1])
        else:
            year = 2001
    return ('deactivated' not in Girl) and (Girl['is_closed'] != True) and (
            Girl['sex'] == 1) and (year >= 2000) and (
                   (('relation' in Girl) and (Girl['relation'] in [0, 6, 1])) or ('relation' not in Girl)) and (
                   (('city' in Girl) and (Girl['city']['id'] == 23)) or ('city' not in Girl))


id = 1

init = tqdm(range(VkPublicMembers_Thousands), ncols=100, desc='Создание списка ползователей ' + VkPublicName)

x = 0
for i in init:
    VkPublic += VkPublic_temp['items']
    VkPublic_temp = vk.groups.getMembers(group_id=VkPublicName, count=1000, offset=(x + 1) * 1000)
    x += 1
init.close()

print('Готово!')

time.sleep(1)

init = tqdm(range(len(VkPublic)), ncols=100, desc='Поиск подходящих пользователей ' + VkPublicName)

for i in init:
    girl = vk.users.get(user_id=VkPublic[i], fields=['sex', 'bdate', 'screen_name', 'city', 'relation'])[0]
    if fitGirl(girl) and not recordExists(girl['screen_name']):
        SQLite_request_add = (id, girl['first_name'], girl['last_name'], 'https://vk.com/' + girl['screen_name'])
        cursor.execute("INSERT INTO Browser_" + VkPublicName + " VALUES (?,?,?,?)", SQLite_request_add)
        conn.commit()
        id += 1
