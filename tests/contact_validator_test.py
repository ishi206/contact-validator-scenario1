import pytest

from src.contact_validator import (
    is_valid_email,
    is_valid_phone,
    mask_email,
    normalize_phone
)


def test_is_valid_email_true():
    email = "student@lpu.in"
    result = is_valid_email(email)
    assert result == True


def test_is_valid_email_type_error():
    with pytest.raises(TypeError):
        is_valid_email(12345)


def test_is_valid_phone_true():
    phone = "555-123-4567"
    result = is_valid_phone(phone)
    assert result == True


def test_mask_email_basic():
    """Test masking a typical email address."""
    # Arrange
    email = "priya@example.com"

    # Act
    result = mask_email(email)

    # Assert
    assert result == "pr***@example.com"

def test_normalize_phone():
    phone = "555-123-4567"
    result = normalize_phone(phone)
    assert result == "5551234567"
def test_is_valid_phone_false():
    phone = "12345"
    result = is_valid_phone(phone)
    assert result == False


def test_mask_email_short_local():
    email = "ab@example.com"
    result = mask_email(email)
    assert result == "a*@example.com"


def test_normalize_phone_invalid():
    with pytest.raises(ValueError):
        normalize_phone("12345")