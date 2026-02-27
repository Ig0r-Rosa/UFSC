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
+!morri(NewX,NewY)[source(S)]: true <-
    -morri(NewX,NewY)[source(S)].

{ include("$jacamoJar/templates/common-cartago.asl") }
{ include("$jacamoJar/templates/common-moise.asl") }

// uncomment the include below to have an agent compliant with its organisation
//{ include("$moiseJar/asl/org-obedient.asl") }
