namespace Exercicio
{
    partial class Logado
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.usuarioTexto = new System.Windows.Forms.Label();
            this.regProd = new System.Windows.Forms.Button();
            this.ProdText = new System.Windows.Forms.TextBox();
            this.label1 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.ValorNum = new System.Windows.Forms.NumericUpDown();
            this.Lista = new System.Windows.Forms.ListBox();
            ((System.ComponentModel.ISupportInitialize)(this.ValorNum)).BeginInit();
            this.SuspendLayout();
            // 
            // usuarioTexto
            // 
            this.usuarioTexto.AutoSize = true;
            this.usuarioTexto.Location = new System.Drawing.Point(12, 38);
            this.usuarioTexto.Name = "usuarioTexto";
            this.usuarioTexto.Size = new System.Drawing.Size(74, 16);
            this.usuarioTexto.TabIndex = 1;
            this.usuarioTexto.Text = "Bem vindo!";
            // 
            // regProd
            // 
            this.regProd.Location = new System.Drawing.Point(385, 621);
            this.regProd.Name = "regProd";
            this.regProd.Size = new System.Drawing.Size(105, 54);
            this.regProd.TabIndex = 2;
            this.regProd.Text = "Registrar";
            this.regProd.UseVisualStyleBackColor = true;
            this.regProd.Click += new System.EventHandler(this.regProd_Click);
            // 
            // ProdText
            // 
            this.ProdText.Location = new System.Drawing.Point(15, 653);
            this.ProdText.Name = "ProdText";
            this.ProdText.Size = new System.Drawing.Size(198, 22);
            this.ProdText.TabIndex = 3;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(12, 634);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(54, 16);
            this.label1.TabIndex = 5;
            this.label1.Text = "Produto";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(229, 634);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(39, 16);
            this.label2.TabIndex = 6;
            this.label2.Text = "Valor";
            // 
            // ValorNum
            // 
            this.ValorNum.Location = new System.Drawing.Point(232, 653);
            this.ValorNum.Maximum = new decimal(new int[] {
            100000000,
            0,
            0,
            0});
            this.ValorNum.Name = "ValorNum";
            this.ValorNum.Size = new System.Drawing.Size(120, 22);
            this.ValorNum.TabIndex = 7;
            // 
            // Lista
            // 
            this.Lista.FormattingEnabled = true;
            this.Lista.ItemHeight = 16;
            this.Lista.Location = new System.Drawing.Point(15, 93);
            this.Lista.Name = "Lista";
            this.Lista.Size = new System.Drawing.Size(475, 500);
            this.Lista.TabIndex = 8;
            // 
            // Logado
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.Color.Silver;
            this.ClientSize = new System.Drawing.Size(506, 703);
            this.Controls.Add(this.Lista);
            this.Controls.Add(this.ValorNum);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.ProdText);
            this.Controls.Add(this.regProd);
            this.Controls.Add(this.usuarioTexto);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedToolWindow;
            this.Name = "Logado";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "Programa";
            ((System.ComponentModel.ISupportInitialize)(this.ValorNum)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion
        private System.Windows.Forms.Label usuarioTexto;
        private System.Windows.Forms.Button regProd;
        private System.Windows.Forms.TextBox ProdText;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.NumericUpDown ValorNum;
        private System.Windows.Forms.ListBox Lista;
    }
}