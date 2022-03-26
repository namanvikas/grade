from tkinter import *

root=Tk()
root.title("Grade")
root.geometry("600x400")

grade3_label=Label(root)
grade10_label=Label(root)
grade15_label=Label(root)



class grade :
    
 def_init_(self, language_arts ,mathematics)
    self.language_arts= language_arts
    self.mathematics= mathematics
    
object_grade3=grade_3(40,50)
object_grade10=grade_3(40,50)
object_grade15=grade_3(40,50)

grade_3_btn=Button(root,text="Grade 3",commond=object_grade3.percantage)
grade_10_btn=Button(root,text="Grade 3",commond=object_grade3.percantage)
grade_15_btn=Button(root,text="Grade 3",commond=object_grade3.percantage)

grade_3_btn.place(relx=0.2,rely=0.2,anchor=CENTER)
grade_10_btn.place(relx=0.2,rely=0.5,anchor=CENTER)
grade_15_btn.place(relx=0.2,rely=0.10,anchor=CENTER)


