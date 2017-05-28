def domain_name(url):
    if '//' not in url:
        m= url.index('.')+1
        n= get_second_index(url,'.')
        return ( url[m:n])
    if 'www'  in url:
        return str(url.split('//')[1].split('.')[1])
    else:
        return url.split('//')[1].split('.')[0]

def get_second_index(input_string, sub_string):
    return input_string.index(sub_string, input_string.index(sub_string) + 1)