from django.db import models
from ckeditor.fields import RichTextField
class Institut(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название института')
    
    class Meta:
        verbose_name = 'Институт'
        verbose_name_plural = 'Институты'
    def __str__(self):
        return f"{self.name}"


class Kafedra(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название кафедры')
    institut = models.ForeignKey('Institut', on_delete=models.CASCADE)
    kafedra_url = models.URLField(max_length=255, verbose_name='Ссылка на страницу кафедры', default='https://hgpurf.ru/')
    #karedra_tags = RichTextField(verbose_name='Теги кафедры') #Ставить через пробел
    kafedra_card_img = models.ImageField(upload_to='kafedra_images/', verbose_name='Изображение кафедры', default='default_kaf.jpg')
    #director = models.ForeignKey('Employee', on_delete=models.PROTECT, verbose_name='Заведующий', related_name="+")
    #about = RichTextField(verbose_name='О кафедре', blank=True)
    #email = models.EmailField(verbose_name='E-mail', blank=True)
    #phone = models.CharField(max_length=255, verbose_name='Телефон', blank=True)
    #employees = models.ManyToManyField('Employee')
    #about_employees = RichTextField(blank=True)
    # education program in model EducationProgram (foreighn key)
    # discipline in model Discipline (foreighn key)
    #science_info = RichTextField(blank=True)
    #practice_info = RichTextField(blank=True)
    #mission = RichTextField(blank=True)
    #tasks = RichTextField(blank=True)

    class Meta:
        verbose_name = 'Кафедра'
        verbose_name_plural = 'Кафедры'

    def __str__(self):
        return f"{self.name}"


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
    prof_interests = RichTextField(verbose_name='Проф.интересы', blank=True)
    expirience = RichTextField(verbose_name='Опыт', blank=True)
    achivements = RichTextField(verbose_name='Достижения', blank=True)
    education = RichTextField(verbose_name='Образование', blank=True)
    prof_dev = RichTextField(verbose_name='Повышение квалификации', blank=True)
    # participation = RichTextField(verbose_name='Участие в ОП университета', blank=True)??????????????????
    # disciplines = RichTextField(verbose_name='Перечень дисциплин', blank=True)???????????
    projects = RichTextField(verbose_name='Учатие в проектах', blank=True)


    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return f"{self.name}"


class Discipline(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название дисциплины')
    kafedra = models.ForeignKey('Kafedra', on_delete=models.PROTECT, related_name='kafedra')


    class Meta:
        verbose_name = 'Дисциплина'
        verbose_name_plural = 'Дисциплины'

    def __str__(self):
        return f"{self.name}"


class EduLevel(models.TextChoices):
    bachelor = 'Бакалавриат'
    magister = 'Магистратура'
    specialty = 'Специалитет'
    aspirant = 'Аспирантура'


class LerningTime(models.TextChoices):
    four = '4 года'
    four_half = '4 года 6 месяцев'
    five = '5 лет'
    five_half = '5 лет 6 месяцев'


    class Meta:
        verbose_name = 'Время обучения'
        verbose_name_plural = 'Время обучения'

    def __str__(self):
        return f"{self.name}"
    
class EduForms(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Форма обучения'
    def __str__(self):
        return f"{self.name}"


class EduProgram(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название программы')
    edu_number = models.CharField(max_length=100, verbose_name='Шифр')
    level = models.CharField(choices=EduLevel.choices, max_length=100)
    edu_form = models.ManyToManyField(EduForms, through='EduProgramEduForm')
    about_program = RichTextField(verbose_name='О программе')
    exam_ege = RichTextField(verbose_name='Экзамены ЕГЭ')
    exam_spo = RichTextField(verbose_name='Экзамены СПО')
    #advantage = models.ForeignKey('EduProgramAdvantageText', on_delete=models.DO_NOTHING, verbose_name='Преимущество')
    #suitable = models.ForeignKey('Suitable', on_delete=models.DO_NOTHING, verbose_name='Кому подходит')
    #key_skills = models.ForeignKey('KeySkills', on_delete=models.DO_NOTHING, verbose_name='Чему научитесь')
    #program_structure = models.ForeignKey('ProgramStructure', on_delete=models.DO_NOTHING, verbose_name='Что будете изучать')
    #position = models.ForeignKey('Position', on_delete=models.DO_NOTHING, verbose_name='Кем будете работать')
    #perspective = models.ForeignKey('Perspective', on_delete=models.DO_NOTHING, verbose_name='Перспективы трудоустройства')
    kafedra_name = models.ForeignKey('Kafedra', on_delete=models.DO_NOTHING, verbose_name='Выпускающая кафедра')
    edu_card_img = models.ImageField(upload_to='edu_program_images/', verbose_name='Изображение карточки ОП')
    edu_prog_banner_img = models.ImageField(upload_to='edu_program_images/', verbose_name='Изображение баннера ОП')
    edu_prog_advantage_img = models.ImageField(upload_to='edu_program_images/', verbose_name='Изображение блока преимуществ ОП')
    edu_prog_structure_img = models.ImageField(upload_to='edu_program_images/', verbose_name='Изображение блока структуры ОП')
    edu_prog_perspective_img1 = models.ImageField(upload_to='edu_program_images/', verbose_name='Изображение1 блока перспектив ОП')
    edu_prog_perspective_img2 = models.ImageField(upload_to='edu_program_images/', verbose_name='Изображение2 блока перспектив ОП')
    edu_prog_perspective_img3 = models.ImageField(upload_to='edu_program_images/', verbose_name='Изображение3 блока перспектив ОП')
    

    class Meta:
        verbose_name = 'Образовательная программа'
        verbose_name_plural = 'Образовательные программы'

    def __str__(self):
        name_kod = self.name + ' ' + self.edu_number[0:9:]
        return f"{name_kod}"
    
class EduProgramEduForm(models.Model):
    edu_program = models.ForeignKey(EduProgram, on_delete=models.CASCADE)
    edu_form = models.ForeignKey(EduForms, on_delete=models.PROTECT)
    lerning_time = models.CharField(choices=LerningTime.choices, max_length=100)
    budget_places = models.IntegerField()
    contract_places = models.IntegerField()

    class Meta:
        verbose_name = 'Форма и период обучения'
        verbose_name_plural = 'Формы и периоды обучения'

    def __str__(self):
        concat = str(self.edu_program.edu_number) + '---' + str(self.edu_form.name)
        return f"{concat}"


class EduProgramAdvantageText(models.Model):
    op = models.ForeignKey('EduProgram', on_delete=models.CASCADE, verbose_name='ОП')
    name = models.CharField(max_length=255, verbose_name="Название преимущества")
    text = RichTextField(verbose_name="Описание преимущества")


    class Meta:
        verbose_name = 'Преимущества ОП'
        verbose_name_plural = 'Преимущества ОП'

    def __str__(self):
        return f"{self.name}"


class Suitable(models.Model):
    op = models.ForeignKey('EduProgram', on_delete=models.CASCADE, verbose_name='ОП')
    text = RichTextField(verbose_name='Кому подходит программа')


    class Meta:
        verbose_name = 'Кому подходит'
        verbose_name_plural = 'Кому подходит'

    def __str__(self):
        return f"{self.text[0:50:]}"


class KeySkills(models.Model):
    op = models.ForeignKey('EduProgram', on_delete=models.CASCADE, verbose_name='ОП')
    text = RichTextField(verbose_name='Чему научитесь')


    class Meta:
        verbose_name = 'Ключевые навыки'
        verbose_name_plural = 'Ключевые навыки'

    def __str__(self):
        return f"{self.text[0:50:]}"

class ProgramStructure(models.Model):
    op = models.ForeignKey('EduProgram', on_delete=models.CASCADE, verbose_name='ОП')
    name = models.CharField(max_length=255, verbose_name="Название профиля")
    text = RichTextField(verbose_name='Что будете изучать')


    class Meta:
        verbose_name = 'Структура ОП'
        verbose_name_plural = 'Структура ОП'

    def __str__(self):
        return f"{self.name}"

class Position(models.Model):
    op = models.ForeignKey('EduProgram', on_delete=models.CASCADE, verbose_name='ОП')
    text = RichTextField(verbose_name='Кем будете работать')


    class Meta:
        verbose_name = 'Кем работать'
        verbose_name_plural = 'Кем работать'

    def __str__(self):
        return f"{self.text[0:50:]}"

class Perspective(models.Model):
    op = models.ForeignKey('EduProgram', on_delete=models.CASCADE, verbose_name='ОП')
    text = RichTextField(verbose_name="Перспективы трудоустройства")


    class Meta:
        verbose_name = 'Перспективы'
        verbose_name_plural = 'Перспективы '

    def __str__(self):
        return f"{self.text[0:50:]}"
