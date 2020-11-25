from phonenumbers import geocoder, carrier, parse, timezone, phonenumberutil

class Cellphone:
    def __init__(self, nro_cellphone, lang_cellphone):
        self.nro_cellphone = nro_cellphone
        self.lang_cellphone = lang_cellphone
        self.ch_number = self.getChNumber()

    def getChNumber(self):
        return parse(self.nro_cellphone, self.lang_cellphone)


    def check_number_cellphone(self):
        country = geocoder.description_for_number(self.ch_number, self.lang_cellphone)
        return country


    def check_operator_cellphone(self):
        operator = carrier.name_for_number(self.ch_number, self.lang_cellphone)
        return operator


    def check_timezone_cellphone(self):
        tz = timezone.time_zones_for_number(self.ch_number)
        return tz

if __name__ == '__main__':

    list_nro_cellphone = [
        '+5518988063287',
        '+558134233404',
        '+918870990898'
    ]
    list_lang_cellphone = [
        'pt-br',
        'pt-br',
        'RO'
    ]
    for nro_cellphone, lang_cellphone in zip(list_nro_cellphone, list_lang_cellphone):
        try:
            cellphone = Cellphone(nro_cellphone, lang_cellphone)
            cellphone.check_number_cellphone()
            print(f'OPERATOR..: {cellphone.check_operator_cellphone()}')
            print(f'NUMBER..: {cellphone.check_timezone_cellphone()[0]}')
            print('*'*80)
        except phonenumberutil.NumberParseException:
            ...
