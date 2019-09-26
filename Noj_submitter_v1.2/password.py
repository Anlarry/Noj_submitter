import binascii

def Decode(s):
    s = s[2:-1]
    b = s.encode()
    return binascii.a2b_hex(b).decode()


def Insert(user, pd):
    try:
        pd_file = open(".\password.txt", "a")
        user = binascii.b2a_hex(user.encode())
        pd = binascii.b2a_hex(pd.encode())
        # print(user, pd)
        # print(type(user))
        print(user, pd, file=pd_file)
        pd_file.close()

        return 'save succeed'
    except IOError:
        return "can not find password file"

def get_user():
    try :
        pd_file = open(".\password.txt", "r")
        user = {}
        for line in pd_file:
            if line == "\n":
                continue
            line = line.split()
            # print(Decode(line[0]))

            t_u, t_p = map(Decode, line)
            user[t_u] = t_p
            # user.append(t_u)
            # pd.append(t_p)
        pd_file.close()

        return user
    except IOError:
        return []

# def debug():
#     # Insert("sdfs", "sdfs")
#     user= get_user()
#     print(user)

# debug()