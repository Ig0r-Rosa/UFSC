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
    public partial class Programa : Form
    {
        public Programa()
        {
            InitializeComponent();
            if(ConectarSQL.Conectar("exercicio_6_1"))
            {
                StatusCon.Text = "Conectado com sucesso!!";
            }
            else
            {
                StatusCon.Text = "Não foi conectado :C";
            }
        }

        private void Entrar_Click(object sender, EventArgs e)
        {
            string usuario = TextLogin.Text;
            string senha = TextSenha.Text;

            Conta aUser = ContaBDD.VerificarUsuario(usuario);
            if (aUser != null && aUser.Password == senha)
            {
                MessageBox.Show("Você logou com sucesso!!");
                Logado f2 = new Logado(aUser);
                f2.Show();
            }
            else
            {
                MessageBox.Show("Não logou, tente novamente!");
                TextLogin.Text = "";
                TextSenha.Text = "";
            }
        }

        private void Cadastrar_Click(object sender, EventArgs e)
        {
            cadastro f3 = new cadastro();
            f3.Show();
        }
    }
}
