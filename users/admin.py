from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser,Post
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    
    # 1. Tartiblashni phone_number ga o'zgartiramiz
    ordering = ('phone_number',)
    
    # 2. Ro'yxatda ko'rinadigan ustunlar
    list_display = ('phone_number', 'is_staff', 'is_active', 'birth_date')
    
    # 3. Qidiruv maydonini username dan phone_number ga o'zgartiramiz
    search_fields = ('phone_number',)

    # 4. Standart UserAdmin dagi username ga bog'liq filterlarni tozalaymiz
    filter_horizontal = ()
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    fieldsets = (
        (None, {'fields': ('phone_number', 'password')}),
        ('Shaxsiy ma\'lumotlar', {'fields': ('birth_date', 'profile_picture', 'first_name', 'last_name', 'email')}),
        ('Huquqlar', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        ('Muhim sanalar', {'fields': ('last_login', 'date_joined')}),
    )

    # Yangi foydalanuvchi qo'shish oynasi uchun
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone_number', 'password', 'birth_date', 'profile_picture'),
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Post)

