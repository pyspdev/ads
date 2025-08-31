import duckdb
con = duckdb.connect('mydb.duckdb')
con.execute("CREATE TABLE test (id INTEGER)")
con.close()
print("DuckDB works!")