if __name__ == '__main__':
    st_class = []
    st_mark = []
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        st = [name,score]
        st_mark.append(score)
        st_class.append(st)
    
    min_mark =min(st_mark)
    indexes=[]
    for p in st_mark:
        if p == min_mark:
            indexes.append(st_mark.index(p))
    for q in indexes:
        st_mark.pop(q)
    st_marks = set(st_mark)
    second_min = min(st_marks)
    classified_std = [std[0] for std in st_class if std[1]==second_min]
    classified_std.sort()
    for st in classified_std:
        print(st)
    
