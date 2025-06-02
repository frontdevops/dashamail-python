from setuptools import setup, find_packages

setup(
    name='dasha-mail',
    version='0.1.0',
    description='DashaMail API client for Python: sync and async, aiohttp/requests',
    author='Alexander Majorov',
    author_email='alexander.majorov@gmail.com',
    url='https://github.com/your-vendor/dasha-mail-python-client',
    packages=find_packages(),
    python_requires='>=3.10',
    install_requires=[],
    extras_require={
        "sync": ["requests>=2.0"],
        "async": ["aiohttp>=3.8.0"],
        "flask": ["Flask>=2.0"]
    },
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3.13',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
