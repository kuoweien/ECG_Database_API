from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from hrvdata import models
from hrvdata.models import BasicData
from hrvdata.models import RecordHrvData
from hrvdata.models import PdfReport
from hrvdata.models import EcgData
from django.views.decorators.csrf import csrf_exempt
import sys
import json
import datetime

# Create your views here.
@csrf_exempt

def create_hrvdata(request):
    if request.method == "POST":
        received_json_data=json.loads(request.body.decode("utf-8"))

        data_id = received_json_data['DataID']
    
        # Record User Info
        user_id = received_json_data['User_Info']['UserIDItem']
        user_name = received_json_data['User_Info']['UserNameItem']
        gender = received_json_data['User_Info']['GenderItem']

        birth_year = received_json_data['User_Info']['BirthdayYearItem']	
        birth_month = received_json_data['User_Info']['BirthdayMonthItem'] 
        birth_day = received_json_data['User_Info']['BirthdayDayItem']
        birth = datetime.date(birth_year, birth_month, birth_day)
        
        # Record Device Info
        device_id = received_json_data['Device_Use_Info']['MeasureDeviceItem']
        measure_time = received_json_data['Device_Use_Info']['MeasureTimeItem'] 
        measure_duration = received_json_data['Device_Use_Info']['MeasureDurationItem']
        handle_status = received_json_data['Device_Use_Info']['HandleStatusItem']
        

        # Record HRV Data
        hr = received_json_data['Hrv_Data']['HRItem']
        rrmean = received_json_data['Hrv_Data']['MeanNNItem']	
        rr = received_json_data['Hrv_Data']['NItem']
        rriv = received_json_data['Hrv_Data']['RRIVItem']
        blance = received_json_data['Hrv_Data']['BlanceItem']
        sdnn = received_json_data['Hrv_Data']['SDNNItem']
        ans = received_json_data['Hrv_Data']['ANSItem']
        sym = received_json_data['Hrv_Data']['SYMItem']
        vag = received_json_data['Hrv_Data']['VAGItem']	
        tp = received_json_data['Hrv_Data']['TPItem']	
        sdnnz = received_json_data['Hrv_Data']['SDNNZItem'] 
        ansz = received_json_data['Hrv_Data']['ANSZItem'] 
        symz = received_json_data['Hrv_Data']['SYMZItem']	
        vagz = received_json_data['Hrv_Data']['VAGZItem']	
        tpz = received_json_data['Hrv_Data']['TPZItem']	
        sym_modulation = received_json_data['Hrv_Data']['SYMModulationItem']	
        rwave_validation = received_json_data['Hrv_Data']['RWaveValidityItem']	
        history_text = received_json_data['Hrv_Data']['HistoryItem']
        remark_text = received_json_data['Hrv_Data']['RemarkItem']
        sugegest_text = received_json_data['Hrv_Data']['SuggestItem']
        spo2 = received_json_data['Hrv_Data']['SpO2Item'] 
        rmssd = received_json_data['Hrv_Data']['RMSSDItem']
        af = received_json_data['Hrv_Data']['AFItem']

        # Record PDF and ECG file
        pdf_str_data = received_json_data['File_Info']['PdfBinaryFileItem']
        pdf_binary_data = bytes(pdf_str_data, 'utf-8')
        ecg_str_data = received_json_data['File_Info']['EcgBinaryFileItem']
        ecg_binary_data = bytes(ecg_str_data, 'utf-8')
        ecg_clip_binary_data = ecg_binary_data[200: len(ecg_binary_data)-200]
	
        try:

            BasicData.objects.create(DataID=data_id, UserID=user_id, UserName=user_name, Gender=gender, BirthdayDate=birth)


            RecordHrvData.objects.create(DataID=data_id,            
            MeasureDevice=device_id, MeasureTime=measure_time, MeasureDuration=measure_duration, HandleStatus=handle_status, 
            HR=hr, MeanNN=rrmean, N=rr, RRIV=rriv, Blance=blance, SDNN=sdnn, ANS=ans, SYM=sym, VAG=vag,TP=tp, SDNNZ=sdnnz, ANSZ=ansz, SYMZ=symz, 
            VAGZ=vagz, TPZ=tpz, SYMModulation=sym_modulation, RWaveValidity=rwave_validation, History=history_text, Remark=remark_text, Suggest=sugegest_text,SpO2=spo2, RMSSD=rmssd,AF=af
            )

            PdfReport.objects.create(DataID=data_id, PdfBinaryData=pdf_binary_data)

            EcgData.objects.create(DataID=data_id, EcgBinaryData=ecg_clip_binary_data)

            discription="success"
        

        except:
            print('Error: {}. {}, line: {}'.format(sys.exc_info()[0],sys.exc_info()[1],sys.exc_info()[2].tb_lineno))

        dic_Response={"Status":discription}
	
    return HttpResponse(json.dumps(dic_Response, indent = 4,ensure_ascii=False), content_type="application/json")


