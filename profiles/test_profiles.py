import pytest
from django.urls import reverse
from profiles.profiles_factories import ProfileFactory


@pytest.mark.django_db
def test_profiles_index_view(client):
    """
    Test the profiles index view.
    Ensures the view renders the correct template and contains the page title.
    """
    ProfileFactory.create_batch(3)  # Create 3 profiles
    url = reverse('profiles_index')
    response = client.get(url)

    assert response.status_code == 200
    assert '<title>' in response.content.decode('utf-8')  # Check for the title element
    assert 'Profiles' in response.content.decode('utf-8')  # Adjust according to the actual title content in template


@pytest.mark.django_db
def test_profile_detail_view(client):
    """
    Test the profile detail view.
    Ensures the view renders the correct profile details.
    """
    profile = ProfileFactory()
    url = reverse('profile', args=[profile.user.username])
    response = client.get(url)

    assert response.status_code == 200
    assert '<title>' in response.content.decode('utf-8')
    assert profile.user.username in response.content.decode('utf-8')
