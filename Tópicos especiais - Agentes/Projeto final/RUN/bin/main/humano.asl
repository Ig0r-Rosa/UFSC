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

+!goToGoal: pos(X,Y) & goal(Xg,Yg) & (X==Xg) & (Y==Yg) & (Xg == 0) & (Yg == 0) <-
    .print("Sai da masmorra.");
    setInitial(0,X,Y);
    attView;
    .my_name(N);
    .kill_agent(N).

+!goToGoal: pos(X,Y) & goal(Xg,Yg) & (X==Xg) & (Y==Yg) <-
    .print("Cheguei no final da masmorra.");
    -+goal(0,0);
    !!goToGoal.

+!goToGoal: pos(X,Y) & goal(Xg,Yg) & id(ID) <-
    .wait(200);
    decideMover(ID,X,Y,Xg,Yg,NewX,NewY,Inter);
    -+pos(NewX,NewY);
    attView;
    !!verInter(NewX,NewY,Inter).

// Interações com o ambiente
+!verInter(NewX,NewY,Inter): (Inter == -3) & timer(T) & T > 20000 <- 
    .print("[morreu]").
    .broadcast(achieve, morri(NewX,NewY)).

+!verInter(NewX,NewY,Inter): (Inter == -3) & timer(T) <- 
    -+timer(T + 200);
    !!goToGoal.

+!verInter(NewX,NewY,Inter): (Inter == -2) <- 
    .print("Abri uma porta!");
    !!goToGoal.

+!verInter(NewX,NewY,Inter): true <- 
    -+timer(0);
    !!goToGoal.

// Comunicação
/*+!morri(NewX,NewY)[source(S)]: clerigo <-
    -+goal(NewX,NewY);
    -morri(NewX,NewY)[source(S)].*/
    
+!morri(NewX,NewY)[source(S)]: true <-
    -morri(NewX,NewY)[source(S)].

{ include("$jacamoJar/templates/common-cartago.asl") }
{ include("$jacamoJar/templates/common-moise.asl") }

// uncomment the include below to have an agent compliant with its organisation
//{ include("$moiseJar/asl/org-obedient.asl") }
