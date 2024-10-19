
from sql_connection import get_sql_connection

def get_all_products(connection):
    cursor=connection.cursor()
    query="SELECT Product_id , Product_name , Price_per_unit , uom_name FROM grocery_management_system.products inner join grocery_management_system.uom on products.uom_id=uom.uom_id ;"
    cursor.execute(query)
    response=[]
    for(Product_id,Product_name,Price_per_unit,uom_name) in cursor:
        response.append({
            "Product_id":Product_id,
            "Product_name":Product_name,
            "Price_per_unit":Price_per_unit,
            "uom_name":uom_name })
        
    return response

def insert_new_product(connection,product):
    cursor=connection.cursor()

    query="insert into products (Product_name ,Price_per_unit,uom_id) values(%s,%s,%s)"
    data=(product["Product_name"],product["Price_per_unit"],product["uom_id"])
    cursor.execute(query,data)

    connection.commit()

    return cursor.lastrowid

def delete_product(connection,pid):
    cursor=connection.cursor()
    query="delete from products where Product_id=" + str(pid)
    cursor.execute(query)
    connection.commit()


if __name__=="__main__":
    connection=get_sql_connection()
    delete_product(connection,5)
    
