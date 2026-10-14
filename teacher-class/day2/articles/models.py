from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    # auto_now_at : 객체가 처음 생성 될 때의 시간
    created_at = models.DateTimeField(auto_now_add=True)
    # auto_now : 객체가 저장 될 때마다의 시간
    updated_at = models.DateTimeField(auto_now=True)


