def textfile_read(path, encoding="utf-8"):
    '''

    Načtení textového souboru

    :param path: cesta k souboru (string)
    :param encoding: kódování (string)
    :return: data v podobě string
    '''
    try:
        with open(path, "r", encoding=encoding) as file:
            data = file.read()
    except FileNotFoundError as error:
        print("Soubor nebyl nalezen")
        data = False
    except Exception as error:
        print("Chyba nacteni souboru: " + error + type(error))
        data = False
    finally:
        # print("Tohle se provede vždy")
        pass
    return data


def textfile_write(path, text="", encoding="utf-8"):
    '''

        Načtení textového souboru

        :param path: cesta k souboru (string)
        :param text: textová data (string)
        :param encoding: kódování (string)
        :return: data v podobě string
        '''
    try:
        with open(path, mode="w", encoding=encoding) as file:
            file.write(text)
            file.close()
            return True
    except TypeError as error:
        print("Zadan spatny datovy typ")
        return False
    except Exception as error:
        print("Chyba zapisu do souboru: " + error + type(error))
        return False