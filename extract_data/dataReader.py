import numpy as np

def data_process(fileName:str):
    '''
    extract data according to rules

    '''
    my_data = np.genfromtxt(fileName, delimiter=',')
    # print(my_data.shape)
    my_data2 = my_data.T
    # print(my_data2.shape)

    rows,columns = my_data2.shape

    csv1 = np.zeros((rows,8))
    csv1Row = 0
    csv1Column = 0

    csv2 = np.zeros((rows*2,7))
    csv2Row = 0
    csv2Column = 0

    csv3 = np.zeros((rows,6))
    csv3Row = 0
    csv3Column = 0

    row = 0
    column = 0

    while row < rows:
        feature = my_data2[row]
        column = 0
        csv1Column = 0
        csv3Column = 0
        flag = False
        _count = 0
        flag2 = False

        index = feature[column]

        while column < columns:
            if(feature[column]==1e9 and feature[column+1]==1e9):
                column += 2

                if(feature[column]==1):
                    column += 1
                    count = (int)(feature[column])
                    column += 1

                    if(flag2==False):
                        flag2 = True
                        csv1[csv1Row][csv1Column] = index
                        csv1Column += 1

                    for i in range (0,count):
                        csv1[csv1Row][csv1Column] = feature[column]
                        csv1Column += 1
                        column += 1

                elif(feature[column]==2):
                    while(feature[column]!=1e9):
                    
                        if(flag==False):
                            flag = True
                            column += 1
                            count = (int)(feature[column])
                            if(count == 6):
                                _count = 6

                            column += 1
                            csv2Column = 0

                            csv2[csv2Row][csv2Column] = index
                            csv2Column += 1

                            for i in range(0,_count):
                                csv2[csv2Row][csv2Column] = feature[column]
                                csv2Column += 1
                                column += 1
                            # print(csv2Row)
                            csv2Row += 1
                        else:
                            csv2Column = 0

                            csv2[csv2Row][csv2Column] = index
                            csv2Column += 1

                            for i in range(0,_count):
                                csv2[csv2Row][csv2Column] = feature[column]
                                csv2Column += 1
                                column += 1
                            # print(csv2Row)
                            csv2Row += 1

                elif(feature[column]==3):
                    column += 1
                    count = (int)(feature[column])
                    column += 1
                    
                    csv3[csv3Row][csv3Column] = index
                    csv3Column += 1
                        
                    for i in range (0,count):
                        csv3[csv3Row][csv3Column] = feature[column]
                        csv3Column += 1
                        column += 1
                elif(feature[column]==1e9 and feature[column+1]==1e9 and feature[column+2]==1e9):
                    break
                else:
                    print("undefined error")
            else:
                column += 1
    
        row += 1
        csv1Row += 1
        csv3Row += 1

    np.savetxt('test1.csv',csv1,delimiter=',')
    np.savetxt('test2.csv',csv2,delimiter=',')
    np.savetxt('test3.csv',csv3,delimiter=',')


def main():
    data_process('data.csv')

if __name__ == '__main__':
    main()