from django.db import models

class Institut(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название института')


class Kafedra(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название кафедры')
    institut = models.ForeignKey('Institut', on_delete=models.CASCADE)
    director = models.ForeignKey('Employee', on_delete=models.PROTECT, verbose_name='Заведующий', related_name="+")
    about = models.TextField(verbose_name='О кафедре', blank=True)
    email = models.EmailField(verbose_name='E-mail', blank=True)
    phone = models.CharField(max_length=255, verbose_name='Телефон', blank=True)
    employees = models.ManyToManyField('Employee')
    about_employees = models.TextField(blank=True)
    # education program in model EducationProgram (foreighn key)
    # discipline in model Discipline (foreighn key)
    science_info = models.TextField(blank=True)
    practice_info = models.TextField(blank=True)
    mission = models.TextField(blank=True)
    tasks = models.TextField(blank=True)


class Employee(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    surname = models.CharField(max_length=255, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=255, verbose_name='Отчество', blank=True)
    post = models.CharField(max_length=255, verbose_name='Должность')
    academic_degree = models.CharField(max_length=255, verbose_name='Ученая степень', blank=True)
    academic_title = models.CharField(max_length=255, verbose_name='Ученое звание', blank=True)
    other_post = models.CharField(max_length=255, verbose_name='Иные должности', blank=True)
    email = models.EmailField(verbose_name='E-mail', blank=True)
    phone = models.CharField(max_length=255, verbose_name='Телефон', blank=True)
    spin_rinz = models.CharField(max_length=255, verbose_name='SPIN-РИНЦ', blank=True)
    orcid = models.CharField(max_length=255, verbose_name='ORCID', blank=True)
    prof_interests = models.TextField(verbose_name='Проф.интересы', blank=True)
    expirience = models.TextField(verbose_name='Опыт', blank=True)
    achivements = models.TextField(verbose_name='Достижения', blank=True)
    education = models.TextField(verbose_name='Образование', blank=True)
    prof_dev = models.TextField(verbose_name='Повышение квалификации', blank=True)
    # participation = models.TextField(verbose_name='Участие в ОП университета', blank=True)??????????????????
    # disciplines = models.TextField(verbose_name='Перечень дисциплин', blank=True)???????????
    projects = models.TextField(verbose_name='Учатие в проектах', blank=True)


class Discipline(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название дисциплины')
    kafedra = models.ForeignKey('Kafedra', on_delete=models.PROTECT, related_name='kafedra')


class EduLevel(models.TextChoices):
    bachelor = 'Бакалавриат'
    magister = 'Магистратура'
    specialty = 'Специалитет'
    aspirant = 'Аспирантура'


class EduForms(models.Model):
    name = models.CharField(max_length=100)


class EduProgram(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название программы')
    edu_number = models.CharField(max_length=100, verbose_name='Шифр')
    level = models.CharField(choices=EduLevel.choices, max_length=100)
    edu_form = models.ManyToManyField(EduForms, through='EduProgramEduForm')
    about_program = models.TextField(verbose_name='О программе')
    exam_ege = models.TextField(verbose_name='Экзамены ЕГЭ')
    exam_spo = models.TextField(verbose_name='Экзамены СПО')
    advantage = models.ForeignKey('EduProgramAdvantageText', on_delete=models.DO_NOTHING, verbose_name='Преимущество')
    suitable = models.ForeignKey('Suitable', on_delete=models.DO_NOTHING, verbose_name='Кому подходит')
    key_skills = models.ForeignKey('KeySkills', on_delete=models.DO_NOTHING, verbose_name='Чему научитесь')
    program_structure = models.ForeignKey('ProgramStructure', on_delete=models.DO_NOTHING, verbose_name='Что будете изучать')
    position = models.ForeignKey('Position', on_delete=models.DO_NOTHING, verbose_name='Кем будете работать')
    perspective = models.ForeignKey('Perspective', on_delete=models.DO_NOTHING, verbose_name='Перспективы трудоустройства')
    kafedra_name = models.CharField(max_length=255, verbose_name="Выпускающая кафедра")
    kafedra_url = models.URLField(max_length=255, verbose_name='Ссылка на страницу кафедры')
    karedra_tags = models.TextField(verbose_name='Теги кафедры') #Ставить через пробел
    kafedra_card_img = models.ImageField(upload_to='kafedra_images/', verbose_name='Изображение кафедры')
    edu_card_img = models.ImageField(upload_to='edu_program_images/', verbose_name='Изображение карточки ОП')
    edu_prog_banner_img = models.ImageField(upload_to='edu_program_images/', verbose_name='Изображение баннера ОП')
    edu_prog_advantage_img = models.ImageField(upload_to='edu_program_images/', verbose_name='Изображение блока преимуществ ОП')
    edu_prog_structure_img = models.ImageField(upload_to='edu_program_images/', verbose_name='Изображение блока структуры ОП')
    edu_prog_perspective_img1 = models.ImageField(upload_to='edu_program_images/', verbose_name='Изображение1 блока перспектив ОП')
    edu_prog_perspective_img2 = models.ImageField(upload_to='edu_program_images/', verbose_name='Изображение2 блока перспектив ОП')
    edu_prog_perspective_img3 = models.ImageField(upload_to='edu_program_images/', verbose_name='Изображение3 блока перспектив ОП')
    

class EduProgramEduForm(models.Model):
    edu_program = models.ForeignKey(EduProgram, on_delete=models.CASCADE)
    edu_form = models.ForeignKey(EduForms, on_delete=models.PROTECT)
    lerning_time = models.CharField(max_length=100)
    budget_places = models.IntegerField()
    contract_places = models.IntegerField()


class EduProgramAdvantageText(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название преимущества")
    text = models.TextField(verbose_name="Описание преимущества")


class Suitable(models.Model):
    text = models.TextField(verbose_name='Кому подходит программа')


class KeySkills(models.Model):
    text = models.TextField(verbose_name='Чему научитесь')


class ProgramStructure(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название профиля")
    text = models.TextField(verbose_name='Что будете изучать')


class Position(models.Model):
    text = models.TextField(verbose_name='Кем будете работать')


class Perspective(models.Model):
    text = models.TextField(verbose_name="Перспективы трудоустройства")
