from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.db import models
from django.db.models.signals import post_save

User = get_user_model()


class Prf(models.Model):

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    customer = models.OneToOneField(
        User,
        verbose_name="Пользователь",
        on_delete=models.CASCADE
    )

    delivery_address = models.TextField(
        'Адрес доставки',
        default='Заполнить'
    )

    phone_number = models.IntegerField(
        'телефон',
        default='+375'
    )

    def __str__(self):
        return 'Профиль пользователя {}'.format(self.customer)


def create_profile(sender, instance, **kwargs):
    if kwargs['created']:
        user_profile = Prf.objects.create(customer=instance)

        # Дописать проверку на добавление суперпользователя!!!

        managers_group, created = Group.objects.get_or_create(
            name='Customers'
        )
        instance.groups.add(managers_group)


post_save.connect(create_profile, sender=User)
