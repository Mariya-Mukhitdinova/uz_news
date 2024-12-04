from django.db import models


# Create your models here.
class CategoryNews(models.Model):
    category_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class New(models.Model):
    new_name = models.CharField(max_length=55)
    new_descr = models.TextField()
    new_image = models.FileField(upload_to="new_image")
    new_category = models.ForeignKey(CategoryNews, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.new_name

    class Meta:
        verbose_name = "New"
        verbose_name_plural = "News"
