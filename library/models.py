class GiveOut(models.Model):
    """
        Model of giving-out a document to an user
    """
    user = models.ForeignKey('auth.User', on_delete=models.PROTECT)
    patron = models.ForeignKey('PatronInfo', on_delete=models.PROTECT)
    document = models.ForeignKey('Document', on_delete=models.PROTECT)
    document_instance = models.ForeignKey('DocumentInstance', on_delete=models.PROTECT)
    timestamp = models.DateTimeField(auto_now=True)
    renewed_times = models.IntegerField(help_text='Number of renewals made by the user', null=True, default=0)

    class Meta:
        ordering = ('document_instance__due_back',)

    @property
    def is_overdue(self):
        return self.document_instance.is_overdue

    def get_absolute_url(self):
        return reverse('return-document', args=[str(self.id)])

    def get_absolute_renew_url(self):
        return reverse('renew-document', args=[str(self.id)])