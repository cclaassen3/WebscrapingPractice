from tkinter import *
import urllib.request

class ShowFinder:

    def __init__(self, rootwin):
        
        #initialize the frame
        self.rootwin = rootwin
        self.rootwin.title("Main Menu")
        frame = Frame(self.rootwin)
        frame.grid()
        frame.columnconfigure(0, minsize=250)
        frame.columnconfigure(1, minsize=150)
        frame.rowconfigure(0, minsize=5)
        frame.rowconfigure(1, minsize=30)
        frame.rowconfigure(3, minsize=20)
        frame.rowconfigure(8, minsize=20)

        #create labels with info
        titleLabel = Label(frame, text='Fox Theater: Upcoming Shows & Events')
        titleLabel.grid(row=1, column=0, columnspan=3)


        #create five buttons
        button1 = Button(frame, text="Click here to get the latest info", fg='red3', command=self.retrieveWebsiteInfo)
        button1.grid(row=2, column=0, columnspan=3, sticky=E+W)

        self.thing1 = StringVar(value="")
        self.thing2 = StringVar(value="")
        self.thing3 = StringVar(value="")
        self.thing4 = StringVar(value="")
        
        button2 = Button(frame, text="View Date(s)", fg='midnight blue', command=self.openInfo1)
        button2.grid(row=4, column=1, sticky=E+W)
        entry1 = Entry(frame, textvariable=self.thing1, state='readonly', justify='center')
        entry1.grid(row=4,column=0, sticky=E+W)

        button3 = Button(frame, text="View Date(s)", fg='blue2', command=self.openInfo2)
        button3.grid(row=5, column=1, sticky=E+W)
        entry2 = Entry(frame, textvariable=self.thing2, state='readonly', justify='center')
        entry2.grid(row=5,column=0, sticky=E+W)

        button4 = Button(frame, text="View Date(s)", fg='purple', command=self.openInfo3)
        button4.grid(row=6, column=1, sticky=E+W)
        entry3 = Entry(frame, textvariable=self.thing3, state='readonly', justify='center')
        entry3.grid(row=6,column=0, sticky=E+W)

        button5 = Button(frame, text="View Date(s)", fg='gold', command=self.openInfo4)
        button5.grid(row=7, column=1, sticky=E+W)
        entry4 = Entry(frame, textvariable=self.thing4, state='readonly', justify='center')
        entry4.grid(row=7,column=0, sticky=E+W)

        self.inforetrieved = False


    def retrieveWebsiteInfo(self):

        request = urllib.request.Request('http://foxtheatre.org/shows-and-events/')
        response = urllib.request.urlopen(request)
        the_page = response.read()
        original_text = the_page.decode()
        the_text = original_text.replace("&#8217;","\'")

        #first info
        date1_start = the_text.find('<div class="date"><p>')
        date1_end = the_text.find('</p></div>', date1_start)
        self.date1 = the_text[date1_start+21:date1_end-10]
        title1_start = the_text.find('<h3>')
        title1_end = the_text.find('</h3>')
        self.thing1.set(the_text[title1_start+7:title1_end])
            #to retrieve the link to buy tickets
            #link1_start = the_text.find('<a href=', title1_end)
            #link1_end = the_text.find('</a>', link1_start)
            #self.link1 = the_text[link1_start+9:link1_end-9]
        

        #second info
        date2_start = the_text.find('<div class="date"><p>', title1_end)
        date2_end = the_text.find('</p></div>', date2_start)
        self.date2 = the_text[date2_start+21:date2_end-10]
        title2_start = the_text.find('<h3>', title1_end)
        title2_end = the_text.find('</h3>', title2_start)
        self.thing2.set(the_text[title2_start+7:title2_end-1])

        #third info
        date3_start = the_text.find('<div class="date"><p>', title2_end)
        date3_end = the_text.find('</p></div>', date3_start)
        self.date3 = the_text[date3_start+21:date3_end-10]
        title3_start = the_text.find('<h3>', title2_end)
        title3_end = the_text.find('</h3>', title3_start)
        self.thing3.set(the_text[title3_start+7:title3_end-1])

        #fourth info
        date4_start = the_text.find('<div class="date"><p>', title3_end)
        date4_end = the_text.find('</p></div>', date4_start)
        self.date4 = the_text[date4_start+21:date4_end-10]
        title4_start = the_text.find('<h3>', title3_end)
        title4_end = the_text.find('</h3>', title4_start)
        self.thing4.set(the_text[title4_start+7:title4_end-1])

        self.inforetrieved = True

    def openInfo1(self):
        if self.inforetrieved:
            #create toplevel GUI and display info
            self.rootwin.withdraw()
            self.info1Win = Toplevel()
            self.info1Win.title(self.thing1.get())
            frame = Frame(self.info1Win)
            frame.grid()
            dateLabel = Label(frame, text=self.date1)
            dateLabel.grid(row = 0, column=0)
            returnButton = Button(frame, text='Return to Main Menu', command=self.info1Return)
            returnButton.grid(row=2, column=0)
            frame.rowconfigure(1, minsize=100)
            frame.rowconfigure(3, minsize=20)


    def openInfo2(self):
        if self.inforetrieved:
            #create toplevel GUI and display info
            self.rootwin.withdraw()
            self.info2Win = Toplevel()
            self.info2Win.title(self.thing2.get())
            frame = Frame(self.info2Win)
            frame.grid()
            dateLabel = Label(frame, text=self.date2)
            dateLabel.grid(row = 0, column=0)
            returnButton = Button(frame, text='Return to Main Menu', command=self.info2Return)
            returnButton.grid(row=2, column=0)
            frame.rowconfigure(1, minsize=100)
            frame.rowconfigure(3, minsize=20)


    def openInfo3(self):
        if self.inforetrieved:
            #create toplevel GUI and display info
            self.rootwin.withdraw()
            self.info3Win = Toplevel()
            self.info3Win.title(self.thing3.get())
            frame = Frame(self.info3Win)
            frame.grid()
            dateLabel = Label(frame, text=self.date3)
            dateLabel.grid(row = 0, column=0)
            returnButton = Button(frame, text='Return to Main Menu', command=self.info3Return)
            returnButton.grid(row=2, column=0)
            frame.rowconfigure(1, minsize=100)
            frame.rowconfigure(3, minsize=20)


    def openInfo4(self):
        if self.inforetrieved:
            #create toplevel GUI and display info
            self.rootwin.withdraw()
            self.info4Win = Toplevel()
            self.info4Win.title(self.thing4.get())
            frame = Frame(self.info4Win)
            frame.grid()
            dateLabel = Label(frame, text=self.date4)
            dateLabel.grid(row = 0, column=0)
            returnButton = Button(frame, text='Return to Main Menu', command=self.info4Return)
            returnButton.grid(row=2, column=0)
            frame.rowconfigure(1, minsize=100)
            frame.rowconfigure(3, minsize=20)
        

    def info1Return(self):
        #close current GUI and re-open main menu
        self.info1Win.destroy()
        self.rootwin.deiconify()
        

    def info2Return(self):
        #close current GUI and re-open main menu
        self.info2Win.destroy()
        self.rootwin.deiconify()
        

    def info3Return(self):
        #close current GUI and re-open main menu
        self.info3Win.destroy()
        self.rootwin.deiconify()
        

    def info4Return(self):
        #close current GUI and re-open main menu
        self.info4Win.destroy()
        self.rootwin.deiconify()

        
rootwin = Tk()
app = ShowFinder(rootwin)
rootwin.mainloop()
            
        
