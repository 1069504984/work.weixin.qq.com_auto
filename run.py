import pytest
from common.send_email import SendEmail


if __name__ == '__main__':
    pytest.main(['-s', 'testcase/test_member_manage.py', '--html=report/html/report.html', '--self-contained-html'])
    SendEmail().send_email('./report/html/report.html')
