import pytest
from twttr import shorten

def test_twttr():
    assert(shorten("Rajiuddin"))=="Rjddn"
    assert(shorten("twitter"))=="twttr"
    assert(shorten("Raj12"))=="Rj12"
    assert(shorten("India"))=="nd"
    assert(shorten("Me, & You"))=="M, & Y"