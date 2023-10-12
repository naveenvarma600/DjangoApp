from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test


def user_required(function=None, redirect_field_name = REDIRECT_FIELD_NAME, login_url = 'login'):
    """
    decorator for views that check that the logged in user in a student ,
    redirect to the log-in page if neccessary
    :param function:
    :param redirect_field_name:
    :param login_url:
    :return:
    """
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_user or u.is_superuser,
        login_url = login_url,
        redirect_field_name= redirect_field_name,
    )
    if function:
        return actual_decorator(function)
    return actual_decorator

def musician_required(function=None, redirect_field_name = REDIRECT_FIELD_NAME, login_url = 'login'):
    """
        decorator for views that check that the logged in user in a student ,
        redirect to the log-in page if neccessary
        :param function:
        :param redirect_field_name:
        :param login_url:
        :return:
        """
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_musician or u.is_superuser,
        login_url=login_url,
        redirect_field_name=redirect_field_name,
    )
    if function:
        return actual_decorator(function)
    return actual_decorator