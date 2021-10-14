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
        self.assertEqual(faces, "RWxxOx")
    
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
        cube.initialize(SAMPLE_CUBE)
        self.assertEqual(cube.getCube(), SAMPLE_CUBE)
        
        
    
