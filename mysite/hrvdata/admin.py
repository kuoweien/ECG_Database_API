from django.contrib import admin 
from .models import BasicData 
from .models import RecordHrvData 
from .models import PdfReport
from .models import EcgData

class basicdataAdmin(admin.ModelAdmin):
   list_display=('DataID', 'UserID', 'UserName', 'Gender', 'BirthdayDate')


class hrvdataAdmin(admin.ModelAdmin):
   list_display=('DataID',	'MeasureDevice', 'MeasureTime', 'MeasureDuration', 'HandleStatus',  
   'HR', 'MeanNN',	'N',	'RRIV',	'Blance',	'SDNN', 'RMSSD','ANS',	'SYM',	'VAG',	'TP',	'SDNNZ', 
   'ANSZ', 'SYMZ',	'VAGZ',	'TPZ',	'SYMModulation',	'RWaveValidity',	'History', 'Remark', 'Suggest', 'SpO2', 'AF'
)

class pdfreportAdmin(admin.ModelAdmin):
   list_display=('DataID', 'PdfBinaryData')

class ecgdataAdmin(admin.ModelAdmin):
   list_display=('DataID', 'EcgBinaryData_col1', 'EcgBinaryData_col2','EcgBinaryData_col3','EcgBinaryData_col4','EcgBinaryData_col5' )



# Register your models here.
admin.site.register(BasicData, basicdataAdmin) 
admin.site.register(RecordHrvData, hrvdataAdmin) 
admin.site.register(PdfReport, pdfreportAdmin) 
admin.site.register(EcgData, ecgdataAdmin) 
