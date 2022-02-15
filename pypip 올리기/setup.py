from setuptools import setup, find_packages

setup(
    name                = 'pip이름',
    version             = '버전은 0.1부터',
    description         = 'pypi 이름',
    author              = 'pypi 이름',
    author_email        = '이메일 넣고',
    url                 = 'github주소',
    download_url        = 'github주소',
    install_requires    =  [],
    packages            = find_packages(exclude = []),
    keywords            = ['ccpy'],
    python_requires     = '>=3',
    package_data        = {},
    zip_safe            = False,
    classifiers         = [
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)