from .models import User, Order
from uuid import UUID


class UserService:
    """Service that is responsible for managing User entity."""

    def new_user(self, user_data):
        """
        Create a new user and commit changes to the database.
        :param user_data: dictionary that contains information about new user
        """
        user_instance = self._create_user_instance(
            email=user_data['email'],
            phone_number=user_data['phone_number'],
            first_name=user_data['first_name'],
            last_name=user_data['last_name'],
        )
        user_instance.is_active = True
        user_instance.set_password(user_data['password2'])
        user_instance.save()
        return user_instance

    @staticmethod
    def activate_user_profile(user):
        """Activate user profile after successful email verification."""
        user.is_active = True
        user.save()

    @staticmethod
    def get_user(user_id: UUID):
        """Retrieve user with the provided id."""
        return User.objects.get(id=user_id)

    @staticmethod
    def _create_user_instance(email, phone_number, first_name, last_name):
        return User(
            email=email,
            phone_number=phone_number,
            first_name=first_name,
            last_name=last_name
        )

    @staticmethod
    def get_user_orders(user):
        return Order.objects.filter(user=user).all()


user_service = UserService()