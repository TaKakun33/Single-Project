# ==================================================Validate Input==================================================
        
def validate(input_str):
    if input_str.isdigit():
        return int(input_str)
    else:
        return float(input_str)
    
def validate_age(input_value):
    if int(input_value) in range(1,101):
        return int(input_value)
    else:
        return False
    
def validate_tall(input_value):
    if validate(input_value) in range(1,251):
        return validate(input_value)
    else:
        return False
    
def validate_weight(input_value):
    if validate(input_value) in range(1,151):
        return validate(input_value)
    else:
        return False

def validate_matrix(input_value):
    try:
        return validate(input_value)
    except (TypeError, ValueError, AttributeError):
        return 0 
# ==================================================Suit Game==================================================
  
def Suit_Game(Input_Player,Input_Robot): 
    output = lambda player,robot : (player == '1' and robot == '3') or (player == '2' and robot == '1') or (player == '3' and robot == '2')
    
    if output(Input_Player,Input_Robot):
        return 'You win'
    elif Input_Player == Input_Robot:
      return "Draw!"
    else:
        return 'You Lose'

def convert_Suit(Player):
  if Player == "1" :
    return "Gunting"
  elif Player == "2" :
    return "Batu"
  elif Player == "3" :
    return "Kertas"

# ==================================================temperatur convert==================================================
  
def convensi_suhu (output,Input,degre):
  if Input == 'C':
      if output == 'Re':
          return  round(((4/5) * degre),3)
      elif output == 'F':
          return  round(((9/5) * degre  +  32),3)
      elif output == 'K':
          return round((degre  +  273),3)
      else:
        return degre
      
  elif Input == 'Re':
      if output == 'C':
          return  round(((5/4) * degre),3)
      elif output == 'F':
          return  round(((9/4) * degre  +  32),3)
      elif output == 'K':
          return  round((((5/4) * degre) + 273),3)
      else:
        return degre
      
  elif Input == 'F':
      if output == 'C':
          return  (round((5/9) * (degre - 32)),3)
      elif output == 'Re':
          return  round(((4/9) * (degre - 32)),3)
      elif output == 'K':
          return  round((((5/9) * (degre - 32)) + 273),3)
      else:
        return degre
      
  elif Input == 'K':
      if output == 'C':
          return  round((degre - 273),3)
      elif output == 'Re':
          return  round(((4/5) * (degre - 273)),3)
      elif output == 'F':
          return  round((((9/5) * (degre - 273)) + 32),3)
      else:
        return degre

# ==================================================Life calculator==================================================

def Calori(umur,kelamin,berat):
    if umur > 60 :
        if kelamin == 'l':
            return round(((13.5 * berat) + 487), 2)
        elif kelamin == 'p':
            return round(((10.5 * berat) + 596), 2)

    elif umur > 30 :
        if kelamin == 'l':
            return round(((11.6 * berat) + 879), 2)
        elif kelamin == 'p':
            return round(((8.7 * berat) + 829)), 2

    elif umur > 18 :
        if kelamin == 'l':
            return round(((15.3 * berat) + 679), 2)
        elif kelamin == 'p':
            return round(((14.7 * berat) + 496), 2)

    elif umur > 10 :
        if kelamin == 'l':
            return round(((17.5 * berat) + 651), 2)
        elif kelamin == 'p':
            return round(((12.2 * berat) + 746), 2)

    elif umur > 3 :
        if kelamin == 'l':
            return round(((22.7 * berat) + 495), 2)
        elif kelamin == 'p':
            return round(((22.5 * berat) + 499), 2)

    else:
        if kelamin == 'l':
            return round(((60.9 * berat) - 54), 2)
        elif kelamin == 'p':
            return round(((61 * berat) - 51), 2)

def ideal_body(kelamin,tinggi):
    if kelamin == 'l':
        return round((tinggi - 100) - ((tinggi - 100) * 0.1))
    elif kelamin == 'p':
        return round((tinggi - 100) - ((tinggi - 100) * 0.15))

def IMT(berat,tinggi):
    imt =  round(berat / ((tinggi/100)**2), 3)
    return imt

def Category(imt):
    if imt >= 27.1:
        return "Very Fat"
    elif imt >= 25.1:
        return "Fat"
    elif imt >= 18.5:
        return "Normal"
    elif imt >= 17:
        return "Thin"
    else:
        return "Very Thin"
    
# ==================================================Binary Calculator==================================================
def Decimal_to_Biner(x):
    bit = ''
    underbit = '.'

    Split_input = x.split('.')
    if len(Split_input)== 2:     
        input_1 = int(Split_input[0])
        input_2 = float('0.' + Split_input[1])
    else:
        input_1 = int(Split_input[0])
        input_2 = 0
        underbit = ''
        
    while(input_1):
        bit = bit + str(input_1 % 2)
        input_1 = input_1 // 2
        
    while(input_2):
        input_2 = input_2 * 2
        if input_2 >= 1:
            input_2 = input_2 - 1
            underbit = underbit + '1'
        else:
            underbit = underbit + '0'
            
    bit = bit[::-1] 
    underbit = '%.24s' % underbit # untuk membatasi jumlah biner di belakang koma
    return bit + underbit

# biner ke Desimal
def Biner_to_Decimal(x):
    underdeci = 0
    deci = 0

    Split_input = x.split('.')
    if len(Split_input)== 2:     
        input_1 = Split_input[0]
        input_2 = Split_input[1]
    else:
        input_1 = Split_input[0]
        input_2 = ''
    jumlah_bit = len(input_1) - 1

    for i in input_1:
            if i == '1':
                deci = deci + 2**(jumlah_bit)
                jumlah_bit = jumlah_bit - 1
            elif i == '0':
                deci = deci + 0
                jumlah_bit = jumlah_bit - 1
            
    jumlah_bit = 1
    for i in input_2:
        if i == '1':
            underdeci = underdeci + 2**(-jumlah_bit)
            jumlah_bit = jumlah_bit + 1
        elif i == '0':
            underdeci = underdeci + 0
            jumlah_bit = jumlah_bit + 1
            
    return str(deci + underdeci)

def Decimal_to_Octal(x):
    bit = ''
    underbit = '.'

    Split_input = x.split('.')
    if len(Split_input)== 2:     
        input_1 = int(Split_input[0])
        input_2 = float('0.' + Split_input[1])
    else:
        input_1 = int(Split_input[0])
        input_2 = 0
        underbit = ''
        
    while(input_1):
            bit = bit + str(input_1 % 8)
            input_1 = input_1 // 8
        
    while(input_2):
        if len(underbit) < 18:
            input_2 = str(input_2 * 8)
            Split_input_2 = input_2.split('.')
            underbit = underbit + Split_input_2[0]
            input_2 = float("0." + Split_input_2[1])
        else:
            break
            
    bit = bit[::-1] 
    underbit = '%.24s' % underbit # untuk membatasi jumlah biner di belakang koma
    return bit + underbit

def Octal_to_Decimal(x):
    underoctal = 0
    octal = 0

    Split_input = x.split('.')
    if len(Split_input)== 2:     
        input_1 = Split_input[0]
        input_2 = Split_input[1]
    else:
        input_1 = Split_input[0]
        input_2 = ''
    jumlah_bit = len(input_1) - 1

    for i in input_1:
        octal = (int(i) * (8 ** jumlah_bit)) + octal
        jumlah_bit = jumlah_bit - 1

    for i in input_2:
        underoctal = (float(i) * (8 ** jumlah_bit)) + underoctal
        jumlah_bit = jumlah_bit - 1
        
    return str(octal + underoctal)

def Decimal_to_Hexa(x):
    bit = ''
    underbit = '.'
    hexa = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']

    Split_input = x.split('.')
    if len(Split_input)== 2:     
        input_1 = int(Split_input[0])
        input_2 = float('0.' + Split_input[1])
    else:
        input_1 = int(Split_input[0])
        input_2 = 0
        underbit = ''
        
    while(input_1):
            bit = bit + hexa[input_1 % 16]
            input_1 = input_1 // 16
        
    while(input_2):
        if len(underbit) < 18:
            input_2 = str(input_2 * 16)
            Split_input_2 = input_2.split('.')
            underbit = underbit + hexa[int(Split_input_2[0])]
            input_2 = float("0." + Split_input_2[1])
        else:
            break
            
    bit = bit[::-1] 
    underbit = '%.24s' % underbit # untuk membatasi jumlah biner di belakang koma
    return bit + underbit

def Hexa_to_Decimal(x):
    underhexa = 0
    hexa = 0
    Up9 = { 'A' : 10 ,
            'B' : 11,
            'C' : 12,
            'D' : 13,
            'E' : 14,
            'F' : 15 }
    
    Split_input = x.split('.')
    if len(Split_input)== 2:     
        input_1 = Split_input[0]
        input_2 = Split_input[1]
    else:
        input_1 = Split_input[0]
        input_2 = ''
    jumlah_bit = len(input_1) - 1

    for i in input_1:
        if i in Up9:
            i = Up9.get(i)
        else:
            i = int(i)
        hexa = (i * (16 ** jumlah_bit)) + hexa
        jumlah_bit = jumlah_bit - 1

    for i in input_2:
        if i in Up9:
            i = Up9.get(i)
        else:
            i = int(i)
        underhexa = (float(i) * (16 ** jumlah_bit)) + underhexa
        jumlah_bit = jumlah_bit - 1
        
    return str(hexa + underhexa)

def Binary_Calc(Input, first, last):
    if first == "Decimal":
        if last == "Binary":
            return Decimal_to_Biner(Input)
        elif last == "Octal":
            return Decimal_to_Octal(Input)
        elif last == "Hexadecimal":
            return Decimal_to_Hexa(Input)
        else:
            return Input
        
    elif first == "Binary":
        if last == "Decimal":
            return Biner_to_Decimal(Input)
        elif last == "Octal":
            return Decimal_to_Octal(Biner_to_Decimal(Input))
        elif last == "Hexadecimal":
            return Decimal_to_Hexa(Biner_to_Decimal(Input))
        else:
            return Input
        
    elif first == "Octal":
        if last == "Decimal":
            return Octal_to_Decimal(Input)
        elif last == "Binary":
            return Decimal_to_Biner(Octal_to_Decimal(Input))
        elif last == "Hexadecimal":
            return Decimal_to_Hexa(Octal_to_Decimal(Input))
        else:
            return Input
        
    elif first == "Hexadecimal":
        if last == "Decimal":
            return Hexa_to_Decimal(Input)
        elif last == "Binary":
            return Decimal_to_Biner(Hexa_to_Decimal(Input))
        elif last == "Octal":
            return Decimal_to_Octal(Hexa_to_Decimal(Input))
        else:
            return Input
     
def verivication(Input, first):
    point = Input.count('.')
    if point in [0,1]:
        if first == "Decimal":
            for i in Input:
                if i not in ['0','1','2','3','4','5','6','7','8','9','.']:
                    return False
            return True
        
        elif first == "Binary":
            for i in Input:
                if i not in ['0','1','.']:
                    return False
            return True
        
        elif first == "Octal":
            for i in Input:
                if i not in ['0','1','2','3','4','5','6','7','.']:
                    return False
            return True
        
        elif first == "Hexadecimal":
            for i in Input:
                if i not in ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','.']:
                    return False
            return True
    else:
        return False
            
# ==================================================Matrix==================================================

import numpy as np 

def rank2(a1,a2,b1,b2):
    A = np.array([[a1,a2],
                [b1,b2]])
    return(np.linalg.matrix_rank(A)) 

def rank3(a1,a2,a3,b1,b2,b3,c1,c2,c3):
    A = np.array([[a1,a2,a3],
                [b1,b2,b3],
                [c1,c2,c3]])
    return(np.linalg.matrix_rank(A)) 

def rank4(a1,a2,a3,a4,b1,b2,b3,b4,c1,c2,c3,c4,d1,d2,d3,d4):
    A = np.array([[a1,a2,a3,a4],
                [b1,b2,b3,b4],
                [c1,c2,c3,c4],
                [d1,d2,d3,d4]])
    return(np.linalg.matrix_rank(A)) 

def determinant2(a1,a2,b1,b2):
    A = np.array([[a1,a2],
                [b1,b2]])
    return(round(np.linalg.det(A))) 

def determinant3(a1,a2,a3,b1,b2,b3,c1,c2,c3):
    A = np.array([[a1,a2,a3],
                [b1,b2,b3],
                [c1,c2,c3]])
    return(round(np.linalg.det(A))) 

def determinant4(a1,a2,a3,a4,b1,b2,b3,b4,c1,c2,c3,c4,d1,d2,d3,d4):
    A = np.array([[a1,a2,a3,a4],
                [b1,b2,b3,b4],
                [c1,c2,c3,c4],
                [d1,d2,d3,d4]])
    return(round(np.linalg.det(A))) 
    
# print(determinant2(1,2,3,8))
# print(determinant3(1,2,3,2,4,6,3,6,9))
# print(determinant4(1,2,3,4,2,4,6,8,3,6,9,12,4,8,int("12"),16))
    