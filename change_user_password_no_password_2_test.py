
from endpoints import change_user_password_endpoint

def change_user_password_no_password_2_test():
    y = change_user_password_endpoint(username='user', old_password='asd', password1='asdadad', password2='')
    if (y['message'] == "Empty fields: ['password2']"):
        print('Test success')
    else:
        print('Failed')
        print(y)

change_user_password_no_password_2_test()