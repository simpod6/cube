


class Block(object):    
    faces = ["" for _ in range(6)]
    faceMap = {"U": 0, "L": 1, "F": 2, "R": 3, "D": 4, "B": 5}        
    def __init__(self):
        self.setFaces("xxxxxx")        
    
    def setFaces(self, faceColors):
        self.faces = list(faceColors)
    
    def setFace(self, face, color):
        face = face.upper()        
        self.faces[self.faceMap[face]] = color        
    
    def getFace(self, face):
        return self.faces[self.faceMap[face]]
    
    def getFaces(self):
        return "".join(self.faces)
    
    def rotate(self, direction):
        direction = direction.upper()
        
        if direction == 'F':
            self.faces[0], self.faces[2], self.faces[4], self.faces[5] = self.faces[5], self.faces[0], self.faces[2], self.faces[4]            
        elif direction == 'B':
            self.faces[0], self.faces[2], self.faces[4], self.faces[5] = self.faces[2], self.faces[4], self.faces[5], self.faces[0]            
        elif direction == 'L':            
            self.faces[0], self.faces[3], self.faces[4], self.faces[1] = self.faces[3], self.faces[4], self.faces[1], self.faces[0]
        elif direction == 'R':            
            self.faces[0], self.faces[3], self.faces[4], self.faces[1] = self.faces[1], self.faces[0], self.faces[3], self.faces[4]
        elif direction == 'C':            
            self.faces[1], self.faces[2], self.faces[3], self.faces[5] = self.faces[2], self.faces[3], self.faces[5], self.faces[1]
        elif direction == 'A':            
            self.faces[1], self.faces[2], self.faces[3], self.faces[5] = self.faces[5], self.faces[1], self.faces[2], self.faces[3]
        
        
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

class Cube(object):        
    blocks = [ [ [Block() for _ in range(3)] for _ in range(3)] for _ in range(3)]
    def __init__(self):
        pass
    
    def initialize(self, colors):        
        self.setFace("U", colors)
        colorsL = colors[9:12] + colors[18:21] + colors[27:30]
        self.setFace("L", colorsL)
        colorsF = colors[12:15] + colors[21:24] + colors[30:33]
        self.setFace("F", colorsF)
        colorsR = colors[15:18] + colors[24:27] + colors[33:36]
        self.setFace("R", colorsR)
        colorsD = colors[36:45]
        self.setFace("D", colorsD)
        colorsB = colors[45:]
        self.setFace("B", colorsB)
        

    def setFace(self, face, colors):
        face = face.upper()
        if face == "U":
            for x in range(3):
                for y in range(3):                
                    self.blocks[0][x][y].setFace(face, colors[x*3 + y])
        if face == "L":
            for z in range(3):
                for y in range(3):                
                    self.blocks[z][0][y].setFace(face, colors[z*3 + y])
        if face == "F":
            for z in range(3):
                for x in range(3):                
                    self.blocks[z][x][2].setFace(face, colors[z*3 + x])
        if face == "R":
            for z in range(3):
                for y in range(3):                
                    self.blocks[z][2][y].setFace(face, colors[z*3 + y])
        if face == "D":
            for x in range(3):
                for y in range(3):                
                    self.blocks[2][x][y].setFace(face, colors[x*3 + y])
        if face == "B":
            for x in range(3):
                for z in range(3):                
                    self.blocks[z][x][0].setFace(face, colors[x*3 + z])
        
        
        
            
    def getCube(self):
        faceU = self.getFace("U")
        faceL = self.getFace("L")
        faceF = self.getFace("F")
        faceR = self.getFace("R")
        faceD = self.getFace("D")
        faceB = self.getFace("B")
        cubeStr = faceU + \
                  faceL[0:3] + faceF[0:3] + faceR[0:3] + \
                  faceL[3:6] + faceF[3:6] + faceR[3:6] + \
                  faceL[6:9] + faceF[6:9] + faceR[6:9] + \
                  faceD + \
                  faceB        
        return cubeStr
    
    def getFace(self, face):
        face = face.upper()
        output = ""
        if face == "U":
            for x in range(3):
                for y in range(3):                
                    output += self.blocks[0][x][y].getFace(face)
        elif face == "L":
            for z in range(3):
                for y in range(3):                
                    output += self.blocks[z][0][y].getFace(face)
        elif face == "F":
            for z in range(3):
                for x in range(3):                
                    output += self.blocks[z][x][2].getFace(face)
        elif face == "R":
            for z in range(3):
                for y in range(3):                
                    output += self.blocks[z][2][y].getFace(face)
        elif face == "D":
            for x in range(3):
                for y in range(3):                
                    output += self.blocks[2][x][y].getFace(face)
        elif face == "B":
            for x in range(3):
                for z in range(3):                
                    output += self.blocks[z][x][0].getFace(face)
        
        return output
            
    
    
    
def main():
    mycube = cube()
    mycube.initialize("")        

if __name__ == "__main__":
    main()