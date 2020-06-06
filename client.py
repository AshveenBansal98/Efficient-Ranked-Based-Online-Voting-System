import socket
import random

alpha = 128
beta = 32
gamma = 6
a = 128
b = 172
c = 35402
p = 618985588991170176509438226348256815648557761392071
    
def encrypt(x):    
    n = random.randrange(0, 2 **127)
    d = random.randrange(1, 2 ** b)
    cipher = (x << (a + gamma)) + n + p*d
    return str(cipher)


def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 8080))

    while 1:
        inp = int(input("Enter 1 to add a vote and 2 to exit\n"))
        
        if inp == 2:
            break
            
        if inp != 1:
            continue
          
        votes = [int(item) for item in input("Enter the vote shares of 5 persons: \n").split()]
            
        if len(votes) != 5:
            print("Please enter 5 votes")
            continue
           
        if sum(votes) != 100:
            print("Sum should be 100\n")
            continue
        
        flag = 0
        for x in votes:
            flag |= (x < 0)
        
        if flag:
            print("Vote should only be positive\n")
            continue
            
        cipher = ""
        for i in range(0, 5):
            cipher += encrypt(votes[i]) + " "   
        client.send(cipher.encode('utf-8'))
            
    key = str(-1)
    client.send(key.encode('utf-8'))
    client.close()
    
if __name__=="__main__": 
    main() 
