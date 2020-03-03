from django.contrib import admin
from users.models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'website', 'picture')
    list_display_links = ('user', 'website')
    list_editable = ['phone_number']
    search_fields = ('user__email', 'user__first_name', 'user__last_name')
    list_filter = ('user__is_active', 'user__is_staff', 'created')
    fieldsets = (
        ('Profile' ,{
            'fields': (('user', 'picture'),),
        }),
        ('Extra info', {
            'fields': (
                ('website', 'phone_number'),
                ('biography')
            )
        }),
        ('Metada', {
            'fields': (('created', 'modified',),)
        })

        
    )

    readonly_fields = ('created', 'modified', 'user')

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'

class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)
    list_display = ('username', 
                    'email',
                    'first_name',
                    'last_name',
                    'is_active',
                    'is_staff',
                    )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
    
