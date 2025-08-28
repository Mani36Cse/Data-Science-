class Univariate_class():
    def Univariate(data_set):
        Qual=[]
        Quan=[]
        for y in data_set.columns:
            if data_set[y].dtype=='O':
                Qual.append(y)
            else:
                Quan+=[y]
        return Qual,Quan

    def univeriate(data_set,quan):
        Describe=pd.DataFrame(index=["Mean","Median","Mode","Q1:25%","Q2:50%","Q3:75%","Q4:100%","IQR","1.5rule","Lesser","Greater","Min","Max"], columns=quan)
        for Columns in Describe:
            Describe.loc["Mean",Columns]=data_set[Columns].mean()
            Describe.loc["Median",Columns]=data_set[Columns].median()
            Describe.loc["Mode",Columns]=data_set[Columns].mode()[0]
            Describe.loc["Q1:25%",Columns]=data_set.describe()[Columns]["25%"]
            Describe.loc["Q2:50%",Columns]=data_set.describe()[Columns]["50%"]
            Describe.loc["Q3:75%",Columns]=data_set.describe()[Columns]["75%"]
            Describe.loc["Q4:100%",Columns]=data_set.describe()[Columns]["max"]
            Describe.loc["IQR",Columns]=Describe.loc["Q3:75%",Columns]-Describe.loc["Q1:25%",Columns]
            Describe.loc["1.5rule",Columns]=1.5*Describe.loc["IQR",Columns]
            Describe.loc["Lesser",Columns]=Describe.loc["Q1:25%",Columns]-Describe.loc["1.5rule",Columns]
            Describe.loc["Greater",Columns]=Describe.loc["Q3:75%",Columns]+Describe.loc["1.5rule",Columns]
            Describe.loc["Min",Columns]=data_set[Columns].min()
            Describe.loc["Max",Columns]=data_set[Columns].max()
        return  Describe
#not done
    def outlier_replacement(): 
    for column in Lesser:
        data_set[column][data_set[column]<Describe.loc["Lesser",column]]=Describe.loc["Lesser",column]
    for column in Greater:
        data_set[column][data_set[column]>Describe.loc["Greater",column]]=Describe.loc["Greater",column]
    return data_set

#not done
def outlier_check(Describe,quan):
    Lesser=[]
    Greater=[]
    for columnName in quan:
        if(Describe.loc["Min",columnName]<Describe.loc["Lesser",columnName]):
            Lesser.append(columnName)
        if(Describe.loc["Max",columnName]>Describe.loc["Greater",columnName]):
            Greater.append(columnName)
    return Lesser,Greater

    def freqTable(columnName,data_set):
        freqTable=pd.DataFrame(columns=["Unique_values","Frequency","Relative Frequency","Cumsum"])
        freqTable["Unique_values"]=data_set[columnName].value_counts().index
        freqTable["Frequency"]=data_set[columnName].value_counts().values
        freqTable["Relative Frequency"]=(freqTable["Frequency"]/103)
        freqTable["Cumsum"]=freqTable["Relative Frequency"].cumsum()
        return freqTable