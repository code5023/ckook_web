from django.db import models

# Create your models here.

# 작업 내용 : Work
class Work(models.Model):
    ANDROID = "android"
    IOS = "ios"
    WEB = "web"
    CATEGORIES = (
        (ANDROID, "안드로이드 앱"),
        (IOS, "아이폰 앱"),
        (WEB, "웹"),
    )

    author = models.CharField(max_length=30)
    title = models.CharField(max_length=50)
    category = models.CharField(
        max_length=10,
        choices=CATEGORIES,
        default=ANDROID
    )
    content_txt = models.TextField()

    def __str__(self):
        return "[ {} ] {}, {}".format(self.category, self.title, self.author)

# 댓글
class Comment(models.Model):
    work = models.ForeignKey(
        Work, on_delete=models.CASCADE
    )
    username = models.CharField(max_length=50)
    content = models.TextField()

# # 좋아요
# class Like(models.Model):
#     like_count = models.IntegerField()
