import unittest
from Dial import Dial

class MyTestCase(unittest.TestCase):

    def test_primer_derecha(self):
        dial =  Dial(50)
        dial.rotation(True,20)
        self.assertEqual( 70, dial.x)

    def test_primer_izquierda(self):
        dial =  Dial(50)
        dial.rotation(False,20)
        self.assertEqual( 30, dial.x)

    def test_primer_derecha_superado(self):
        dial = Dial(50)
        dial.rotation(True, 60)
        self.assertEqual(10, dial.x)

    def test_primer_izquierda_superado(self):
        dial = Dial(50)
        dial.rotation(False, 60)
        self.assertEqual(90, dial.x)

    def test_primer_derecha_click(self):
        dial =  Dial(50)
        pasos = dial.rotationWithClick(True,20)
        self.assertEqual( 70, dial.x)
        self.assertEqual(0, pasos)

    def test_primer_izquierda_click(self):
        dial =  Dial(50)
        pasos = dial.rotationWithClick(False,20)
        self.assertEqual( 30, dial.x)
        self.assertEqual(0, pasos)

    def test_primer_derecha_superado_click(self):
        dial = Dial(25)
        pasos = dial.rotationWithClick(True, 199)
        self.assertEqual(24, dial.x)
        self.assertEqual(2, pasos)

    def test_primer_derecha_superado_click_2(self):
        dial = Dial(25)
        pasos = dial.rotationWithClick(True, 200)
        self.assertEqual(25, dial.x)
        self.assertEqual(2, pasos)

    def test_primer_derecha_superado_click_3(self):
        dial = Dial(25)
        pasos = dial.rotationWithClick(True, 201)
        self.assertEqual(26, dial.x)
        self.assertEqual(2, pasos)

    def test_primer_derecha_superado_click_zero(self):
        dial = Dial(50)
        pasos = dial.rotationWithClick(True, 50)
        self.assertEqual(0, dial.x)
        self.assertEqual(0, pasos)

    def test_primer_izquierda_superado_click(self):
        dial = Dial(50)
        pasos = dial.rotationWithClick(False, 60)
        self.assertEqual(90, dial.x)
        self.assertEqual(1, pasos)

    def test_primer_izquierda_superado_click_2(self):
        dial = Dial(50)
        pasos = dial.rotationWithClick(False, 49)
        self.assertEqual(1, dial.x)
        self.assertEqual(0, pasos)

    def test_primer_izquierda_superado_click_3(self):
        dial = Dial(50)
        pasos = dial.rotationWithClick(False, 50)
        self.assertEqual(0, dial.x)
        self.assertEqual(0, pasos)

    def test_primer_izquierda_superado_click_4(self):
        dial = Dial(50)
        pasos = dial.rotationWithClick(False, 51)
        self.assertEqual(99, dial.x)
        self.assertEqual(1, pasos)

    def test_primer_izquierda_superado_click_5(self):
        dial = Dial(50)
        pasos = dial.rotationWithClick(False, 151)
        self.assertEqual(99, dial.x)
        self.assertEqual(2, pasos)

    def test_primer_izquierda_superado_click_5(self):
        dial = Dial(50)
        pasos = dial.rotationWithClick(False, 150)
        self.assertEqual(0, dial.x)
        self.assertEqual(1, pasos)

    def test_primer_izquierda_superado_click_6(self):
        dial = Dial(50)
        pasos = dial.rotationWithClick(False, 149)
        self.assertEqual(1, dial.x)
        self.assertEqual(1, pasos)

    def test_primer_izquierda_superado_click_7(self):
        dial = Dial(0)
        pasos = dial.rotationWithClick(False, 49)
        self.assertEqual(51, dial.x)
        self.assertEqual(0, pasos)

    def test_primer_izquierda_superado_click_zero(self):
        dial = Dial(50)
        pasos = dial.rotationWithClick(False, 50)
        self.assertEqual(0, dial.x)
        self.assertEqual(0, pasos)

if __name__ == '__main__':
    unittest.main()
