// Agent gui in project aula10

/* Initial beliefs and rules */  

timer(0).

/* Initial goals */ 

!checkGrid.

+!checkGrid: pos(X,Y) & id(ID) <-
    ?gridReady(G);
    focus(G);
    setInitial(ID,X,Y);
    attView;
    !goToGoal.

+?gridReady(G): true <- 
    lookupArtifact("grid",G).

-?gridReady(G): true <-
    .wait(50);
    ?gridReady(G).

+!goToGoal: pos(X,Y) & goal(Xg,Yg) & (X==Xg) & (Y==Yg) & (Xg == 0) & (Yg == 0) & not(goalReviver(_,_,_)) <-
    .print("Sai da masmorra.");
    setInitial(0,X,Y);
    attView;
    .my_name(N);
    .send(mestre,tell,saiu);
    .kill_agent(N).

+!goToGoal: pos(X,Y) & goal(Xg,Yg) & (X==Xg) & (Y==Yg) & ladino <-
    .print("Peguei o tesouro, vamos voltar!");
    -+goal(0,0);
    .broadcast(tell, tesouro);
    !!goToGoal.

+!goToGoal: pos(X,Y) & goalReviver(Nome,Xg,Yg) & id(ID) & clerigo <-
    verificaDir(X,Y,Esq,Dir,Cima,Baixo,Achou);
    -+achou(Achou);
    -+rev(Esq,Dir,Cima,Baixo);
    .wait(200);
    decideMover(ID,X,Y,Xg,Yg,NewX,NewY,Inter);
    -+pos(NewX,NewY);
    attView;
    !!verInter(NewX,NewY,0).

+!goToGoal: pos(X,Y) & goal(Xg,Yg) & id(ID) <-
    .wait(200);
    decideMover(ID,X,Y,Xg,Yg,NewX,NewY,Inter);
    -+pos(NewX,NewY);
    attView;
    !!verInter(NewX,NewY,Inter).

// Interações com o ambiente
+!verInter(NewX,NewY,Inter): (Inter == -4) & not(ladino) <- 
    .print("Achei o bau de recompensa, porém, não consigo abrir!!");
    !!goToGoal.

+!verInter(NewX,NewY,Inter): (Inter == -3) & timer(T) & T > 20000 & clerigo <- 
    !!goToGoal.

+!verInter(NewX,NewY,Inter): (Inter == -3) & timer(T) & T > 4000 & not(clerigo) <- 
    .print("[morreu]");
    +morto;
    .broadcast(tell, morri(NewX,NewY)).

+!verInter(NewX,NewY,Inter): (Inter == -3) & timer(T) <- 
    -+timer(T + 200);
    !!goToGoal.

+!verInter(NewX,NewY,Inter): (Inter == -2) <- 
    .print("Abri uma porta!");
    !!goToGoal.

+!verInter(NewX,NewY,Inter): Inter == 0 & achou(1) & rev(Esq,Dir,Cima,Baixo) <-
    .send(mestre,tell,revive(Esq,Dir,Cima,Baixo));
    -achou(1);
    -rev(Esq,Dir,Cima,Baixo);
    !!goToGoal.

+!verInter(NewX,NewY,Inter): true <-
    -+timer(0);
    !!goToGoal.

// Comunicação
+morri(NewX,NewY)[source(S)]: clerigo <-
    +goalReviver(S,NewX,NewY);
    .print("vou ajudar o ",S);
    -morri(NewX,NewY)[source(S)].
    
+morri(NewX,NewY)[source(S)] <-
    -morri(NewX,NewY)[source(S)].

//
+tesouro[source(S)]: not(morto) <-
    .print("Ok, estou voltando!");
    -tesouro[source(S)];
    -+goal(0,0).

+tesouro[source(S)]: morto <-
    -tesouro[source(S)];
    -+goal(0,0).

//
+reviver[source(mestre)]: morto <-
    .print("[voltou a vida]");
    -morto;
    -+timer(0);
    -reviver[source(mestre)];
    !!goToGoal.

+reviver[source(mestre)] <-
    -reviver[source(mestre)].

+reviveu(Nome)[source(mestre)]: clerigo <-
    -goalReviver(Nome,_,_);
    -reviveu(Nome)[source(mestre)].

{ include("$jacamoJar/templates/common-cartago.asl") }
{ include("$jacamoJar/templates/common-moise.asl") }

// uncomment the include below to have an agent compliant with its organisation
//{ include("$moiseJar/asl/org-obedient.asl") }
