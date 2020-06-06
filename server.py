import socket
import threading
import os

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind(('127.0.0.1', 8080))
total_votes = [0,0,0,0,0]
serv.listen(5)
alpha = 128
beta = 32
gamma = 6
a = 128
b = 172
c = 35402
p = 618985588991170176509438226348256815648557761392071
cnt = 0
count_lock = threading.Lock()
votes_lock = threading.Lock()

def decrypt(x):
    return ( (x%p) >> (a + gamma))

def connection(conn):
    global cnt
    global total_votes
    try:
        while True:
            data = conn.recv(4096).decode('utf_8')
            votes = [int(item) for item in data.split()]
            if len(votes) == 1:
                conn.shutdown(1)
                return
            if len(votes) == 5:
                count_lock.acquire()
                cnt += 1
                count_lock.release()
                votes_lock.acquire()
                for i in range(0, 5):
                    total_votes[i] += votes[i]
                votes_lock.release()
    except Exception as e:
        print(e)

def showvotes():
    global cnt
    global total_votes
    while 1:
        inp = int(input("Enter 0 to terminate and show votes\n"))
        if inp == 0:
            count_lock.acquire()
            votes_lock.acquire()
            for i in range(0, 5):
                total_votes[i] = decrypt(total_votes[i])
            print(str(cnt) + " people voted") 
            print(total_votes)
            votes_lock.release()
            os._exit(1)
            

def main():
    print_thread = threading.Thread(target=showvotes)
    print_thread.start()
    
    while True:
        conn, addr = serv.accept()
        T = threading.Thread(target=connection, args=(conn,))
        T.start()  
    
if __name__== "__main__": 
    main() 