# def cp():
#     try:
#         q=input("请输入需要复制的文件名：")
#         f=open(q,'rb')
#         s=f.read()
#         x=s.decode('utf-8')
#         print(x)
#         f.close()
#         print("提取成功")
#         t=input("请输入新的文件名：")
#         fw=open(t,'w')
#         # x=s.decode('utf-8')
#         fw.write(x)
#         fw.close()
#         print("复制成功")

#     except OSError:
#         print("打开失败")
# cp()


def mycopy(src_filename,dst_filename):
    try:
        fr=open(src_filename,'rb')
        try:
            try:
                fw=open(dst_filename,'wb')
                try:
                    while True:
                        b=fr.read(4096)
                        if not b:
                            break
                        fw.write(b)
                finally:
                    fw.close()
            except OSError:
                print("打开目录文件失败")
        finally:
            fr.close()
    except OSError:
        print("打开源文件失败")


src=input("请输入源文件名")
dst=input("请输入目标名")
mycopy(src,dst)