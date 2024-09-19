from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Post(models.Model):
    """
    Модель постов для блога
    """

    STATUS_OPTIONS = (("published", "Опубликовано"), ("draft", "Черновик"))

    title = models.CharField(verbose_name="Название записи", max_length=255)
    slug = models.SlugField(verbose_name="URL", max_length=255, blank=True, unique=True)
    description = models.TextField(verbose_name="Краткое описание", max_length=500)
    text = models.TextField(verbose_name="Полный текст записи")
    category = TreeForeignKey(
        to="Category",
        verbose_name="Категория",
        on_delete=models.PROTECT,
        related_name="posts",
    )
    thumbnail = models.ImageField(
        verbose_name="Изображение записи",
        default="default.jpg",
        blank=True,
        upload_to="images/thumbnails/",
        validators=[
            FileExtensionValidator(
                allowed_extensions=("png", "jpg", "webp", "jpeg", "gif")
            )
        ],
    )
    status = models.CharField(
        verbose_name="Статус записи",
        choices=STATUS_OPTIONS,
        default="published",
        max_length=10,
    )
    create = models.DateTimeField(verbose_name="Время добавления", auto_now_add=True)
    update = models.DateTimeField(verbose_name="Время обновления", auto_now=True)
    author = models.ForeignKey(
        to=User,
        verbose_name="Автор",
        on_delete=models.SET_DEFAULT,
        related_name="author_posts",
        default=1,
    )
    updater = models.ForeignKey(
        to=User,
        verbose_name="Обновил",
        on_delete=models.SET_NULL,
        null=True,
        related_name="updater_posts",
        blank=True,
    )
    fixed = models.BooleanField(verbose_name="Прикреплено", default=False)

    class Meta:
        """
        Название таблицы в базе данных, сортировка по закреплению и дате создания, индексирование, название модели
        """

        db_table = "blog_post"
        ordering = ["-fixed", "-create"]
        indexes = [models.Index(fields=["-fixed", "-create", "status"])]
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"

    def __str__(self):
        return self.title


class Category(MPTTModel):
    """
    Модель категорий с вложенностью
    """

    title = models.CharField(verbose_name="Название категории", max_length=255)
    slug = models.SlugField(verbose_name="URL категории", max_length=255, blank=True)
    description = models.TextField(verbose_name="Описание категории", max_length=300)
    parent = TreeForeignKey(
        to="self",
        verbose_name="Родительская категория",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        db_index=True,
        related_name="children",
    )

    class MPTTMeta:
        """
        Сортировка по вложенности
        """

        order_insertion_by = ("title",)

    class Meta:
        """
        Название модели в админ панели, название таблицы в базе данных
        """

        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        db_table = "app_categories"

    def __str__(self):
        return self.title
