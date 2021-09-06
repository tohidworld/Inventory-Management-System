import json
from datetime import date
import os
def load_file(filename):
    file = open(filename,'r')
    all_content = file.read()
    file.close()
    contents = json.loads(all_content)
    return contents
def save_file(filename,dict):
    json_content = json.dumps(dict)
    file = open(filename,'w')
    file.write(json_content)
    file.close()
def fix_length(text,length):
        if len(text) > length:
            text = text[:length]
        elif len(text) < length:
            text = (text + " "*length)[:length]
        return text       
def print_table(dict):
    print('\nProduct Details')
    product_table = '|Product Id | Product Catogery | Product Name | Product Price | Expiry Date | Warranty Period|'
    print('\n'+product_table)
    print("|"+"="*92+"|")
    for key in dict.keys():
        print("|"+fix_length(str(key),len('Product Id'))+" | "+fix_length(str(dict[key]['product_category']),len('product_category'))+" | "+fix_length(str(dict[key]['product_name']),len('product_name'))+" | "+fix_length(str(dict[key]['product_price']),len('product_price'))+" | "+fix_length(str(dict[key]['expiry_date']),len('expiry_date'))+" | "+fix_length(str(dict[key]['warranty_period']),len('warranty_period'))+"|")
def search_by_id(product_id, dict):
    product_details = {product_id: dict[product_id]}
    return product_details
def search_by_name(product_name, dict):
    product_details = {}
    for key in dict.keys():
        if product_name == dict[key]['product_name']:
            product_details.update({key: dict[key]})
    return product_details
def search_by_category(product_category, dict):
    product_details = {}
    for key in dict.keys():
        if product_category == dict[key]['product_category']:
            product_details.update({key: dict[key]})
    return product_details
def display_products():
    try:
        products = load_file('Product.json')
        product_keys = int(max(products.keys()))
        print_table(products)        
        response = input("\nPress Any Key To Return To Main Menu Or 1 To Exit The Program: ")
    except:
        print("\nNo Product Available Please Add Some Product To Display")    
    return response
def add_product():
    while True:
        try:
            products = load_file('Product.json')
            lst = []
            for key in products.keys():
                lst.append(int(key))
            lst.sort()        
            new_key =  lst[-1] + 1
            for i in range(1, lst[-1]):
                if i not in lst:
                    new_key = i
                    break
        except:
            products = {}
            new_key = 1
        new_product = {}
        new_product[new_key]  = {}
        new_product[new_key]['product_category'] = input('\nEnter Product Category: ')
        if new_product[new_key]['product_category'] != '':
            new_product[new_key]['product_name'] = input('Enter Product Name: ')
            if new_product[new_key]['product_name'] != '':
                new_product[new_key]['product_price'] = input('Enter Product Price: ')
                if new_product[new_key]['product_price'].isdigit():
                    new_product[new_key]['expiry_date'] = input('Enter Expiry Date: ')
                    if new_product[new_key]['expiry_date'] == '':
                        new_product[new_key]['expiry_date'] = '-'
                    new_product[new_key]['warranty_period'] = input('Enter Warranty Period: ')
                    if new_product[new_key]['warranty_period'] == '':
                        new_product[new_key]['warranty_period'] = '-'
                    print_table(new_product)
                    confirmation = input('\nDo You Want To Add This Product (Press Y or y for yes any other key to cancel): ')
                    if confirmation == 'Y' or confirmation == 'y':
                        products.update(new_product)
                        save_file('Product.json',products)
                        print("Product Added Successfully!")
                    else:
                        print("Transection Cancelled")
                else:
                    print('Please Enter Proper Integer In Productd Price')
                    print("Transection Cancelled")
            else:
                print('Product Name cant be empty')
                print("Transection Cancelled")
        else:
            print('\nProduct Category cant be empty')
            print("Transection Cancelled")
        response = input("\nPress Any Key To Continue In This Menu, 0 To Return To Main Menu Or 1 To Exit The Program: ")
        if response == '0':
            break
        if response == '1':
            break
    return response
def update_by_id(product_id,product_details):
    print("\n1 - Update Product Category\n2 - Update Product Name\n3 - Update Product Price\n4 - Update Expiry Date\n5 - Update Warranty Period")
    update_option = input('Select Option: ')
    if update_option == '1':
        product_details[product_id]['product_category'] = input('\nEnter Product Category: ')
        if product_details[product_id]['product_category'] != '':
            check = 0
        else:
            print('\nProduct Category cant be empty')
            print("Transection Cancelled")
            check = 1
    elif update_option == '2':
        product_details[product_id]['product_name'] = input('Enter Product Name: ')
        if product_details[product_id]['product_name'] != '':
            check = 0
        else:
            print('\nProduct Name cant be empty')
            print("Transection Cancelled")
            check = 1
    elif update_option == '3':
        product_details[product_id]['product_price'] = input('Enter Product Price: ')
        if product_details[product_id]['product_price'].isdigit():
            check = 0
        else:
            print('\nPlease Enter Proper Integer In Productd Price')
            print("Transection Cancelled")
            check = 1
    elif update_option == '4':
        product_details[product_id]['expiry_date'] = input('Enter Expiry Date: ')
        if product_details[product_id]['expiry_date'] == '':
            product_details[product_id]['expiry_date'] = '-'
        check = 0
    elif update_option == '5':
        product_details[product_id]['warranty_period'] = input('Enter Warranty Period: ')
        if product_details[product_id]['warranty_period'] == '':
            product_details[product_id]['warranty_period'] = '-'
        check = 0
    else:
        print("\nInvalid Option Selected")
        print("Transection Cancelled")
        check = 1
    return product_details, check
def update_product():
    while True:
        try:
            products = load_file('Product.json')
            product_keys = int(max(products.keys()))
            check = 0
        except:
            print("\nNo Product Available To Update")
            check = 1
        if check == 0:
            print("\n1 - Update By Product ID\n2 - Update By Product Name\n3 - Update By Product Category")
            option = input('Select Option: ')
            if option == '1':
                product_id = input("Enter Product Id: ")
                if product_id in products:
                    product_details = search_by_id(product_id, products)
                    print_table(product_details)
                    confirmation = input("\nDo You Want To Update This Product (Press Y or y for yes any other key to cancel): ")
                    if confirmation == 'Y' or confirmation == 'y':
                        product_details, check = update_by_id(product_id, product_details)                        
                        if check == 0:
                            print_table(product_details)
                            confirmation = input('\nDo You Want To Update This Product (Press Y or y for yes any other key to cancel): ')
                        if confirmation == 'Y' or confirmation == 'y':
                            products.update(product_details)
                            save_file('Product.json',products)
                            print("Product Updated Successfully!")
                        else:
                            print("Transection Cancelled")                    
                    else:
                        print("Transection Cancelled")
                else:
                        print("\nInvalid Product Id")
            elif option == '2':
                    product_name = input("Enter Product Name: ")
                    product_details = search_by_name(product_name, products)
                    if len(product_details.keys()) != 0:
                        print_table(product_details)
                        if len(product_details.keys()) == 1:                            
                            confirmation = input('\nDo You Want To Update This Product (Press Y or y for yes any other key to cancel): ')
                            if confirmation == 'Y' or confirmation == 'y':
                                for key in product_details.keys():
                                    product_id = key
                                product_details, check = update_by_id(product_id, product_details)                        
                            if check == 0:
                                print_table(product_details)
                                confirmation = input('\nDo You Want To Update This Product (Press Y or y for yes any other key to cancel): ')
                                if confirmation == 'Y' or confirmation == 'y':
                                    products.update(product_details)
                                    save_file('Product.json',products)
                                    print("Product Updated Successfully!")
                                else:
                                    print("Transection Cancelled")                    
                            else:
                                print("Transection Cancelled")                            
                        else:
                            print("Multiple Product With Same Name Available")
                            product_id = input("Enter Product Id To Continue Any Other Key To Exit: ")
                            if product_id in product_details.keys():
                                print_table({product_id: product_details[product_id]})
                                confirmation = input('\nDo You Want To Update This Product (Press Y or y for yes any other key to cancel): ')
                                if confirmation == 'Y' or confirmation == 'y':
                                    product_details = {product_id: product_details[product_id]}
                                    product_details, check = update_by_id(product_id, product_details)                        
                                if check == 0:
                                    print_table(product_details)
                                    confirmation = input('\nDo You Want To Update This Product (Press Y or y for yes any other key to cancel): ')
                                    if confirmation == 'Y' or confirmation == 'y':
                                        products.update(product_details)
                                        save_file('Product.json',products)
                                        print("Product Updated Successfully!")
                                    else:
                                        print("Transection Cancelled")                    
                                else:
                                    print("Transection Cancelled")
                            else:
                                print("Transection Cancelled")
                    else:
                        print("No Product Available With This Name")
            elif option == '3':
                    product_category = input("Enter Product Category: ")
                    product_details = search_by_category(product_category, products)
                    if len(product_details.keys()) != 0:
                        print_table(product_details)
                        if len(product_details.keys()) == 1:                            
                            confirmation = input('\nDo You Want To Update This Product (Press Y or y for yes any other key to cancel): ')
                            if confirmation == 'Y' or confirmation == 'y':
                                for key in product_details.keys():
                                    product_id = key
                                product_details, check = update_by_id(product_id, product_details)                        
                            if check == 0:
                                print_table(product_details)
                                confirmation = input('\nDo You Want To Update This Product (Press Y or y for yes any other key to cancel): ')
                                if confirmation == 'Y' or confirmation == 'y':
                                    products.update(product_details)
                                    save_file('Product.json',products)
                                    print("Product Updated Successfully!")
                                else:
                                    print("Transection Cancelled")                    
                            else:
                                print("Transection Cancelled")                            
                        else:
                            print("Multiple Product With Same Category Available")
                            product_id = input("Enter Product Id To Continue Any Other Key To Exit: ")
                            if product_id in product_details.keys():
                                print_table({product_id: product_details[product_id]})
                                confirmation = input('\nDo You Want To Update This Product (Press Y or y for yes any other key to cancel): ')
                                if confirmation == 'Y' or confirmation == 'y':
                                    product_details = {product_id: product_details[product_id]}
                                    product_details, check = update_by_id(product_id, product_details)                        
                                if check == 0:
                                    print_table(product_details)
                                    confirmation = input('\nDo You Want To Update This Product (Press Y or y for yes any other key to cancel): ')
                                    if confirmation == 'Y' or confirmation == 'y':
                                        products.update(product_details)
                                        save_file('Product.json',products)
                                        print("Product Updated Successfully!")
                                    else:
                                        print("Transection Cancelled")                    
                                else:
                                    print("Transection Cancelled")
                            else:
                                print("Transection Cancelled")
                    else:
                        print("No Product Available With This Category")
            else:
                print("\nInvalid Option Selected")
                print("Transection Cancelled")
            response = input("\nPress Any Key To Continue In This Menu, 0 To Return To Main Menu Or 1 To Exit The Program: ")
        else:
            break
        if response == '0':
            break
        if response == '1':
            break
    return response
def delete_product():
    while True:
        try:
            products = load_file('Product.json')
            product_keys = int(max(products.keys()))
            check = 0
        except:
            print("\nNo Product Available To Delete")
            check = 1
        if check == 0:
            print("\n1 - Delete By Product ID\n2 - Delete By Product Name\n3 - Delete By Product Category")
            option = input('Select Option: ')
            if option == '1':
                product_id = input("Enter Product Id: ")
                if product_id in products:
                    print_table({product_id: products[product_id]})
                    confirmation = input("\nDo You Want To Delete This Product (Press Y or y for yes any other key to cancel): ")
                    if confirmation == 'Y' or confirmation == 'y':
                        del products[product_id]
                        save_file('Product.json',products)
                        print("Product Deleted Successfully!")                   
                    else:
                        print("Transection Cancelled")
                else:
                        print("\nInvalid Product Id")
            elif option == '2':
                product_name = input("Enter Product Name: ")
                product_details = search_by_name(product_name, products)
                if len(product_details.keys()) != 0:
                    print_table(product_details)
                    if len(product_details.keys()) == 1:                            
                        confirmation = input('\nDo You Want To Delete This Product (Press Y or y for yes any other key to cancel): ')
                        if confirmation == 'Y' or confirmation == 'y':
                            for key in product_details.keys():
                                product_id = key
                            del products[product_id]
                            save_file('Product.json',products)
                            print("Product Deleted Successfully!")                    
                        else:
                            print("Transection Cancelled")                            
                    else:
                        print("Multiple Product With Same Category Available")
                        product_id = input("Enter Product Id To Continue, a or 'A' To Delete All Product By Same Name or Any Other Key To Exit: ")
                        if product_id in products.keys():
                                print_table({product_id: product_details[product_id]})
                                confirmation = input('\nDo You Want To Delete This Product (Press Y or y for yes any other key to cancel): ')
                                if confirmation == 'Y' or confirmation == 'y':
                                    del products[product_id]
                                    save_file('Product.json',products)
                                    print("Product Deleted Successfully!")                    
                                else:
                                    print("Transection Cancelled")
                        elif product_id == 'A' or product_id == 'a':
                            for key in product_details.keys():
                                del products[key]
                            save_file('Product.json',products)
                            print("Product Deleted Successfully!")
                        else:
                            print("Transection Cancelled")
                else:
                    print("No Product Available With This Name")
            elif option == '3':
                product_category = input("Enter Product Category: ")
                product_details = search_by_category(product_category, products)
                if len(product_details.keys()) != 0:
                    print_table(product_details)
                    if len(product_details.keys()) == 1:                            
                        confirmation = input('\nDo You Want To Delete This Product (Press Y or y for yes any other key to cancel): ')
                        if confirmation == 'Y' or confirmation == 'y':
                            for key in product_details.keys():
                                product_id = key
                            del products[product_id]
                            save_file('Product.json',products)
                            print("Product Deleted Successfully!")                    
                        else:
                            print("Transection Cancelled")                            
                    else:
                        print("Multiple Product With Same Name Available")
                        product_id = input("Enter Product Id To Continue, a or 'A' To Delete All Product By Same Name or Any Other Key To Exit: ")
                        if product_id in products.keys():
                                print_table({product_id: product_details[product_id]})
                                confirmation = input('\nDo You Want To Delete This Product (Press Y or y for yes any other key to cancel): ')
                                if confirmation == 'Y' or confirmation == 'y':
                                    del products[product_id]
                                    save_file('Product.json',products)
                                    print("Product Deleted Successfully!")                    
                                else:
                                    print("Transection Cancelled")
                        elif product_id == 'A' or product_id == 'a':
                            for key in product_details.keys():
                                del products[key]
                            save_file('Product.json',products)
                            print("Product Deleted Successfully!")
                        else:
                            print("Transection Cancelled")
                else:
                    print("No Product Available With This Category")
            else:
                print("\nInvalid Option Selected")
                print("Transection Cancelled")
            response = input("\nPress Any Key To Continue In This Menu, 0 To Return To Main Menu Or 1 To Exit The Program: ")
        else:
            break
        if response == '0':
            break
        if response == '1':
            break
    return response
def search_product():
    while True:
        try:
            products = load_file('Product.json')
            product_keys = int(max(products.keys()))
            check = 0
        except:
            print("\nNo Product Available")
            check = 1
        if check == 0:
            print("\n1 - Search By Product ID\n2 - Search By Product Name\n3 - Search By Product Category")
            option = input('Select Option: ')
            if option == '1':
                product_id = input("Enter Product Id: ")
                if product_id in products:
                    print_table({product_id: products[product_id]})
                else:
                        print("\nInvalid Product Id")
            elif option == '2':
                product_name = input("Enter Product Name: ")
                product_details = search_by_name(product_name, products)
                if len(product_details.keys()) != 0:
                    print_table(product_details)
                else:
                    print("No Product Available With This Name")
            elif option == '3':
                product_category = input("Enter Product Category: ")
                product_details = search_by_category(product_category, products)
                if len(product_details.keys()) != 0:
                    print_table(product_details)
                else:
                    print("No Product Available With This Category")
            else:
                print("\nInvalid Option Selected")
                print("Transection Cancelled")
            response = input("\nPress Any Key To Continue In This Menu, 0 To Return To Main Menu Or 1 To Exit The Program: ")
        else:
            break
        if response == '0':
            break
        if response == '1':
            break
    return response
def print_sales_table(dict):
    header = '|Bill No | Customer Name | Customer Phone No | Product Id | Product Name | Product Price|'
    print('\n'+header)
    print("|"+"="*87+"|")
    for key in dict.keys():
        if key != 'today_total':
            check = 0
            for product in dict[key]['products'].keys():
                if check == 0:
                    print("|"+fix_length(str(key),len('Bill No'))+" | "+fix_length(str(dict[key]['customer_name']),len('customer_name'))+" | "+fix_length(str(dict[key]['customer_number']),len('customer_phone_no'))+" | "+fix_length(str(product),len('Product Id'))+" | "+fix_length(str(dict[key]['products'][product]['product_name']),len('product_name'))+" | "+fix_length(str(dict[key]['products'][product]['product_price']),len('product_price'))+"|")
                    check = 1
                else:
                    print("|"+fix_length(' ',len('Bill No'))+" | "+fix_length(' ',len('customer_name'))+" | "+fix_length(' ',len('customer_phone_no'))+" | "+fix_length(str(product),len('Product Id'))+" | "+fix_length(str(dict[key]['products'][product]['product_name']),len('product_name'))+" | "+fix_length(str(dict[key]['products'][product]['product_price']),len('product_price'))+"|")
            print("|"+"-"*87+"|") 
            print("|"+" "*66+"Total = "+fix_length(str(dict[key]['total']),len('product_price'))+"|")            
            print("|"+"="*87+"|")
def generate_bill(foldername,dict):
    if not os.path.isdir('Sales/Bills/'+foldername):
        os.mkdir('Sales/Bills/'+foldername)
    for key in dict.keys():
        content = ' '*16+'Thank You'+' '*16+'\n\nDate: '+foldername+'\nBill No: '+str(key)+'\nName:'+str(dict[key]['customer_name'])+'\nPhone Number: '+str(dict[key]['customer_number'])+'\n'+'='*41+'\nProduct Id   Product Name   Product Price\n'+'='*41+'\n'
        for product in dict[key]['products'].keys():
            content = content + fix_length(str(product),len('Product Id'))+"   "+fix_length(str(dict[key]['products'][product]['product_name']),len('product_name'))+"   "+fix_length(str(dict[key]['products'][product]['product_price']),len('product_price'))+'\n'
        content = content + '='*41+'\n'+' '*20+'Total = '+fix_length(str(dict[key]['total']),len('product_price'))
        file = open('Sales/Bills/'+foldername+'/Bill_No-'+str(key)+'.txt','w')
        file.write(content)
        file.close()
        print('Bill Saved At Sales/Bills/'+foldername+'/Bill_No-'+str(key)+'.txt')
def new_purchase():
    while True:        
        try:
            products = load_file('Product.json')
            product_keys = int(max(products.keys()))
            check = 0
        except:
            print("\nNo Product Available To Purchase")
            check = 1                   
        if check == 0:
            today = date.today().strftime("%d-%b-%Y")
            filename = 'Sales/'+today+'.json'
            max_bill_no = 0
            try:
                all_sales = load_file('Sales/All_Sales.json')
                all_total = int(all_sales['all_total'])
            except:
                all_sales = {}
                all_total = 0
            try:
                sales = load_file(filename)
                for key in sales:
                    if key != 'today_total':
                        if int(max_bill_no) < int(key):
                            max_bill_no = key
                new_bill = int(max_bill_no) + 1
                today_total = int(sales['today_total'])            
            except:
                sales = {}
                today_total = 0
                new_bill = 1 
            new_purchase = {}
            new_purchase[new_bill] = {}
            new_purchase[new_bill]['products'] = {}
            new_purchase[new_bill]['customer_name'] = input('\nEnter Customer Name: ')
            if  new_purchase[new_bill]['customer_name'] == '':
                print("Customer Name Can't Be Empty")
            else:
                new_purchase[new_bill]['customer_number'] = input('\nEnter Customer Phone Number: ')
                while True:
                    product_id = input("Enter Product Id To Add Product Or Any Other Key To Proceed To Checkout: ")
                    if product_id in products:
                        if product_id not in new_purchase[new_bill]['products'].keys():
                            print_table({product_id: products[product_id]})
                            confirmation = input("\nDo You Want To Add This Product (Press Y or y for yes any other key to cancel): ")
                            if confirmation == 'Y' or confirmation == 'y':
                                new_purchase[new_bill]['products'][product_id] = {}
                                new_purchase[new_bill]['products'][product_id]['product_name'] = products[product_id]['product_name']
                                new_purchase[new_bill]['products'][product_id]['product_price'] = products[product_id]['product_price']
                        else:
                            print("Product Already Added")
                    else:
                        if len(new_purchase[new_bill]['products'].keys()) < 1:
                            check_cart = 0
                            print("No Product Added")
                            break
                        else:
                            check_cart = 1
                            total = 0
                            for key in new_purchase[new_bill]['products'].keys():
                                total = total + int(new_purchase[new_bill]['products'][key]['product_price'])
                            new_purchase[new_bill]['total'] = total
                            break
                if check_cart == 1:
                    print('\nBill Details')
                    print_sales_table(new_purchase)
                    confirmation = input("\nDo You Want To Confirm This Transaction (Press Y or y for yes any other key to cancel): ")
                    if confirmation == 'Y' or confirmation == 'y':
                        today_total = today_total + total
                        all_total = all_total + total
                        sales['today_total'] = today_total
                        all_sales['all_total'] = all_total
                        sales.update(new_purchase)
                        all_sales[today] = today_total
                        save_file(filename,sales)
                        save_file('Sales/All_Sales.json',all_sales)
                        for key in new_purchase[new_bill]['products'].keys():
                                del products[key]
                        save_file('Product.json',products)
                        print("Teansaction Completed Successfully")                        
                        generate_bill(today,new_purchase)
                    else:
                        print("Teansaction Cancelled")
            response = input("\nPress Any Key To Continue In This Menu, 0 To Return To Main Menu Or 1 To Exit The Program: ")
        else:
            break
        if response == '0':
            break
        if response == '1':
            break
    return response
def view_sales():
    while True:
        print("\n1 - View Today Sales\n2 - View All Sales")
        option = input('Select Option: ')
        if option == '1':
            today = date.today().strftime("%d-%b-%Y")
            filename = 'Sales/'+today+'.json'
            try:
                today_sales = load_file(filename)
                print("\nSales Details")
                print_sales_table(today_sales)
                print(" "*63+"All Total = "+fix_length(str(today_sales['today_total']),len('Product Price')))
            except:
                print("\nNo Data Available To Display")
        elif option == '2':
            try:
                all_sales = load_file('Sales/All_Sales.json')
                check = 0
            except:
                print("\nNo Data Available To Display")
                check = 1
            if check == 0:
                while True:
                    print("\nAll Sales Details")
                    header = '|Date        | Total Collection|'
                    print('\n'+header)
                    for key in all_sales:
                        if key != 'all_total':
                            print("|"+fix_length(str(key),11)+" | "+fix_length(str(all_sales[key]),len('Total Collection'))+"|")
                    print("|"+"="*30+"|")
                    print(" "*7+"Total = "+fix_length(str(all_sales['all_total']),len('Total Collection'))+" ")
                    all_sales_date = input("Enter Date To View In Detail Or Any Other Key To Exit: ")
                    if all_sales_date in all_sales.keys():
                        filename = 'Sales/'+all_sales_date+'.json'
                        try:
                            sales = load_file(filename)
                            print("\nSales Details")
                            print_sales_table(sales)
                            print(" "*63+"All Total = "+fix_length(str(sales['today_total']),len('Product Price')))
                            input("\nPress Any Key To Go Back To Previous Menu: ")
                        except:
                            print("\nNo Data Available To Display Please Select Another Date")
                        break
                    else:
                        break                   
        else:
            print("\nInvalid Option Selected")
        response = input("\nPress Any Key To Continue In View Sales Menu, 0 To Return To Main Menu Or 1 To Exit The Program: ")
        if response == '0':
            break
        if response == '1':
            break
    return response
if not os.path.isdir('Sales'):
    os.mkdir('Sales')
if not os.path.isdir('Sales/Bills'):
  os.mkdir('Sales/Bills')            
print("\n***********Inventory Management System***********")
while True:
    print("\n**********Menu**********")
    print("1 - Show All Products\n2 - Add New Product\n3 - Update Product\n4 - Delete A Product\n5 - Search product\n6 - Add New Purchase\n7 - View Sales\n8 - Exit")
    try:
        option = int(input('Select An Option: '))
        if option < 1 or option > 8:
            print("\n**********Please Select A Valid Option**********")
        else:
            if option == 1:
                print("\n**********All Products**********")
                response = display_products()
                if response == '1':
                    break
            if option == 2:
                print("\n**********Add New Product**********")
                response = add_product()
                if response == '1':
                    break
            if option == 3:
                print("\n**********Update Product**********")
                response = update_product()
                if response == '1':
                    break
            if option == 4:
                print("\n**********Delete Product**********")
                response = delete_product()
                if response == '1':
                    break
            if option == 5:
                print("\n*********Search Product**********")
                response = search_product()
                if response == '1':
                    break
            if option == 6:
                print("\n*********Add New Purchase**********")
                response = new_purchase()
                if response == '1':
                    break
            if option == 7:
                print("\n*********View Sales**********")
                response = view_sales()
                if response == '1':
                    break
            if option == 8:
                break
    except:
        print("\n**********Please Select A Valid Option**********")
print("Program Exited Sucessfully")