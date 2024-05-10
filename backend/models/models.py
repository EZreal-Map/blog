from tortoise.models import Model
from tortoise import fields

class Blog(Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=255)
    content = fields.TextField()
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)
     # 一对多关系
    tag =  fields.ForeignKeyField('models.Tag', related_name='blogs')

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
    nickname = fields.CharField(max_length=255, unique=True)
    email = fields.CharField(max_length=255, unique=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)
    
    def to_dict(self):
        return {
            "id": self.id,
            "nickname": self.nickname,
            "email": self.email,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }

class Tag(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)
    
  
class Time(Model):
    id = fields.IntField(pk=True)
    start_time = fields.DatetimeField(auto_now_add=True)
    end_time = fields.DatetimeField(auto_now=True)