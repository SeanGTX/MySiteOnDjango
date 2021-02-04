models_file = open('VkLinkBrowser/apps/Browser/models.py', 'r').readlines()
models = models_file[34:-1]
models_name = []
for i in range(len(models)):
    if 'class' in models[i]:
        a = models[i].split(' ')
        a = a[1].split('(')
        models_name.append(a[0])

print('Список доступных пабликов для удаления:')
for i in range(len(models_name)):
    print(models_name[i])
print()
dead_public = str(input('Введите название паблика, который хотите удалить:'))
