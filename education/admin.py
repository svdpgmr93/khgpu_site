from django.contrib import admin
from .models import *

class AdvantagesInline(admin.TabularInline):
    model = EduProgramAdvantageText

class SuitableInline(admin.TabularInline):
    model = Suitable

class KeySkillsInline(admin.TabularInline):
    model = KeySkills

class ProgramStructureInline(admin.TabularInline):
    model = ProgramStructure

class PositionInline(admin.TabularInline):
    model = Position

class PerspectiveInline(admin.TabularInline):
    model = Perspective

class KafedraAdmin(admin.ModelAdmin):
    list_display = ("name", "institut")

class EduProgramAdmin(admin.ModelAdmin):
    list_display = ("name", "kafedra_name", "level")
    inlines = [AdvantagesInline, SuitableInline, KeySkillsInline, ProgramStructureInline, PositionInline, PerspectiveInline]
    

class EduProgramAdvantageTextAdmin(admin.ModelAdmin):
    list_display = ("name", "op")


class SuitableAdmin(admin.ModelAdmin):
    list_display = ("text", "op")


class KeySkillsAdmin(admin.ModelAdmin):
    list_display = ("text", "op")

class ProgramStructureAdmin(admin.ModelAdmin):
    list_display = ("name", "op")

class PositionAdmin(admin.ModelAdmin):
    list_display = ("text", "op")

class PerspectiveAdmin(admin.ModelAdmin):
    list_display = ("text", "op")




admin.site.register(EduProgram, EduProgramAdmin)
admin.site.register(EduProgramAdvantageText, EduProgramAdvantageTextAdmin)
admin.site.register(Suitable, SuitableAdmin)
admin.site.register(KeySkills, KeySkillsAdmin)
admin.site.register(ProgramStructure, ProgramStructureAdmin)
admin.site.register(Position, PositionAdmin)
admin.site.register(Perspective, PerspectiveAdmin)
admin.site.register(EduProgramEduForm)
admin.site.register(EduForms)
admin.site.register(Institut)
admin.site.register(Kafedra, KafedraAdmin)
