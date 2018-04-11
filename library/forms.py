class RenewDocumentForm(forms.Form):
    due_date = forms.DateField(help_text="Enter the date for renewal")
    max_days = 1
    error_outstanding_request = False
    error_limit_of_renewals = False
    return_date = None

    def clean_due_date(self):
        data = self.cleaned_data['due_date']
        # If date from the past
        if data < self.return_date:
            raise ValidationError('Wrong date - date before the return')

        # If the interval is bigger than 2 weeks
        if data > self.return_date + datetime.timedelta(self.max_days):
            raise ValidationError('Wrong date - out of limit borders')

        if self.error_outstanding_request:
            raise ValidationError('Can not renew - there is an outstanding request for this book')

        if self.error_limit_of_renewals:
            raise ValidationError('Can not renew - reached the limit of renewals')

        return data