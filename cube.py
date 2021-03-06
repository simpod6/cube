import copy
import time

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

class Block(object):    
    faces = ["" for _ in range(6)]
    faceMap = {"U": 0, "L": 1, "F": 2, "R": 3, "D": 4, "B": 5}        
    def __init__(self):
        self.setFaces("......")        
    
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
        
class Cube(object):        
    blocks = [ [ [Block() for _ in range(3)] for _ in range(3)] for _ in range(3)]
    def __init__(self):
        pass
    
    def initialize(self, colors):        
        colorsU = colors[:9]
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
            for y in range(3):
                for x in range(3):                
                    self.blocks[0][x][y].setFace(face, colors[y*3 + x])
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
                    self.blocks[z][2][2-y].setFace(face, colors[z*3 + y])
        if face == "D":
            for y in range(3):
                for x in range(3):                
                    self.blocks[2][x][2-y].setFace(face, colors[y*3 + x])
        if face == "B":
            for z in range(3):
                for x in range(3):                
                    self.blocks[2-z][x][0].setFace(face, colors[z*3 + x])
        
        
        
            
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
            for y in range(3):
                for x in range(3):                
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
                for y in reversed(range(3)):
                    output += self.blocks[z][2][y].getFace(face)
        elif face == "D":
            for y in reversed(range(3)):
                for x in range(3):                
                    output += self.blocks[2][x][y].getFace(face)
        elif face == "B":
            for z in reversed(range(3)):
                for x in range(3):
                    output += self.blocks[z][x][0].getFace(face)
        
        return output
    
    def print(self, face):        
        faceStr = self.getFace(face)
        print(faceStr[0:3])
        print(faceStr[3:6])
        print(faceStr[6:9])
        
    
    def rotate(self, movement):
        
        if movement[0] == 'U':
            face = [ [Block() for _ in range(3)] for _ in range(3)]
            for y in range(3):
                for x in range(3):
                    face[x][y] = copy.deepcopy(self.blocks[0][x][y])            

            if len(movement) == 1:
                face = list(zip(*face))[::-1]
                for x in range(3):
                    for y in range(3):                                            
                        face[x][y].rotate('C')
            elif movement[1] == 'i':
                face = list(zip(*face[::-1]))
                for x in range(3):
                    for y in range(3):
                        face[x][y].rotate('A')

            for y in range(3):
                for x in range(3):
                    self.blocks[0][x][y] = copy.deepcopy(face[x][y])
                    
        if movement[0] == 'R':
            face = [ [Block() for _ in range(3)] for _ in range(3)]
            for y in range(3):
                for x in range(3):
                    face[x][y] = copy.deepcopy(self.blocks[y][2][2-x])            
            if len(movement) == 1:
                face = list(zip(*face))[::-1]
                for x in range(3):
                    for y in range(3):                                            
                        face[x][y].rotate('B')
            elif movement[1] == 'i':
                face = list(zip(*face[::-1]))
                for x in range(3):
                    for y in range(3):
                        face[x][y].rotate('F')
            for y in range(3):
                for x in range(3):
                    self.blocks[y][2][2-x] = copy.deepcopy(face[x][y])
        
        if movement[0] == 'L':
            face = [ [Block() for _ in range(3)] for _ in range(3)]
            for y in range(3):
                for x in range(3):
                    face[x][y] = copy.deepcopy(self.blocks[y][0][x])
                        
            if len(movement) == 1:
                face = list(zip(*face))[::-1]
                for x in range(3):
                    for y in range(3):                                            
                        face[x][y].rotate('F')
            elif movement[1] == 'i':
                face = list(zip(*face[::-1]))
                for x in range(3):
                    for y in range(3):
                        face[x][y].rotate('B')
                                    
            for y in range(3):
                for x in range(3):
                    self.blocks[y][0][x] = copy.deepcopy(face[x][y])
        
        if movement[0] == 'F':
            face = [ [Block() for _ in range(3)] for _ in range(3)]
            for y in range(3):
                for x in range(3):
                    face[x][y] = copy.deepcopy(self.blocks[y][x][2])
                        
            if len(movement) == 1:
                face = list(zip(*face))[::-1]
                for x in range(3):
                    for y in range(3):                                            
                        face[x][y].rotate('R')
            elif movement[1] == 'i':
                face = list(zip(*face[::-1]))
                for x in range(3):
                    for y in range(3):
                        face[x][y].rotate('L')
                                    
            for y in range(3):
                for x in range(3):
                    self.blocks[y][x][2] = copy.deepcopy(face[x][y])        
        
        if movement[0] == 'B':
            face = [ [Block() for _ in range(3)] for _ in range(3)]
            for y in range(3):
                for x in range(3):
                    face[x][y] = copy.deepcopy(self.blocks[y][2-x][0])
                        
            if len(movement) == 1:
                face = list(zip(*face))[::-1]
                for x in range(3):
                    for y in range(3):                                            
                        face[x][y].rotate('L')
            elif movement[1] == 'i':
                face = list(zip(*face[::-1]))
                for x in range(3):
                    for y in range(3):
                        face[x][y].rotate('R')
                                    
            for y in range(3):
                for x in range(3):
                    self.blocks[y][2-x][0] = copy.deepcopy(face[x][y])        
            
        if movement[0] == 'D':
            face = [ [Block() for _ in range(3)] for _ in range(3)]
            for y in range(3):
                for x in range(3):
                    face[x][y] = copy.deepcopy(self.blocks[2][x][2-y])
            
            if len(movement) == 1:
                face = list(zip(*face))[::-1]
                for x in range(3):
                    for y in range(3):                                            
                        face[x][y].rotate('A')
            elif movement[1] == 'i':
                face = list(zip(*face[::-1]))
                for x in range(3):
                    for y in range(3):
                        face[x][y].rotate('C')
                                   
            for y in range(3):
                for x in range(3):
                    self.blocks[2][x][2-y] = copy.deepcopy(face[x][y])
                    
    def sequence(self, movements):
        previousChar = ''
        for char in movements:            
            if char == 'i':
                self.rotate(previousChar + 'i')
                previousChar = ''
            else:
                if previousChar != '':
                    self.rotate(previousChar)
                previousChar = char
        
        if previousChar != '':
            self.rotate(previousChar)
        
                


    
    
def main():
    cube = Cube()
    totalTime = 0
    totalRuns = 100
    
    Start = time.perf_counter()
    for i in range (totalRuns):    
        cube.initialize(SAMPLE_CUBE_2)        
        cube.sequence("BBDBBUFFRRUUFFUURiDBRRFDDFRDiL")
        tic = time.perf_counter()
        cube.sequence("LiDRiFiDDFiRRBiDiRUUFFUURRFFUiBBDiBB")
        toc = time.perf_counter()    
        totalTime += toc - tic
    avgTime = totalTime / totalRuns
    print(f"Total time taken: {totalTime}s")    
    print(f"Average time taken: {avgTime}s")
    print(f"Sequences per second: {1 / avgTime}")

if __name__ == "__main__":
    main()