##question 1
##
##import re
##
##signs = r';|\n'
##
##
##def from_file(fv, store):
##    with open(fv, "r", encoding="utf-8-sig") as f:
##        lines = [line.strip() for line in f if line.strip()]
##
##    if not lines:
##        return ""
##
##    store_title = lines[0]
##
##    for line in lines[1:]:
##        data = re.split(signs, line)
##        if len(data) == 5:
##            store.append(line)
##
##    return store_title
##
##
##def print_store(title, store):
##    print("Building materials store:", title)
##    print("Goods name\tPurpose\t\tPrice\tCountry of origin\tAmount")
##
##    for good in store:
##        data = re.split(signs, good.strip())
##        print(data[0], "\t", data[1], "\t", data[2],
##              "\t", f'{data[3]:<10}', "\t\t", data[4])
##
##
##def find_max_price(store):
##    max_price = 0.1
##    max_name = ""
##
##    for good in store:
##        data = re.split(signs, good.strip())
##
##        if float(data[2]) > max_price:
##            max_price = float(data[2])
##            max_name = data[0]
##
##    return max_price, max_name
##
##
##def rez_file(store1, store2):
##    with open("res_China.txt", "w", encoding="utf-8") as f_res:
##        for good in store1 + store2:
##            data = re.split(signs, good.strip())
##
##            if data[3] == "China" and int(data[4]) > 500:
##                f_res.write(
##                    data[0] + "\t" + data[1] + "\t" +
##                    data[2] + "\t" + data[3] + "\t" +
##                    data[4] + "\n"
##                )
##
##
##store1 = []
##title1 = from_file("no 1.txt", store1)
##print_store(title1, store1)
##
##store2 = []
##title2 = from_file("no 2.txt", store2)
##print_store(title2, store2)
##
##max1, max1_name = find_max_price(store1)
##max2, max2_name = find_max_price(store2)
##
##if max1 > max2:
##    print("Max price is:", max1,
##          "for the good named:", max1_name,
##          "in store:", title1)
##else:
##    print("Max price is:", max2,
##          "for the good named:", max2_name,
##          "in store:", title2)
##
##rez_file(store1, store2)






##Question 2


##def read_file(filename, products):
##    with open(filename, "r", encoding="utf-8") as f:
##        lines = [line.strip() for line in f if line.strip()]
##
##    company_name = lines[0]
##
##    for line in lines[1:]:
##        data = line.split(";")
##        data[1] = float(data[1])
##        data[2] = int(data[2])
##        products.append(data)
##
##    return company_name
##
##
##def print_products(company_name, products):
##    print("\n", company_name)
##    print("Product\t\tPrice\tQuantity")
##
##    for product in products:
##        print(product[0], "\t", product[1], "\t", product[2])
##
##
##def find_max(products):
##    max_price = products[0][1]
##    max_name = products[0][0]
##
##    for product in products:
##        if product[1] > max_price:
##            max_price = product[1]
##            max_name = product[0]
##
##    print("Most expensive product:", max_name)
##    print("Price:", max_price)
##
##
##def calculate_total(products):
##    total = 0
##
##    for product in products:
##        total += product[1] * product[2]
##
##    print("Total value of products:", total)
##
##
##def save_results(products1, products2):
##    with open("juice_results.txt", "w", encoding="utf-8") as f:
##        for product in products1 + products2:
##            if product[2] > 20:
##                f.write(
##                    product[0] + ";" +
##                    str(product[1]) + ";" +
##                    str(product[2]) + "\n"
##                )
##
##
##def main():
##    products1 = []
##    products2 = []
##
##    company1 = read_file("juice1.txt", products1)
##    company2 = read_file("juice2.txt", products2)
##
##    print_products(company1, products1)
##    print_products(company2, products2)
##
##    find_max(products1)
##    find_max(products2)
##
##    calculate_total(products1)
##    calculate_total(products2)
##
##    save_results(products1, products2)
##
##
##main()
##
