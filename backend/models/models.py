from tortoise.models import Model
from tortoise import fields

class Blog(Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=255)
    content = fields.TextField()
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)
    # 多对多关系
    tags = fields.ManyToManyField('models.Tag', related_name='blogs')

class Comment(Model):
    id = fields.IntField(pk=True)
    content = fields.TextField()
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    # 一对多关系
    blog =  fields.ForeignKeyField('models.Blog', related_name='comments')
    # 引用评论ID,null代表一级评论，没有引用
    quoteID = fields.IntField(null=False)


class User(Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=255)
    email = fields.CharField(max_length=255)

class Tag(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)