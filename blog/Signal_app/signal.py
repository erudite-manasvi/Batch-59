from django.contrib.auth.signals import user_logged_in #signal
from django.contrib.auth.models import User #sender
from django.dispatch import Signal,receiver

def login_success( **kwargs): # receiver
    print('I am receiver function!!')
    print(kwargs)
    
user_logged_in.connect(login_success,sender=User)


#custom signal
custom_signal = Signal()

#receiver
@receiver(custom_signal)
def custom_handler(**kwargs):
    print(kwargs)