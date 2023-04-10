import pandas as pd


class User:
    def __init__(self,username,password):
        self.username=username
        self.password=password

    def to_dict(self):
        return {'username':self.username,'password':self.password}
class Login:
    def __init__(self,users_file):
        self.users=pd.read_excel(users_file).apply(lambda x:User (x ['username'],x ['password']),axis=1)

    def login(self,username,password):
        for user in self.users:
            if user.username == username and user.password == password:
                return True
        return False


login =Login('scenario2ID1111.xlsx')

if login.login('aaa', 'aaa@1'):
    print('login done')
else:
    print('login not done')

