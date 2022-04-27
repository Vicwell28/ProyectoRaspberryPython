from requests.structures import CaseInsensitiveDict
import requests

class requestsAPI:

    def __init__(self, ruta, prefix) -> None:
        self.ruta=ruta
        self.prefix=prefix
        self.endpoint=self.ruta+self.prefix
        self.token="Mzc.SLlbvOp7hByTBdF_sO77J9rttTHPFu645bBhier_1tdFoiE1zUXyu15GbkBS"   
    
    ##----------------------------------------------------------------------------------------------##

    def obtenerToken(self,credenciales,path="login"):
        try: 
            path=self.endpoint+path
            headers = CaseInsensitiveDict()
            headers["Accept"] = "application/json"
            response = requests.post(path,data=credenciales, headers=headers)
            if response.status_code == requests.codes.ok:
                self.token = response.json()['access_token']['token']
                return self.token
            else:
                return "Vacio al obtener token"
        except: 
            return "Algo salio mal";
        
    ##----------------------------------------------------------------------------------------------##

    def getIndex(self, path): 
        path=self.endpoint+path
        headers = CaseInsensitiveDict()
        headers["Accept"] = "application/json"
        headers["Authorization"] = "Bearer %s" % self.token
        response = requests.get(path, headers=headers)
        return response.json()
        
    ##----------------------------------------------------------------------------------------------##

    def getShow(self, path): 
        try:
            path=self.endpoint+path
            headers = CaseInsensitiveDict()
            headers["Accept"] = "application/json"
            headers["Authorization"] = "Bearer %s" % self.token
            response = requests.get(path, headers=headers)
            if response.status_code == requests.codes.ok: 
                return response.json()
            else: 
                return "A123456789lgo salio mal getShow()"
        except: 
            return "Fatal error"
       
    ##----------------------------------------------------------------------------------------------##

    def postStore(self, data, path):
        path=self.endpoint+path
        data = data
        headers = CaseInsensitiveDict()
        headers["Accept"] = "application/json"
        headers["Authorization"] = "Bearer %s" % self.token
        response = requests.post(path,json=data, headers=headers)
        return response.json()

        
    ##----------------------------------------------------------------------------------------------##

    def putUpdate(self, data, path):
        try:
            path=self.endpoint+path
            data = {}
            headers = CaseInsensitiveDict()
            headers["Accept"] = "application/json"
            headers["Authorization"] = "Bearer %s" % self.token
            response = requests.put(path,json=data, headers=headers)
            if response.status_code == requests.codes.ok: 
                return response.json()
            else: 
                return "Algo salio mal putUpdate()"
        except: 
            return "Fatal error"

    ##----------------------------------------------------------------------------------------------##

    def delDestroy(self, path):
        try:
            path=self.endpoint+path
            data = {}
            headers = CaseInsensitiveDict()
            headers["Accept"] = "application/json"
            headers["Authorization"] = "Bearer %s" % self.token
            response = requests.delete(path,json=data, headers=headers)
            if response.status_code == requests.codes.ok: 
                return response.json()
            else: 
                return "Algo salio mal delDestroy()"
        except: 
            return "Fatal error"