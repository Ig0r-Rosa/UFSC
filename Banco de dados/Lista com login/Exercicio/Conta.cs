using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Exercicio
{
    public class Conta
    {
        private string _usuario;
        private string _senha;

        public Conta(string login, string senha)
        {
            UserName = login;
            Password = senha;
        }

        public String UserName
        {
            get { return _usuario; }
            set { _usuario = value; }
        }

        public String Password
        {
            get { return _senha; }
            set { _senha = value; }
        }
    }
}
