import numpy as np 

# data 에 동일한 값이 연속할 때, 차이가 나도록 처리 
def data_diff(data):
    data = np.array(data,np.double)
    diff_ = data[1:] - data[:-1]
    idxs = np.where(diff_==0)
    # print("diffeq" , idxs)
    for idx in reversed(idxs):
        data[idx] = data[idx+1] + 1.e-6
    return data 