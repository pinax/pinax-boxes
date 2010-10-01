from django.conf import settings

from fixture_generator import fixture_generator

from boxes.models import Box


@fixture_generator(Box)
def initial_data():
    Box.objects.create(label="home_sidebar_title", content="Welcome to our Alpha v1")
    Box.objects.create(label="home_sidebar_content", content="admin conrolled message/html here. (note to self: add twitter and moro links here)")
    Box.objects.create(label="ad_300", content="""
        <a href="#">
            <img src="%(STATIC_URL)simg/a/ads/ani-ad-main.jpg" alt="Ad" />
        </a>""" % {"STATIC_URL": settings.STATIC_URL}
    )
