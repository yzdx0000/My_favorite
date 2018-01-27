#!/usr/local/bin/python3
# -*- coding:utf-8 -*-

__author__ = 'wx'

'发邮件'

import os, time, sys
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.image import MIMEImage
from ariix_project.tests.test_case.models import ariix_config


# print(sys.getdefaultencoding())


def send_email_att():
    '''带附件的邮件'''
    _user = ariix_config.user
    _pwd = ariix_config.pwd
    _to = ariix_config.Email_Receiver
    print("邮件接收人:  %s"%_to)
    curtime = (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

    msg = MIMEMultipart()
    msg["Subject"] = "Ariix_AutoTest_%s" % (curtime)
    msg["From"] = _user
    msg["To"] = ", ".join(_to)

    msg.attach(MIMEText('各位，请查看附件', 'plain', 'utf-8'))

    report = os.getcwd()+r"\render.html"
    print(report)
    if os.path.exists(report):
        att1 = MIMEText(open(report, 'rb').read(), 'base64', 'utf-8')
        att1["Content-Type"] = 'application/octet-stream'
        att1["Content-Disposition"] = 'attachment; filename="ariix_test_report.html"'
        msg.attach(att1)
    else:
        print("文件不存在")

        # nohup = r'/opt/auto_dbmasker_3.2.1.3/nohup.out'
        # if os.path.exists(nohup):
        #     att2 = MIMEText(open('/opt/auto_dbmasker_3.2.1.3/nohup.out', 'rb').read(), 'base64', 'utf-8')
        #     att2["Content-Type"] = 'application/octet-stream'
        #     att2["Content-Disposition"] = 'attachment; filename="nohup.txt"'
        #     msg.attach(att2)
        # else:
        #     print("nohup.out不存在")
    #
    # png = r'/opt/auto_dbmasker_3.2.1.3/tools/anhua.png'
    # if os.path.exists(png):
    #     fp = open('/opt/auto_dbmasker_3.2.1.3/tools/anhua.png', 'rb')
    #     msgImage = MIMEImage(fp.read())
    #     fp.close()
    #     msgImage.add_header('Content-ID', '<image1>')
    #     msg.attach(msgImage)
    # else:
    #     print("anhua.png不存在")

    try:
        sm = smtplib.SMTP_SSL("smtp.qq.com", 465)
        sm.login(_user, _pwd)
        sm.sendmail(_user, _to, msg.as_string())
        #       sm.quit()
        print("发送成功")
    except smtplib.SMTPException as e:
        print("发送失败")
        raise e
    finally:
        pass


# 查找作为邮件附件的最新测试报告
def find_new_report():
    # test_report = r"C:\Users\Wind.wang\PycharmProjects\Ariix_autotest\ariix_project\tests\report\test_report"
    test_report = os.path.dirname(os.path.dirname(os.getcwd())) + r"\report\test_report"
    # print(test_report)
    lists1 = os.listdir(test_report)
    # print(lists1)
    lists1.sort(key=lambda fn: os.path.getatime(test_report + "\\" + fn))
    directoy_new = os.path.join(test_report, lists1[-1])
    # print(directoy_new)
    lists2 = os.listdir(directoy_new)
    # print(lists2)
    lists2.sort(key=lambda fn: os.path.getatime(directoy_new + "\\" + fn))
    report_new = os.path.join(directoy_new, lists2[-1])
    file_name = report_new.split("\\")[-1]
    # print(report_new)
    return [report_new, file_name]


if __name__ == '__main__':
   # find_new_report()
    send_email_att()
