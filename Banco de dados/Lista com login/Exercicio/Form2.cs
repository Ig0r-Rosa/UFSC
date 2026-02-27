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
    public partial class Logado : Form
    {
        Conta conta;
        public Logado(Conta usuario)
        {
            InitializeComponent();
            conta = usuario;
            usuarioTexto.Text = "Bem vindo " + conta.UserName + "!!";
            AttLista();
        }

        private void regProd_Click(object sender, EventArgs e)
        {
            try
            {
                string query = "insert into exercicio_6_1.Produtos(nome, valor, fk_Conta_Login) values(@nome,@valor,@fk_Conta_Login);commit;";
                if (ConectarSQL.QueryInsertProd(query, ProdText.Text, Convert.ToInt32(ValorNum.Value), conta.UserName))
                {
                    MessageBox.Show("Cadastrado com sucesso!!");
                    ProdText.Text = "";
                    AttLista();
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

        private void AttLista()
        {
            Lista.Items.Clear();
            DataTable tabela = ListaBDD.Lista(conta.UserName);
            foreach(DataRow dr in tabela.Rows)
            {
                string Produto = dr["nome"].ToString();
                string Valor = dr["valor"].ToString();
                Lista.Items.Add(Produto + " : " + Valor);
            }
        }
    }
}
