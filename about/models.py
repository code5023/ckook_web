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
    RECEIVED = "rec"
    UNRECEIVED = "un"
    CATEGORIES = (
        (RECEIVED, "승인"),
        (UNRECEIVED, "미승인"),
    )
    work = models.ForeignKey(
        Work,
        related_name="work_comment",
        on_delete=models.CASCADE
    )
    category = models.CharField(
        max_length=10,
        choices=CATEGORIES,
        default=UNRECEIVED
    )
    username = models.CharField(max_length=50)
    content = models.TextField()

    def __str__(self):
        return "[ {} ] {},{}/ {} : {}".format(self.category, self.work.category, self.work.title, self.username, self.content)

# # 좋아요
# class Like(models.Model):
#     like_count = models.IntegerField()
