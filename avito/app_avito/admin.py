from django.contrib import admin
from .models import Avito
from django.db.models import QuerySet

class AvitoAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "price", "user", "auction", "created_date", "updated_date", "photo"]
    list_filter = ["auction", "created_at"]
    actions = ["make_auction_as_false", "make_auction_as_true"]
    readonly_fields = ("created_date", "photo")
    fieldsets = (
        (
            "Общие",{
                "fields": ("title", "description", "user", "image", "photo" ,"created_date"),
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
    def make_auction_as_false(self, request, queryset: QuerySet):
        count = queryset.update(auction=False)
        self.message_user(
            request,
            f"Было обновлено: {count}"
        )

    @admin.display(description="Добавить возможность торга")
    def make_auction_as_true(self, request, queryset: QuerySet):
        count = queryset.update(auction=True)
        self.message_user(
            request,
            f"Было обновлено: {count}"
        )

admin.site.register(Avito, AvitoAdmin)


