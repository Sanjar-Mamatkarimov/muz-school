from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Application, Review
from .utils import send_telegram_notification

@receiver(post_save, sender=Application)
def notify_admin_new_application(sender, instance, created, **kwargs):
    if created:  # Только если это новая запись, а не редактирование старой
        message = (
            f"🎹 <b>Новая заявка на сайте!</b>\n\n"
            f"👤 <b>Имя:</b> {instance.name}\n"
            f"📞 <b>Телефон:</b> {instance.phone}\n"
            f"🎸 <b>Инструмент:</b> {instance.instrument or 'Не указан'}\n"
            f"👶 <b>Возраст:</b> {instance.age or 'Не указан'}\n"
            f"📝 <b>Тип:</b> {instance.get_application_type_display()}\n"
            f"💬 <b>Комментарий:</b> {instance.message or '-'}"
        )
        send_telegram_notification(message)

@receiver(post_save, sender=Review)
def notify_admin_new_review(sender, instance, created, **kwargs):
    if created:
        # Уведомляем даже если отзыв еще не опубликован (is_published=False)
        message = (
            f"⭐ <b>Новый отзыв ожидает модерации!</b>\n\n"
            f"👤 <b>От:</b> {instance.name}\n"
            f"📊 <b>Оценка:</b> {'★' * instance.rating}\n"
            f"💬 <b>Текст:</b> {instance.text}"
        )
        send_telegram_notification(message)