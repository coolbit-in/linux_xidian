# coding:utf-8
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
import re
class StatusFileParser():
    '''
    print match_list
    match_list[0] #name
    match_list[1] #idle/busy
    match_list[2] #time
    match_list[3] #success/fail
    match_list[4] #size
    '''
    def __init__(self, file_path):
        self.file_handle = None
        self.distribution_list = []
        with open(file_path, 'r') as self.file_handle:
            re_pattern = r'(\S+)\s+(\S+)\s+(\d+-\d+-\d+ \S+)\s+(\S+)\s+(\S+)'
            match_list = re.findall(re_pattern, self.file_handle.read())
            for item in match_list:
                if item[1] == 'idle':
                    status = item[3]
                else:
                    status = item[1]
                name = item[0]
                time = item[2]
                size = item[4]
                self.distribution_list.append(Distribution(name, status, time, size))

class Distribution():
    '''
    每一个源都是他的对象
    '''
    def __init__(self, name, status, last_rsync_time, size):
        self.name = name
        self.status = status
        self.last_rsync_time = last_rsync_time
        self.size = size
        translate_to_chinese_dict = {'busy': '正在同步', 'success': '同步成功', 'fail': '同步失败'}
        self.status = translate_to_chinese_dict[self.status]


def show_mirrors_status(request):
    parser = StatusFileParser('/srv/log_new/status.log')
    distribution_list = parser.distribution_list
    html_template = get_template('index.html')
    html_context = Context({'distribution_list': distribution_list})
    html  = html_template.render(html_context)
    return HttpResponse(html)

