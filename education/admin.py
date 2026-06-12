from django.contrib import admin
from .models import *

class KafedraAdmin(admin.ModelAdmin):
    list_display = ("name", "institut")


class EduProgramAdmin(admin.ModelAdmin):
    list_display = ("name", "kafedra_name", "level")


admin.site.register(EduProgram, EduProgramAdmin)
admin.site.register(EduProgramAdvantageText)
admin.site.register(Suitable)
admin.site.register(KeySkills)
admin.site.register(ProgramStructure)
admin.site.register(Position)
admin.site.register(Perspective)
admin.site.register(EduProgramEduForm)
admin.site.register(EduForms)
admin.site.register(Institut)
admin.site.register(Kafedra, KafedraAdmin)
