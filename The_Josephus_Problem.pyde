import math as m
r=140
i=0
n=10
a=TWO_PI/n
v=range(1,n+1)

def gon(n,R):
    a=TWO_PI/n
    for j in range(n+1):
        stroke(200)
        strokeWeight(4)
        point(cos(j*a)*R,sin(j*a)*R)

def setup():
    size(2*r+100,2*r+100)
    background(0)
    translate(width/2, height/2)
    gon(n,r)
    
def draw():
    global n
    global i
    translate(width/2, height/2)

    strokeWeight(10)
    
    stroke(0,0,225)
        
    if len(v)!=1:
        if i+1==len(v):
            stroke(0,0,225)
            point(r*cos(v[i]*a),r*sin(v[i]*a))
            stroke(255,0,0)
            point(r*cos(v[0]*a),r*sin(v[0]*a))
            print v[0]
            del v[0]
            print v
            delay(600)
            i=0
        elif i+1>len(v):            
            i=0
            stroke(0,0,225)
            point(r*cos(v[i]*a),r*sin(v[i]*a))
            stroke(255,0,0)
            point(r*cos(v[i+1]*a),r*sin(v[i+1]*a))
            print v[i+1]
            del v[i+1]
            print v
            delay(600)
            i=i+1
        else:
            stroke(0,0,225)
            point(r*cos(v[i]*a),r*sin(v[i]*a))
            stroke(255,0,0)
            point(r*cos(v[i+1]*a),r*sin(v[i+1]*a))
            print v[i+1]
            del v[i+1]
            print v
            delay(600)
            i=i+1
    else:
        stroke(0,255,0)
        point(r*cos(v[0]*a),r*sin(v[0]*a))
        print v
    
    
