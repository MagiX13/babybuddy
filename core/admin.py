# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Child, DiaperChange, Feeding, Note, Sleep, TummyTime


@admin.register(Child)
class ChildAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'birth_date',)
    list_filter = ('last_name',)
    search_fields = ('first_name', 'last_name', 'birth_date',)


@admin.register(DiaperChange)
class DiaperChangeAdmin(admin.ModelAdmin):
    list_display = ('child', 'time', 'wet', 'solid', 'color')
    list_filter = ('child', 'wet', 'solid', 'color')
    search_fields = ('child__first_name', 'child__last_name',)


@admin.register(Feeding)
class FeedingAdmin(admin.ModelAdmin):
    list_display = ('start', 'end', 'duration', 'child', 'type', 'method',)
    list_filter = ('child', 'type', 'method',)
    search_fields = ('child__first_name', 'child__last_name', 'type', 'method',)


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('time', 'child', 'note',)
    list_filter = ('child',)
    search_fields = ('child__last_name',)


@admin.register(Sleep)
class SleepAdmin(admin.ModelAdmin):
    list_display = ('start', 'end', 'duration', 'child',)
    list_filter = ('child',)
    search_fields = ('child__first_name', 'child__last_name',)


@admin.register(TummyTime)
class TummyTimeAdmin(admin.ModelAdmin):
    list_display = ('start', 'end', 'duration', 'child', 'milestone',)
    list_filter = ('child',)
    search_fields = ('child__first_name', 'child__last_name', 'milestone',)
