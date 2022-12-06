from django.db import models
import datetime

# Create your models here.
class BasicData(models.Model):

	DataID = models.CharField(default='A123456789_20220629131831', max_length=124) # Primary Key

	UserID = models.TextField(default='A123456789') 
	UserName = models.TextField(default='郭怡彤')
	Gender = models.BooleanField(default=True)
	#BirthdayYearItem = models.IntegerField(default=0)
	#BirthdayMonthItem = models.IntegerField(default=0)
	#BirthdayDayItem = models.IntegerField(default=0)
	BirthdayDate = models.DateField(default=datetime.date.today)
	
	class Meta:
		db_table='UserData' # Show in MariaDB

	def __str__(self):
		return self.DataID #表示顯示cName欄位"""



class RecordHrvData(models.Model):

	DataID = models.CharField(default='A123456789_20220629131831', max_length=124) # Primary Key
	# Record Device Info
	MeasureDevice = models.TextField(default='00:30:04:1A:53:BC')
	MeasureTime = models.TextField(default='20220629131831')
	MeasureDuration = models.IntegerField(default=0)
	HandleStatus = models.BooleanField(default=True)	
	# HRV
	HR = models.FloatField(default=0.0)
	MeanNN = models.FloatField(default=0.0)
	N = models.FloatField(default=0.0)
	RRIV = models.FloatField(default=0.0)
	Blance = models.FloatField(default=0.0)
	SDNN = models.FloatField(default=0.0)
	ANS = models.FloatField(default=0.0)
	SYM = models.FloatField(default=0.0)
	VAG = models.FloatField(default=0.0)
	TP = models.FloatField(default=0.0)
	SDNNZ = models.FloatField(default=0.0)
	ANSZ = models.FloatField(default=0.0)
	SYMZ = models.FloatField(default=0.0)
	VAGZ = models.FloatField(default=0.0)
	TPZ = models.FloatField(default=0.0)
	SYMModulation = models.FloatField(default=0.0)
	RWaveValidity = models.FloatField(default=0.0)
	History = models.TextField(default=' ')
	Remark = models.TextField(default=' ')
	Suggest = models.TextField(default=' ') 
	SpO2 = models.IntegerField(default=0)
	RMSSD = models.IntegerField(default=0)
	AF = models.IntegerField(default=0)

	class Meta:
		db_table='RecordData'

	def __str__(self):
		return self.DataID #表示顯示cName欄位"""



# Report Table
class PdfReport(models.Model):
	DataID = models.CharField(default='A123456789_20220629131831', max_length=124) # Primary Key
	PdfBinaryData = models.BinaryField()

	class Meta:
		db_table='PdfReport'

	def __str__(self):
		return self.DataID #表示顯示cName欄位"""



class EcgData(models.Model):
	DataID = models.CharField(default='A123456789_20220629131831', max_length=124) # Primary Key
	EcgBinaryData = models.BinaryField()

	class Meta:
		db_table='EcgData'

	def __str__(self):
		return self.DataID #表示顯示cName欄位"""
