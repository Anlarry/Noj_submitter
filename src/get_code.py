def get_code(file_name):
    "get code from file"
    code = ""
    try:
        F = open(file_name, "r", encoding = "utf-8")
        for line in F:
            code += line
        F.close()
    except IOError:
        print("can not find the file")        
    return code

#print(get_code("for_noj\main.py"))
