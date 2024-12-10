import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm



def main():
    lato=float(input("Lunghezza lato:\t"))
    n=int(input("Numero punti griglia:\t"))
    cx=float(input("Coordinata X centro lato:\t"))
    cy=float(input("Coordinata Y centro lato:\t"))
    clato=float(input("Lunghezza lato carica:\t"))  
    itipo=int(input("1 Monopolo, 2 Dipolo, 3 Quadropolo:\t"))
    rho=100
    vb=0
    h=lato/(n-1)

    m=np.zeros((n,n,n,n),dtype=np.float64)
    f=np.zeros((n,n),dtype=np.float64)
    charge=np.zeros((n,n),dtype=np.float64)

    nx0=int((cx-clato/2)/lato*n)
    nx1=int((cx+clato/2)/lato*n)
    ny0=int((cy-clato/2)/lato*n)
    ny1=int((cy+clato/2)/lato*n)
    nxm=int((cx)/lato*n)
    nym=int((cy)/lato*n)

    for i in range(1,n-1):
        for j in range(1,n-1):
            m[i,j,i,j]=-2.0*2/h**2

            m[i,j,i+1,j]=1.0/h**2
            m[i,j,i-1,j]=1.0/h**2
            m[i,j,i,j+1]=1.0/h**2
            m[i,j,i,j-1]=1.0/h**2

    for i in range(n):
            m[0,i,0,i]=1.0
            m[i,0,i,0]=1.0
            m[n-1,i,n-1,i]=1.0
            m[i,n-1,i,n-1]=1.0

    for i in range(n):
            f[0,i]=vb
            f[i,0]=vb
            f[n-1,i]=vb
            f[i,n-1]=vb

    if(itipo==1):
        for i in range(nx0,nx1):
            for j in range(ny0,ny1):
                f[i,j]=rho
                charge[i,j]=rho
    elif(itipo==2):
         for i in range(nx0,nx1):
            for j in range(ny0,ny1):
                f[i,j]=rho
                if(i>=nxm):
                    f[i,j]=rho
                    charge[i,j]=rho
                else:
                    charge[i,j]=-rho
                    f[i,j]=-rho

    else:
         for i in range(nx0,nx1):
            for j in range(ny0,ny1):
                f[i,j]=rho
                if((i-nxm)*(j-nym)>=0):
                    f[i,j]=rho
                    charge[i,j]=rho
                else:
                    charge[i,j]=-rho
                    f[i,j]=-rho
                  
             
    m=m.reshape((n**2,n**2))
    f=f.reshape((n**2))
    phi=np.linalg.solve(m,f)
    phi=phi.reshape(n,n)

    X=np.zeros((n,n),dtype=np.float64)
    Y=np.zeros((n,n),dtype=np.float64)
    for i in range(n):
         for j in range(n):
              X[i,j]=h*i
              Y[i,j]=h*j
              

    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    ax.plot_surface(X, Y, charge, vmin=charge.min() * 2, cmap=cm.Blues)

    ax.set(xticklabels=[],
       yticklabels=[],
       zticklabels=[])

    plt.show()

    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    ax.plot_surface(X, Y, phi, vmin=phi.min() * 2, cmap=cm.Blues)

    ax.set(xticklabels=[],
       yticklabels=[],
       zticklabels=[])

    plt.show()


if __name__ == "__main__":
    main()




