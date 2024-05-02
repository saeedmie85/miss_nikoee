from . import jalali
from django.utils import timezone
def jalali_converter(date):
    print(timezone.localtime(date),'***********')
    date_str= date.strftime('%Y-%m-%d')
    jalali_list=list(jalali.Gregorian(date_str).persian_tuple())
    print(jalali_list)
    months=('فروردین',
            'اردیبهشت',
            'خرداد',
            'تیر',
            'مرداد',
            'شهریور',
            'مهر',
            'ابان',
            'اذر',
            'دی',
            'بهمن',
            'اسفند',)
    jalali_list[1] = months[jalali_list[1]-1]
    print(jalali_list)
    output=f'{jalali_list[2]} {jalali_list[1]} {jalali_list[0]}'
    return output