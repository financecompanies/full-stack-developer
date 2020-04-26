users = [
    {
        '_id': '428dc3e4-6cd4-4c69-809f-b58a73feb4a1',
        '_salt': b'$2b$14$A5ivnPNBz12bITLFdKBiG.',
        'email': 'riddlerich@corpulse.com',
        'name': 'Riddle Rich',
        'password': b'$2b$14$A5ivnPNBz12bITLFdKBiG..SjOLJUwf6VqaFgkgEWibVW6ifCHP52',
        'registered': '2019-10-22T11:37:41 +03:00',
        'username': 'riddle.rich'
    },
    {
        '_id': '89935185-aeee-45e1-ad2d-18ed97ae66e8',
        '_salt': b'$2b$14$o2eNiqgmXKRgwwbjWAae5u',
        'email': 'noellesalinas@corpulse.com',
        'name': 'Noelle Salinas',
        'password': b'$2b$14$o2eNiqgmXKRgwwbjWAae5uqLw3856XpyT7UNoXwAQnZoxCz/YYHBK',
        'registered': '2014-01-12T05:43:33 +02:00',
        'username': 'noelle.salinas'
    },
    {
        '_id': '579d4e01-af2f-4f05-9aa5-0d4c2b4065f5',
        '_salt': b'$2b$14$8BLCWD7ykgqfcE1eGWxyru',
        'email': 'ilaburns@corpulse.com',
        'name': 'Ila Burns',
        'password': b'$2b$14$8BLCWD7ykgqfcE1eGWxyruVAdwLSZOFcXZajPgXBp26twP.Wl3YNW',
        'registered': '2018-04-16T06:10:02 +03:00',
        'username': 'ila.burns'
    },
    {
        '_id': '88743299-3191-4533-8f51-41aca3bd4d18',
        '_salt': b'$2b$14$YCLazmALsbqkRLBCCIp5Qu',
        'email': 'mariwebb@corpulse.com',
        'name': 'Mari Webb',
        'password': b'$2b$14$YCLazmALsbqkRLBCCIp5QuiFHHVJGGmH.E8N8jT6DI2gNYYNGAyaC',
        'registered': '2018-12-17T11:38:59 +02:00',
        'username': 'mari.webb'
    },
    {
        '_id': '0c3321ba-cb9a-4e31-9ecc-5b07ffd29191',
        '_salt': b'$2b$14$1w3EBiUH6k7pvwpfpYrTBO',
        'email': 'johnsonalford@corpulse.com',
        'name': 'Johnson Alford',
        'password': b'$2b$14$1w3EBiUH6k7pvwpfpYrTBOpu8eRi/oaVYs9sEqU4UV8k1zSBEK6H2',
        'registered': '2016-03-18T06:54:55 +03:00',
        'username': 'johnson.alford'
    },
    {
        '_id': '0b321cab-b6bd-4cd5-b55d-c6d0e3d76845',
        '_salt': b'$2b$14$m4/oAEKJv089MRkzdQUB4O',
        'email': 'mcclurejoyce@corpulse.com',
        'name': 'Mcclure Joyce',
        'password': b'$2b$14$m4/oAEKJv089MRkzdQUB4OfQ0sm1GvWR6bBBmwuPWuleG59nSfTQy',
        'registered': '2020-02-05T10:08:57 +03:00',
        'username': 'mcclure.joyce'
    },
    {
        '_id': '8a3b4c6e-c88f-4a09-bf53-3237eca06ff6',
        '_salt': b'$2b$14$iFjDmLpg2TVNgy32Jnwdxe',
        'email': 'caldwellmcclain@corpulse.com',
        'name': 'Caldwell Mcclain',
        'password': b'$2b$14$iFjDmLpg2TVNgy32JnwdxebGKNnwG5IOK5nwfqiFHJtscpJAym4lC',
        'registered': '2019-07-15T01:14:55 +03:00',
        'username': 'caldwell.mcclain'
    },
    {
        '_id': '8f1bb4c5-51ab-4ded-958e-5f2741431a67',
        '_salt': b'$2b$14$ZJol2239Rp5rnYHhpaV4Ue',
        'email': 'lestergarrison@corpulse.com',
        'name': 'Lester Garrison',
        'password': b'$2b$14$ZJol2239Rp5rnYHhpaV4Uec/74AfuzNDlGK/hIvxs7S2mKL7gCYzG',
        'registered': '2015-12-18T03:14:48 +02:00',
        'username': 'lester.garrison'
    },
    {
        '_id': 'd0b802cf-129e-425c-b5e4-cc4591a27b91',
        '_salt': b'$2b$14$2odanXjq0NAWpIMW7tGQEO',
        'email': 'bergcraft@corpulse.com',
        'name': 'Berg Craft',
        'password': b'$2b$14$2odanXjq0NAWpIMW7tGQEOv19bossPaNe8fhp1.bl4Xo4p1dZM4su',
        'registered': '2016-07-03T05:46:22 +03:00',
        'username': 'berg.craft'
    }
]


def find_user(username):
    """Lookup for user filtering by the username.

    It raises a `StopIteration` if no user was found.
    """
    return next(user for user in users if user['username'] == username)
