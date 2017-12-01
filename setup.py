from distutils.core import setup

setup(
    name='mastodon_backup',
    version='0.0.1',
    description="Utility for backing up your Mastodon content",
    author="Alex Schroeder",
    author_email="alex@gnu.org",
    url='https://github.com/kensanata/mastodon-backup#mastodon-backup',
    classifiers=[
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Communications',
        'Intended Audience :: End Users/Desktop',
        'Environment :: Console',
        'Development Status :: 5 - Production/Stable',
    ],
    packages=["mastodon_backup"],
    entry_points={
        "console_scripts": ["mastodon_backup=mastodon_backup:main"]
    },
    install_requires=[
        "mastodon.py",
        "pysmartdl",
        "progress",
        "html2text",
    ],
)