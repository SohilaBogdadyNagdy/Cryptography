
#Author : Sohila Bogdady
#Date : 14 April 2016
#The Data Encryption Standard (DES) algorithm, adopted by the U.S. government in July 1977.
#DES is a block cipher that transforms 64-bit data blocks under a 56-bit secret key.
#DES is a "symmetrical" encryption algorithm: same key that is used for encryption is used to decrypt the message.
import sys
class DES ():
    def __init__(self, key):
        self.key = key
        #convert string to byte in python
        if  (len (key) != 8 ):
           raise ValueError ("key should be 8 bytes = 64 bits ")
        elif (len(key) == 8 ):
            
           self.enkey= key.encode (encoding='UTF-8')
           #binary version of key
           self.original= ''.join(format(x, 'b') for x in bytearray(self.enkey))
           print (self.original)
           #print (len (self.original))
           # put original in list
           self.listkey=list (self.original)
           #print (self.listkey)
           self .__pc1method__()
     
    def   __pc1method__(self):
        print (self.listkey)
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
        print (self.C)
                # Calculate the 16 sub keys. Start with i = 1.
        self.createsubkeys()
    def createsubkeys(self) :
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
       #print ("hello in permutation 2 ")
       #print (self.c)
       print (self.c[0][25])
       self.Concat = []
       j=0
       #print (self.c[0])
       #print (self.d[0])
       while (j <= 16 ):
          self.Concat.append (self.c[j] + self.d[j])
          j=j+1
       print (len (self.Concat) )
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
        print (self.Concat[16] )
        print  (self.k[16])



#test
test = DES('encrypte')





