import numpy as np
import matplotlib.pyplot as plt


def main():
    ry2eV=13.605*2
    a=float(input("Largezza buca (Bohr):\t"))
    n=int(input("Numero punti di griglia:\t"))
    h=a/(n-1)
    v=np.zeros((n),dtype=np.float64)
    vk=int(input("Tipo di Potenziale: 1 Piatto 2 Gradino\t"))
    if(vk==1):
        v[:]=0.
    elif(vk==2):
        for i in range(n):
            if(i>n/2): 
                v[i]=1.
    
    m=np.zeros((n-2,n-2),dtype=np.float64)
    
    for i in range(0,n-2):
        m[i,i]=(-2.0*(-0.5)/h**2+v[i])
    for i in range(0,n-3):
        m[i,i+1]=(-0.5)/h**2
    for i in range(1,n-2):
        m[i,i-1]=(-0.5)/h**2

#   print(m)
    e, w = np.linalg.eigh(m)

    
#   for i in range(n-2):
#       print("Energia calcolata (eV):\t"+str(e[i]*ry2eV ),"\t e quella di una buca piatta (ev):\t"+str(np.pi**2/(2*a**2)*(i+1)**2*ry2eV))

    nump=int(input("Numeri di auto-funzioni da stampare"))
    fig, ax = plt.subplots()
    fig2, ax2 = plt.subplots()
    fig3, ax3 = plt.subplots()

    
    lx=np.zeros((n,nump),dtype=np.float64)
    ly=np.zeros((n,nump),dtype=np.float64)
    for i in range(n):
        lx[i,:]=i*h
    ly[0,:]=0
    ly[n-1,:]=0
    line=[]
    for ip in range(nump):
        for j in range(n-2):
            ly[j+1]=w[j,ip]**2
       
        plt.plot(lx[:,ip],ly[:,ip])

    ax.set( xlabel='X [Bohr]')
    ax.legend()


    ax2.set_title("Autoenergie")
    ax2.plot(range(len(e)), e)

    constB = 1 / (2 * a**2)
    bessel0 = constB * np.asarray( [3.141593, 6.283185, 9.424778, 12.566371, 15.707963] )**2
    ax3.plot(range(len(bessel0)), bessel0, label="teorica")
    ax3.plot( range(len(e[:5])), e[:5], label="calcolata")
    ax3.legend()
    ax3.grid()
    
    plt.show()







 


if __name__ == "__main__":
    main()
