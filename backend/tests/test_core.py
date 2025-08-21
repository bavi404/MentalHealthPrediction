from backend.app.core.text_cleaning import clean_text


def test_clean_text_basic():
    assert clean_text("Visit https://example.com!") == "visit"
    assert clean_text(123) == ""

