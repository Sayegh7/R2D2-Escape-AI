%
%pad(3,4,s).
pad(0,2,s).
%rock(4,7,s).
%immovable(5,2,s).
immovable(2,2,s).
teleporter(1,1,s).
rock(0,1,s).
rock(X,Y,result(A,S)):-
   (
     (A=left,X<3,H is X+1,\+immovable(X,Y,S),\+pad(H,Y,S),H1 is X+2,H1<3,H<3,rock(H,Y,S),robot(H1,Y,S));
     (A=right,X>=0,H is X-1,\+immovable(X,Y,S),\+pad(H,Y,S),H1 is X-2,H1>=0,H>=0,rock(H,Y,S),robot(H1,Y,S));
     (A=up,Y>=0,V is Y-1,\+immovable(X,Y,S),\+pad(X,V,S),V1 is Y-2,V1>=0,V>=0,rock(X,V,S),robot(X,V1,S));
     (A=down,Y<3,V is Y+1,\+immovable(X,Y,S),\+pad(X,V,S),V1 is Y+2,V1<3,V<3,rock(X,V,S),robot(X,V1,S))
   	)
   ;
   (
     (\+A=left; (X1 is X+1,immovable(X1,Y,S),rock(X,Y,S))),
     (\+A=right;(X1 is X-1,immovable(X1,Y,S),rock(X,Y,S))),
     (\+A=up;(Y1 is Y-1,immovable(X,Y1,S),rock(X,Y,S))),
     (\+A=down;(Y1 is Y+1,immovable(X,Y1,S),rock(X,Y,S))),
	   (\+A=left;(pad(X,Y,S),rock(X,Y,S))),
	   (\+A=right;(pad(X,Y,S),rock(X,Y,S))),
	   (\+A=up;(pad(X,Y,S),rock(X,Y,S))),
	   (\+A=down;(pad(X,Y,S),rock(X,Y,S))),
     (\+A=left;(H is X+1,H<3,\+robot(H,Y,S),rock(X,Y,S))),
    (\+A=right;(H is X-1,H>=0,\+robot(H,Y,S),rock(X,Y,S))),
    (\+A=up;(V is Y-1,V>=0,\+robot(X,V,S),rock(X,Y,S))),
    (\+A=down;(V is Y+1,V<3,\+robot(X,V,S),rock(X,Y,S)))

	).

robot(0,0,s).
robot(X,Y,result(A,S)):-
	(

		(A=left,X<3,H is X+1,\+immovable(X,Y,S), robot(H,Y,S));
		(A=right,X>=0,H is X-1,\+immovable(X,Y,S), robot(H,Y,S));
		(A=up,Y>=1,V is Y-1,\+immovable(X,Y,S),robot(X,V,S));
		(A=down,Y<3,V is Y+1,\+immovable(X,Y,S),robot(X,V,S));
    (A=left,X<3,H is X+1,H1 is X+2,rock(X,Y,S),\+rock(H1,Y,S),\+immovable(H1,Y,S), robot(H,Y,S));
		(A=right,X>=0,H is X-1,H1 is X-2,rock(X,Y,S),\+rock(H1,Y,S),\+immovable(H1,Y,S), robot(H,Y,S));
		(A=up,Y>=0,V is Y-1,V1 is Y-2,rock(X,Y,S),\+rock(V1,Y,S),\+immovable(X,V1,S),robot(X,V,S));
		(A=down,Y<3,V is Y+1,V1 is Y+2,rock(X,Y,S),\+rock(V1,Y,S),\+immovable(X,V1,S),robot(X,V,S))
			)

	;
    (
	(
       (A=left,X1 is X+1,immovable(X1,Y,S),robot(X,Y,S));
       (A=right,X1 is X-1,immovable(X1,Y,S),robot(X,Y,S));
       (A=up,Y1 is Y-1,immovable(X,Y1,S),robot(X,Y,S));
       (A=down,Y1 is Y+1,immovable(X,Y1,S),robot(X,Y,S))
		)

	).
wintemp(X,Y,S):-
robot(X,Y,S),
rock(0,2,S).

generate(X,Y,S,N):-
 ((call_with_depth_limit(wintemp(X,Y,S),N,Z)), \+Z=depth_limit_exceeded)
 ;(( call_with_depth_limit(wintemp(X,Y,S),N,depth_limit_exceeded)), N1 is N+1,generate(X,Y,S,N1)).

%
