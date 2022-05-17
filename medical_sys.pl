symptom(cold,cough).
symptom(cold,runnynose).
symptom(cold,nasal_spray).
symptom(covid,fever).
symptom(covid,headache).
symptom(covid,fatigue).
treatment(cold,Nicip+).
treatment(covid,remdisivir).

go:-
write("symptom 1 "),
read(X),
nl,
write("symptom 2"),
read(Y),
nl,
write("symptom 3"),
read(P),
nl,
(symptom(Z,X),symptom(Z,Y),symptom(Z,P)),
write("You are Suffering From "),
write(Z),
treatment(Z,T),
write(" Treatment is "),
write(T).