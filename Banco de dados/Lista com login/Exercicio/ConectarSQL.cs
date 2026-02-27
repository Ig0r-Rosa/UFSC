using System;
using System.Collections.Generic;
using System.Data;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using MySql.Data.MySqlClient;

namespace Exercicio
{
    class ConectarSQL
    {
        public static MySqlConnection conexao;
        public static MySqlCommand comando;
        public static MySqlDataAdapter adaptador;
        public static DataTable dataTable;

        //"CREATE DATABASE IF NOT EXISTS nome; use nome"
        //"CREATE TABLE IF NOT EXISTS"

        public static bool Conectar(string BDD)
        {
            try
            {
                MySqlConnectionStringBuilder builder = new MySqlConnectionStringBuilder();
                builder.Server = "127.0.0.1";
                builder.UserID = "usuario";
                builder.Password = "usuario";
                builder.Database = BDD;
                builder.SslMode = MySqlSslMode.None;
                conexao = new MySqlConnection(builder.ToString());
                return true;
            }
            catch
            {
                return false;
            }
        }

        public static MySqlCommand QueryBDD(string query, string login)
        {
            try
            {
                if(conexao != null)
                {
                    conexao.Open();
                    comando = conexao.CreateCommand();
                    comando.CommandType = CommandType.Text;
                    comando.CommandText = query;
                    comando.Parameters.AddWithValue("@login", login);
                    comando.ExecuteNonQuery();
                    conexao.Close();
                }
            }
            catch
            {
                conexao.Close();
            }
            return comando;
        }

        public static bool QueryInsertConta(string query, string usuario, string senha) 
        {
            try
            {
                if (conexao != null)
                {
                    conexao.Open();
                    comando = conexao.CreateCommand();
                    comando.CommandType = CommandType.Text;
                    comando.CommandText = query;
                    comando.Parameters.AddWithValue("@login", usuario);
                    comando.Parameters.AddWithValue("@senha", senha);
                    comando.ExecuteNonQuery();
                    conexao.Close();
                    return true;
                }
                return false;
            }
            catch
            {
                conexao.Close();
                return false;
            }
        }

        public static bool QueryInsertProd(string query, string produto, int valor, string usuario)
        {
            try
            {
                if (conexao != null)
                {
                    conexao.Open();
                    comando = conexao.CreateCommand();
                    comando.CommandType = CommandType.Text;
                    comando.CommandText = query;
                    comando.Parameters.AddWithValue("@nome", produto);
                    comando.Parameters.AddWithValue("@valor", valor);
                    comando.Parameters.AddWithValue("@fk_Conta_Login", usuario);
                    comando.ExecuteNonQuery();
                    conexao.Close();
                    return true;
                }
                return false;
            }
            catch
            {
                conexao.Close();
                return false;
            }
        }

        public static MySqlCommand QueryItens(string query, string usuario)
        {
            try
            {
                if (conexao != null)
                {
                    conexao.Open();
                    comando = conexao.CreateCommand();
                    comando.CommandType = CommandType.Text;
                    comando.CommandText = query;
                    comando.Parameters.AddWithValue("@login", usuario);
                    comando.ExecuteNonQuery();
                    conexao.Close();
                }
            }
            catch
            {
                conexao.Close();
            }
            return comando;
        }
    }
}
