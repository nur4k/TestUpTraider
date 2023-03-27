from django.contrib import admin

from menu.models import TreeMenu, TreeMenuCategory


admin.site.register([TreeMenu, TreeMenuCategory])
