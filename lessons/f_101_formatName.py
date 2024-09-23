def f_101_formatName(f_name, l_name):
    """return a formatted name with first letter of first name and last name in uppercase"""
    if f_name == '' or l_name == '':
        return 'Please enter a valid name'
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f'{formated_f_name} {formated_l_name}'

fomated_result = f_101_formatName('john', 'doe') # John Doe
print(f"fomated_result: {fomated_result}")

