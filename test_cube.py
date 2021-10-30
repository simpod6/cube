from unittest import TestCase
from cube import Block, Cube

SAMPLE_CUBE = "RRR"\
              "RRR"\
              "RRR"\
           "WWWGGGYYY"\
           "WWWGGGYYY"\
           "WWWGGGYYY"\
              "OOO"\
              "OOO"\
              "OOO"\
              "BBB"\
              "BBB"\
              "BBB"
              
SAMPLE_CUBE_2 = "ABC"\
                "DEF"\
                "GHI"\
             "JKLMNOPQR"\
             "STUVWXYZa"\
             "bcdefghij"\
                "klm"\
                "nop"\
                "qrs"\
                "tuv"\
                "wxy"\
                "z12"

class TestBlock(TestCase):
    
    def setUp(self):
        pass

    def test_block(self):
        block = Block()
        block.setFaces("RWGYOB")
        faces = block.getFaces()
        self.assertEqual(faces, "RWGYOB")
    
    def test_block_set_face(self):
        block = Block()
        block.setFace("U", "R")
        block.setFace("L", "W")
        block.setFace("D", "O")
        faces = block.getFaces()
        self.assertEqual(faces, "RW..O.")
    
    def test_block_set_face_all(self):
        block = Block()
        block.setFace("U", "R")
        block.setFace("L", "W")
        block.setFace("F", "G")
        block.setFace("R", "Y")
        block.setFace("D", "O")
        block.setFace("B", "B")
        faces = block.getFaces()
        self.assertEqual(faces, "RWGYOB")
    
    def test_getFace(self):
        block = Block()
        block.setFaces("RWGYOB")
        self.assertEqual(block.getFace("U"), "R")
        self.assertEqual(block.getFace("L"), "W")
        self.assertEqual(block.getFace("F"), "G")
        self.assertEqual(block.getFace("R"), "Y")
        self.assertEqual(block.getFace("D"), "O")
        self.assertEqual(block.getFace("B"), "B")
    
    def test_rotate_F(self):
        block = Block()
        block.setFaces("RWGYOB")
        block.rotate('F')
        faces = block.getFaces()        
        self.assertEqual(faces, "BWRYGO")
    
    def test_rotate_B(self):
        block = Block()
        block.setFaces("BWRYGO")
        block.rotate('B')
        faces = block.getFaces()        
        self.assertEqual(faces, "RWGYOB")
    
    def test_rotate_R(self):
        block = Block()
        block.setFaces("RWGYOB")
        block.rotate('R')
        faces = block.getFaces()        
        self.assertEqual(faces, "WOGRYB")
        
    def test_rotate_L(self):
        block = Block()
        block.setFaces("WOGRYB")
        block.rotate('L')
        faces = block.getFaces()        
        self.assertEqual(faces, "RWGYOB")
        
    def test_rotate_C(self):
        block = Block()
        block.setFaces("RWGYOB")
        block.rotate('C')
        faces = block.getFaces()        
        self.assertEqual(faces, "RGYBOW") 
    
    def test_rotate_A(self):
        block = Block()
        block.setFaces("RGYBOW")
        block.rotate('A')
        faces = block.getFaces()        
        self.assertEqual(faces, "RWGYOB") 
    
class TestCube(TestCase):        
    def test_cube(self):
        cube = Cube()
        cube.initialize(SAMPLE_CUBE)
        self.assertEqual(cube.getFace("U"), "RRRRRRRRR")
        self.assertEqual(cube.getFace("L"), "WWWWWWWWW")
        self.assertEqual(cube.getFace("F"), "GGGGGGGGG")
        self.assertEqual(cube.getFace("R"), "YYYYYYYYY")
        self.assertEqual(cube.getFace("D"), "OOOOOOOOO")
        self.assertEqual(cube.getFace("B"), "BBBBBBBBB")
        
    def test_cube2(self):
        cube = Cube()
        cube.initialize(SAMPLE_CUBE_2)
        self.assertEqual(cube.getFace("U"), "ABCDEFGHI")
        self.assertEqual(cube.getFace("L"), "JKLSTUbcd")
        self.assertEqual(cube.getFace("F"), "MNOVWXefg")
        self.assertEqual(cube.getFace("R"), "PQRYZahij")
        self.assertEqual(cube.getFace("D"), "klmnopqrs")
        self.assertEqual(cube.getFace("B"), "tuvwxyz12")
    
    def test_cube3(self):
        cube = Cube()
        cube.initialize(SAMPLE_CUBE_2)
        self.assertEqual(cube.getCube(), SAMPLE_CUBE_2)
    
    def test_cube_rotate_U(self):
        cube = Cube()
        cube.initialize(SAMPLE_CUBE_2)        
        cube.rotate("U")        
        self.assertEqual(cube.getCube(), "GDA"\
                                         "HEB"\
                                         "IFC"\
                                      "MNOPQR21z"\
                                      "STUVWXYZa"\
                                      "bcdefghij"\
                                         "klm"\
                                         "nop"\
                                         "qrs"\
                                         "tuv"\
                                         "wxy"\
                                         "LKJ")
    
    def test_cube_rotate_check(self):
        cube = Cube()
        cube.initialize(SAMPLE_CUBE_2)        
        cube.print("R")
        cube.rotate("R")        
        cube.print("R")
        '''
        self.assertEqual(cube.getCube(), "RRR"\
                                         "RRR"\
                                         "RRR"\
                                      "GGGYYYBBB"\
                                      "WWWGGGYYY"\
                                      "WWWGGGYYY"\
                                         "OOO"\
                                         "OOO"\
                                         "OOO"\
                                         "WWW"\
                                         "BBB"\
                                         "BBB")
        '''
    def test_cube_rotate_Ui(self):
        cube = Cube()
        cube.initialize(SAMPLE_CUBE_2)
        cube.rotate("Ui")        
        self.assertEqual(cube.getCube(), "CFI"\
                                         "BEH"\
                                         "ADG"\
                                      "21zJKLMNO"\
                                      "STUVWXYZa"\
                                      "bcdefghij"\
                                         "klm"\
                                         "nop"\
                                         "qrs"\
                                         "tuv"\
                                         "wxy"\
                                         "RQP")
    
    def test_cube_rotate_R(self):
        cube = Cube()
        cube.initialize(SAMPLE_CUBE_2)
        cube.rotate("R")        
        self.assertEqual(cube.getCube(), "ABO"\
                                         "DEX"\
                                         "GHg"\
                                      "JKLMNmhYP"\
                                      "STUVWpiZQ"\
                                      "bcdefsjaR"\
                                         "klv"\
                                         "noy"\
                                         "qr2"\
                                         "tuC"\
                                         "wxF"\
                                         "z1I")
    
    def test_cube_rotate_Ri(self):
        cube = Cube()
        cube.initialize(SAMPLE_CUBE_2)
        cube.rotate("Ri")        
        self.assertEqual(cube.getCube(), "ABv"\
                                         "DEy"\
                                         "GH2"\
                                      "JKLMNCRaj"\
                                      "STUVWFQZi"\
                                      "bcdefIPYh"\
                                         "klO"\
                                         "noX"\
                                         "qrg"\
                                         "tum"\
                                         "wxp"\
                                         "z1s")
        
    def test_cube_rotate_L(self):
        cube = Cube()
        cube.initialize(SAMPLE_CUBE_2)
        cube.rotate("L")        
        self.assertEqual(cube.getCube(), "tBC"\
                                         "wEF"\
                                         "zHI"\
                                      "bSJANOPQR"\
                                      "cTKDWXYZa"\
                                      "dULGfghij"\
                                         "Mlm"\
                                         "Vop"\
                                         "ers"\
                                         "kuv"\
                                         "nxy"\
                                         "q12")
        
    def test_cube_rotate_Li(self):
        cube = Cube()
        cube.initialize(SAMPLE_CUBE)
        cube.rotate("Li")        
        self.assertEqual(cube.getCube(), "GRR"\
                                         "GRR"\
                                         "GRR"\
                                      "WWWOGGYYY"\
                                      "WWWOGGYYY"\
                                      "WWWOGGYYY"\
                                         "BOO"\
                                         "BOO"\
                                         "BOO"\
                                         "RBB"\
                                         "RBB"\
                                         "RBB")        
        
    def test_cube_rotate_F(self):
        cube = Cube()
        cube.initialize(SAMPLE_CUBE_2)
        cube.rotate("F")        
        self.assertEqual(cube.getCube(), "ABC"\
                                         "DEF"\
                                         "dUL"\
                                      "JKkeVMGQR"\
                                      "STlfWNHZa"\
                                      "bcmgXOIij"\
                                         "hYP"\
                                         "nop"\
                                         "qrs"\
                                         "tuv"\
                                         "wxy"\
                                         "z12")
    
    def test_cube_rotate_Fi(self):
        cube = Cube()
        cube.initialize(SAMPLE_CUBE_2)
        cube.rotate("Fi")        
        self.assertEqual(cube.getCube(), "ABC"\
                                         "DEF"\
                                         "PYh"\
                                      "JKIOXgmQR"\
                                      "STHNWflZa"\
                                      "bcGMVekij"\
                                         "LUd"\
                                         "nop"\
                                         "qrs"\
                                         "tuv"\
                                         "wxy"\
                                         "z12")
    
