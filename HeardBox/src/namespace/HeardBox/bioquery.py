import uniprot
import uniprot_tools as uni 
from Bio import Entrez
from validate_email import validate_email
import pyDNS
class HeardSet


class BioQuery: 

    def __init__(self, queryType):
        self.queryType = queryType
        self.command = []
    
    
    def send_command(self, command):
        self.command.append(command)

    def  _dat_grab (self, command):
       
       handle = Entrez.efetch(
            db = DB, id = ID, rettype = RETTYPE),
        record = SeqIO.read( handle, RETTYPE ),
            return record

    def lit_search(self, command)
        #parse record for literature references


    def GOgrab(self, commanda)

    def homology
            