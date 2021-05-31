import time

def encrypt(string):
    num = 13
    encrypted_string = ''
    for char in string:
        encrypted_string += chr(ord(char) + num)
    return encrypted_string


def decrypt(encrypted_string):
    num = 13
    string = ''
    for char in encrypted_string:
        string += chr(ord(char) - num)
    return string


def return_file_line(username, password):
    return '|{}|{}|\n'.format(username, password)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    lines = []
    with open('base.txt', 'r') as file:
        lines = file.readlines()

    # Puts all users into a list of tuples
    users = [(line.split('|')[1], line.split('|')[2]) for line in lines]

    # Calculates mean time added to authenticate user
    start_auth_time = time.time()
    [encrypt(user[1]) for user in users]
    end_auth_time = time.time()

    mean_added_auth_time = (end_auth_time - start_auth_time) / len(lines)

    # Encrypts all users and adds them to a file
    start_all_time = time.time()

    with open('encrypted_base.txt', 'w') as encrypted_file:
        for user in users:
            encrypted_file.write(return_file_line(user[0], encrypt(user[1])))

    end_all_time = time.time()

    time_to_encrypt_all = end_all_time - start_all_time

    print('Mean time added per user: {} seconds'.format(mean_added_auth_time))
    print('Total time: {:.2f} seconds'.format(time_to_encrypt_all))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
