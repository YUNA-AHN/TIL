from django.db import models


class Doctor(models.Model):
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 의사 {self.name}'


class Patient(models.Model):
    # 외래 키 생성
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 환자 {self.name}'


# 코드 예시
# 2명의 의사 생성
doctor1 = Doctor.objects.create(name='allie')
doctor2 = Doctor.objects.create(name='barbie')
# 각 환자를 서로 다른 의사에게 예약
patient1 = Patient.objects.create(name='carol', doctor=doctor1)
patient2 = Patient.objects.create(name='duke', doctor=doctor2)
# 두 의사에게 모두 진료를 받고자 함 -> 1번 데이터가 중복되어 입력
patient3 = Patient.objects.create(name='carol', doctor=doctor2)
patient4 = Patient.objects.create(name='duke', doctor=doctor1, doctor2)
