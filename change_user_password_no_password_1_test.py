
from endpoints import change_user_password_endpoint

def change_user_password_no_password_1_test():
    y = change_user_password_endpoint(username='user', old_password='asd', password1='', password2='cvcvvcxv')
    if (y['message'] == "Empty fields: ['password1']"):
        print('Test success')
    else:
        print('Failed')
        print(y)

change_user_password_no_password_1_test()