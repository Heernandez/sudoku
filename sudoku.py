from celda import Celda

TABLERO = [
    [[],[],[], [],[],[], [],[],[]],
    [[],[],[], [],[],[], [],[],[]],
    [[],[],[], [],[],[], [],[],[]],

    [[],[],[], [],[],[], [],[],[]],
    [[],[],[], [],[],[], [],[],[]],
    [[],[],[], [],[],[], [],[],[]],

    [[],[],[], [],[],[], [],[],[]],
    [[],[],[], [],[],[], [],[],[]],
    [[],[],[], [],[],[], [],[],[]]
]

TABLERO_HERMANOS = [
    [[[0,1]],[[0,0]],[], [],[],[], [],[],[]],
    [[],[],[], [],[],[], [],[],[]],
    [[],[],[], [],[],[], [],[],[]],

    [[],[],[], [],[],[], [],[],[]],
    [[],[],[], [],[],[], [],[],[]],
    [[],[],[], [],[],[], [],[],[]],

    [[],[],[], [],[],[], [],[],[]],
    [[],[],[], [],[],[], [],[],[]],
    [[],[],[], [],[],[], [],[],[]]
]  
TABLERO_SUMAS = [  # y , x
    [[11],[11],[10], [10],[ 7],[ 4], [ 4],[10],[11]],
    [[ 8],[10],[14], [20],[ 7],[16], [16],[10],[11]],
    [[ 8],[10],[14], [20],[20],[16], [12],[12],[15]],

    [[13],[ 4],[ 4], [13],[13],[12], [11],[15],[15]],
    [[13],[ 7],[13], [14],[14],[12], [11],[ 7],[ 8]],
    [[17],[ 7],[13], [ 5],[ 4],[10], [ 7],[ 7],[ 8]],

    [[17],[11],[12], [ 5],[ 4],[10], [ 7],[14],[14]],
    [[11],[11],[12], [18],[18],[13], [13],[17],[14]],
    [[10],[10],[ 4], [ 4],[18],[13], [13],[17],[17]]
]

TABLERO_POSIBLES = [
    [[],[],[], [],[],[], [],[],[]],
    [[],[],[], [],[],[], [],[],[]],
    [[],[],[], [],[],[], [],[],[]],

    [[],[],[], [],[],[], [],[],[]],
    [[],[],[], [],[],[], [],[],[]],
    [[],[],[], [],[],[], [],[],[]],

    [[],[],[], [],[],[], [],[],[]],
    [[],[],[], [],[],[], [],[],[]],
    [[],[],[], [],[],[], [],[],[]]
]

class Sudoku:

    def __init__(self):
        self.tablero = TABLERO
        self.inicializeCells()
    
    def inicializeCells(self):
        # Inicializa celdas
        #cont = 1
        for row in range(len(self.tablero)):# iteracion sobre filas
            #iterar sobre columnas
            for column in range(len(self.tablero)):# iteracion sobre columnas
                newCell = Celda()
                newCell.setSiblings(TABLERO_HERMANOS[row][column]) #seteo de coordenadas de los hermanos
                #print(newCell.getSiblings())
                newCell.setTotalAdd(TABLERO_SUMAS[row][column]) # seteo del total de la suma con sus hermanos
                #cont+=1
                self.tablero[row][column] = newCell #guardo el objeto en el tablero

    def calculateNewPossiblesKiller(self):
        # se encarga de actualizar la lista de posibles con la regla killer
        pass

    def setNewPossibility(self):
        # setea un valor final
        pass        

    def calculateNewPossibles(self):
        # se encarga de actualizar la lista de posibles con la regla normal
        pass

    def validateRegularRule(self):
        # valida que se el sudoku actual este cumpliendo las reglas
        # (filas,columnas y cuadro)
        pass

    def validateKillerRule(self):
        # valida que se el sudoku actual este cumpliendo las reglas killer (sumas)
        return True
        pass
    
    def validateRules(self):
        # Valida que se esten cumpliendo las reglas, posterior a un cambio
        # devuelve true si el cambio es correcto y false si debe deshacerse
        pass

    def solveSudokuKiller(self):
        # Inicia la solucion de un sudoku killer
        pass
    
    def solveSudokuRegular(self):
        # Inicia la solucion de un sudoku regular
        pass



sudoku = Sudoku()


celda0_0 = sudoku.tablero[0][0]

celda0_1 = sudoku.tablero[0][1]
print(celda0_0.getValue() if celda0_0.getValue() != "" else "vacio"," ",celda0_0.getValue() if celda0_1.getValue() != "" else "vacio",)

celda0_0.setValue("9")
celda0_1.setValue("9")


print(celda0_0.getValue()," ",celda0_1.getValue())

print(sudoku.validateKillerRule())

#devuelve true si cumple, false sino cumple la regla
# devuelve false si cumple la regla, true si esta fallando la regla

#sudoku.inicializeCells()