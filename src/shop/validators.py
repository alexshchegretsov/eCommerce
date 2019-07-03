from django.core.exceptions import ValidationError

def validate_file_size(value):
    file_size = value.size

    if file_size > 20971520:
        raise ValidationError("The maximum file size can be uploaded is 20MB")
    else:
        return value