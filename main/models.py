from django.db import models

class SiteSettings(models.Model):
    logo = models.ImageField(upload_to='logos/', verbose_name="Логотип школы", blank=True, null=True)
    
    hero_image = models.ImageField(upload_to='hero/', verbose_name="Главное фото (фоновое)", blank=True)
    
    title = models.CharField(max_length=255, verbose_name="Заголовок на главном экране")
    subtitle = models.TextField(verbose_name="Подзаголовок (описание)")
    logo_text = models.CharField(max_length=100, default="Школа им. С. Бекмуратова", verbose_name="Текст логотипа")
    
    about_title = models.CharField(max_length=100, default="О нашей школе", verbose_name="Заголовок 'О школе'")
    about_description = models.TextField(verbose_name="Текст описания школы")
    about_image = models.ImageField(upload_to='about/', verbose_name="Фото для блока 'О школе'", blank=True)

    footer_copy = models.CharField(max_length=255, verbose_name="Текст копирайта в футере")
    address = models.CharField(max_length=255, verbose_name="Адрес", blank=True)
    phone = models.CharField(max_length=50, verbose_name="Телефон", blank=True)
    
    instagram_url = models.URLField(
        max_length=500, 
        verbose_name="Ссылка на Instagram", 
        blank=True, 
        null=True,
        help_text="Вставьте ссылку на Instsgram"
    )

    class Meta:
        verbose_name = "Основные настройки"
        verbose_name_plural = "Основные настройки"

    def __str__(self):
        return "Настройки контента лендинга"


class Department(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название отделения")
    icon = models.ImageField(upload_to='icons/', verbose_name="Иконка (картинка)", blank=True, null=True)
    description = models.TextField(verbose_name="Краткое описание", blank=True)

    class Meta:
        verbose_name = "Отделение"
        verbose_name_plural = "Отделения"

    def __str__(self):
        return self.name


class Event(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название мероприятия")
    day = models.CharField(max_length=2, verbose_name="Число")
    month = models.CharField(max_length=20, verbose_name="Месяц")
    location = models.CharField(max_length=255, verbose_name="Место проведения")

    class Meta:
        verbose_name = "Мероприятие"
        verbose_name_plural = "Афиша"
        ordering = ['id']

    def __str__(self):
        return f"{self.day} {self.month} - {self.title}"
    
    
class Application(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя ученика")
    phone = models.CharField(max_length=20, verbose_name="Номер телефона")
    instrument = models.CharField(max_length=100, verbose_name="Инструмент/Отделение", blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата заявки")

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"

    def __str__(self):
        return f"{self.name} - {self.phone}"
    
    
class Reward(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название награды")
    image = models.ImageField(upload_to='rewards/', verbose_name="Изображение награды")
    description = models.TextField(verbose_name="Описание", blank=True, null=True)
    order = models.PositiveIntegerField(default=0, verbose_name="Порядок сортировки")

    class Meta:
        verbose_name = "Награда"
        verbose_name_plural = "Награды"
        ordering = ['order']

    def __str__(self):
        return self.title
    
    
class Teacher(models.Model):
    full_name = models.CharField(max_length=255, verbose_name="ФИО учителя")
    photo = models.ImageField(upload_to='teachers/', verbose_name="Фотография")
    specialty = models.CharField(max_length=100, verbose_name="Специализация (напр. Фортепиано)")
    experience = models.CharField(max_length=100, verbose_name="Стаж/Регалии", blank=True)
    description = models.TextField(verbose_name="О себе", blank=True)
    order = models.PositiveIntegerField(default=0, verbose_name="Порядок вывода")

    class Meta:
        verbose_name = "Учитель"
        verbose_name_plural = "Наши учителя"
        ordering = ['order']

    def __str__(self):
        return self.full_name
        