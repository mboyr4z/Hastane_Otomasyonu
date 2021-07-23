class clickedEvents():
    def __init__(self,var):
        self.var = var

    def f_RegisterToLogin(self):
        self.var.screen_login.show()
        self.var.screen_register.close()

    def f_LoginToRegister(self):
        self.var.screen_login.close()
        self.var.screen_register.show()
