from wtforms import SelectMultipleField

class NonValidatingSelectField(SelectMultipleField):
    def pre_validate(self, form):
        pass
