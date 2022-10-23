import pytest 

from django import urls


@pytest.mark.parametrize('view_name', ['my_profile_page', 'edit_profile_page'])
def test_private_views(view_name, client):
    url = urls.reverse(view_name)
    resp = client.get(url)
    assert resp.status_code == 302