from django.contrib import admin
from uQuery.admin import UserModelAdmin
from uQuery.c10004.models import *


admin.site.register(User10004, UserModelAdmin)

class QiTianDaShengAdmin(UserModelAdmin):
        list_filter = []
        def get_queryset(self, request):
                qs = super(QiTianDaShengAdmin, self).get_queryset(request)
                return qs.filter(fwqID="1010")

admin.site.register(QiTianDaSheng, QiTianDaShengAdmin)

class ShuiLianDongTianAdmin(UserModelAdmin):
        list_filter = []
        def get_queryset(self, request):
                qs = super(ShuiLianDongTianAdmin, self).get_queryset(request)
                return qs.filter(fwqID="1011")
        
admin.site.register(ShuiLianDongTian, ShuiLianDongTianAdmin)

class DaNaoTianGongAdmin(UserModelAdmin):
        list_filter = []
        def get_queryset(self, request):
                qs = super(DaNaoTianGongAdmin, self).get_queryset(request)
                return qs.filter(fwqID="1012")

admin.site.register(DaNaoTianGong, DaNaoTianGongAdmin)

class LingXiaoBaoDianAdmin(UserModelAdmin):
        list_filter = []
        def get_queryset(self, request):
                qs = super(LingXiaoBaoDianAdmin, self).get_queryset(request)
                return qs.filter(fwqID="1013")

admin.site.register(LingXiaoBaoDian, LingXiaoBaoDianAdmin)

class PengLaiXianJingAdmin(UserModelAdmin):
        list_filter = []
        def get_queryset(self, request):
                qs = super(PengLaiXianJingAdmin, self).get_queryset(request)
                return qs.filter(fwqID="1014")

admin.site.register(PengLaiXianJing, PengLaiXianJingAdmin)

class FangCunLingTaiAdmin(UserModelAdmin):
        list_filter = []
        def get_queryset(self, request):
                qs = super(FangCunLingTaiAdmin, self).get_queryset(request)
                return qs.filter(fwqID="1015")

admin.site.register(FangCunLingTai, FangCunLingTaiAdmin)

class XieYueSanXingAdmin(UserModelAdmin):
        list_filter = []
        def get_queryset(self, request):
                qs = super(XieYueSanXingAdmin, self).get_queryset(request)
                return qs.filter(fwqID="1016")

admin.site.register(XieYueSanXing, XieYueSanXingAdmin)

class QingHuaXianFuAdmin(UserModelAdmin):
        list_filter = []
        def get_queryset(self, request):
                qs = super(QingHuaXianFuAdmin, self).get_queryset(request)
                return qs.filter(fwqID="1017")

admin.site.register(QingHuaXianFu, QingHuaXianFuAdmin)

class PuTuoXianJingAdmin(UserModelAdmin):
        list_filter = []
        def get_queryset(self, request):
                qs = super(PuTuoXianJingAdmin, self).get_queryset(request)
                return qs.filter(fwqID="1018")

admin.site.register(PuTuoXianJing, PuTuoXianJingAdmin)

class DaLeiYinSiAdmin(UserModelAdmin):
        list_filter = []
        def get_queryset(self, request):
                qs = super(DaLeiYinSiAdmin, self).get_queryset(request)
                return qs.filter(fwqID="1019")

admin.site.register(DaLeiYinSi, DaLeiYinSiAdmin)

class DongTuDaTangAdmin(UserModelAdmin):
        list_filter = []
        def get_queryset(self, request):
                qs = super(DongTuDaTangAdmin, self).get_queryset(request)
                return qs.filter(fwqID="1020")

admin.site.register(DongTuDaTang, DongTuDaTangAdmin)

class YaoChiShengYuAdmin(UserModelAdmin):
        list_filter = []
        def get_queryset(self, request):
                qs = super(YaoChiShengYuAdmin, self).get_queryset(request)
                return qs.filter(fwqID="1021")

admin.site.register(YaoChiShengYu, YaoChiShengYuAdmin)

class TianFuZhiGuoAdmin(UserModelAdmin):
        list_filter = []
        def get_queryset(self, request):
                qs = super(TianFuZhiGuoAdmin, self).get_queryset(request)
                return qs.filter(fwqID="1022")

admin.site.register(TianFuZhiGuo, TianFuZhiGuoAdmin)

class CaiYunZhiNanAdmin(UserModelAdmin):
        list_filter = []
        def get_queryset(self, request):
                qs = super(CaiYunZhiNanAdmin, self).get_queryset(request)
                return qs.filter(fwqID="1023")

admin.site.register(CaiYunZhiNan, CaiYunZhiNanAdmin)

class XiaoLeiYinSiAdmin(UserModelAdmin):
        list_filter = []
        def get_queryset(self, request):
                qs = super(XiaoLeiYinSiAdmin, self).get_queryset(request)
                return qs.filter(fwqID="1024")

admin.site.register(XiaoLeiYinSi, XiaoLeiYinSiAdmin)

class TaiXuHuanJingAdmin(UserModelAdmin):
        list_filter = []
        def get_queryset(self, request):
                qs = super(TaiXuHuanJingAdmin, self).get_queryset(request)
                return qs.filter(fwqID="1025")

admin.site.register(TaiXuHuanJing, TaiXuHuanJingAdmin)

