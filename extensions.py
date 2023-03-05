def main():
    name = input("Enter the file name ").strip()
    my_list = []
    doc1 = []
    doc2 = []
    doc4 = []
    s = ''
    s1 = ''
    for i in name:
        my_list.append(i)
    dot_position = dot_check(my_list)
    leng = dot_position + len(my_list)
    while dot_position < 0:
        doc = [my_list[dot_position]]
        for j in doc:
            doc1.append(j)
        dot_position = dot_position + 1
    for i in range(leng):
        doc3 = [my_list[i]]
        doc2 = doc2 + doc3
    len(my_list)
    len(doc2)
    if doc1[0] == '.':
        for u in doc1:
            if u != '.':
                doc4.append(u)

    for r in doc2:
        s = s + r
    for k in doc4:
        s1 = s1 + k

    if(s1=='jpeg' or s1=='jpg'):
        print('image/jpeg',end='')
    elif(s1=='png'):
        print('image/png',end='')
    elif(s1=='gif'):
        print('image/gif',end='')
    elif(s1=='pdf' or s1=='PDF' or s1=='txtpdf'):
        print('application/pdf',end='')
    elif(s1=='zip'):
        print('application/zip',end='')
    elif(s1=='txt'):
        print('text/plain',end='')
    else:
        print('application/octet-stream',end='')





def dot_check(my_list1):
    g = 0
    lenght1 = len(my_list1)
    for j in range(lenght1 - 1):

        if my_list1[j] == '.':
            break
        g += 1
    h = g - lenght1
    return h


main()

