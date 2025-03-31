import tkinter

root = tkinter.Tk()
root.title("캔버스 만들기")
#root.geometry- 창의 크기를 지정해줌
canvas=tkinter.Canvas(root, width=800, height=600, bg="beige")

bgimg=tkinter.PhotoImage(file="miko.png")#같은 파일 안에 있어야 불러오기 쉬움
canvas.create_image(400,300,image=bgimg)


canvas.pack()
root.mainloop()