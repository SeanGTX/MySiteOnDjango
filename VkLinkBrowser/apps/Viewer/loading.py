import vk_api.tools
from tqdm import tqdm
import sys


vk_session = vk_api.VkApi('79996002174', '128256512102420484096QWEasdfZXCmegboyZZ')
vk_session.auth()
vk = vk_session.get_api()

a = vk.groups.getMembers(group_id='empire_pva', count=1000)

VkPublic = []

num = a['count'] // 1000
init = tqdm(range(num), ncols=100, desc='Создание списка')
for i in init:
    VkPublic += a['items']
    a = vk.groups.getMembers(group_id='empire_pva', count=1000,  offset=(i + 1) * 1000)
    init.clear()
init = 1

print(sys.getsizeof(VkPublic))
print(len(VkPublic))
print(VkPublic)

