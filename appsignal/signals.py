import re
from venv import create
from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed

from django.contrib.auth.models import User

from django.dispatch import receiver

@receiver(user_logged_in, sender=User)
def login_success_signal(sender,request,user, **kwargs):
    print('--------------------------------')
    print("Lgged in Succesfully  Run INTRO====================, ")
    print("Sender" ,sender)
    print("Request" ,request)
    print("User" ,user)
    print(f'Kwrgs : {kwargs}')

#user_logged_in.connect(login_success_signal,sender=User) #now we config it in app.py file 

@receiver(user_logged_out, sender=User)
def log_out_signal(sender,request,user, **kwargs):
    print('--------------------------------')
    print("Log out   Succesfully  End Game ================ ")
    print("Sender" ,sender)
    print("Request" ,request)
    print("User" ,user)
    print(f'Kwrgs : {kwargs}')

#user_logged_out.connect(log_out_signal,sender=User)    -  we have another method to connect use decorator first import 


@receiver(user_login_failed)
def log_in_faild_signal(sender,credentials, request,**kwargs):
    print('--------------------------------')
    print("Log In   UnSuccesfully  Try Again  ================ ")
    print("Sender" ,sender)
    print("Request" ,request)
    print('credentials',credentials)
    print(f'Kwrgs : {kwargs}')





''' BUILT IN METHOD '''
from django.db.models.signals import  pre_init,pre_save,pre_delete,post_init,post_save,post_delete

@receiver(pre_save,sender = User)                      #save th user
def pre_save_signal(sender,instance ,**kwargs):
    print('--------------------------------')
    print("Pre Save Signal is here  ================ ")
    print("Sender" ,sender)
    print("Intance" ,instance)
    print(f'Kwrgs : {kwargs}')


@receiver(post_save,sender = User)
def post_save_signal(sender,instance,created,**kwargs):
    if created:
        print('--------------------------------')
        print("Post Save Signal is here  ================ ")
        print("New Record")
        print("Sender" ,sender)
        print("Intance" ,instance)
        print("created",created)
        print(f'Kwrgs : {kwargs}')
    else:                                                 #update the user 
        print('--------------------------------')
        print("Post save (update) Signal is here  ================ ")
        print("Update Signal ")
        print("Sender" ,sender)
        print("Intance" ,instance)
        print(f'Kwrgs : {kwargs}')



@receiver(pre_delete,sender = User)                       #delete the post
def pre_delete_signal(sender,instance ,**kwargs):
    print('--------------------------------')
    print("Pre Delete Signal is here  ================ ")
    print("Sender" ,sender)
    print("Intance" ,instance)
    print(f'Kwrgs : {kwargs}')


@receiver(post_delete,sender = User)                   
def post_delete_signal(sender,instance ,**kwargs):
    print('--------------------------------')
    print("Post delete  Signal is here  ================ ")
    print("Sender" ,sender)
    print("Intance" ,instance)
    print(f'Kwrgs : {kwargs}')



@receiver(pre_init,sender = User)                      #just run the server
def post_delete_signal(sender,*args ,**kwargs):
    print('--------------------------------')
    print("Pre init   Signal is here  ================ ")
    print("Sender" ,sender)
    print(f"args  : {args}" )
    print(f'Kwrgs : {kwargs}')





@receiver(post_init,sender = User)                 
def post_delete_signal(sender,*args,**kwargs):
    print('--------------------------------')
    print("Post init   Signal is here  ================ ")
    print("Sender" ,sender)
    print(f"args  : {args}" )
    print(f'Kwrgs : {kwargs}')



'''=========================================================='''



from django.core.signals import request_started,request_finished, got_request_exception

@receiver(request_started)
def start_request(sender,environ, **kwargs):
    print('--------------------------------')
    print("Request Start   Signal is here  ================ ")
    print("Sender" ,sender)
    print(f"environ  : {environ}" )
    print(f'Kwrgs : {kwargs}')
                                                            

                                          #for check start,finish hit urls in your brower
@receiver(request_finished)
def end_request(sender, **kwargs):
    print('--------------------------------')
    print("Request Ended Signal is here  ================ ")
    print("Sender" ,sender)
    print(f'Kwrgs : {kwargs}')


@receiver(got_request_exception)
def sexception_request(sender,request, **kwargs):              #for check this we need view see view file 
    print('--------------------------------')
    print("Request  Exeption   Signal is here  ================ ")
    print("Sender" ,sender)
    print("Request",request )
    print(f'Kwrgs : {kwargs}')



#database connections 


from django.db.backends.signals import connection_created

@receiver(connection_created)            #for check this just runthe server

def con_deb(sender,connection, **kwargs):
    print('--------------------------------')
    print("Initial connection to the database   Signal is here  ================ ")
    print("Sender" ,sender)
    print("connection",connection )
    print(f'Kwrgs : {kwargs}')
