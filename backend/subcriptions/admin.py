
# from django.contrib import admin
# from .models import Package, EventSubscription


# @admin.register(Package)
# class PackageAdmin(admin.ModelAdmin):
#     list_display = (
#         'name',
#         'price',
#         'duration_days',
#         'storage_limit_mb',
#         'max_events',
#         'is_active',
#     )

#     search_fields = ('name',)
#     list_filter = ('is_active',)


# @admin.register(EventSubscription)
# class EventSubscriptionAdmin(admin.ModelAdmin):
#     list_display = (
#         'event',
#         'organizer',
#         'package',
#         'start_date',
#         'end_date',
#         'status',
#     )

#     search_fields = (
#         'event__title',
#         'organizer__username',
#         'package__name',
#     )

#     list_filter = ('status', 'package')
