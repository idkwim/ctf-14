import math

def makeNextFraction(fraction):
    (a,b) = fraction
    res=b//a
    a1=b%a
    b1=a
    return res, (a1,b1)

def makeContinuedFraction(fraction):
    (a,b) = fraction
    v=[]
    v.append(0)
    while not a == 1:
        r, fraction = makeNextFraction(fraction)
        (a,b) = fraction
        v.append(r)
    v.append(b)
    return v

def makeIndexedConvergent(sequence, index):
    (a,b)=(1,sequence[index])
    while index>0:
        index-=1
        (a,b)=(b,sequence[index]*b+a)
    return (b,a)

def makeConvergents(sequence):
    r=[]
    for i in range(0,len(sequence)):
        r.append(makeIndexedConvergent(sequence,i))
    return r

def isqrt(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x

def solveQuadratic(a,b,c):
    d = isqrt(b*b - 4*a*c)
    if d*d != b*b - 4*a*c:
         return []
    if (-b+d) % (2*a) != 0 or (-b-d) % (2*a) != 0:
         return []
    p = (-b + d) // (2*a)
    q = (-b - d) // (2*a)
    return [p, q]
    

def wienerAttack(N,e):
    conv=makeConvergents(makeContinuedFraction((e,N)))
    for frac in conv:
        (k,d)=frac
        if k == 0:
            continue
        phiN=((e*d)-1)//k
        roots=solveQuadratic(1, -(N-phiN+1), N)
        if len(roots) == 2:
            p=roots[0]%N
            q=roots[1]%N
            if(p*q==N):
                return p, q

if __name__ == '__main__':
    n = """00:99:4a:5e:2c:23:03:b4:09:43:d9:b7:44:b5:70:
    9e:e6:01:fb:5c:4a:c3:00:cf:a4:4a:76:08:10:7a:
    74:d0:6a:c0:49:63:a3:f8:20:1f:a7:80:13:35:ed:
    d3:f3:23:09:04:25:92:4b:74:f6:ac:39:ee:af:f7:
    b4:a6:bc:aa:24:15:33:fd:5f:57:50:5b:38:86:68:
    f2:4d:8d:65:33:07:45:cc:51:5e:e1:b3:c9:60:16:
    b3:99:c3:5e:ef:ef:06:12:ba:ff:82:76:10:88:11:
    7b:07:e2:5f:92:63:f9:14:98:10:23:31:91:65:d2:
    09:c4:78:4b:c3:7a:92:ed:7f:ec:b4:70:31:7b:3f:
    de:53:43:cd:d9:aa:13:79:4b:74:83:18:92:cf:6e:
    a1:00:2d:7a:3f:76:0f:1b:b3:ed:fb:f6:27:3b:15:
    36:11:27:42:4f:17:12:89:2e:0c:6c:c7:59:b3:c6:
    90:da:8c:61:84:a9:0b:e6:48:6b:8f:25:c7:45:55:
    4c:0a:aa:44:57:64:58:9a:51:77:03:8a:67:cd:73:
    e6:6f:e1:b0:d5:59:e0:bb:be:3e:5b:8d:4a:ee:f7:
    2f:fa:87:4c:c1:61:10:bb:c1:35:c3:e9:92:8c:5f:
    ca:e7:37:81:5f:49:fb:02:3c:64:ed:a6:2a:d2:ed:
    7d:0d:32:24:96:17:dc:51:2d:c5:40:00:6c:0f:05:
    9b:2f:da:eb:3b:0a:e1:c2:b9:61:5d:b7:c8:3b:90:
    9e:22:27:19:45:17:36:e1:f0:7c:39:19:c3:96:5f:
    d9:d0:03:bd:88:13:ec:1e:9c:d5:40:fa:f7:f7:0f:
    72:fe:8f:0f:54:4b:2c:ab:51:a8:a0:62:86:5a:e4:
    f4:6a:05:30:b7:e1:1a:26:4d:71:7f:3c:f1:3b:60:
    18:d0:9d:e1:a0:c2:8e:a2:0c:ee:2a:67:11:da:5d:
    11:5f:d7:1c:09:6d:11:5c:13:f0:b5:e4:0d:94:69:
    6c:67:10:5c:2f:70:9a:e5:d2:fe:0a:c8:58:47:b3:
    c9:01:7a:ce:7d:b2:eb:00:d4:10:d9:d2:da:76:85:
    77:6a:80:99:47:2d:01:79:1c:57:81:0d:16:0a:bd:
    6c:9e:42:02:76:32:0e:b1:1b:80:a0:b2:f5:72:2e:
    20:e9:d8:82:2a:1d:14:3c:97:a6:3e:f8:17:33:e5:
    2f:26:3e:3a:7f:77:b6:90:0b:f9:5d:a2:15:54:4d:
    f5:1e:61:ec:c4:68:f0:37:a2:b3:9c:cf:15:3d:98:
    4b:32:a9:a4:ce:75:7b:bb:38:79:8c:e0:b0:80:f5:
    03:ce:1a:39:6d:47:e1:4c:c4:1b:f1:8e:34:ed:bd:
    91:37:eb"""
    e = """38:0d:01:ed:b6:ec:c7:5e:51:05:6e:f6:0d:ec:80:
    7a:8c:17:35:6e:a6:64:4e:cf:62:c2:b8:57:63:f7:
    9f:a6:5f:1b:54:d4:ff:28:3f:bb:0b:0b:3e:6f:a5:
    71:86:c5:2b:ea:20:e0:96:36:8c:19:41:41:cd:ed:
    75:97:8b:be:14:d2:70:9d:20:14:56:01:d0:dd:6b:
    7e:2d:f0:dd:ed:42:a5:14:d2:98:c6:81:82:28:9b:
    82:41:aa:09:af:eb:e7:f3:d0:a1:87:a6:54:5b:89:
    a0:6c:ee:52:87:e8:25:72:64:e0:4b:d0:96:83:d9:
    b4:b3:b0:4f:2e:a8:67:82:d3:e3:79:e5:01:4f:f6:
    16:20:2c:78:ad:9b:08:01:b6:7e:ee:ea:af:3b:43:
    05:5a:6f:09:6c:9b:fb:11:9f:1b:57:c7:8c:6e:40:
    50:ac:f3:c9:67:7f:93:25:7a:2b:aa:b9:ff:bc:0f:
    56:2f:c6:4d:46:8d:63:9d:b0:90:cd:b6:26:10:12:
    68:fb:c2:86:c5:c9:84:5a:ba:fb:6c:06:fc:06:25:
    90:4c:cf:32:83:7f:b2:fd:5d:16:0d:f8:36:0b:33:
    fe:2f:a5:5f:b4:3f:d4:ba:0b:a6:9d:de:44:f7:2f:
    9e:06:50:9a:63:6e:c8:45:68:57:59:7b:9a:55:30:
    b4:3b:6c:2f:11:03:8c:9f:ce:71:d5:de:bd:7b:63:
    c7:fb:1d:af:7c:84:37:90:93:b1:f9:d8:f5:e1:d4:
    ab:5e:96:e4:87:c4:ac:4c:d1:62:97:67:a5:59:e0:
    fe:95:69:99:75:d3:b2:96:9f:bc:48:e6:c0:52:9b:
    42:e4:50:51:ac:5c:e9:98:b8:a7:77:25:12:dc:32:
    c4:89:02:a9:96:c3:fb:d3:15:96:7b:e6:a4:03:55:
    63:08:8f:3b:be:e7:9d:c3:24:fd:08:3b:2e:52:9f:
    2d:11:4b:ae:5e:6d:ea:53:dd:e3:e5:18:08:1a:4a:
    13:e6:96:b5:0e:d8:a5:1b:ac:56:53:53:a9:8a:6b:
    84:1f:ad:79:8e:97:01:50:62:99:56:a4:81:6b:1d:
    79:68:f6:5c:ef:e7:1b:19:20:73:41:2c:dd:69:c0:
    c2:22:19:a4:9c:58:91:e6:36:66:2a:e3:42:9c:a9:
    c2:a3:a2:9a:89:25:16:74:b3:7c:07:6f:66:24:4b:
    41:fb:22:8c:82:56:89:67:c0:94:0e:45:4f:49:74:
    f6:8d:18:63:f7:39:8d:dd:62:31:fa:e8:c7:ff:6f:
    83:fa:f3:1b:47:2e:75:ae:26:ce:d5:98:19:1b:0f:
    62:7d:c2:75:9e:2a:9a:86:0a:3e:3b:03:ca:f6:8a:
    ac:bf"""

    n = int(n.replace(":","").replace("\n","").replace(" ",""), 16)
    e = int(e.replace(":","").replace("\n","").replace(" ",""), 16)   

    p, q = wienerAttack(n, e)
    print(str(p) + '\n')
    print(str(q) + '\n')
    print(str(e) + '\n')