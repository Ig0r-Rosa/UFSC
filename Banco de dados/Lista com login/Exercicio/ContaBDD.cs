using MySql.Data.MySqlClient;
using System;
using System.Collections.Generic;
using System.Data;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Exercicio
{
    public static class ContaBDD
    {
        private static MySqlCommand comando = null;
        private static DataTable tabela;
        private static MySqlDataAdapter adaptador;

        public static Conta VerificarUsuario(string usuario)
        {
            string query = "SELECT * FROM exercicio_6_1.Conta where login = (@login) limit 1";
            comando = ConectarSQL.QueryBDD(query, usuario);
            Conta aUser = null;
            if (comando != null)
            {
                tabela = new DataTable();
                adaptador = new MySqlDataAdapter(comando);
                adaptador.Fill(tabela);
                foreach (DataRow dr in tabela.Rows)
                {
                    string uName = dr["login"].ToString();
                    string password = dr["senha"].ToString();
                    aUser = new Conta(uName, password);
                }
            }
            return aUser;
        }
    }
}
