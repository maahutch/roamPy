
from pageFunc import pageIterate


class licenses(object):

    def __init__(self, url, header):
        
        self.url = url 
        self.header = header

    def getLicenses(self):

        urlLic = self.url + 'licenses'

        res = pageIterate(urlLic, self.header)

        return(res)


    def getLicenseswRels(self, relations):

        relStr = ','.join([str(item) for item in relations])

        urlLic = self.url + 'licenses?includes=' + relStr

        res = pageIterate(urlLic, headers = self.header)

        return(res)