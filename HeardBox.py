# hello.py
import webbrowser
import numpy as np
import xlwings as xw
import win32api
import Bio
import uniprot_tools as uni 


def std_redirection(fileobj): 
    old = sys.stdout
    sys.stdout = fileobj
    try:
        yield fileobj
    finally:
        sys.stdout = old

def test():                                           #Test Python-Excel Interface is working correctly
    wb = xw.Book.caller()
    wb.sheets[1].range('A1').value = 'Hello World!'

def protGrab():   
    selectedACC = np.array([] , dtype = 'U' )         #Initialises Accession ID array
    selectedTerms = np.array([] , dtype = 'U' )       #Initialises Term ID array
    rownum = 1
    wb = xw.Book.caller()                             #Open Heard Supplementary Table and Select Sheet 4
    sht= wb.sheets['Sheet4']
    for row in range(1, 10):
        for col in range(1, 10):
            
        #if sht.api.OLEObjects("Check Box" + str(checkIter)).Object.Value  == Tru:
        #    np.append(selected, sht.range('B' + str(cellLat)))
            checkCell= 'B' + str(rownum)
            print(checkCell)
            #if sht.range((row,col)).value == True:
            if sht.range(checkCell).options(numbers=lambda x: str(int(x))).value == True: 
                #win32api.MessageBox(wb.app.hwnd, sht.range('C' + str(rownum)).value)
                selectedACC = np.append(selectedACC, sht.range('C' + str(rownum)).options(numbers=lambda x: str(int(x))).value)
                selectedTerms = np.append(selectedTerms, sht.range('D' + str(rownum)).options(numbers=lambda x: str(int(x))).value)
        #checkIter+=1   
            rownum +=1
    #break
    selectedACC = ', '.join(str(e) for e in selectedACC) 
    selectedTerms = ', '.join(str(e) for e in selectedTerm) 
    win32api.MessageBox(wb.app.hwnd, selected)

def download():
    download = True                     #Simple Boolean values for the checkboxes on the excel input form.

def dbSearch():    
    dbSearch = True

def ALIGN():
    ALIGN = True

def BLAST():
    BLAST= True

def pepQuery():
    pepQuery = True

def resetParams():                      #Reset after each form call
    BLAST = False
    ALIGN = False
    download = False
    dbSearch = False    
    pepQuery = False




def ExecuteQuer():
    if len(selectedACC) < 1:
         win32api.MessageBox(wb.app.hwnd, "Valid Accession Numbers are needed for anything other than Literature Database Search!")   #Error Catch
    
    if BLAST == True:                               
        runblast = 1
        
    if ALIGN == True:
        if len(selectedACC) == 1:
            if download == True:
                with open('/' + selectedTerms[0] + '.txt', 'w') as out:
                    with custom_redirection(out):
                        print uni.map(selectedACC[0], f='ACC', t='P_ENTREZGENEID')
        else:
            for i in len(formSelected):
                if download == True:
                    with open('/sequence.txt', 'w') as out:
                        with custom_redirection(out):
                            print uni.map(formSelected[i], f='ACC', t='P_ENTREZGENEID')
                else:

    if dbSearch == True:
        webbrowser.open_new_tab(url[https://www.ncbi.nlm.nih.gov/pubmed/?term= + selectedTerm])

    



   
    