from setuptools import setup, Extension, find_packages

with open("README.md", encoding="utf-8") as f:
    readme = f.read()

setup(
    name="mtprotocrypt",
    version="1.2.6.5b",
    description="Fast and Portable Cryptography Extension Library for Pyrogram",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/pyrogram",
    download_url="https://github.com/hazy-kun/tgcrypto/releases/latest",
    author="Dan",
    author_email="dan@pyrogram.org",
    license="LGPLv3+",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
        "Operating System :: OS Independent",
        "Programming Language :: C",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: Implementation",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Security",
        "Topic :: Security :: Cryptography",
        "Topic :: Internet",
        "Topic :: Communications",
        "Topic :: Communications :: Chat",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
    keywords="pyrogram telegram crypto cryptography encryption mtproto extension library aes",
    project_urls={
        "Tracker": "https://github.com/pyrogram/tgcrypto/issues",
        "Community": "https://t.me/pyrogram",
        "Source": "https://github.com/pyrogram/tgcrypto",
        "Documentation": "https://docs.pyrogram.org",
    },
    python_requires="~=3.9",
    packages=find_packages(),
    test_suite="tests",
    zip_safe=False,
    ext_modules=[
        Extension(
            "tgcrypto",
            sources=[
                "tgcrypto/tgcrypto.c",
                "tgcrypto/aes256.c",
                "tgcrypto/ige256.c",
                "tgcrypto/ctr256.c",
                "tgcrypto/cbc256.c"
            ]
        )
    ]
)
