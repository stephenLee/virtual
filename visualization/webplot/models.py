from django.db import models

class plot1d(models.Model):
    name = models.CharField(max_length=20, verbose_name='Function Name')
    function = models.CharField(max_length=256,
                   help_text='Enter your function f(x) here.')
    startpoint = models.DecimalField(max_digits=5, 
                                     decimal_places=1,
                                     verbose_name='Starting Point min(x)',
                                     help_text='x max')
    steps = models.DecimalField(max_digits=4,
                                decimal_places=0,
                                verbose_name='Number of Steps on X-Axis',
                                help_text='n')
    endpoint = models.DecimalField(max_digits=5,
                                   decimal_places=1,
                                   verbose_name='Ending Point max(x)',
                                   help_text='x min')

    def __unicode__(self):
        return u'%s' % self.name

    class Meta:
        ordering = ('id',)
        verbose_name = ('1D Function Plot')
        verbose_name_plural = ('1D Function Plots')
                                     
