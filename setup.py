from setuptools import setup


setup(
    name='Flask-Restful-MQTT',
    version='0.1',
    url='https://github.com/SergioML9/flask-restful-mqtt/',
    license='BSD',
    author='Sergio Muñoz',
    author_email='sergio.munoz@upm.es',
    description='Very short description',
    long_description=__doc__,
    packages=['flask_restful_mqtt'],
    # if you would be using a package instead use packages instead
    # of py_modules:
    # packages=['flask_sqlite3'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask',
        'flask-mqtt',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)