import pytest
from hotelpro.tests.fixtures import api_client
from hotelpro.tests import factories
from rest_framework import status
from hotelpro.apps.account.models import UserOTP


def test_register_user_send_code(db, api_client):
    endpoint = "/account/register/"
    client = api_client()
    user_obj = factories.AccountFactory.build()
    params = {"phone_number": str(user_obj.phone_number)}
    print(params)
    get_response = client.get(endpoint, {"phone_number": user_obj.phone_number})
    print(get_response)
    validated_data = {"phone_number": user_obj.phone_number, "code": "123456"}
    UserOTP.objects.create(**validated_data)
    data = {
        **validated_data,
        "username": user_obj.username,
        "password": '123456789',
    }

    post_response = client.post(path=endpoint, **data)
    

    assert get_response.status_code == status.HTTP_200_OK
    assert post_response.status_code == status.HTTP_201_CREATED
