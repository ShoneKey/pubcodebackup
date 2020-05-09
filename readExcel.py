
import xlrd

class ReadExcel():
    def __init__(self,path,sheetname):
    #打开excel文件，获取workbook对象
        self.workbook=xlrd.open_workbook(path)

    #利用workbook对象获取sheet对象
        self.sheet=self.workbook.sheet_by_name(sheetname)

        self.row_nums = self.sheet.nrows

        self.col_nums = self.sheet.ncols

    #利用sheet对象获取表格数据-两种方式
    #获取某一行Row对象
    # row1=sheet.row(0)
    # print(row1[0].value)
    #获取某一行Rowvalue
    # row2=sheet.row_values(0)
    # print(row2[0])

        self.sheet.cell_value(1,2)
    #定义一个函数，获取指定单元格数据
    def get_value_by_row_colum(self,row,col):
        try:
            return self.sheet.row_values(row - 1)[col - 1]
        except Exception as ec:
            print(ec)

    #获取某行数据
    # row_var=sheet.row_values(0)

    #获取某列数据
    # col_var=sheet.col_values(0)

    #获取当前sheet的行数，列数
    # row_nums=sheet.nrows#取最多数据列的行
    # col_nums=sheet.ncols#取最多数据行的列
    #获取当前sheet所有数据

#定制化输出数据格式
#定制化格式2，保存对象形式的数据

    def get_data(self):
        sheet_data = []
        #确定表头
        headers=self.sheet.row_values(0)
        #获取表头下的数据
        for r in range(1,self.row_nums):
            row_vars=self.sheet.row_values(r)
            tmp_dict=dict(zip(headers,row_vars))
            sheet_data.append(tmp_dict)
        return sheet_data


    def get_data2(self):
        sheet_data=[Cousre(self.sheet.row_values(r)[0],self.sheet.row_values(r)[1]) for r in range(1, self.row_nums)]

        return sheet_data

class Cousre():
    def __init__(self,name,desc):
        self.name=name#课程名称
        self.desc=desc#课程描述

if __name__ == '__main__':
    re=ReadExcel('接口数据.xlsx','课程管理')
    listData=re.get_data2()
    # print(listData[0]['课程名称'])
    print(listData[1].name)
    print(listData[1].desc)