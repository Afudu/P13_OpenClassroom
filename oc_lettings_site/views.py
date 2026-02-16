from django.shortcuts import render
from sentry_sdk import capture_exception


# Lorem ipsum dolor sit amet, consectetur adipiscing elit.
# Quisque molestie quam lobortis leo consectetur ullamcorper non id est.
# Praesent dictum, nulla eget feugiat sagittis, sem mi convallis eros,
# vitae dapibus nisi lorem dapibus sem.
# Maecenas pharetra purus ipsum, eget consequat ipsum lobortis quis.
# Phasellus eleifend ex auctor venenatis tempus.
# Aliquam vitae erat ac orci placerat luctus.
# Nullam elementum urna nisi, pellentesque iaculis enim cursus in.
# Praesent volutpat porttitor magna, non finibus neque cursus id.
def index(request):
    return render(request, 'home/index.html')


def trigger_error(request):
    """
    This is an intentional error that will be captured by Sentry when triggered.
    It allows to make sure that error logging in sentry is working.
    """
    try:
        # ZeroDivisionError triggered.
        1 / 0
    except Exception as e:
        capture_exception(e)
        return render(request, 'home/error.html')


def privacy_policy_view(request):
    """Render the privacy policy page."""
    return render(request, 'home/privacy_policy_template.html')
