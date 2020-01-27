from analytics.seo.url_inspection import URL
from analytics.seo.utm_tags import utm_tag


def test_url_inspection():
    testurl = "https://www.hemnet.se"
    url = URL(testurl)
    url.inspect()
    assert isinstance(url, URL)
    assert url.attributes is not None
    assert url.attributes["status_code"] == 200


def test_utm_tags():
    good_url = "https://www.google.com/"
    alternative_url = "https://www.emailservice.com"
    source = "google"
    alternative_source = "newsletter"
    medium = "cpc"
    alternative_medium = "email"
    name = "spring_sale"
    alternative_name = "fall_sale"
    alternative_term = "running_shoes"
    alternative_content = "email_banner"

    google_tag = utm_tag(good_url, source, medium, name)
    email_tag = utm_tag(
        alternative_url,
        alternative_source,
        alternative_medium,
        alternative_name,
        alternative_term,
        alternative_content,
    )

    correct_google_utm = "https://www.google.com/?utm_source=google&utm_medium=cpc&utm_campaign=spring_sale"
    correct_email_utm = "https://www.emailservice.com/?utm_source=newsletter&utm_medium=email&utm_campaign=fall_sale&utm_term=running_shoes&utm_content=email_banner"
    assert google_tag == correct_google_utm
    assert email_tag == correct_email_utm
