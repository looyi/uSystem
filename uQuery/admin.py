from django.contrib import admin

class UserModelAdmin(admin.ModelAdmin):
	list_display = ('time', 'fwqName', 'fwqID', 'usrID', 'usrName')
	list_per_page = 10
	list_filter = ['fwqName']
	search_fields = ['usrName']
	readonly_fields = ('time', 'fwqName', 'fwqID', 'usrID', 'usrName', 'account', 'app', 'device', 'udid', 'usrTel')
	actions = None
