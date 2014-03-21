from django.db import models

class Komentar(models.Model):
	nama = models.CharField('Nama', max_length = 100)
	bekerja = models.CharField('Bekerja Di', max_length = 100)
	jabatan = models.CharField('Jabatan', max_length = 100)
	email = models.EmailField('Email', max_length = 100)
	komentar = models.TextField('Komentar', max_length = 255)
	tanggal = models.DateTimeField(auto_now_add=True)
	aktif = models.BooleanField('Ya/Tidak', default=False, help_text= 'Centang jika ingin mengaktifkan')

	def __unicode__(self):
		return self.nama

	class meta:
		db_table = 'testimonial_komentar'