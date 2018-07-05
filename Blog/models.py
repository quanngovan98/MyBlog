from django.db import models
from taggit.managers import TaggableManager  # dùng để thêm tag, sẽ có trong phần sau
import string
import re
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# KHONGDAU---------------------------------------------------------
# -*- coding: utf-8 -*-
INTAB = "ạảãàáâậầấẩẫăắằặẳẵóòọõỏôộổỗồốơờớợởỡéèẻẹẽêếềệểễúùụủũưựữửừứíìịỉĩýỳỷỵỹđẠẢÃÀÁÂẬẦẤẨẪĂẮẰẶẲẴÓÒỌÕỎÔỘỔỖỒỐƠỜỚỢỞỠÉÈẺẸẼÊẾỀỆỂỄÚÙỤỦŨƯỰỮỬỪỨÍÌỊỈĨÝỲỶỴỸĐ \'\":_“!”"
INTAB = [str(ch) for ch in str(INTAB)]
OUTTAB = "a" * 17 + "o" * 17 + "e" * 11 + "u" * 11 + "i" * 5 + "y" * 5 + "d" + "A" * 17 + "O" * 17 + \
    "E" * 11 + "U" * 11 + "I" * 5 + "Y" * 5 + "D" + "-" + "-" + "-" + "-" + "-" + "-" + "-" + "-"
r = re.compile("|".join(INTAB))
replaces_dict = dict(zip(INTAB, OUTTAB))


def khongdau(utf8_str):
    str(utf8_str)
    return r.sub(lambda m: replaces_dict[m.group(0)], utf8_str)
# KHONGDAU---------------------------------------------------------


class Category(models.Model):
    name = models.CharField(max_length=100, default='none', unique=True)
    describe = models.CharField(max_length=200, default='none')

    def __str__(self):  # dùng để trả về tên đại diện của class khi được gọi tới
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100)
    # body = models.TextField()
    body=RichTextUploadingField(blank=True,null=True)
    date = models.DateTimeField(auto_now_add=True)
    # to_field là chỉ định trường được trỏ tới, mặc định là pk
    category = models.ForeignKey(Category, to_field='name', default='Game', on_delete=models.CASCADE)
    tags = TaggableManager()
    slugifytitle = models.CharField(max_length=100, default='no need to fill', unique=True)
    image=models.ImageField(null=True)

    def save(self, *args, **kwargs):
        self.slugifytitle = khongdau(self.title)
        super(Post, self).save()

    def __str__(self):  # dùng để trả về tên đại diện của class khi được gọi tới
        return self.title