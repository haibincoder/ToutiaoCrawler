def list_to_txt(list,file_name):
    file = open('c:\\users\\bin\\desktop\\svd\\quchanneng\\'+ file_name +'.txt', 'w')
    for i in list:
        k = ' '.join([str(j) for j in i])
        file.write(k + "\n")
    file.close()