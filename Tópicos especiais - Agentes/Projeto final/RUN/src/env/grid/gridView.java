package grid;
import java.awt.event.*;
import javax.swing.*;
import cartago.*;
import cartago.tools.GUIArtifact; 
import grid.gridView.Grid.TestPane;
 
import java.awt.*;
import java.util.*;

public class gridView extends GUIArtifact {

	public int linhas = 20;
	public int colunas = 10;
	public int obstaculo = -1;
	public int porta = -2;
	public Grid frame = new Grid();
	
	public int[][] grid = {
            { 0, 0, 0,-1, 0, 0, 0, 0, 0, 0},
            { 0, 0, 0,-1, 0, 0, 0, 0, 0, 0},
            { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
            {-1,-1,-1,-1,-1,-1,-1,-1,-1,-2},
            {-3,-3,-3,-1, 0, 0, 0, 0, 0, 0},
            {-3,-3,-3,-2, 0, 0, 0, 0, 0, 0},
            {-3,-3,-3,-1, 0, 0, 0, 0, 0, 0},
            {-3,-3,-3,-1, 0, 0, 0, 0, 0, 0},
            {-3,-3,-3,-1, 0, 0, 0, 0, 0,-1},
            {-3,-3,-3,-1, 0, 0, 0, 0,-1,-1},
            {-3,-3,-3,-1, 0, 0, 0,-1,-1,-1},
            {-1,-1,-1,-1, 0, 0, 0,-2,-3,-3},
            {-1,-2,-1, 0, 0, 0, 0,-1,-3,-3},
            { 0, 0, 0, 0, 0, 0, 0,-1,-3,-3},
            { 0, 0, 0, 0, 0, 0, 0,-1,-3,-3},
            { 0, 0, 0, 0, 0, 0, 0,-1,-3,-3},
            { 0, 0, 0, 0, 0, 0, 0,-1,-3,-3},
            { 0, 0, 0, 0, 0, 0, 0,-1,-3,-3},
            { 0, 0, 0, 0,-1,-2,-1,-1,-1,-1},
            { 0, 0, 0, 0,-1, 0, 0, 0, 0,-4}};

	public class Grid {
		public TestPane gridView;

		public static void main(String[] args) {
		}

		public Grid() {
			gridView = new TestPane(linhas, colunas);

			EventQueue.invokeLater(new Runnable() {
				@Override
				public void run() {
					try {
						UIManager.setLookAndFeel(UIManager.getSystemLookAndFeelClassName());
					} catch (ClassNotFoundException | InstantiationException | IllegalAccessException | UnsupportedLookAndFeelException ex) {
						ex.printStackTrace();
					}
					JFrame frame = new JFrame("Testing");
					frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
					frame.add(gridView);
					frame.pack();
					frame.setLocationRelativeTo(null);
					frame.setVisible(true);
				}
			});
		}

		public class TestPane extends JPanel {

			public int tilesX;
			public int tilesY;
			public Color[][] tileColor;

			public TestPane(int X, int Y) {
				tilesX = X;
				tilesY = Y;
				tileColor = new Color[X][Y];
				for (Color[] row: tileColor)
    				Arrays.fill(row, Color.WHITE);
			}

			@Override
			public Dimension getPreferredSize() {
				return new Dimension(20*tilesX, 20*tilesY);
			}

			protected void paintComponent(Graphics g) {
				super.paintComponent(g);
				Graphics2D g2d = (Graphics2D) g.create();
				int size = Math.min(getWidth() - 4, getHeight() - 4) / 10;

				int y = (getHeight() - (size * tilesY)) / 2;
				for (int horz = 0; horz < tilesY; horz++) {
					int x = (getWidth() - (size * tilesX)) / 2;
					for (int vert = 0; vert < tilesX; vert++) {
						g.setColor(tileColor[vert][horz]);
    					g.fillRect(x, y, (size-1), (size-1));
						g.drawRect(x, y, size, size);
						x += size;
					}
					y += size;
				}
				g2d.dispose();
			}

			public void setTileColor(int X, int Y, int R, int G, int B) 
			{
				Color newCl = new Color(R,G,B); 
				tileColor[X][Y] = newCl;
				super.repaint();
			}
		}
	}

	@OPERATION void setInitial(int ID,int X,int Y){
		grid[X][Y] = ID;
	}

	@OPERATION void attView(){
		for(int i=0; i < linhas; i++)
		{
			for(int j=0; j<colunas; j++)
			{
				if(grid[i][j] == -4)
				{
					frame.gridView.setTileColor(i, j, 200, 200, 50);
				}
				else if(grid[i][j] == -3)
				{
					frame.gridView.setTileColor(i, j, 50, 200, 50);
				}
				else if(grid[i][j] == -2)
				{
					frame.gridView.setTileColor(i, j, 92, 64, 51);
				}
				else if(grid[i][j] == -1)
				{
					frame.gridView.setTileColor(i, j, 0, 0, 0);
				}
				else if(grid[i][j] == 0)
				{
					frame.gridView.setTileColor(i, j, 255, 255, 255);
				}
				else
				{
					frame.gridView.setTileColor(i, j, corPersonagem[grid[i][j] -1][0],  corPersonagem[grid[i][j] -1][1],  corPersonagem[grid[i][j] -1][2]);
				}
			}
		}
	}

	// Algoritmo de movimento
	int[][][] gridVisitado;
	int[][] corPersonagem;
	int[] backupValor;

	@OPERATION void inicializar(int numAgentes)
	{
		gridVisitado = new int[numAgentes][linhas][colunas];
		corPersonagem = new int[numAgentes][3];
		backupValor = new int[numAgentes];

		for(int i = 0; i < numAgentes;i++)
		{
			for(int j = 0; j < 3; j++)
			{
				Random rand = new Random();
				corPersonagem[i][j] = rand.nextInt(255);
			}
		}
	}

	@OPERATION void verificaDir(int X, int Y,
	OpFeedbackParam<Integer> Esq, OpFeedbackParam<Integer> Dir,
	OpFeedbackParam<Integer> Cima, OpFeedbackParam<Integer> Baixo,
	OpFeedbackParam<Integer> Achou){

		int aux = 0;
        if (X > 0)
		{ 
			Esq.set(grid[X-1][Y]);
			if(grid[X-1][Y] > 0)
			{
				aux++;
			}
		}
		else
		{
			Esq.set(-1);
		}
        if (Y < colunas - 1)
		{
			Baixo.set(grid[X][Y+1]);
			if(grid[X][Y+1] > 0)
			{
				aux++;
			}
		}
		else
		{
			Baixo.set(-1);
		}
        if (X < linhas - 1)
		{
			Dir.set(grid[X+1][Y]);
			if(grid[X+1][Y] > 0)
			{
				aux++;
			}
		}
		else
		{
			Dir.set(-1);
		}
        if (Y > 0)
	 	{
			Cima.set(grid[X][Y-1]);
			if(grid[X][Y-1] > 0)
			{
				aux++;
			}
		}
		else
		{
			Cima.set(-1);
		}

		if(aux > 0)
		{
			Achou.set(1);
		}
		else
		{
			Achou.set(0);
		}
	}

	@OPERATION void decideMover(int ID, int X, int Y, int Xg, int Yg,
	OpFeedbackParam<Integer> NewX, OpFeedbackParam<Integer> NewY,
	OpFeedbackParam<Integer> Inter){
		int bestAction = 0;
		int newX = X, newY = Y;
		
		bestAction = getBestAction(ID, X, Y, Xg, Yg);

        switch (bestAction) {
            case 0: //Esq
                if (X > 0) newX = X - 1;
                break;
            case 1: //Baixo
                if (Y < colunas - 1) newY = Y + 1;
                break;
            case 2: //Dir
                if (X < linhas - 1) newX = X + 1;
                break;
            case 3: //Cima
                if (Y > 0) newY = Y - 1;
                break;
			default:
				break;
        }
		
		if(grid[newX][newY] == -1)
		{
			gridVisitado[ID-1][newX][newY]=2;
			newX = X;
			newY = Y;
		}
		else if(grid[newX][newY] > 0)
		{
			gridVisitado[ID-1][newX][newY]=1;
			newX = X;
			newY = Y;
		}
		
		gridVisitado[ID-1][X][Y] = 1;
		
		grid[X][Y] = backupValor[ID-1];
		
		if(grid[X][Y] <= 0 && (X != newX || Y != newY))
		{
			backupValor[ID-1] = grid[newX][newY];
		}
		
		grid[newX][newY]= ID;
		Inter.set(backupValor[ID-1]);
		NewX.set(newX);
		NewY.set(newY);
	}

	int calcHeur(int ID, int X, int Y, int Xg, int Yg)
	{
		Random rand = new Random();
    	return Math.abs(X - Xg) + Math.abs(Y - Yg) + rand.nextInt(3);
	}

	int getBestAction(int ID, int X, int Y, int Xg, int Yg)
	{
		int[] dx = {-1, 0, 1, 0};
		int[] dy = {0, 1, 0, -1};
		int bestAction = -1;
		int minHeur = Integer.MAX_VALUE;

		for (int i = 0; i < 4; i++) {
			int newX = X + dx[i];
			int newY = Y + dy[i];

			if (newX >= 0 && newX < linhas && newY >= 0 && newY < colunas
			&& gridVisitado[ID-1][newX][newY] <= 0 && (grid[newX][newY] == 0 || grid[newX][newY] < -1)) {
				int heur = calcHeur(ID, newX, newY, Xg, Yg);
				if (heur < minHeur) {
					minHeur = heur;
					bestAction = i;
				}
			}
		}

		if(bestAction == -1)
		{
			for(int i=0; i < linhas;i++)
			{
				for(int j=0; j < colunas; j++)
				{
					if(gridVisitado[ID-1][i][j] == 1)
					{
						gridVisitado[ID-1][i][j] = 0;
					}
				}
			}
			Random rand = new Random();
			bestAction = rand.nextInt(4);
		}

		return bestAction;
	}

}
