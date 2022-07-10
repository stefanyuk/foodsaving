from .models import User


class UserService:
    def new_user(self, user_data):
        user_data.pop("confirm_password")
        user = User(**user_data)
        user.save()
        return user
