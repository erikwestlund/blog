from wtforms import SelectMultipleField


class NonValidatingMultiSelectField(SelectMultipleField):
    def pre_validate(self, form):
        pass
