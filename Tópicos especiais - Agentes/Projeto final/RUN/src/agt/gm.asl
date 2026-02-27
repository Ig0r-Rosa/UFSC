// Agent gui in project aula10

/* Initial beliefs and rules */

/* Initial goals */

!test_gui.

+!test_gui
  <- makeArtifact("grid","grid.gridView",[],D);
  		focus(D);
      ?numAgentes(N);
      inicializar(N).

// limpa msg de broadcast
+morri(NewX,NewY)[source(S)]: true <-
    -morri(NewX,NewY)[source(S)].

+tesouro[source(S)] <-
    -+goal(0,0).

// revive alguem com base no ID
+revive(Esq,Dir,Cima,Baixo)[source(S)]: Esq > 0 <-
    ?agente(Esq,Nome);
    .print("Agente ID:",Esq," ",Nome);
    .send(Nome,tell,reviver);
    .send(S,tell,reviveu(Nome));
    -revive(Esq,Dir,Cima,Baixo)[source(S)].

+revive(Esq,Dir,Cima,Baixo)[source(S)]: Dir > 0 <-
    ?agente(Dir,Nome);
    .print("Agente ID:",Dir," ",Nome);
    .send(Nome,tell,reviver);
    .send(S,tell,reviveu(Nome));
    -revive(Esq,Dir,Cima,Baixo)[source(S)].

+revive(Esq,Dir,Cima,Baixo)[source(S)]: Cima > 0 <-
    ?agente(Cima,Nome);
    .print("Agente ID:",Cima," ",Nome);
    .send(Nome,tell,reviver);
    .send(S,tell,reviveu(Nome));
    -revive(Esq,Dir,Cima,Baixo)[source(S)].

+revive(Esq,Dir,Cima,Baixo)[source(S)]: Baixo > 0 <-
    ?agente(Baixo,Nome);
    .print("Agente ID:",Baixo," ",Nome);
    .send(Nome,tell,reviver);
    .send(S,tell,reviveu(Nome));
    -revive(Esq,Dir,Cima,Baixo)[source(S)].

// Saiu da masmorra
+saiu[source(S)] <-
  -agente(_,S);
  -saiu[source(S)].

{ include("$jacamoJar/templates/common-cartago.asl") }
{ include("$jacamoJar/templates/common-moise.asl") }

// uncomment the include below to have an agent compliant with its organisation
//{ include("$moiseJar/asl/org-obedient.asl") }
