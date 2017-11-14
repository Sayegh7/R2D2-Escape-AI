% 
pad(3,4,s).
pad(5,3,s).
pad(3,8,s).
pad(8,7,s).
rock(5,8,s).
rock(6,5,s).
rock(1,4,s).
rock(4,7,s).
immovable(5,2,s).
immovable(8,8,s).
teleporter(4,1,s).
robot(8,7,s).




robot(X,Y,result(A,S)):-
	(
		(
		(A=left,H is X+1, robot(H,Y,S));
		(A=right,H is X-1, robot(H,Y,S));
		(A=up,V is Y-1, robot(X,V,S));
		(A=down,V is Y+1, robot(X,V,S))
		)
	);
(
	(
       (A=left,immovable(X-1,Y,S),H is X+1,robot(H,Y,S));
       (A=right,immovable(X+1,Y,S),H is X-1 ,robot(H,Y,S));
       (A=up,immovable(X,Y-1,S),V is Y-1 ,robot(X,V,S));
       (A=down,immovable(X,Y+1,S),V is Y+1 ,robot(X,V,S))
		)
	).

generate(X,Y,S,N):-
 ((call_with_depth_limit(robot(X,Y,S),N,Z)), \+Z=depth_limit_exceeded)
 ;(( call_with_depth_limit(robot(X,Y,S),N,depth_limit_exceeded)), N1 is N+1,generate(X,Y,S,N1)).

%