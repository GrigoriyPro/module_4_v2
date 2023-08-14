from django.contrib import admin
from .models import Avito

class AvitoAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "price", "auction", "created_date", "updated_date"]
    list_filter = ["auction", "created_at"]
    actions = ["make_auction_as_false", "make_auction_as_true"]
    fieldsets = (
        (
            "Общие",{
                "fields": ("title", "description"),
            }
        ),
        (
            "Финансы",{
                "fields":("price", "auction"),
                "classes":["collapse"],
            }
        ),
    )

    @admin.display(description="Убрать возможность торга")
    def make_auction_as_false(self, request, queryset):
        queryset.update(auction=False)

    @admin.display(description="Добавить возможность торга")
    def make_auction_as_true(self, request, queryset):
        queryset.update(auction=True)


admin.site.register(Avito, AvitoAdmin)
