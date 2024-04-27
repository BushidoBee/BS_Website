import unittest
import RL_DBMod

def add(a, b):
    return a + b

def AddNewUser(Var1, Var2, Var3, Var4, Var5):
    New_User = RL_DBMod.Account(First_Name=Var1, Last_Name=Var2, Phone_Number=Var3, Email=Var4, Password=Var5)
    New_User.save()
    return New_User.objects.filter

def UserVerify(Var1, Var2):
    Ver_User = RL_DBMod.Account.objects.filter(First_Name="Joshua", Last_Name="Broussard")
    return Ver_User

class TestAddFunction(unittest.TestCase):
    def RLDB_NewUser(self):
        f_name, l_name = "Joshua", "Broussard"
        Phone, Email = "281-513-4148", "jbroussard@icloud.com"
        Pwd = "Self_t3st_45$!"
        self.assertEqual(AddNewUser(f_name, l_name, Phone, Email, Pwd), UserVerify(f_name, l_name))

if __name__ == '__main__':
    unittest.main()