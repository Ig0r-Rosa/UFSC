using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Exercicio
{
    public partial class cadastro : Form
    {
        public cadastro()
        {
            InitializeComponent();
        }

        private void cadastrar_Click(object sender, EventArgs e)
        {
            try
            {
                string query = "insert into exercicio_6_1.Conta(login, senha) values(@login,@senha);commit;";
                if(ConectarSQL.QueryInsertConta(query, ContaText.Text, SenhaText.Text))
                {
                    MessageBox.Show("Cadastrado com sucesso!!");
                    Close();
                }
                else
                {
                    MessageBox.Show("Não foi possivel cadastrar, tente novamente!!");
                }
            }
            catch
            {
                MessageBox.Show("Não foi possivel cadastrar, tente novamente!!");
            }
        }
    }
}
