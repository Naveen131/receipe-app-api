from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from core import models
from django.utils.translation import gettext as _
# Register your models here.
class UserAdmin(BaseUserAdmin):
    orderding =['id']
    list_display=['email','username']
    fieldsets = (
        (None,{'fields':('email','password')}),
        (_('Personal_info'),{'fields':('username',)}),
        (
            _('Permissions'),
            {
            'fields':('is_active','is_staff','is_superuser')
            }
        ),
        (_('Importantdates'),{'fields':('last_login',)})
    )

    ad_fieldsets = (
    (None,{
        'classes':('wide'),
        'filelds' :('email','password1','password2')
    }),
    )

admin.site.register(models.User,UserAdmin)
