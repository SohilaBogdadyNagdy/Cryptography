
#Author : Sohila Bogdady
#Date : 14 April 2016
#The Data Encryption Standard (DES) algorithm, adopted by the U.S. government in July 1977.
#DES is a block cipher that transforms 64-bit data blocks under a 56-bit secret key.
#DES is a "symmetrical" encryption algorithm: same key that is used for encryption is used to decrypt the message.
import sys
class DES ():
    def __init__(self, key,Data):
        self.key = key
        #convert string to byte in python
        if  (len (key) != 8 ):
           raise ValueError ("key should be 8 bytes = 64 bits ")
        elif (len(key) == 8 ):
           self.enkey= key.encode (encoding='UTF-8')
           #binary version of key
           self.original= ''.join(format(x, 'b') for x in bytearray(self.enkey))
           #print (self.original)
           #print (len (self.original))
           # put original in list
           self.listkey=list (self.original)
           #print (self.listkey)
           self.Data = Data
           self .__pc1method__()
           
     
    def   __pc1method__(self):
        """pc1method"""
        #print (self.listkey)
        #to make correct permutation on list key we need add bit at the begining each row 
        self.listkey.insert(0,'0')
        self.listkey.insert(8,'0')
        self.listkey.insert(16,'0')
        self.listkey.insert(24,'0')
        self.listkey.insert(32,'0')
        self.listkey.insert(40,'0')
        self.listkey.insert(48,'0')
        self.listkey.insert(56,'0')
        #print(len(self.listkey)) 
        #print (self.listkey)
        # Perform the following permutation on the 64-bit key.
        pc1=[57, 49 ,41, 33, 25, 17, 9,
                           1 , 58, 50 ,42 ,34 ,26, 18,
                           10, 2, 59, 51, 43, 35, 27,
                           19 ,11, 3, 60, 52 ,44 ,36,
                           63, 55 ,47, 39, 31 ,23 ,15,
                           7, 62, 54 ,46, 38, 30, 22,
                          14 ,6, 61, 53, 45, 37, 29,
                          21 ,13, 5, 28 ,20 ,12, 4,
                     ]
        #sort listkey according to permutation number #1
        self.listkeypc1 =  []
        #print ("test here")
        i = 56
        while (i >= 0):
            self.listkeypc1.append (self.listkey[i])
            i -=8
        i=57
        while (i >=1):
            
            self.listkeypc1.append(self.listkey[i])
            i = i-8
        i=58
        while (i>=2):
            self.listkeypc1.append(self.listkey[i])
            i-=8
        i=59
        while (i>=35):
            
            self.listkeypc1.append(self.listkey[i])
            i-=8
        i=62
        while (i>=6):
            self.listkeypc1.append(self.listkey[i])
            i-=8
        i=61
        while (i>=5):
            self.listkeypc1.append(self.listkey[i])
            i-=8
        i=60
        while (i>=4):
            self.listkeypc1.append(self.listkey[i])
            i-=8
        i=27
        while (i>=3):
            self.listkeypc1.append(self.listkey[i])
            i-=8
                #print (self.listkeypc1)
                #print (len (self.listkeypc1) )
                # Split the permuted key into two halves. The first 28 bits are called C[0] and the last 28 bits are called D[0].
        self.C = self.listkeypc1[:28]
        self.D =self.listkeypc1[28:]
        self.createsubkeys()
        #print (self.C)
        #print ("fff")
                # Calculate the 16 sub keys. Start with i = 1.
        
    def createsubkeys(self) :
        print ("sub keys")
        print ("create 16 subkeys")
        self.c=[self.C]
        self.d=[self.D]
        #print(self.c[0])
        #print (self.d[0])
        #print (len(self.c[0]))
        #print (len (self.d[0]))
        j=1
        while (j <=16):
            if (j==1 or j==2 or j==9 or j==16 ):
                
               copypofcurrentlist=self.c[j-1][:]
               fe=copypofcurrentlist[0]
               shiftingcurrentlist= copypofcurrentlist[1:]
               shiftingcurrentlist.append(fe)
               self.c.append(shiftingcurrentlist)
               j+=1
            else:
                
                copypofcurrentlist=self.c[j-1][:]
                fe=copypofcurrentlist[0]
                se=copypofcurrentlist[1]
                shiftingcurrentlist= copypofcurrentlist[2:]
                shiftingcurrentlist.append(fe)
                shiftingcurrentlist.append(se)
                self.c.append(shiftingcurrentlist)
                j+=1

        #i =0
        # while (i<=16):
        #print (self.c[i])
        #print ("----------")
        #i = i+1
        j=1
        while (j <=16):
            if (j==1 or j==2 or j==9 or j==16 ):
                
               copypofcurrentlist=self.d[j-1][:]
               fe=copypofcurrentlist[0]
               shiftingcurrentlist= copypofcurrentlist[1:]
               shiftingcurrentlist.append(fe)
               self.d.append(shiftingcurrentlist)
               j+=1
            else:
                
                copypofcurrentlist=self.d[j-1][:]
                fe=copypofcurrentlist[0]
                se=copypofcurrentlist[1]
                shiftingcurrentlist= copypofcurrentlist[2:]
                shiftingcurrentlist.append(fe)
                shiftingcurrentlist.append(se)
                self.d.append(shiftingcurrentlist)
                j+=1
        self.Permute_the_concatenation()
       
    def  Permute_the_concatenation(self):    
       print ("hello in permutation 2 ")
       #print (self.c)
       #print (self.c[0][25])
       self.Concat = []
       j=0
       #print (self.c[0])
       #print (self.d[0])
       while (j <= 16 ):
          self.Concat.append (self.c[j] + self.d[j])
          j=j+1
       #print (len (self.Concat) )
       self.__pc2method__()
    def  __pc2method__(self):
        __pc2 = [
		13, 16, 10, 23,  0,  4,
		 2, 27, 14,  5, 20,  9,
		22, 18, 11,  3, 25,  7,
		15,  6, 26, 19, 12,  1,
		40, 51, 30, 36, 46, 54,
		29, 39, 50, 44, 32, 47,
		43, 48, 38, 55, 33, 52,
		45, 41, 49, 35, 28, 31
	]
        #print (len (__pc2))
        #generate k 
        self.k =[]
        j=0
        while (j<=16):
            i=0
            self.mid=[]
            while (i < 48):
                 self. mid.append ( self.Concat[j][__pc2[i]])
                 i+=1
            self.k.append(self.mid)
            j+=1
        self.__processEnteredData()
        #print (self.Concat[16] )
        #print  (self.k[16])
            
    def __processEnteredData(self):
        #block of data must be 64 bit  data
        if  (len (self.Data) ==8 ):
            print ("no  padding ")
            self.MakeListORPadding() 
        elif (len (self.Data) > 8 ):
            print ("block is too large")
            self.MakeListORPadding() 
        else :
            print ("padding")
            self.MakeListORPadding() 
    def  MakeListORPadding (self):
           self.enData= self.Data.encode (encoding='UTF-8')
           #binary version of key
           self.databit= ''.join(format(x, 'b') for x in bytearray(self.enData))
           #print (self.databit)
           self.listDataBits=list (self.databit)
           #print (self.listDataBits)
           #print (len (self.listDataBits))
           #padding 
           while (len (self.listDataBits) < 64 ):
               self.listDataBits.append('0')
           #print (len (self.listDataBits))
           #print (self.listDataBits)
           if (len (self.listDataBits ) > 64):
               self.listDataBits = self.listDataBits[:64]
               #print (self.listDataBits )
               #print (len (self.listDataBits))
               #Perform the following IP on data block.�
               self.Initial_Permutation  ()
    def  Initial_Permutation  (self):
        __ip = [ 57, 49, 41, 33, 25, 17, 9,  1,
	    59, 51, 43, 35, 27, 19, 11, 3,
	    61, 53, 45, 37, 29, 21, 13, 5,
	    63, 55, 47, 39, 31, 23, 15, 7,
	    56, 48, 40, 32, 24, 16, 8,  0,
	    58, 50, 42, 34, 26, 18, 10, 2,
	    60, 52, 44, 36, 28, 20, 12, 4,
	    62, 54, 46, 38, 30, 22, 14, 6
	]
        self.IP = []
        l=0
        while (l <64 ):
            self. IP.append (self.listDataBits [__ip[l]])
            l = l+1
        #print (self.IP)
        self.L=[self.IP[:32]]
        self.R=[self.IP[32:]]
        __expansion = [
		31,  0,  1,  2,  3,  4,
		 3,  4,  5,  6,  7,  8,
		 7,  8,  9, 10, 11, 12,
		11, 12, 13, 14, 15, 16,
		15, 16, 17, 18, 19, 20,
		19, 20, 21, 22, 23, 24,
		23, 24, 25, 26, 27, 28,
		27, 28, 29, 30, 31,  0
	]
        self.ER=[[]]
        self.EL=[[]]
        J=0
        while (J<48):
            self.ER[0].append(self.R[0][ __expansion[J]])
            self.EL[0].append(self.L[0][ __expansion[J]])
            J=J+1
        #print (self.EL)
        #print (len (self.EL[0]))
        self.Sub_key_to_DataBlock()      
    def  Sub_key_to_DataBlock(self):
        #here we Apply the 16 sub keys to the data block.
         j =1
         while (j <=16 ):
            if (j==1 or j==2 or j==9 or j==16 ):
                
               copypofcurrentlist=self.L[j-1][:]
               fe=copypofcurrentlist[0]
               shiftingcurrentlist= copypofcurrentlist[1:]
               shiftingcurrentlist.append(fe)
               self.L.append(shiftingcurrentlist)
               j+=1
            else:
                
                copypofcurrentlist=self.L[j-1][:]
                fe=copypofcurrentlist[0]
                se=copypofcurrentlist[1]
                shiftingcurrentlist= copypofcurrentlist[2:]
                shiftingcurrentlist.append(fe)
                shiftingcurrentlist.append(se)
                self.L.append(shiftingcurrentlist)
                j+=1
         #print (self.L)
         #print (self.L[3])
         j =1
         while (j <=16 ):
            if (j==1 or j==2 or j==9 or j==16 ):
                
               copypofcurrentlist=self.R[j-1][:]
               fe=copypofcurrentlist[0]
               shiftingcurrentlist= copypofcurrentlist[1:]
               shiftingcurrentlist.append(fe)
               self.R.append(shiftingcurrentlist)
               j+=1
            else:
                
                copypofcurrentlist=self.R[j-1][:]
                fe=copypofcurrentlist[0]
                se=copypofcurrentlist[1]
                shiftingcurrentlist= copypofcurrentlist[2:]
                shiftingcurrentlist.append(fe)
                shiftingcurrentlist.append(se)
                self.R.append(shiftingcurrentlist)
                j+=1
         #print (self.R)
         #print (self.R[3])
         """Apply Expanding 48 bit statrting from  i =1"""
         __expansion = [
		31,  0,  1,  2,  3,  4,
		 3,  4,  5,  6,  7,  8,
		 7,  8,  9, 10, 11, 12,
		11, 12, 13, 14, 15, 16,
		15, 16, 17, 18, 19, 20,
		19, 20, 21, 22, 23, 24,
		23, 24, 25, 26, 27, 28,
		27, 28, 29, 30, 31,  0
	]
         
         m = 1
         while (m <= 16):
            J=0
            NowER =[]
            NowEL =[]
            while (J<48):
                NowER.append (self.R[m][__expansion[J]])
                NowEL .append(self.L[m][ __expansion[J]])
                J=J+1
            self.ER.append(NowER)
            self.EL.append(NowEL)
            m+=1
         #print (len (self.ER[0]))
         #Perform Exclusive-or E(R[i-1]) with K[i].
         self.Exclusive_or()
    def  Exclusive_or(self):
        
        """E(R[i-1]) with K[i].
            XOR: If one, and only one, of the expressions evaluates to True, result is True Perform Exclusive-or E(R[i-1]) with K[i].�
        0 xor 0 = 0 , 1 xor 1 = 0 ,  0 xor 1 = 1 , 1 xor 0 = 1
        """
        print (1 ^ 0 )
        print (0 ^ 0)
        print (1^1)
        print (0 ^1)
        i=0
        self.ResultXOR = []
        while (i <=16):
            j = 0
            NowRes = []
            while (j < 48 ):
                currentbit =   int(self.ER [i][j]) ^ int(self.k [i][j]) 
                NowRes.append (currentbit)
                j+=1
            self.ResultXOR.append (NowRes)
            i+=1

        #print ((self.ResultXOR[2]))
        self.BreakResultofXOR()
    def  BreakResultofXOR(self) :
        """Break E(R[i-1]) xor K[i] into eight 6-bit blocks.
         Bits 1-6 are B[1], bits 7-12 are B[2], and so on with bits 43-48 being B[8]."""
        self.B = []
        j=0
        while (j<=16):
            self.CLB = []
            self.CLB .append (self.ResultXOR[j][:6])
            self.CLB .append ( self.ResultXOR[j][6:12])
            self.CLB .append ( self.ResultXOR[j][12:18])
            self.CLB .append ( self.ResultXOR[j][18:24])
            self.CLB .append ( self.ResultXOR[j][24:30])
            self.CLB .append ( self.ResultXOR[j][30:36])
            self.CLB .append ( self.ResultXOR[j][36:42])
            self.CLB .append ( self.ResultXOR[j][42:])
            #print (self.CLB)
            self.B.append (self.CLB)
            j+=1
        #print (self.B)
        self.__Substitution()

    def __Substitution (self):
        """Substitute the values found in the S-boxes for all B[j]. Start with j = 1.
           All values in the S-boxes should be considered 4 bits wide.
          Take the 1st and 6th bits of B[j] together as a 2-bit value (call it m)
          indicating the row in S[j] to look in for the substitution.
          Take the 2nd through 5th bits of B[j] together as a 4-bit value (call it n)
           indicating the column in S[j] to find the substitution."""
        __sbox = [
		# S1
                                   [
		 [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
		 [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
		 [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
		 [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
                                    ],
		# S2
                                   [
		[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
		 [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
		 [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
		 [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
                                    ],
		# S3
                                   [
		[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
		 [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
		 [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
		 [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
                                     ],
		# S4
                                   [
		[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
		 [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
		 [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
		 [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
                                    ],
		# S5
                                   [
		[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
		 [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
		 [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
		 [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
                                     ],
		# S6
                                   [
		[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
		 [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
		 [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
		 [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
                                     ],

		# S7
                                   [
		[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
		 [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
		 [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
		 [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
                                     ],

		# S8
                                   [
		[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
		 [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
		[ 7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
		 [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
                                    ]
	]
        print ( __sbox [0][0][5])

        print (self.B[0])
        m = self.B[0][0][0] + self.B[0][0][5]
        n = self.B[0][0][1:5]
        #print (m)
        #convert m to integer value
        #print (self.B[0][0][5])
        mvalue = ( 2* self.B[0][0][0] ) + (1* self.B[0][0][5])
        print (mvalue )
        #convert n to integer value
        #print (n)
        #print (n[3])
        nvalue = n[3]*1
        nvalue = nvalue + (n[2] *2)
        nvalue = nvalue + (n[1] *4)
        nvalue = nvalue + (n[0] *8 )
        print (nvalue )
        
        
        
        
         



        
            
            
                
        
  
                
        
                
        
        

      
                             

        
        
        
               


           
           
        

    
            
            
            
        



#test
test = DES('encrypte','mydataaaaaaaa')





