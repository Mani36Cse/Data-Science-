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