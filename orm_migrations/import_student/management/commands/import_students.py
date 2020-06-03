import json
from django.core.management.base import BaseCommand
from orm_migrations.school.models import Student, Teacher


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('orm_migrations/school.json', 'r', encoding='utf8') as json_file:
            reader = json.load(json_file)
            for row in reader:
                if row['model'] == 'school.teacher':
                    teacher = Teacher.objects.create(name=row['fields']['name'],
                                                     subject=row['fields']['subject'],)
                    teacher.save()
                elif row['model'] == 'school.student':
                    student = Student.objects.create(name=row['fields']['name'],
                                                     subject=row['fields']['group'],
                                                     teacher=row['fields']['teacher'],)
                    student.save()
