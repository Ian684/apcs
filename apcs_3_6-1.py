def main():
    s=str(input())[1:].replace("\n","").replace("L","TL").replace("E","TE").split("T")
    current=0
    st=[[1,-1,-1,0]]
    q=[]
    while current<len(s):
        if s[current][0]=="L":
            st.append([int(s[current][1:]),-1,-1,0])
        elif s[current]=="E":
            st[-1][3]+=abs(st[-1][1]-st[-1][2])*(st[-1][0]-1)#iter
            q=st.pop()
            if st[-1][1]!=-1:st[-1][3]+=abs(st[-1][2]-q[1])*st[-1][0]#前
            else:st[-1][1]=q[1]
            st[-1][2]=q[2]
            st[-1][3]+=q[3]*st[-1][0]#L(x中迴+iter)
        else:
            if st[-1][1]==-1:st[-1][1]=int(s[current])
            if st[-1][2]!=-1:
                st[-1][3]+=abs(int(s[current])-st[-1][2])*st[-1][0]#中迴
            st[-1][2]=int(s[current])
        current+=1
    print(st[-1][3])
main()