# Inventory Management System

A software developed using Python which provides a easy way to track the products, customers as well as purchase and sales information. It  is a command line interface tool which is very light and it is designed to provide a user friendly and engaging interface. It can run continuously and perform different operations that user want unless the user opt for the exit option. It generates bill.txt file to print bills for the customer and  also keeps a copy of the same in the system. It all stores transactions of today total sales, total all time sales. It can delete a product automatically from the product records when it is purchased and the product id is released so when a new product is  added instead of using (max + 1) product id it actually search for products id's that was released and assign the product id  to the product so that it can prevent overgrowing of numbers in product id's. It uses .json files to store the records.

## Features
1. Show All Products
2. Add New Product
3. Update Product
    * Update By Product Id
    * Update By Product Name
    * Update By Product Category
4. Delete Product
    * Delete By Product Id
    * Delete By Product Name
    * Delete By Product Category
 5. Search Product
    * Search By Product Id
    * Search By Product Name
    * Search By Product Category
6. Add New Purchase
7. View Sales
     * View Today Sales
     * View All Sales
       -  All Sales Table
       - Enter Specific Date To See A Record in Detail
8. Exit

## Files

There is a **ims.py file**  which is our main program that we have to run besides these there is one **Products.json file** which keep records of all the products available. It is placed in the same directory as of the ims.py file. 
There is one  **Sales folder** also placed in the same directory. Inside this folder there is one **All_sales.json file** which keep record of all the products purchased and this program also generates **[date].json file** automatically in the Sales folder  to keep record of all  purchase on a particular day. 
There is a **Bills folder** inside Sales Folder. Inside this folder there are folders named [date] automatically generated by the program when needed and inside those date folders we will have **Bill_No-[x].txt files** stored which can be used to print bills and keep record of the bills in the system.

## Create files and folders

It can make all the required files and folders by itself if it is not available. For this the **os** module is used

## Requirements

**Python** should be installed on the system and **json, datetime and os libraries** are also required to function correctly.
