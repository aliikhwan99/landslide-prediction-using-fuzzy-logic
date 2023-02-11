
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import skfuzzy as fuzz
from skfuzzy import control as ctrl
from tkinter import *
import numpy as np
import webbrowser

class Calculate:

    def __init__(self):


        # Create object

        window = Tk()

        def callback(url):
          webbrowser.open_new_tab(url)




        # NEW WINDOW-INSTRUCTION
        def openNewWindow(*url):

         # be treated as a new window
         newWindow = Toplevel(window)

         # Toplevel widget
         newWindow.title("INSTRUCTION")
         bg = PhotoImage(file = "INS4.png")

         # Create Canvas
         canvas1 = Canvas( newWindow, width = 400,
                 height = 400)

         canvas1.pack(fill = "both", expand = True)


        # Display image
         canvas1.create_image( 0, 0, image = bg,
                     anchor = "nw")


         # sets the geometry of toplevel
         newWindow.geometry("1366x780")


         link = Label(newWindow, text="www.LandslideDetectionSystem.com",font=('Helveticabold', 15), fg="blue", cursor="hand2")
         link.pack()
         link.bind("<Button-1>", lambda e:
         callback("https://docs.google.com/document/d/1tvIQKiJSivKY6mCO6dRdN3tI3rcnP1oNcMk8kyVGEtA/edit"))



         newWindow.mainloop()



        def update():
          window.destroy()
          Calculate()



        # Add image file
        bg = PhotoImage( file = "backgroundL10.png")

        # Show image using label
        label1 = Label( window, image = bg)
        label1.place(x = 0,y = 0)



        window.title("LANDSLIDE VULNERABILITY CALCULATION")
        window.geometry('1366x780')


        # variables to store inputs
        self.pv = StringVar()
        self.interest_rate = StringVar()
        self.term = StringVar()
        self.term2 = StringVar()
        self.term3 = StringVar()


        # varianbles for outputs
        self.total = StringVar()

        # Add cog variable
        self.cog = StringVar()
        self.result= StringVar()


        Button(window, bg= "#ffff1a" ,text="INSTRUCTION", width = 12,height = 1,  command=openNewWindow).grid(row=917,column=259, padx= (0,0), pady=30)
        # text boxes to hold inputs and outputs
        Label(window, text=None).grid(row=917,column=259,padx=(250,0), pady=30)#TO CREATE WHITESPACE
        Label(window, text=None).grid(row=918,column=259,padx=(250,0), pady=30)
        #Label(window, text=None).grid(row=919,column=259,padx=(250,0), pady=30)
        Entry(window, textvariable = self.pv ,
              justify=CENTER).grid(row=928,column=250 ,padx=(255,0), pady=25)
        Entry(window, textvariable = self.interest_rate,
              justify=CENTER).grid(row=930,column=250, padx=(255,0), pady=25)
        Entry(window, textvariable = self.term,
              justify=CENTER).grid(row=950,column=250, padx=(250,0), pady=25)
        Entry(window, textvariable = self.term2,
              justify=CENTER).grid(row=970,column=250, padx=(250,0), pady=25)
        Entry(window, textvariable = self.term3,
              justify=CENTER).grid(row=990,column=250, padx=(250,0), pady=25)
        Label(window, textvariable = self.total,
            font="Helvetica 12 bold",
            justify=CENTER).grid(row=1000,column=250, padx =(250,0), pady=30)
        Label(window, textvariable = self.cog,
            font="Helvetica 12 bold",
            justify=CENTER).grid(row=1000,column=253, padx =(253,0), pady=30)

        Button(window, text="CALCULATE CENTROID", width = 22,height = 3,  command=self.calcPayment).grid(row=1001,column=250, padx= (250,0), pady=30)
        Label(window, textvariable = self.result, font="Helvetica 12 bold",justify=CENTER).grid(row=1001,column=253, padx =(250,0), pady=30)
        Button(window, text="REFRESH", width = 24,height = 3,  command=update).grid(row=1001,column=254, padx= (254,0), pady=30)


        window.mainloop()


    def calcPayment(self):
      #try:

        pv = int(self.pv.get())
        rate = int(self.interest_rate.get())
        term = int(self.term.get())
        term2 = int(self.term2.get())
        term3 = int(self.term3.get())
        result = str(self.result.get())

        # Generate universe variables
        # Antecedent
        rainfall = ctrl.Antecedent(np.arange(0, 101, 1), 'rainfall')
        landslope = ctrl.Antecedent(np.arange(0, 101, 1), 'landslope')
        topSoilMoist = ctrl.Antecedent(np.arange(0, 101, 1), 'topSoilMoist')
        botSoilMoist = ctrl.Antecedent(np.arange(0, 101, 1), 'botSoilMoist')
        vibration = ctrl.Antecedent(np.arange(0, 11, 1), 'vibration')

        # Consequent
        landslide = ctrl.Consequent(np.arange(0, 300, 1), 'landslide')

        # Generate fuzzy membership functions
        #Rainfall
        rainfall['low'] = fuzz.trapmf(rainfall.universe, [0, 0, 30, 50])
        rainfall['medium'] = fuzz.trimf(rainfall.universe, [30, 50, 70])
        rainfall['high'] = fuzz.trapmf(rainfall.universe, [50, 70, 100, 100])

        # Landslope
        landslope['flat'] = fuzz.trapmf(landslope.universe, [0, 0, 20, 30])
        landslope['sloping'] = fuzz.trimf(landslope.universe, [20, 30, 40])
        landslope['steep'] = fuzz.trapmf(landslope.universe, [30, 40, 100, 100])

        # Top soil moist
        topSoilMoist['low'] = fuzz.trapmf(topSoilMoist.universe, [0, 0, 30, 40])
        topSoilMoist['medium'] = fuzz.trimf(topSoilMoist.universe, [30, 35, 40])
        topSoilMoist['high'] = fuzz.trapmf(topSoilMoist.universe, [30, 40, 100, 100])

        # Bot soil moist
        botSoilMoist['low'] = fuzz.trapmf(botSoilMoist.universe, [0, 0, 30, 40])
        botSoilMoist['medium'] = fuzz.trimf(botSoilMoist.universe, [30, 35, 40])
        botSoilMoist['high'] = fuzz.trapmf(botSoilMoist.universe, [30, 40, 100, 100])

        # Vibration
        vibration['low'] = fuzz.trapmf(vibration.universe, [0, 0, 2, 4])
        vibration['medium'] = fuzz.trimf(vibration.universe, [3, 4, 5])
        vibration['high'] = fuzz.trapmf(vibration.universe, [3, 5, 10, 10])

        # Landslide vulnerability
        landslide['very safe'] = fuzz.trapmf(landslide.universe, [0, 0, 40, 75])
        landslide['relatively safe'] = fuzz.trapmf(landslide.universe, [50, 95, 130, 165])
        landslide['relatively potential'] = fuzz.trapmf(landslide.universe, [90, 110, 140, 150])
        landslide['potential'] = fuzz.trapmf(landslide.universe, [125, 190, 210, 225])
        landslide['very potential'] = fuzz.trapmf(landslide.universe, [235, 240, 250, 270])




        """# Fuzzy Rules"""

        rule1 = ctrl.Rule(rainfall['low'] & landslope['flat'] & topSoilMoist['medium'] & botSoilMoist['high'] & vibration['low'], landslide['relatively potential'])
        rule2 = ctrl.Rule(rainfall['low'] & landslope['flat'] & topSoilMoist['high'] & botSoilMoist['high'] & vibration['high'], landslide['relatively potential'])
        rule3 = ctrl.Rule(rainfall['low'] & landslope['flat'] & topSoilMoist['low'] & botSoilMoist['high'] & vibration['medium'], landslide['relatively safe'])
        rule4 = ctrl.Rule(rainfall['low'] & landslope['flat'] & topSoilMoist['medium'] & botSoilMoist['medium'] & vibration['high'], landslide['relatively safe'])
        rule5 = ctrl.Rule(rainfall['low'] & landslope['flat'] & topSoilMoist['low'] & botSoilMoist['medium'] & vibration['medium'], landslide['relatively safe'])

        rule6 = ctrl.Rule(rainfall['medium'] & landslope['steep'] & topSoilMoist['low'] & botSoilMoist['medium'] & vibration['high'], landslide['potential'])
        rule7 = ctrl.Rule(rainfall['low'] & landslope['flat'] & topSoilMoist['low'] & botSoilMoist['medium'] & vibration['medium'], landslide['relatively safe'])
        rule8 = ctrl.Rule(rainfall['low'] & landslope['flat'] & topSoilMoist['low'] & botSoilMoist['high'] & vibration['medium'], landslide['relatively safe'])
        rule9 = ctrl.Rule(rainfall['low'] & landslope['flat'] & topSoilMoist['low'] & botSoilMoist['low'] & vibration['medium'], landslide['very safe'])
        rule10 = ctrl.Rule(rainfall['low'] & landslope['flat'] & topSoilMoist['high'] & botSoilMoist['low'] & vibration['high'], landslide['relatively safe'])

        rule11 = ctrl.Rule(rainfall['high'] & landslope['sloping'] & topSoilMoist['medium'] & botSoilMoist['high'] & vibration['high'], landslide['potential'])
        rule12 = ctrl.Rule(rainfall['medium'] & landslope['steep'] & topSoilMoist['high'] & botSoilMoist['medium'] & vibration['medium'], landslide['potential'])
        rule13 = ctrl.Rule(rainfall['low'] & landslope['flat'] & topSoilMoist['low'] & botSoilMoist['high'] & vibration['medium'], landslide['relatively safe'])
        rule14 = ctrl.Rule(rainfall['low'] & landslope['steep'] & topSoilMoist['medium'] & botSoilMoist['high'] & vibration['high'], landslide['potential'])
        rule15 = ctrl.Rule(rainfall['medium'] & landslope['steep'] & topSoilMoist['medium'] & botSoilMoist['low'] & vibration['high'], landslide['potential'])

        rule16 = ctrl.Rule(rainfall['low'] & landslope['flat'] & topSoilMoist['low'] & botSoilMoist['low'] & vibration['high'], landslide['relatively safe'])
        rule17 = ctrl.Rule(rainfall['low'] & landslope['sloping'] & topSoilMoist['low'] & botSoilMoist['high'] & vibration['high'], landslide['relatively potential'])
        rule18 = ctrl.Rule(rainfall['low'] & landslope['flat'] & topSoilMoist['high'] & botSoilMoist['medium'] & vibration['medium'], landslide['relatively safe'])
        rule19 = ctrl.Rule(rainfall['low'] & landslope['flat'] & topSoilMoist['medium'] & botSoilMoist['low'] & vibration['medium'], landslide['very safe'])
        rule20 = ctrl.Rule(rainfall['medium'] & landslope['sloping'] & topSoilMoist['high'] & botSoilMoist['high'] & vibration['high'], landslide['potential'])

        rule21 = ctrl.Rule(rainfall['low'] & landslope['flat'] & topSoilMoist['low'] & botSoilMoist['high'] & vibration['high'], landslide['relatively potential'])
        rule22 = ctrl.Rule(rainfall['low'] & landslope['flat'] & topSoilMoist['medium'] & botSoilMoist['medium'] & vibration['high'], landslide['relatively safe'])
        rule23 = ctrl.Rule(rainfall['medium'] & landslope['steep'] & topSoilMoist['low'] & botSoilMoist['medium'] & vibration['high'], landslide['potential'])
        rule24 = ctrl.Rule(rainfall['low'] & landslope['flat'] & topSoilMoist['high'] & botSoilMoist['medium'] & vibration['high'], landslide['relatively potential'])
        rule25 = ctrl.Rule(rainfall['low'] & landslope['sloping'] & topSoilMoist['low'] & botSoilMoist['medium'] & vibration['medium'], landslide['relatively safe'])

        rule26 = ctrl.Rule(rainfall['low'] & landslope['sloping'] & topSoilMoist['low'] & botSoilMoist['medium'] & vibration['high'], landslide['relatively potential'])
        rule27 = ctrl.Rule(rainfall['low'] & landslope['steep'] & topSoilMoist['high'] & botSoilMoist['high'] & vibration['high'], landslide['very potential'])
        rule28 = ctrl.Rule(rainfall['low'] & landslope['steep'] & topSoilMoist['high'] & botSoilMoist['medium'] & vibration['high'], landslide['potential'])
        rule29 = ctrl.Rule(rainfall['medium'] & landslope['steep'] & topSoilMoist['high'] & botSoilMoist['medium'] & vibration['high'], landslide['very potential'])
        rule30 = ctrl.Rule(rainfall['medium'] & landslope['steep'] & topSoilMoist['low'] & botSoilMoist['medium'] & vibration['high'], landslide['potential'])

        rule31 = ctrl.Rule(rainfall['low'] & landslope['flat'] & topSoilMoist['low'] & botSoilMoist['low'] & vibration['low'], landslide['very safe'])
        rule32 = ctrl.Rule(rainfall['low'] & landslope['flat'] & topSoilMoist['medium'] & botSoilMoist['high'] & vibration['high'], landslide['relatively potential'])
        rule33 = ctrl.Rule(rainfall['low'] & landslope['flat'] & topSoilMoist['medium'] & botSoilMoist['low'] & vibration['medium'], landslide['very safe'])

        rule34 = ctrl.Rule(rainfall['low'] & landslope['flat'] & topSoilMoist['medium'] & botSoilMoist['low'] & vibration['medium'], landslide['very safe'])
        rule35 = ctrl.Rule(rainfall['high'] & landslope['steep'] & topSoilMoist['low'] & botSoilMoist['low'] & vibration['high'], landslide['potential'])
        rule36 = ctrl.Rule(rainfall['high'] & landslope['sloping'] & topSoilMoist['low'] & botSoilMoist['medium'] & vibration['medium'], landslide['potential'])

        rule37 = ctrl.Rule(rainfall['high'] & landslope['flat'] & topSoilMoist['medium'] & botSoilMoist['low'] & vibration['high'], landslide['potential'])
        rule38 = ctrl.Rule(rainfall['high'] & landslope['steep'] & topSoilMoist['medium'] & botSoilMoist['high'] & vibration['low'], landslide['potential'])
        rule39 = ctrl.Rule(rainfall['high'] & landslope['sloping'] & topSoilMoist['medium'] & botSoilMoist['medium'] & vibration['low'], landslide['potential'])
        rule40 = ctrl.Rule(rainfall['high'] & landslope['flat'] & topSoilMoist['high'] & botSoilMoist['high'] & vibration['low'], landslide['potential'])

        rule41 = ctrl.Rule(rainfall['high'] & landslope['sloping'] & topSoilMoist['high'] & botSoilMoist['high'] & vibration['low'], landslide['potential'])

        """# Control System Creation"""
        vulnerability_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10,
                                         rule11, rule12, rule13, rule14, rule15, rule16, rule17, rule18, rule19, rule20,
                                         rule21, rule22, rule23, rule24, rule25, rule26, rule27, rule28, rule29, rule30,
                                         rule31, rule32, rule33, rule34, rule35, rule36, rule37, rule38, rule39, rule40,
                                         rule41])




        vulnerability = ctrl.ControlSystemSimulation(vulnerability_ctrl)


        vulnerability.input['rainfall'] = pv
        vulnerability.input['landslope'] = rate
        vulnerability.input['topSoilMoist'] = term
        vulnerability.input['botSoilMoist'] = term2
        vulnerability.input['vibration'] = term3


        # CHECK ERROR IF ONE OF THE INPUT ARE MORE THAN MAX
        if pv>100 or rate>100 or term>100 or term2>100 or term3>10:
            messagebox.showerror("ERROR: 1", "One of the input value are more than maximum value, please refresh the page")
            self.update().get()

        # CHECK ERROR IF ONE OF THE INPUT LESS THAN 0
        if pv<0 or rate<0 or term<0 or term2<0 or term3 <0:
          messagebox.showerror("ERROR: 2", "Not accepting negative value, please refresh the page")
          update().get()


        total = pv+rate+term+term2+term3

        if total<43:
             messagebox.showerror("ERROR:3", "Total value cannot less than 43, because the value is unlogical base on previous recorded data, please refresh the page")
             self.window.destroy().get()



        self.total.set( format(total, "8,.2f"))


        if total < 270:



          vulnerability.compute()



          print("TEST",bool(vulnerability.compute()))

          #landslide.view(sim=vulnerability)

          #cog = vulnerability.output['landslide']

          #self.cog.set(format(cog, "8,.2f"))


        else:
          messagebox.showerror("ERROR: 4", "No Rules Found or value more than maximum value, please refresh the page")
          print('Error: No Rules Found')

        cog = vulnerability.output['landslide']

        #assert bool(vulnerability.output['landslide']) == False, "Invalid Value, please refresh and refer to the rules for accurate input"
      #except AssertionError as msg:

       # messagebox.showerror("ERROR: 4", msg)


        print("TEST",bool(cog))

        self.cog.set(format(cog, "8,.2f"))

        # TO DETERMINE THE CLASSIFICATION OF VALNERABILITY
        if cog>235 and cog<=266:
            result="very potential"
        elif cog>125 and cog<=235:
            result="potential"
        elif cog>110 and cog<=150:
         if cog>=90 and cog<=150:
            result="relatively potential"
        elif cog>51 and cog<=165:
            result="relatively safe"
        elif cog>43 and cog<=75:
             result = "very safe"

        self.result.set(result)



        if bool(result) == True and bool(cog) == True :

            print("succesfull")

            rainfall.view()

            landslope.view()

            topSoilMoist.view()

            botSoilMoist.view()

            vibration.view()

            landslide.view(sim=vulnerability)

            print(bool(result))

            print(bool(cog))

        elif bool(result) == False and bool(cog) == True :
             print("Rules not found")
             print(bool(result))
             print(bool(cog))
             messagebox.showerror("ERROR: 5", "No Rules Found, please refresh the page")

        elif bool(result) == True and bool(cog) == False :
             print("Rules not found")
             print(bool(result))
             print(bool(cog))
             messagebox.showerror("ERROR: 6", "No Rules Found, please refresh the page")\

        elif bool(result) == False and bool(cog) == False :
             print("Rules not found")
             print(bool(result))
             print(bool(cog))
             messagebox.showerror("ERROR: 7", "No Rules Found, please refresh the page")


        else:
            print("Rules not found")
            print(bool(result))
            print(bool(cog))
            messagebox.showerror("ERROR: 8", "No Rules Found, please refresh the page")





         #print(vulnerability.output['landslide'])

        #landslide.view()




Calculate()

