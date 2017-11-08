#---------------------------TuShareInterface------------------------------
#Program develop by other language ex. Cpp ,can use this call tushare API
#@Author Sun Yuan Shan 2017
#@www.programtrader.net
#@Beijing YunQuant S&T Ltd. Co.
#@History Verision
#@2017-11-08 V1.0 提供实时行情接口，以及历史K线接口
#-------------------------------------------------------------------------

import tushare as ts                             #引入tushare库

#获取实时行情函数
#参数：股票代码（字符串型）
#返回：dict
def GetRealTimeQuotes(stockID):
    ret_dict={}                                  #返回dict
    df = ts.get_realtime_quotes(stockID)         #取df从ts中
    ret_dict=df.to_dict(orient="record")         #从df导入dict，导入格式参见Test4.py
    return ret_dict

#获取K线行情函数
#参数：股票代码（字符串型），时间框架（字符串型）
#返回：list每一个行都是一个dict
def GetKData(stockID,timeFrame):
    values_dict={}                               #保存返回列表值dict
    if cmp(timeFrame,"D")==0 or cmp(timeFrame,"d")==0 :
        df = ts.get_hist_data(stockID,ktype='d') #取日线数据
    elif cmp(timeFrame,"W")==0 or cmp(timeFrame,"w")==0 :
        df = ts.get_hist_data(stockID,ktype='w') #取周线数据
    elif cmp(timeFrame,"M")==0 or cmp(timeFrame,"m")==0 :
        df = ts.get_hist_data(stockID,ktype='M') #取月线数据
    elif cmp(timeFrame,"5")==0 :
        df = ts.get_hist_data(stockID,ktype='5') #取5分钟数据
    elif cmp(timeFrame,"15")==0 :
        df = ts.get_hist_data(stockID,ktype='15') #取15分钟数据
    elif cmp(timeFrame,"30")==0 :
        df = ts.get_hist_data(stockID,ktype='30') #取30分钟数据
    elif cmp(timeFrame,"60")==0 :
        df = ts.get_hist_data(stockID,ktype='60') #取60分钟数据    
    values_dict=df.to_dict(orient="record")      #从df导入dict
    li_date=df.index.tolist()                    #从df中导出索引（日期）顺序是一致的
    i=0
    ret_li=[]
    for date_item in li_date :                   #循环遍历list
        new_dict=values_dict[i]                  #将值列表中的元素取出来
        str_len=len(date_item)                   #取字符串长度
        if 10 == str_len :                       #如果字符长度只有10，那么只有日期数据，没有时间数据
            new_dict["date"]=date_item           #保存日期数据
            new_dict["time"]="00:00:00"          #生成时间数据
        elif 19 == str_len :                     #如果字符长度是19，那么还包含有时间数据
            new_dict["date"]=date_item[0:10]     #截取前10个字符
            new_dict["time"]=date_item[-8:]      #截取后9个字符
        #print new_dict
        ret_li.append(new_dict)                  #将dict添加到list之中
        i+=1
    return ret_li