import requests
import pytest

def add_course(data):
    body={
        'action':'add_course',
        'data':data

    }
    resp=requests.post('http://localhost/api/mgr/sq_mgr/',data=body)
    # print(resp.json())
    return resp.json()

#只获取添加课程所需的数据
def get_addCourse_data():
    from read_excel import get_data
    all_datas=get_data('doc/教管系统-测试用例V1.2.xls', '课程管理')
    course_data=[]
    for data in all_datas:
        if data['功能']=='增加课程':
            res=data['请求参数'],data['断言']
            course_data.append(res)

    return  course_data

@pytest.mark.parametrize('params,expect',get_addCourse_data())
def test_addCourse(params,expect):
    actual_retcode = add_course(params)['retcode']
    actual = f'{{"code":{actual_retcode}}}'
    assert expect == actual



@pytest.mark.parametrize('a,b',[(1,1),(1,2),(2,2)])
def test_ddt(a,b):
    assert a==b


