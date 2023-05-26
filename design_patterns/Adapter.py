import pandas as pd

class ReadJson:

    def read_json(self):
        return 'read json!'


class ReadXml:

    def read_xml(self):
        return 'read Xml!'


class XmlAdapter(ReadJson):

    def __init__(self, xml):
        self.xml = xml


    def read_json(self):
        return self.xml.read_xml()



xml = ReadXml()
print(xml.read_xml())
new_xml = XmlAdapter(xml)
print(new_xml.read_json())
