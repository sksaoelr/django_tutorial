from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'user_id',
        # 'user_pw',
        'user_name',
        'user_email',
        'user_register_dttm'
    )

    list_display_links = (
        'user_id',
        # 'user_pw',
        'user_name',
        # 'user_email',
        'user_register_dttm'
    )
    