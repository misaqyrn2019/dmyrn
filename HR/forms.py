from django import forms
from inventory.models import (
    Personnel
	)

class DefinePersonnel(forms.ModelForm):
	class Meta:
		model = Personnel
		fields = ['Id','IdUsers','PersonnelCode','PeriodName','OrganizationName','DayStatus','Date','Login1','Login2',
            'Login3','Logout1','Logout2','Logout3','TimeSpent','LoginDelay','LogoutRush','WorkDeduction','OvertimeLogin',
            'OvertimeLogout','TotalOvertime','Transportation','HourlyLeave','HourlyMission','RoofOvertimeRemained']