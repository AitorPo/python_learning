# Colección de elementos key - value. Equivalente a un array asociativo o un JSON

persona = {
    'nombre': 'Aitor',
    'apellidos': 'Poquet',
    'web': 'aitor.com'
}

print(persona)
print(persona['web'])

contactos = [
    {
        'nombre': 'Aitor',
        'email': 'aitor.com'
    },
    {
        'nombre': 'Aina',
        'email': 'aina.com'
    },
    {
        'nombre': 'Frida',
        'email': 'frida.com'
    }
]

print(contactos)
contactos[0]['nombre'] = 'Aitoret'
print(contactos[0]['nombre'])

print('\n')
for contacto in contactos:
    print(f'Nombre del contacto: {contacto["nombre"]}');
    print(f'Email del contacto: {contacto["email"]}');
    print('-----------------------');