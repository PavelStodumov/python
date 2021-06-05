import re


def email_parse(mail):
    if re.fullmatch(r'[^\s].[^\s]+@[^\s].[^\s]+\.[a-z]{2,}', e_mail):
        return {'username': re.match(r'.[^@]+', mail).group(),
                'domain': re.search(r'[^@]+$', mail).group()}
    else:
        raise ValueError(f'incorrect e-mail {e_mail}')


e_mail = 'someone@geekbrains.ru'
print(email_parse(e_mail))
# как то так себе это понял
