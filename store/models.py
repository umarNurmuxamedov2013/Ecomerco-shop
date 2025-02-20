from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)  # blank=True bo'lishi kerak
    brand = models.CharField(max_length=200, default="Brand yo'q")
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    image = models.ImageField(upload_to="products/")
    product_ctg = models.ForeignKey('Category', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Products"

    def __str__(self):
        return self.title

    # def save(self, *args, **kwargs):
    #     if not self.slug:  # Slug bo'sh bo'lsa, avtomatik generatsiya qilamiz
    #         self.slug = slugify(self.title)
    #     super().save(*args, **kwargs)
