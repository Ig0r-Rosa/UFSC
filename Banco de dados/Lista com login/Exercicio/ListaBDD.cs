using MySql.Data.MySqlClient;
using System;
using System.Collections.Generic;
using System.Data;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Exercicio
{
    public static class ListaBDD
    {
        private static MySqlCommand comando = null;
        private static DataTable tabela;
        private static MySqlDataAdapter adaptador;

        public static DataTable Lista(string usuario)
        {
            string query = "SELECT exercicio_6_1.Produtos.nome, exercicio_6_1.Produtos.valor FROM exercicio_6_1.Produtos where fk_Conta_Login = (@login)";
            comando = ConectarSQL.QueryBDD(query, usuario);
            if (comando != null)
            {
                tabela = new DataTable();
                adaptador = new MySqlDataAdapter(comando);
                adaptador.Fill(tabela);
            }
            return tabela;
        }
    }
}
