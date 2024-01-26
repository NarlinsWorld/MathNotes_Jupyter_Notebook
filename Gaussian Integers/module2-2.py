#!/usr/bin/env python
# coding: utf-8

# In[3]:
"""Functions in the module named module2.

N(z1) Returns the Gaussian norm of a single complex number given as the argument
GaussianDivide(z1,z2) Return Quotient,Remainder from division of 2 complex numbers given as arguments
Gmod(z1,z2) Return Remainder from z1/z2 given as arguments
GaussianGCD(z1,z2) Return GCD of two Gaussian Integers
Iss_Prime(n) Return True if input integer n is prime.
"""

    
def N(z_1):
    '''Returns the Gaussian norm of a single complex number given as the argument.'''
    return (z_1.real)**2+(z_1.imag)**2

def GaussianDivide(z_1,z_2):
    '''Return Quotient,Remainder from division of 2 complex numbers given as arguments.'''
    t=z_1/z_2
    if t.real<0 and t.imag<0: s=t-.5-.5j
    if t.real>=0 and t.imag<0: s=t+.5-.5j
    if t.real<0 and t.imag>=0: s=t-.5+.5j
    if t.real>=0 and t.imag>=0: s=t+.5+.5j
    α = int(s.real) 
    β = int(s.imag)
    γ=α+β*1j
    r=z_1-γ*z_2
    return γ,r  #Quotient and Remainder
    
def Gmod(z_1,z_2):
    '''Return Remainder from z1/z2 given as arguments.'''
    t=z_1/z_2
    if t.real<0 and t.imag<0: s=t-.5-.5j
    if t.real>=0 and t.imag<0: s=t+.5-.5j
    if t.real<0 and t.imag>=0: s=t-.5+.5j
    if t.real>=0 and t.imag>=0: s=t+.5+.5j
    α = int(s.real) 
    β = int(s.imag)
    γ=α+β*1j
    r=z_1-γ*z_2
    return r  #Remainder

def GaussianGCD(a,b):
    '''Where a and b are Gaussian Integers returns
    a single Gaussian Integer that is the greatest common divisor.'''
    while b!=0:
        r= m1.Gmod(a,b)   
        a=b
        b=r
    return a

def iss_prime(n):
    '''True if input integer n is prime.'''
    if n <= 3:
        return n > 1
    else: 
        if n%2 == 0 or n%3 == 0:
            return False
        i=5
    while i * i <= n:
        if n%i == 0 or n%(i + 2) == 0:
            return False
        i=i + 6
    return True

