import base64
coded_string = 'aHR0cHM6Ly9yZW50cnkub3JnL2ZpcmVoYXdrNTIjc2VydmljZXM='

decoded = base64.b64decode(coded_string)

print(decoded)

