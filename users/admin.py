from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

Account = get_user_model()


class AccountAdmin(UserAdmin):
    model = Account
    list_display = ('email', 'first_name', 'last_name', 'phone_number',)
    search_fields = ('email', )
    readonly_fields = ('id', 'date_joined', 'last_login',)
    fieldsets = (
        (None, {
            "fields": (
                ('email', 'first_name', 'last_name', 'is_staff',)

            ),
        }),
    )

    add_fieldsets = (
    (None, {
        'classes': ('wide',),
        'fields': ('email', 'phone_number', 'home_address',  'password1', 'password2'),
    }),
)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    ordering = ('email',)

admin.site.register(Account, AccountAdmin)