def acceleration(u,v,t):
    eq= (v-u)/t
    return eq


v=25
u=0
t=10

a=acceleration(u,v,t)
print("the acceleration where final velocity v is {0} initial velocity u is {1} and time t is {2} is equal to {3} ".format(v,u,t,a))