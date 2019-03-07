#2x2lik matrisin determinantını bulunuz

matris_1=[[1,2,4],[3,4,4]]
matris_2=[[1,2,3],[4,5,6],[7,8,9]]
matris_3=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
matris_1,matris_2
matris_3

def det_from_2_by_2(m_1):
    s_1=m_1[0][0]*m_1[1][1]
    s_2=m_1[0][1]*m_1[1][0]
    s_3=s_1-s_2
    return s_3


def delete_row_col_from_matris(m_1,i,j):
    result=[]
    size_1=(len(m_1))
    size_2=(len(m_1[0]))

    for a in range(size_1):
        if(i==a):
            continue
        row_1=[]
        for b in range(size_2):
            if(b==j):
                continue
            row_1.append(m_1[a][b])
        result.append(row_1)
    return result

def det_from_3_by_3(m_1):

     a_1=m_1[0][0]
     a_2=delete_row_col_from_matris(m_1,0,0)
     a_3=det_from_2_by_2(a_2)
     a_4=a_1*a_3

     b_1=m_1[0][1]
     b_2=delete_row_col_from_matris(m_1,0,1)
     b_3=det_from_2_by_2(b_2)
     b_4=b_1*b_3

     c_1=m_1[0][2]
     c_2=delete_row_col_from_matris(m_1,0,2)
     c_3=det_from_2_by_2(c_2)
     c_4=c_1*c_3
     return a_4-b_4+c_4
matris_2
det_from_3_by_3(matris_2)

#4x4lük matrisin determinantı
def det_from_4_by_4(m_1):
     a_1=m_1[0][0]
     a_2=delete_row_col_from_matris(m_1,0,0)
     a_3=det_from_3_by_3(a_2)
     a_4=a_1*a_3

     b_1=m_1[0][1]
     b_2=delete_row_col_from_matris(m_1,0,1)
     b_3=det_from_3_by_3(b_2)
     b_4=b_1*b_3

     c_1=m_1[0][2]
     c_2=delete_row_col_from_matris(m_1,0,2)
     c_3=det_from_3_by_3(c_2)
     c_4=c_1*c_3

     d_1=m_1[0][3]
     d_2=delete_row_col_from_matris(m_1,0,3)
     d_3=det_from_3_by_3(d_2)
     d_4=d_1*d_3
     return a_4-b_4+c_4-d_4
matris_3
det_from_4_by_4(matris_3)
     
    

     
     
