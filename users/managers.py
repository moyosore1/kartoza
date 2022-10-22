from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(
        self,
        email,
        phone_number,
        home_address,
        longitude,
        latitude,
        password=None,
        **other_fields
    ):
        if not email:
            raise ValueError("User must have an email address.")

        user = self.model(
            email=self.normalize_email(email),
            phone_number=phone_number,
            home_address=home_address,
            longitude=longitude,
            latitude=latitude,
            **other_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(
        self,
        email,
        phone_number,
        home_address,
        longitude,
        latitude,
        password,
    ):
        user = self.create_user(
            email=self.normalize_email(email),
            phone_number=phone_number,
            home_address=home_address,
            longitude=longitude,
            latitude=latitude,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self.db)
        return user
