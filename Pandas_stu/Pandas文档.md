## ① 2024/8/9 对列进行排序 （知识点） 
- 针对单个列名进行排序
  - df.sort_values(by="列名",ascending=False) ~ by为指定需要排序的列名，ascending 表示排序是否为 True表示升序 False表示降序
- 针对多个列名进行排序
  - df.sort_values(by=["列名1","列名2"]，ascending=[False,True]) ~指定多个列名进行排序，并指定每个列名的排序是升序还是降序