from kivymd.app import MDApp
from kivymd.uix.button import *  
from kivymd.uix.screen import MDScreen
from kivymd.uix.dialog import *
from kivymd.uix.screenmanager import MDScreenManager
import re 
class HomeScreen(MDScreen):
    pass
class LOGIN(MDScreen):
    pass
class REGISTER(MDScreen):
    def validate_form(self):
        username = self.ids.username.text
        email = self.ids.email.text
        dob = self.ids.dob.text
        password = self.ids.pswd.text
        confirm_password = self.ids.cmpswd.text
        errors = []

        # Validate username
        if not username:
            errors.append("Username is required.")

        # Validate email
        if not email:
            errors.append("Email is required.")
        elif not self.is_valid_email(email):
            errors.append("Invalid email address.")

        # Validate Date of Birth (example: must be in the format YYYY-MM-DD)
        if not dob:
            errors.append("Date of Birth is required.")
        elif not self.is_valid_date(dob):
            errors.append("Invalid date format. Use YYYY-MM-DD.")
        
         # Validate password
        if not password:
            errors.append("Password is required.")
        elif len(password) < 6:  # Example password length validation
            errors.append("Password must be at least 6 characters long.")
        
        # Validate confirm password
        if not confirm_password:
            errors.append("Confirm Password is required.")
        elif password != confirm_password:
            errors.append("Passwords do not match.")

        if errors:
            error_message = '\n'.join(errors)
            self.show_error_dialog(error_message)
        else:
            self.ids.username.text = ''
            self.ids.email.text = ''
            self.ids.dob.text = ''
            self.ids.password.text = ''
            self.ids.confirm_password.text = ''
            # Add further actions upon successful validation

    def is_valid_email(self, email):
        # Simple regex for email validation
        return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None

    def is_valid_date(self, date):
        # Example date validation (YYYY-MM-DD format)
        try:
            from datetime import datetime
            datetime.strptime(date, '%Y-%m-%d')
            return True
        except ValueError:
            return False

    def show_error_dialog(self, message):
    # Create the dialog instance
        self.dialog = MDDialog(
            title="Validation Error",
            text=message,
            size_hint=(0.8, 1),
            auto_dismiss=False,
            buttons=[
                MDFlatButton(
                    text="OK",
                    on_release=self.dismiss_dialog
                ),
                MDFlatButton(
                    text="Exit",
                    on_release=self.exit_app
                )
            ]
        )
    # Open the dialog
        self.dialog.open()

    def dismiss_dialog(self, instance):
        # Dismiss the dialog
        self.dialog.dismiss()

    def exit_app(self, instance):
        # Dismiss the dialog first
        self.dismiss_dialog(instance)
        # Stop the application
        MDApp.get_running_app().stop()

class login(MDApp):
    def build(self):
        self.theme_cls.theme_style="Dark"
        return 
    
login().run()
