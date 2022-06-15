import sqlite3

try:
    conn = sqlite3.connect(database/db_censoapi.db)
    conn.execute('DROP TABLE IF EXISTS tb_regioes')
    conn.execute('''
        CREATE TABLE tb_regioes ( 
            num int NOT NULL AUTO_INCREMENT, 
            nome varchar(50), 
            idh float,   
            cid_populosa varchar(50),  
            PRIMARY KEY (num)  
            );
    ''')
    conn.execute(
        '''
        INSERT INTO `tb_regioes` (nome, idh, cid_populosa)
        VALUES
            ('Sudeste', '0.795', 'São Paulo'),
           ('Nordeste', '0.710', 'Salvador');
        '''
    )
    conn.commit()
    print("Operacao realizada com sucesso!")
except:
    print("ERRO")
finally:
    conn.close()
