3000 'Exer 7-1; particle on spheroid earth **
3010 SCREEN 1: COLOR 0,2: KEY OFF: CLS
3020 'absolute 1 and 2, relative 3 and 4
3021 'expert odd, novice even       # expert means that particle moves at the same rate as the rotation of the planet
3030 PRINT "TWO VIEWS"              ' novice means that the particle moves at a different rate than the rotation of the planet
3031 PRINT"expert":PRINT"novice"
3040 LOCATE 2,30:PRINT"on back"
3050 PSET(292,12),1
3060 LOCATE 21,6:PRINT"absolute"    ' this refers to the frame of reference
3070 LOCATE 21,24:PRINT"relative"
3080 PSET(80,12),2:PSET(80,20),3

3090 PI = 3.14159: W=10: W2=W^2     ' set all the constants, W = rotation rate of the planet
3091 DT=0.005: FACT = 60:INC=PI/16
3100 GOSUB 3360

3110 LOCATE 23,1:INPUTE "lat";LA    ' ask for user to enter a latitude
3120 FOR I=1 TO 4:LA(I)=LA*PI/180   ' start all particles at the chosen latitude
3121 LO(I) = -PI/2  :NEXT           ' set the same starting longitude
3130 LAD(1)=0: LAD(3)=0             ' set the time derivatives for lat and lon for experts
3131 LAD(2)=V:LAD(4)=LAD(2)         ' set the time derivatives for lat and lon for novices
3140 LOCATE 23,20:INPUT "u,v";U,V   ' ask for user to enter the starting velocity, relative to rotating planet
3150 LAD(1)=0: LAD(3)=0
3151 LAD(2)=V:LAD(4)=LAD(2)
3160 LOD(2)=U/COS(LA(1))+W : LOD(4)=LOD(2)
3170 LODD(2)=2*TAN(LA(2))*LAD(2)*LOD(2)     ' integration in absolute frame
3178 AAA=SIN(LA(2))*COS(LA(2))
3179 BBB=(W2-(LOD(2))^2)
3180 LADD(2)=AAA*BBB
3190 LOD(2)=LOD(2)+DT*LODD(2)
3191 LAD(2)=LAD(2)+LADD(2)*DT
3200 T=T+DT:A$=INKEY$:IF A$= "S" THEN WS=0
3201 'LOCATE 3,15:PRINT "BULGE GONE":BEEP
3210 LA(2)=LA(2)+DT*LAD(2)
3211 LO(2)=LO(2)+DT*LOD(2):LO(4)=LO(2)-W*T
3220 LA(4)=LA(2): LO(1)=LO(1)+W*DT          ' integration in relative frame
3230 FOR I=1 TO 4: RHO(I)=COS(LA(I))        ' convert to x,y coordinates
3240 X(I) = RHO(I)*COS(LO(I))
3241 Y(I) = RHO(I)*SIN(LO(I))*SIN(INC)
3250 Z(I)=Y(I)+SIN(LA(I))*COS(INC)
3260 IF Y(1)<0 THEN C(1)=2 ELSE C(1)=1      ' set color of particles depending on position
3270 IF Y(2)<0 THEN C(2)=3 ELSE C(2)=1
3280 IF Y(3)<0 THEN C(3)=2 ELSE C(3)=1
3290 IF Y(4)<0 THEN C(4)=3 ELSE C(4)=2
3300 IF I=1 THEN GOTO 3301 ELSE GOTO 3310   ' plot position of four points on the spheres
3301 PSET(70+FACT*X(1),90-FACT*Z(1)),C(1)
3312 GOTO 3340
3310 IF I=2 THEN GOTO 3311 ELSE GOTO 3320
3311 PSET(70+FACT*X(2),90-FACT*Z(2)),C(2)
3312 GOTO 3340
3320 IF I=3 THEN GOTO 3321 ELSE GOTO 3330
3321 PSET(220+FACT*X(3),90-FACT*Z(3)),C(3)
3322 GOTO 3340
3330 IF I=4 THEN GOTO 3331 ELSE GOTO 3340
3331 PSET(220+FACT*X(4),90-FACT*Z(4)),C(4)
3332 GOTO 3340
3340 NEXT
3350 GOTO 3170

3360 J=INC: 'PLOT THE TWO SPHERES"
3370 FOR I=0 TO 1
3380 CIRCLE (220-150*I,90),60,1,0,2*PI,1        ' CIRCLE (x,y), radius, color, start, end, aspect
3390 CIRCLE (220-150*I,90),60,1,0,2*PI,SIN(J)
3400 C9=60*SIN(PI/6)*COS(J)
3405 AN=SIN(J)
3410 K9=60*COS(PI/6)
3420 CIRCLE(220-150*I,90-C9),K9,1,0,2*PI,AN
3430 CIRCLE(220-150*I,90+C9),K9,1,0,2*PI,AN
3440 C9=60*SIN(PI/3)*COS(J)
3450 K9 = 60*COS(PI/3)
3460 CIRCLE(220-150*I,90-C9),K9,1,0,2*PI,AN
3470 CIRCLE(220-150*I,90+C9),K9,1,0,2*PI,AN
3470 NEXT
3490 RETURN 
 

