extern crate oracle;
use oracle::{Connection};

fn main() {

    let conn = Connection::connect("GWSTD", "chinaport2018", "//192.168.10.133:1521/JGDBM").unwrap();
    let sql = "select ename, sal, comm from emp where empno = :1";
    let mut stmt = conn.prepare(sql, &[]).unwrap();
    let rows = stmt.query(&[]).unwrap();

    // print column types
    for (idx, info) in rows.column_info().iter().enumerate() {
        if idx != 0 {
            print!(",");
        }
        print!("{}", info);
    }
    println!("");

    for row_result in rows {
        // print column values
        for (idx, val) in row_result.unwrap().sql_values().iter().enumerate() {
            if idx != 0 {
                print!(",");
            }
            print!("{}", val);
        }
        println!("");
    }
   
    println!("Hello, world!");
}

