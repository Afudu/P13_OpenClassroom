import pytest
from django.urls import reverse
from lettings.lettings_factories import LettingFactory


@pytest.mark.django_db
def test_lettings_index_view(client):
    """
    Test the lettings index view.
    Ensures the view renders the correct template and contains the page title.
    """
    LettingFactory.create_batch(3)  # Create 3 lettings
    url = reverse('lettings_index')
    response = client.get(url)

    assert response.status_code == 200
    # Check for the title element
    assert '<title>' in response.content.decode('utf-8')
    # Adjust according to the actual title content in template
    assert 'Lettings' in response.content.decode('utf-8')


@pytest.mark.django_db
def test_letting_detail_view(client):
    """
    Test the letting detail view.
    Ensures the view renders the correct letting details.
    """
    letting = LettingFactory()
    url = reverse('letting', args=[letting.id])
    response = client.get(url)

    assert response.status_code == 200
    assert '<title>' in response.content.decode('utf-8')
    assert letting.title in response.content.decode('utf-8')
