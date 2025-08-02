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