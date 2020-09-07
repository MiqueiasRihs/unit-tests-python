import unittest

class VerificarPangramaTests(unittest.TestCase):
    def test_metodo_de_teste(self):
        # Arrange
        frase = "Zebras caolhas de Java querem mandar fax para moça gigante de New York"

        #Act
        frase_eh_pangrama = verificar_pangrama(frase)

        #Assert
        self.assertEqual(True, frase_eh_pangrama)

        