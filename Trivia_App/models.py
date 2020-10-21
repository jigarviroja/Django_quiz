from django.db import models

# Create your models here.


class Person(models.Model):

    name = models.CharField(max_length=50, default=None)
    # question1 = models.CharField(max_length=400, null=True)
    # question2 = models.CharField(max_length=400, null=True)
    # ans1 = models.CharField(max_length=20, choices=(("Sachine Tendulkar", "Sachine Tendulkar"), ("Virat Kohli", "Virat Kohli"),
    #                                                 ("Adam Gilchirst", "Adam Gilchirst"), ("Jacques Kallis", "Jacques Kallis")), null=True)

    # ans2 = models.CharField(max_length=20, choices=(("White", "White"), ("Yellow",
    #                                                                      "Yellow"), ("Orange", "Orange"), ("Green", "Green")), null=True)

    def __str__(self):
        return self.name


# class Question(models.Model):

#     quiz_question = models.CharField(max_length=50, default=None)
#     question_type = models.CharField(max_length=15,
#                                      choices=(('single', 'single'), ('multiple', 'multiple')))

#     def __str__(self):
#         return self.quiz_question


# class Option(models.Model):

#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     option = models.CharField(max_length=50)

#     def __str__(self):
#         return self.option


# class Result(models.Model):

#     name = models.ForeignKey(Person, on_delete=models.CASCADE, null=True)
#     question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)
#     option = models.CharField(max_length=100, null=True)


class FinalResult(models.Model):
    name = models.CharField(max_length=20, null=True)
    question = models.CharField(max_length=200, null=True)
    option = models.CharField(max_length=100, null=True)
    time = models.CharField(max_length=100, null=True)
