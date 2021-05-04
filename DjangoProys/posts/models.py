""" Posts Models """

#Django
from django.db import models
from django.contrib.auth.models import User as User2

class User(models.Model):
    """User Models"""
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    is_admin = models.BooleanField(default=False)

    bio = models.TextField(blank=True)

    birthdate = models.DateField(blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """ Return email. """
        return self.email

"""

def Ejercicios de Inserciones en Shell (InteractiveConsole):

    >>> from posts.models import User

    >>> pablo = User.objects.create(
    ...     email='nick@gmail.com',
    ...     password='123456',
    ...     first_name='Pablo',
    ...     last_name='Apellido'
    ... )

    >>> pablo.email = 'nombre@gmail.com'
    >>> pablo.save()
    >>> pablo.email
    'nombre@gmail.com'

    >>> arturo = User()
    >>> arturo.email = 'artur@gmail.com'
    >>> arturo.first_name = 'Arturo'
    >>> arturo.last_name = 'Mendez'
    >>> arturo.password = 'MSIComputer'
    >>> arturo.is_admin = True
    >>> arturo.save()

    >>> arturo.pk
    2

    #arturo.delete()


    Segundo Ejercicio

    from datetime import date

    users = [
        {
            'email': 'cvander@platzi.com',
            'first_name': 'Christian',
            'last_name': 'Van der Henst',
            'password': '1234567',
            'is_admin': True
        },
        {
            'email': 'freddier@platzi.com',
            'first_name': 'Freddy',
            'last_name': 'Vega',
            'password': '987654321'
        },
        {
            'email': 'yesica@platzi.com',
            'first_name': 'Yésica',
            'last_name': 'Cortés',
            'password': 'qwerty',
            'birthdate': date(1990, 12,19)
        },
        {
            'email': 'arturo@platzi.com',
            'first_name': 'Arturo',
            'last_name': 'Martínez',
            'password': 'msicomputer',
            'is_admin': True,
            'birthdate': date(1981, 11, 6),
            'bio': "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."
        }
    ]

    from posts.models import User

    for user in users:
        obj = User(**user)
        obj.save()
        print(obj.pk, ':', obj.email)



    >>> from posts.models import User
    >>> platzi_users = User.objects.filter(email__endswith = '@platzi.com')
    >>> platzi_users
    <QuerySet [<User: cvander@platzi.com>, <User: freddier@platzi.com>, <User: yesica@platzi.com>, <User: arturo@platzi.com>]>
    >>> 

    >>> users = User.objects.all()
    >>> users
    <QuerySet [<User: nombre@gmail.com>, <User: artur@gmail.com>, <User: cvander@platzi.com>, <User: freddier@platzi.com>, <User: yesica@platzi.com>, <User: arturo@platzi.com>]>

    >>> platzi_users = User.objects.filter(email__endswith = '@platzi.com').update(is_admin = True)
    >>> platzi_users
    4

    >>> platzi_users = User.objects.filter(email__endswith = '@platzi.com')
    >>> for u in platzi_users:
    ...     print(u.email, ':', u.is_admin)
    ... 
    cvander@platzi.com : True
    freddier@platzi.com : True
    yesica@platzi.com : True
    arturo@platzi.com : True
    >>> 

"""


class Post(models.Model):
    """ Post Model """

    user = models.ForeignKey(User2, on_delete=models.CASCADE)
    profile = models.ForeignKey('users.Profile', on_delete=models.CASCADE)

    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='posts/photos')

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """ Return title and username. """
        return '{} by @{}'.format(self.title, self.user.username)
    
 















