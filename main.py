import requests

user='python24'
password='TCMS9L'
sender='python2024' # отправитель
reciever='79163439281' # получатель
text='Hello world!'


url=f'https://my3.webcom.mobi/sendsms.php?user={python24}&pwd={password}&sadr={sender}&dadr={reciever}&text={text}'
print(url)
response=request.get(url)
print(response)

if response.status_code==200:
    print('Сообщение успешно отправлено!')
else:
    print(f'Ошибка при отправке {response.status_code}')