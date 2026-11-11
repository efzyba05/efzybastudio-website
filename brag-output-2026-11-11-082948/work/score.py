import numpy as np, wave
SR=48000; B=60/96; N=562; DUR=N/30; L=int(DUR*SR)+SR//2
rng=np.random.default_rng(7)
def buf(): return np.zeros(L)
def at(b): return int(round(b*B*SR))
def hz(m): return 440*2**((m-69)/12)
def onepole(x,fc):
    a=np.exp(-2*np.pi*fc/SR); y=np.empty_like(x); s=0.
    # vectorized via lfilter-like loop in chunks (scipy-free)
    try:
        from scipy.signal import lfilter; return lfilter([1-a],[1,-a],x)
    except Exception:
        for i,v in enumerate(x): s=(1-a)*v+a*s; y[i]=s
        return y
def add(dst,sig,start,g=1.):
    e=min(L,start+len(sig)); dst[start:e]+=g*sig[:e-start]
def env_ad(n,att,dec):
    t=np.arange(n)/SR; return np.minimum(1,t/max(att,1e-4))*np.exp(-t/dec)

piano,pad,bass,drums,fx=buf(),buf(),buf(),buf(),buf()
# chords (MIDI): Dm9, Bbmaj7, Gm9, A7sus4
CH=[[50,57,60,64,65],[46,57,62,65,69],[43,58,62,65,69],[45,57,62,64,67]]
ROOT=[38,34,31,33]
def pnote(m,dur=2.5,vel=1.):
    n=int(dur*SR); t=np.arange(n)/SR; f=hz(m); s=np.zeros(n)
    for k,amp in [(1,1),(2,.45),(3,.22),(4,.12),(5,.06)]:
        s+=amp*np.sin(2*np.pi*f*k*t*(1+.0004*k))*np.exp(-t*(1.2+.9*k))
    s+= .02*onepole(rng.standard_normal(n),3000)*np.exp(-t*60)
    return vel*s*np.minimum(1,t/.004)
def padchord(notes,dur):
    n=int(dur*SR); t=np.arange(n)/SR; s=np.zeros(n)
    for m in notes:
        for d in (-.07,0,.07):
            ph=2*np.pi*hz(m+12)*(1+d/100*3)*t
            s+=np.sin(ph)+.3*np.sin(2*ph)+.12*np.sin(3*ph)
    s=onepole(s,1400)
    e=np.minimum(1,t/1.2)*np.minimum(1,(dur-t)/0.8).clip(0,1)
    return s*e/len(notes)/3
# --- pad: every bar (4 beats) from 0
for bar in range(8):
    c=CH[bar%4] if bar<7 else CH[0]
    dur=4*B+0.9 if bar<7 else 2*B+1.0
    add(pad,padchord(c,dur),at(bar*4)-int(.3*SR) if bar else 0,1)
# --- piano: chords from beat 6; arps 8ths from 13 to 27; final chord at 31
for b in range(5,11):
    if b%2==1 or b==5:
        c=CH[(b//4)%4]
        for i,m in enumerate(c): add(piano,pnote(m+12,3,.55),at(b)+i*int(.012*SR))
for h in range(11*2,24*2):  # eighths
    b=h/2; c=CH[(int(b)//4)%4]; pat=[0,2,4,3,1,3,4,2]
    m=c[pat[h%8]]+24; v=.32 if h%2 else .42
    add(piano,pnote(m,1.6,v),at(b))
for b in (24,26):
    c=CH[(b//4)%4]
    for i,m in enumerate(c): add(piano,pnote(m+12,3,.5),at(b)+i*int(.015*SR))
for i,m in enumerate([50,57,62,64,65,69,76]): add(piano,pnote(m+12,4.5,.55),at(28)+i*int(.02*SR))
# --- bass from 6
def bnote(m,dur):
    n=int(dur*SR); t=np.arange(n)/SR; s=np.tanh(1.6*np.sin(2*np.pi*hz(m)*t))
    return s*np.minimum(1,t/.01)*np.minimum(1,(dur-t)/.08).clip(0,1)
for b in range(5,28,2):
    if 24<=b<28: continue
    add(bass,bnote(ROOT[(b//4)%4],2*B*.95),at(b),.5)
add(bass,bnote(38,3.2),at(28),.45)
# --- drums
def kick():
    n=int(.45*SR); t=np.arange(n)/SR; f=45+80*np.exp(-t*28)
    return np.sin(2*np.pi*np.cumsum(f)/SR)*np.exp(-t*7.5)
def shaker():
    n=int(.09*SR); t=np.arange(n)/SR; x=rng.standard_normal(n); x=x-onepole(x,5000)
    return x*np.minimum(1,t/.012)*np.exp(-t*45)
for b in range(5,24):
    if b<11 and (b-5)%2: continue
    add(drums,kick(),at(b),.8 if b>=11 else .6)
for h in range(11*2,24*2): add(drums,shaker(),at(h/2),.10 if h%2 else .05)
# --- fx: stamp boom + bell at beat 1, riser into 6 and 13, swell into 22, click + bell at 31
def boom():
    n=int(2.2*SR); t=np.arange(n)/SR
    return (np.sin(2*np.pi*hz(26)*t)*np.exp(-t*2.2)+.25*onepole(rng.standard_normal(n),180)*np.exp(-t*9))
def bell(m,dur=3.5,g=1):
    n=int(dur*SR); t=np.arange(n)/SR; f=hz(m)
    return g*sum(a*np.sin(2*np.pi*f*r*t)*np.exp(-t*d) for r,a,d in [(1,1,1.1),(2.76,.35,2.4),(5.4,.15,4),(2,.25,1.6)])*np.minimum(1,t/.002)
def riser(dur):
    n=int(dur*SR); t=np.arange(n)/SR; x=onepole(rng.standard_normal(n),900)+.0
    return x*(t/dur)**2.5*np.minimum(1,(dur-t)/.02)
add(fx,boom(),at(1),.9); add(fx,bell(74,4,.35),at(1)); add(fx,bell(81,3,.15),at(2))
add(fx,riser(2*B),at(3),.35); add(fx,riser(2*B),at(9),.3); add(fx,riser(1.5*B),at(18.5),.25)
for b in (11,14,17): add(fx,bell(86 if b!=16 else 84,1.5,.07),at(b))
add(fx,boom(),at(20),.35)
n=int(.05*SR); t=np.arange(n)/SR; click=onepole(rng.standard_normal(n),2500)*np.exp(-t*120)
add(fx,click,at(28),.25); add(fx,bell(86,4,.18),at(28)); add(fx,bell(74,4,.18),at(28))
# --- reverb (FFT convolution with synthetic stereo IR)
def ir(sec,seed):
    r=np.random.default_rng(seed); n=int(sec*SR); t=np.arange(n)/SR
    x=r.standard_normal(n)*np.exp(-t*3.2/sec*2.2); x=onepole(x,5000); x[:int(.02*SR)]*=np.linspace(0,1,int(.02*SR)); return x/np.sqrt((x**2).sum())
def conv(x,h):
    m=len(x)+len(h)-1; F=1<<int(np.ceil(np.log2(m)))
    return np.fft.irfft(np.fft.rfft(x,F)*np.fft.rfft(h,F),F)[:len(x)]
dry = .55*piano + .42*pad + .55*bass + .75*drums + .6*fx
send= .5*piano + .5*pad + .08*drums + .7*fx
irL,irR=ir(2.6,1),ir(2.6,2)
L_=dry+ .35*conv(send,irL); R_=dry+.35*conv(send,irR)
# gentle width: pad slight offset
d=int(.011*SR); R_[d:]+= .06*pad[:-d]
st=np.stack([L_,R_],1)
# end fade over last 1.2s of video and trim
st=st[:int(DUR*SR)]
fe=int(1.2*SR); st[-fe:]*=np.linspace(1,0,fe)[:,None]**1.5
st=np.tanh(st/np.abs(st).max()*1.1)*.8
w=wave.open('score.wav','wb'); w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
w.writeframes((st*32767).astype('<i2').tobytes()); w.close(); print('ok',st.shape[0]/SR)
