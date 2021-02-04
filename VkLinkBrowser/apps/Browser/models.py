from django.db import models
import inspect
import sys


class Public(models.Model):
    name = models.CharField('name', max_length=50)
    surname = models.CharField('surname', max_length=50)
    VKLink = models.CharField('VKLink', max_length=50)

    def __str__(self):
        return self.name + ' ' + self.surname + ' ' + self.VKLink

    def getName(self):
        return self.name

    def getSurname(self):
        return self.surname

    def getVKLink(self):
        return self.VKLink

    def getListOfRecord(self):
        return [self.name, self.surname, self.VKLink]

    def getChildClassesName():
        classes = [cls_name for cls_name, cls_obj in inspect.getmembers(sys.modules['Browser.models']) if
                   inspect.isclass(cls_obj)]
        classes.remove('Public')
        classes.remove('favorites')
        return classes

    class Meta:
        abstract = True

class favorites(Public):
    pass

class empire_pva(Public):
    pass

class thisisbabaika(Public):
  pass

class doska_pozora30(Public):
  pass


class nachnissebya_astr(Public):
  pass


class indigus_astrakhan(Public):
  pass

