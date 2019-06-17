# hello.py
import webbrowser
import numpy as np
import xlwings as xw
import win32api

def world():
    wb = xw.Book.caller()
    wb.sheets[1].range('A1').value = 'Hello World!'

def protGrab():   
    selected = np.array([] , dtype = 'U' )
    rownum = 1
    wb = xw.Book.caller()
    sht= wb.sheets['Sheet4']
    #sht.autofit()
    #rng = xw.Range(autofit(r))
    #wb.stable = xw.Range('A2:10').table.options(pd.DataFrame, index=False).value
 #   rng = [0, 1, 2, 3, 4, 5, 6, 7]
#    for r in rng:
   # if sht.range('B' + str(rownum)).value == True:
   #     win32api.MessageBox(wb.app.hwnd, sht.range('C' + str(rownum)).value)
    
    for row in range(1, 10):
        for col in range(1, 10):
            
        #if sht.api.OLEObjects("Check Box" + str(checkIter)).Object.Value  == Tru:
        #    np.append(selected, sht.range('B' + str(cellLat)))
            checkCell= 'B' + str(rownum)
            print(checkCell)
            #if sht.range((row,col)).value == True:
            if sht.range(checkCell).options(numbers=lambda x: str(int(x))).value == True: 
                #win32api.MessageBox(wb.app.hwnd, sht.range('C' + str(rownum)).value)
                selected = np.append(selected, sht.range('C' + str(rownum)).options(numbers=lambda x: str(int(x))).value)
        #checkIter+=1   
            rownum +=1
    #break
    selected = ', '.join(str(e) for e in selected)  
    #map(unicode, map(repr,list))
    win32api.MessageBox(wb.app.hwnd, selected)

def formRecieve():
    formSelected = # array for the search terms in the form.
def Download():


def PubMedSearch():    
    userTerms = str(formSelected) 
    webbrowser.open_new_tab(url[https://www.ncbi.nlm.nih.gov/pubmed/?term= + userTerms])
    
def SeqAlign():


def BLAST():

    
    

   
    