from django.contrib import admin


# Register your models here.
# admin 페이지에서 보여주기 위한
from testStartApp.models import Test


class TestAdmin(admin.ModelAdmin):
    list_display = ('title', 'create_date')


admin.site.register(Test, TestAdmin)
