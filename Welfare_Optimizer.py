import numpy as np
from scipy.optimize import minimize
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

# Project: Quantum-Assisted Welfare Scheme Allocation Optimizer
B = ["B1","B2","B3","B4"]
S = ["Education","Healthcare","Housing"]
P = np.array([3,2,3,1])
V = np.array([[90,70,60],[80,85,50],[60,95,70],[75,65,90]])
E = np.array([[1,1,0],[1,0,1],[0,1,1],[1,1,1]])
C = [2,2,2]
n, m, N, K = 4, 3, 12, 300

q = lambda i,j: i*m + j
Q = np.zeros((N,N))

for i in range(n):
    for j in range(m):
        k = q(i,j)
        Q[k,k] -= P[i]*V[i,j]
        if not E[i,j]: Q[k,k] += K
        Q[k,k] -= K
        for l in range(j+1,m):
            Q[k,q(i,l)] += 2*K

for j in range(m):
    for i in range(n):
        Q[q(i,j),q(i,j)] += K*(1-2*C[j])
    for i in range(n):
        for k in range(i+1,n):
            Q[q(i,j),q(k,j)] += 2*K

h = -np.diag(Q)/2
J = {(i,j): Q[i,j]/4 for i in range(N) for j in range(i+1,N) if Q[i,j]}
for (i,j),v in J.items():
    h[i] -= v
    h[j] -= v

def qc(g,b):
    c = QuantumCircuit(N)
    for i in range(N):
        c.h(i)
        c.rz(2*g*h[i], i)
    for (i,j),v in J.items():
        c.cx(i,j)
        c.rz(2*g*v, j)
        c.cx(i,j)
    for i in range(N):
        c.rx(2*b, i)
    return c

def score(x):
    return np.sum(x.reshape(n,m)*P[:,None]*V)

def valid(x):
    X = x.reshape(n,m)
    return np.all(X.sum(1)==1) and np.all(X.sum(0)<=C) and np.all(X[E==0]==0)

def energy(x):
    return sum(Q[i,i]*x[i]+sum(Q[i,j]*x[i]*x[j] for j in range(i+1,N)) for i in range(N))

def obj(p):
    s = Statevector.from_instruction(qc(*p))
    return sum(abs(s.data[k])**2 * energy(np.array([(k>>i)&1 for i in range(N)])) for k in range(2**N))

r = minimize(obj, [.5,.5], method="COBYLA", options={"maxiter":30})
s = Statevector.from_instruction(qc(*r.x))
probs = np.abs(s.data)**2

best = next((np.array([(k>>i)&1 for i in range(N)]) for k in np.argsort(probs)[::-1] if valid(np.array([(k>>i)&1 for i in range(N)]))), None)

def make_x(c):
    x = np.zeros(N, dtype=int)
    for i,j in enumerate(c):
        x[q(i,j)] = 1
    return x

classical = max((make_x(c) for c in np.ndindex(*(m,)*n)), key=lambda x: score(x) if valid(x) else -1)

print("QUANTUM-ASSISTED WELFARE SCHEME ALLOCATION OPTIMIZER - Qiskit Fall Fest Nuzvid")
print("\nQAOA ALLOCATION")
for i in range(n):
    print(f"{B[i]} -> {S[np.argmax(best.reshape(n,m)[i])]}")
print(f"QAOA VALUE: {score(best)}")

print("\nCLASSICAL BASELINE")
for i in range(n):
    print(f"{B[i]} -> {S[np.argmax(classical.reshape(n,m)[i])]}")
print(f"CLASSICAL VALUE: {score(classical)}")

print("\nQAOA CIRCUIT")
print(qc(*r.x).draw())
