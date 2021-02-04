from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
from Browser.models import *

i = 1
CurPublic = ''


def viewer(request, Public_id):
    global CurPublic
    global i
    if CurPublic != Public_id:
        i = 1

    GirlTable = globals()[Public_id]

    UserRecord = GirlTable.objects.get(id=i).getListOfRecord()

    Username = UserRecord[0] + ' ' + UserRecord[1]
    VKLink = UserRecord[2]
    NumOfRecords = GirlTable.objects.all().order_by("-id")[0].id
    print('_' * 50)
    print('request is ', request)
    print('request.POST is ', request.POST)
    print('request.GET is ', request.GET)
    GET = request.GET
    print('RightButton.x' in GET)
    if 'RightButton.x' in GET:
        return render_to_response('Viewer/list.html', {'Username': Username,
                                                'VKLink': VKLink,
                                                'Public_id': Public_id,
                                                'id': i,
                                                'NumOfRecords': NumOfRecords
                                                })
    print('_' * 50)
    if request.GET.get('>') == '>':
        i += 1
    if request.GET.get('<') == '<' and i <= 2:
        i -= 1
    CurPublic = Public_id
    return render(request, 'Viewer/list.html', {'Username': Username,
                                                'VKLink': VKLink,
                                                'Public_id': Public_id,
                                                'id': i,
                                                'NumOfRecords': NumOfRecords
                                                })
